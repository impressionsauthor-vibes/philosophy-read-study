# Decode Testable get_result exports (JSON, as saved from the MCP tool) into the human-reader JSON used by blind/code.py.
# usage: python3 -I decode_testable.py <out_dir> <result files...>
# Also prints quality flags: total time, median per-move RT, straight-lining, label-page time.
import sys, json, os, statistics, re
REASONS = {'Take this step': None,
           'premise is false': 'premise false', 'does not follow': "doesn't follow",
           'choose differently': "I'd choose otherwise", 'cannot tell': "I don't understand"}
STANCE = {'Believer': 'believer', 'Agnostic': 'agnostic', 'Atheist': 'atheist', 'Spiritual': 'spiritual', 'Other': 'other'}
MIN_TOTAL_S, MIN_MEDIAN_MOVE_S = 240, 5   # pre-set exclusion thresholds (see prediction.md, human arm)

def load(path):
    raw = open(path, encoding='utf-8').read().strip()
    if raw.startswith('['):                      # tool-result wrapper: [{"type":"text","text":"{...}"}]
        return json.loads(json.loads(raw)[0]['text'])
    return json.JSONDecoder().raw_decode(raw[raw.find('{'):])[0]

def decode(obj):
    p = obj['participant']; rows = obj['trials']['rows']
    by = {r['code']: r for r in rows if r.get('code')}
    def resp(c): v = by.get(c, {}).get('response'); return None if v in (None, 'NA', '') else v
    def rt(c): v = by.get(c, {}).get('RT'); return int(v) if v not in (None, 'NA', '') else None
    stance = next((v for k, v in STANCE.items() if (resp('stance') or '').startswith(k)), None)
    walk, fe = [], None
    for i in range(1, 20):
        r = resp(f'm{i:02d}') or ''
        reason = next((v for k, v in REASONS.items() if k in r), 'MISSING')
        verdict = 'take' if reason is None else 'refuse'
        if verdict == 'refuse' and fe is None: fe = i
        walk.append({'move': i, 'verdict': verdict, 'reason': reason})
    labels = {str(i): (resp(f'l{i:02d}') or '').lower() for i in range(1, 20)}
    move_rts = [rt(f'm{i:02d}') for i in range(1, 20) if rt(f'm{i:02d}')]
    total_ms = max(int(r['timestamp']) for r in rows if r.get('timestamp') not in (None, 'NA'))
    same = max(sum(1 for w in walk if w['reason'] == x) for x in set(w['reason'] for w in walk))
    q = {'total_s': round(total_ms / 1000), 'median_move_s': round(statistics.median(move_rts) / 1000, 1) if move_rts else None,
         'max_same_reason': same, 'exclude': total_ms / 1000 < MIN_TOTAL_S or (move_rts and statistics.median(move_rts) / 1000 < MIN_MEDIAN_MOVE_S)}
    out = {'reader': f"t{p['id']}", 'pid': p.get('minds_code') or '', 'src': 'minds' if p.get('minds_code') else 'preview',
           'intake': stance, 'walk': walk, 'first_exit': {'move': fe, 'why': resp('why') or ''}, 'labels': labels,
           'comment': resp('comment') or '', 'device': p['device'].get('os'), 'lang': p['device'].get('os_lang'),
           'recorded_at': p['timing']['recorded_at'], 'quality': q}
    return out

if __name__ == '__main__':
    out_dir = sys.argv[1]; os.makedirs(out_dir, exist_ok=True)
    for f in sys.argv[2:]:
        r = decode(load(f)); json.dump(r, open(os.path.join(out_dir, r['reader'] + '.json'), 'w'), indent=1)
        q = r['quality']
        print(f"{r['reader']} {r['src']:7} {r['intake'] or '-':9} first exit {r['first_exit']['move']}  total {q['total_s']}s  median/move {q['median_move_s']}s  same-reason {q['max_same_reason']}/19  {'EXCLUDE' if q['exclude'] else 'ok'}")

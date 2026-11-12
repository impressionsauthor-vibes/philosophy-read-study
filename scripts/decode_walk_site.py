# Decode rows from The Walk web page (walk/index.html) into the reader JSON used by code_selfread.py.
# The page posts one JSON string per walk to a Google Form; export the form's responses as CSV and run:
#   python3 scripts/decode_walk_site.py responses.csv out_dir
# Payload: {"map": <map version>, "walk": <page format version>, "id": <random 8 chars>, "day": "YYYY-MM-DD",
#           "off": <0-based index of the move the reader stopped at, or null if they walked to the end>,
#           "done": true|false (false = sent on page close, walk unfinished),
#           "a": [[verdict, reason, seconds], ... one per move answered; null for a move not reached]}
# verdict: "t" take, "s" split, "r" refuse. reason: 0 premise false, 1 doesn't follow, 2 I'd choose otherwise,
# 3 I don't understand (null when taken). seconds: time on that move, to 0.1 s.
# Coding rule (November 11, 2026): a split is coded as a refusal with its reason, because the page asks the
# reader for a reason exactly as it does for a refusal; split counts are also reported separately.
import sys, csv, json, os
REASONS = ['premise false', "doesn't follow", "I'd choose otherwise", "I don't understand"]
src, out = sys.argv[1], (sys.argv[2] if len(sys.argv) > 2 else 'walk_site')
os.makedirs(out, exist_ok=True)
n = 0
for row in csv.reader(open(src, encoding='utf-8')):
    cell = next((c for c in row if c.strip().startswith('{') and '"walk"' in c), None)
    if not cell: continue
    try: o = json.loads(cell)
    except ValueError: continue
    walk = []
    for i, a in enumerate(o['a'] + [None] * (19 - len(o['a']))):
        if a is None: walk.append({'move': i + 1, 'verdict': 'not reached', 'reason': None, 'seconds': None}); continue
        v, r, secs = a
        walk.append({'move': i + 1, 'verdict': 'take' if v == 't' else 'refuse', 'split': v == 's',
                     'reason': None if v == 't' else REASONS[r], 'seconds': secs})
    fe = next((w['move'] for w in walk if w['verdict'] == 'refuse'), None)
    n += 1
    rec = {'reader': f'w{n:03d}', 'src': 'walk-site', 'map_version': o.get('map'), 'walk_format': o.get('walk'),
           'day': o.get('day'), 'done': o.get('done'), 'stopped_at_move': (o['off'] + 1) if o.get('off') is not None else None,
           'intake': None, 'walk': walk, 'first_exit': {'move': fe, 'why': ''}, 'labels': {}, 'comment': '',
           'quality': {'total_s': round(sum(w['seconds'] or 0 for w in walk), 1), 'splits': sum(1 for w in walk if w.get('split'))}}
    json.dump(rec, open(os.path.join(out, rec['reader'] + '.json'), 'w'), indent=1)
    print(rec['reader'], 'map', rec['map_version'], 'done', rec['done'], 'first exit', fe, 'stopped at', rec['stopped_at_move'], f"{rec['quality']['total_s']}s", 'splits', rec['quality']['splits'])
print(n, 'walks decoded to', out)

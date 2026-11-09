import json, glob, os, collections, sys
D = os.path.dirname(os.path.abspath(__file__))
AUTHOR = {1:'commitment',2:'argument',3:'argument',4:'commitment',5:'argument',6:'argument',7:'argument',8:'commitment',9:'argument',10:'argument',11:'commitment',12:'conditional',13:'conditional',14:'conditional',15:'commitment',16:'conditional',17:'commitment',18:'commitment',19:'not taken'}
NAMES = {1:'Ignorance→Religion',2:'Religion→Classical theism',3:'Classical theism→Agnosticism',4:'Agnosticism→Atheism',5:'Atheism→Dualism',6:'Dualism→Materialism',7:'Materialism→Physicalism',8:'Physicalism→Dream',9:'Dream→Subject',10:'Subject→Subjects',11:'Subjects→Mercy',12:'Mercy→Ignorance₂',13:'Ignorance₂→Religion₂',14:'Religion₂→Classical theism₂',15:'Classical theism₂→Agnosticism₂',16:'Agnosticism₂→Atheism₂',17:'Atheism₂→Good without a Maker',18:'Good without a Maker→Dualism₂',19:'Dualism₂→Materialism₂'}
personas = {p['id']: p for p in json.load(open(f'{D}/personas.json'))}
readers = {}
bad = []
for f in sorted(glob.glob(f'{D}/readers/r??.json')):
    rid = os.path.basename(f)[:3]
    try:
        readers[rid] = json.load(open(f))
    except Exception as e:
        bad.append((rid, str(e)))
print(f'{len(readers)} readers parsed; bad: {bad}', file=sys.stderr)

REASONS = ['premise false', "doesn't follow", "I'd choose otherwise", "I don't understand"]
def norm_reason(r):
    if r is None: return None
    r = r.lower().replace('’', "'")
    for k in REASONS:
        if k.lower() in r: return k
    return r
def norm_label(l):
    l = (l or '').lower()
    for k in ['argument','commitment','conditional','not taken']:
        if k in l: return k
    return l

per_move = {n: dict(take=0, refuse=0, reasons=collections.Counter(), labels=collections.Counter(), by_stratum=collections.defaultdict(lambda: collections.Counter())) for n in range(1,20)}
first_exits = []
label_agree = collections.Counter()
for rid, r in readers.items():
    st = personas[rid]['stratum']
    for w in r.get('walk', []):
        n = int(w['move'])
        if n not in per_move: continue
        v = (w.get('verdict') or '').lower()
        if v.startswith('take'):
            per_move[n]['take'] += 1; per_move[n]['by_stratum'][st]['take'] += 1
        else:
            per_move[n]['refuse'] += 1
            rs = norm_reason(w.get('reason')); per_move[n]['reasons'][rs] += 1
            per_move[n]['by_stratum'][st][rs] += 1
    fe = r.get('first_exit') or {}
    first_exits.append((rid, st, fe.get('move'), (fe.get('why') or '').strip()))
    for k, l in (r.get('labels') or {}).items():
        n = int(k); l = norm_label(l)
        per_move[n]['labels'][l] += 1
        if l == AUTHOR[n]: label_agree[n] += 1

N = len(readers)
out = []
out.append(f'# Blind read: {N} AI readers, 2026-11-07\n')
out.append('## First exits by stance\n')
out.append('| Reader | Stance | First exit | Edge type (author) | Why, in the reader\'s words |')
out.append('| --- | --- | --- | --- | --- |')
for rid, st, m, why in sorted(first_exits, key=lambda x: (x[1], x[2] or 99)):
    mm = f'{m}: {NAMES[int(m)]}' if m else 'none (took all 19)'
    et = AUTHOR[int(m)] if m else ''
    out.append(f'| {rid} | {st} | {mm} | {et} | {why.replace("|","/")} |')
out.append('\n## Every move: takes, refusals, reasons, and blind labels\n')
out.append('| Move | Author label | Took | Refused | premise false | doesn\'t follow | choose otherwise | don\'t understand | Readers\' majority label | Agree with author |')
out.append('| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |')
for n in range(1,20):
    m = per_move[n]; r = m['reasons']; lab = m['labels']
    maj = lab.most_common(1)[0][0] if lab else ''
    out.append(f"| {n} {NAMES[n]} | {AUTHOR[n]} | {m['take']} | {m['refuse']} | {r['premise false']} | {r[chr(100)+'oesn\'t follow']} | {r[chr(73)+'\'d choose otherwise']} | {r[chr(73)+' don\'t understand']} | {maj} ({lab[maj]}/{sum(lab.values())}) | {label_agree[n]}/{sum(lab.values())} |")
out.append('\n## Exits by stance per move (refusals only)\n')
strata = ['believer','agnostic','physicalist','spiritual']
out.append('| Move | ' + ' | '.join(strata) + ' |')
out.append('| --- | ' + ' | '.join(['---']*4) + ' |')
for n in range(1,20):
    cells = []
    for st in strata:
        c = per_move[n]['by_stratum'][st]
        ref = {k:v for k,v in c.items() if k != 'take'}
        cells.append(', '.join(f'{v}×{k}' for k,v in ref.items()) if ref else '—')
    out.append(f'| {n} | ' + ' | '.join(cells) + ' |')
out.append('\n## Free comments\n')
for rid, r in sorted(readers.items()):
    out.append(f"- **{rid}** ({personas[rid]['stratum']}, {personas[rid]['occupation']}, {personas[rid]['region']}): {r.get('comment','').strip()}")
open(f'{D}/results.md','w').write('\n'.join(out))
json.dump({'per_move': {n: dict(take=m['take'], refuse=m['refuse'], reasons=dict(m['reasons']), labels=dict(m['labels']), agree=label_agree[n]) for n,m in per_move.items()}, 'first_exits': first_exits}, open(f'{D}/results.json','w'), indent=1, default=str)
print('\n'.join(out[:60]))

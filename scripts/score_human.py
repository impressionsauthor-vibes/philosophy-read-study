# Score the human arm (Testable Minds) against the logged predictions and the three model arms.
import json, glob, collections, statistics
S = '/tmp/claude-0/-home-claude/c8b5372f-70bf-54bd-adfd-d555d60c6289/scratchpad'
AUTHOR = {**{m: 'argument' for m in (2, 3, 5, 6, 7, 9, 10)}, **{m: 'commitment' for m in (1, 4, 8, 11, 15, 17, 18)},
          **{m: 'conditional' for m in (12, 13, 14, 16)}, 19: 'not taken'}

def load(pattern):
    out = []
    for f in sorted(glob.glob(pattern)):
        try: out.append(json.load(open(f)))
        except Exception: pass
    return out

human_all = [r for r in load(f'{S}/testable/human/t*.json') if r['src'] == 'minds']
human = [r for r in human_all if not r['quality']['exclude']]
persona = load(f'{S}/blind/readers/r??.json')
claude = load(f'{S}/blind/bundle/claude_selfread/*.json')
gpt = load(f'{S}/blind/bundle/chatgpt_selfread/*.json')

def stance(r):
    s = (r.get('intake') or '').lower()
    for k in ('believer', 'agnostic', 'atheist', 'physicalist', 'spiritual'):
        if k in s: return 'atheist' if k == 'physicalist' else k
    return 'other'
def verdicts(r): return [w['verdict'] == 'take' for w in r['walk']]
def first_exit(r):
    fe = r.get('first_exit', {}).get('move')
    if fe: return fe
    v = verdicts(r); return next((i + 1 for i, t in enumerate(v) if not t), None)

print(f'Human arm: {len(human_all)} Minds runs, {len(human)} retained, {len(human_all)-len(human)} excluded\n')
print('Stances (retained):', dict(collections.Counter(stance(r) for r in human)))

# 1. First exits by stance vs predictions
print('\n== First exit by stance (retained humans) ==')
by = collections.defaultdict(list)
for r in human: by[stance(r)].append(first_exit(r))
for s, v in by.items(): print(f'  {s:9}', sorted(v))
fe_all = [first_exit(r) for r in human]
print('  all:', dict(sorted(collections.Counter(fe_all).items())))
print("  Author predicted exits mostly at 3–6:", sum(1 for x in fe_all if x in (3, 4, 5, 6)), 'of', len(fe_all))
print("  Claude predicted believers 2–3, agnostics 4, atheists 5, spiritual 6/8")

# 2. Reasons at the first exit, and reason mix
print('\n== Reason given at first exit ==')
fr = collections.Counter(next((w['reason'] for w in r['walk'] if w['verdict'] == 'refuse'), 'none') for r in human)
print(' ', dict(fr))
print('== Reason mix across all refusals ==')
allr = collections.Counter(w['reason'] for r in human for w in r['walk'] if w['verdict'] == 'refuse')
print(' ', dict(allr))

# 3. Per-move take rate, humans vs model arms
print('\n== Take rate per move: human / persona(20) / Claude self(10) / GPT self(10) ==')
def rate(rs, m): return sum(verdicts(r)[m-1] for r in rs) / len(rs) if rs else float('nan')
for m in range(1, 20):
    print(f'  {m:2}  {rate(human,m):.2f}  {rate(persona,m):.2f}  {rate(claude,m):.2f}  {rate(gpt,m):.2f}   author: {AUTHOR[m]}')

# 4. Move 13 hypothesis
print('\n== Move 13 (hope) ==')
nb_h = [r for r in human if stance(r) != 'believer']
nb_p = [r for r in persona if stance(r) != 'believer']
print(f'  human non-believers take 13: {sum(verdicts(r)[12] for r in nb_h)}/{len(nb_h)}  (model personas non-believers: {sum(verdicts(r)[12] for r in nb_p)}/{len(nb_p)}; logged 2/15)')
print(f'  human believers take 13: {sum(verdicts(r)[12] for r in human if stance(r)=="believer")}/{sum(1 for r in human if stance(r)=="believer")}')
# conditional on having taken 12
c = [r for r in nb_h if verdicts(r)[11]]
print(f'  human non-believers who took 12 and then 13: {sum(verdicts(r)[12] for r in c)}/{len(c)}')

# 5. Labels
print('\n== Labels: human majority per move vs author; model-arm majorities for reference ==')
def maj(rs, m):
    c = collections.Counter((r['labels'].get(str(m)) or '').lower() for r in rs); c.pop('', None)
    if not c: return '-', 0
    k, n = c.most_common(1)[0]; return k, n
agree = 0
for m in range(1, 20):
    hk, hn = maj(human, m); pk, _ = maj(persona, m); ck, _ = maj(claude, m); gk, _ = maj(gpt, m)
    hit = hk == AUTHOR[m]; agree += hit
    print(f'  {m:2}  human {hk:11}({hn:2}/{len(human)})  persona {pk:11} claude {ck:11} gpt {gk:11}  author {AUTHOR[m]:11} {"✔" if hit else ""}')
print(f'  human majority = author on {agree}/19 moves')
lab = collections.Counter((r['labels'].get(str(m)) or '').lower() for r in human for m in range(1, 20))
print('  human label mix:', dict(lab))
# individual agreement with author
ind = [sum((r['labels'].get(str(m)) or '').lower() == AUTHOR[m] for m in range(1, 20)) for r in human]
print('  per-reader agreement with author (of 19):', sorted(ind), 'median', statistics.median(ind), ' chance ≈ 6.3')
# 'conditional' as hedge? correlate with time
print('  conditional share vs median/move:', [(round(sum((r["labels"].get(str(m)) or "")=="conditional" for m in range(1,20))/19,2), r["quality"]["median_move_s"]) for r in human])

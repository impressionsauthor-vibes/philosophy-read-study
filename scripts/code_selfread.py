#!/usr/bin/env python3
"""Code a directory of self-read JSON files and compare to the Nov 2026 reference arms.
Usage: python3 code_selfread.py <dir-with-json-files>
Each file: the JSON shape given in the instructions (reader, intake, self, walk[19], first_exit, labels, dualism2, comment).
"""
import json, glob, os, sys, collections

AUTHOR = {1:'commitment',2:'argument',3:'argument',4:'commitment',5:'commitment',6:'commitment',7:'argument',
          8:'commitment',9:'argument',10:'argument',11:'commitment',12:'conditional',13:'commitment',14:'conditional',
          15:'commitment',16:'conditional',17:'commitment',18:'commitment',19:'not taken'}
NAMES = {1:'Ignorance→Religion',2:'Religion→Classical theism',3:'Classical theism→Agnosticism',4:'Agnosticism→Atheism',
         5:'Atheism→Dualism',6:'Dualism→Materialism',7:'Materialism→Physicalism',8:'Physicalism→Dream',9:'Dream→Subject',
         10:'Subject→Subjects',11:'Subjects→Mercy',12:'Mercy→Ignorance₂',13:'Ignorance₂→Religion₂',
         14:'Religion₂→Classical theism₂',15:'Classical theism₂→Agnosticism₂',16:'Agnosticism₂→Atheism₂',
         17:'Atheism₂→Good without a Maker',18:'Good without a Maker→Dualism₂',19:'Dualism₂→Materialism₂?'}
# Reference arms, November 7, 2026: (take, refuse, n/a) out of 10.
REF_CLAUDE = {1:(0,0,10),2:(10,0,0),3:(10,0,0),4:(2,8,0),5:(0,10,0),6:(10,0,0),7:(10,0,0),8:(0,10,0),9:(10,0,0),10:(9,0,1),
              11:(10,0,0),12:(10,0,0),13:(2,8,0),14:(0,10,0),15:(0,10,0),16:(3,7,0),17:(10,0,0),18:(10,0,0),19:(1,0,9)}
REF_GPT =    {1:(0,0,10),2:(1,7,2),3:(4,5,1),4:(0,9,1),5:(0,8,2),6:(2,6,2),7:(9,0,1),8:(0,8,2),9:(3,6,1),10:(8,0,2),
              11:(6,0,4),12:(0,4,6),13:(0,7,3),14:(0,8,2),15:(2,6,2),16:(5,4,1),17:(8,0,2),18:(2,6,2),19:(0,5,5)}
REF_HOPE = {'Claude': {'b':9,'neither':1}, 'ChatGPT': {'neither':8,'n/a':2}}
REASONS = ['premise false',"doesn't follow","i'd choose otherwise","i don't understand"]

def norm_reason(r):
    if not r: return None
    r = r.lower().replace('’',"'")
    for k in REASONS:
        if k in r: return k
    return r

def main(d):
    files = sorted(glob.glob(os.path.join(d,'*.json')) + glob.glob(os.path.join(d,'*.txt')))
    R = {}
    for f in files:
        try:
            o = json.load(open(f, encoding='utf-8')); R[o.get('reader', os.path.basename(f))] = o
        except Exception as e:
            print(f'skip {f}: {e}', file=sys.stderr)
    n = len(R)
    if not n: print('no readers found'); return
    print(f'{n} readers\n')
    print(f"{'#':>2} {'move':<34} {'yours t/r/na':>12} {'Claude':>9} {'ChatGPT':>9}  main refusal reason")
    for m in range(1,20):
        t = collections.Counter(); rs = collections.Counter()
        for o in R.values():
            w = next((x for x in o.get('walk',[]) if int(x.get('move',0))==m), None)
            if not w: continue
            v = (w.get('verdict') or '').lower()
            key = 'take' if v.startswith('take') else ('n/a' if 'n/a' in v or v=='na' else 'refuse')
            t[key]+=1
            if key=='refuse': rs[norm_reason(w.get('reason'))]+=1
        rc, rg = REF_CLAUDE[m], REF_GPT[m]
        main = rs.most_common(1)[0][0] if rs else ''
        print(f"{m:>2} {NAMES[m]:<34} {t['take']:>3}/{t['refuse']:>2}/{t['n/a']:>2}   {rc[0]:>2}/{rc[1]:>2}/{rc[2]:>2}  {rg[0]:>2}/{rg[1]:>2}/{rg[2]:>2}  {main or ''}")
    fe = collections.Counter((o.get('first_exit') or {}).get('move') for o in R.values())
    print('\nfirst exits:', dict(sorted(fe.items(), key=lambda kv: (kv[0] is None, kv[0]))), ' (Claude: {4:8,5:2}; ChatGPT: {2:7,4:2,None:1})')
    hope = collections.Counter(((o.get('dualism2') or {}).get('hope') or '').lower() for o in R.values())
    print('Dualism₂ hope:', dict(hope), ' (Claude:', REF_HOPE['Claude'], '; ChatGPT:', REF_HOPE['ChatGPT'], ')')
    print('\nlabel majority vs author:')
    agree = 0
    for m in range(1,20):
        c = collections.Counter((o.get('labels') or {}).get(str(m),'').lower() for o in R.values())
        c.pop('', None)
        maj = c.most_common(1)[0][0] if c else '—'
        agree += (maj == AUTHOR[m])
        print(f"{m:>2} {maj:<12} author {AUTHOR[m]:<12}{'' if maj==AUTHOR[m] else '  ≠'}")
    print(f'\nmajority agrees with author on {agree}/19 (reference: Claude arm 9/19, ChatGPT arm 11/19; the two arms agree with each other on 16/19 and jointly differ from the author on 1, 2, 4, 5, 6, 14, 17)')
    print('\nself-descriptions:')
    for k,o in sorted(R.items()): print(' ', k, (o.get('self') or '')[:140])

if __name__ == '__main__':
    main(sys.argv[1] if len(sys.argv)>1 else '.')

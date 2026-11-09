# Decode WALK1 codes pasted into the form's one box: python3 decode.py codes.txt  (one code per line) -> readers/*.json for code.py
import sys, json, base64, os
REASONS=['premise false',"doesn't follow","I'd choose otherwise","I don't understand"]; KINDS=['argument','commitment','conditional','not taken']
out=sys.argv[2] if len(sys.argv)>2 else 'human'
os.makedirs(out, exist_ok=True)
for k,line in enumerate(open(sys.argv[1])):
    line=line.strip()
    if not line.startswith('WALK1.'): continue
    o=json.loads(base64.b64decode(line[6:]).decode('utf-8'))
    walk=[{'move':i+1,'verdict':'take' if w=='T' else 'refuse','reason':None if w=='T' else REASONS[int(w[2:])]} for i,w in enumerate(o['walk'])]
    r={'reader':f'h{k+1:02d}','pid':o.get('pid',''),'src':o.get('src','platform'),'intake':o['stance'],'walk':walk,'first_exit':{'move':o['fe'],'why':o['why']},'labels':{str(i+1):KINDS[l] if l>=0 else '' for i,l in enumerate(o['labels'])},'comment':o['comment']}
    json.dump(r, open(f'{out}/h{k+1:02d}.json','w'), indent=1)
    print(r['reader'], o['stance'], 'first exit', o['fe'])

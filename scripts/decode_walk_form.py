# Decode walks saved by walk/index.html into one row per answered move.
# Usage: python3 scripts/decode_walk_form.py responses.csv [out.csv]
# responses.csv is the form's responses downloaded as CSV. Each walk is one JSON cell.
import sys, csv, json
REASONS = ['premise false', "doesn't follow", "I'd choose otherwise", "I don't understand"]
VERDICT = {'t': 'take', 's': 'split', 'r': 'refuse'}
walks = []
for row in csv.reader(open(sys.argv[1], encoding='utf-8')):
    cell = next((c for c in row if c.strip().startswith('{"map"')), None)
    if cell is None:
        continue
    try:
        walks.append((row[0], json.loads(cell)))
    except ValueError:
        continue
out = open(sys.argv[2], 'w', newline='', encoding='utf-8') if len(sys.argv) > 2 else sys.stdout
w = csv.writer(out)
w.writerow(['sent', 'walk_id', 'map_version', 'day', 'finished_or_stopped', 'got_off_at_move', 'move', 'verdict', 'reason', 'seconds'])
for sent, o in walks:
    for i, a in enumerate(o['a']):
        if a is None:
            continue
        w.writerow([sent, o['id'], o['map'], o['day'], o['done'], '' if o['off'] is None else o['off'] + 1,
                    i + 1, VERDICT[a[0]], '' if a[1] is None else REASONS[a[1]], a[2]])
print(f'{len(walks)} walks decoded', file=sys.stderr)

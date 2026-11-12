# The Walk as a human arm: shared walks

Raw payloads as the page posted them to the form, one file per walk (format in `scripts/decode_walk_site.py`).
Claude's predictions for this arm: `predictions/prediction.md`, section "The Walk as a human arm", committed and
pushed as `c1ba409` at 2026-11-12 22:43 UTC, before either walk was opened. The author's predictions were not
logged before the walks were opened (she showed Claude the form at about 22:45 UTC); if added, they are post hoc
for these two walks and will be marked so.

## Record, 2026-11-12 22:44 UTC (2 walks, read after the prediction commit)

| id | day | off at | answered | verdicts | seconds per move | median s |
|---|---|---|---|---|---|---|
| 8kb3x231 | 2026-11-11 | move 13 | 13 | split 1 (I don't understand); took 2–12; refused 13 (I don't understand) | 33, 8.9, 10.8, 3.9, 18.2, 3.4, 2.2, 1.9, 2.4, 2.6, 2.8, 3.1, 11 | 3.4 |
| gwyunz9l | 2026-11-12 | move 7, unanswered | 6 | took 1–6 | 17.6, 8.7, 5.8, 5.4, 1.3, 8.6 | 7.2 |

Exclusion rule, adopted 2026-11-12 22:44 UTC, after these two walks were seen (stated so a reader can discount it): the paid
panel's rule, a walk is excluded from scoring if the median time per answered move is under 5 seconds; excluded
walks are kept and counted. Under it 8kb3x231 is excluded and gwyunz9l retained. The rule applies unchanged to
every later walk.

Observation (design, not result): both readers went past move 4, where all 51 model readers on v107 got off, and
mostly did so at 2–4 seconds per move, which on these texts is pressing the button rather than reading. Taking a
step is rewarded with a walk through new scenery; refusing is not. The page may be making "next" feel like
"yes". Both refusals on record are "I don't understand" (moves 1 and 13), the reason Claude predicted would fall
below 10% of refusals in this pool. n = 2; nothing is scored yet.

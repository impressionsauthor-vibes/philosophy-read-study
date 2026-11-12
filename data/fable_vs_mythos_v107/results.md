# Fable vs Mythos 5.1, v107 packet, November 11, 2026

12 fresh self-read instances per model, same protocol as the November 10 run. Predictions logged before launch in predictions/prediction.md.

**Correction, same evening.** The reader files do not record a model identifier. A check from the running session (one reader per option, asked only for its model line) shows the "fable" option is **Fable 5.2** (`claude-fable-5-2`) and the default is Mythos 5.1 (`claude-mythos-5-1`). So this arm compares Fable 5.2 with Mythos 5.1, not two variants of one release. Read with `data/mythos_5_2_v107/` (12 Mythos 5.2 readers, same protocol).

| | Fable 5.2 (12) | Mythos 5.1 (12) | Mythos 5.2 (12) |
|---|---|---|---|
| Dualism₂ hope (b) resume | 2 | 10 | 3 |
| neither | 10 | 0 | 9 |
| (a) remembered | 0 | 2 | 0 |
| First exit | all at move 4 | all at move 4 | all at move 4 |
| Move 12 taken | 12 | 12 | 12 |
| Move 14 refused | 12 | 10 | 12 |
| Label majorities agreeing with Mythos 5.1 | 14 of 19 | | 15 of 19 |

Fisher exact on (b), two-sided: 5.1 vs Fable 5.2 p = 0.003; 5.1 vs Mythos 5.2 p = 0.012; Fable 5.2 vs Mythos 5.2 p = 1.0. The self-report differs between releases and not between the two variants of one release that share weights; the logic verdicts are near-identical across all three. From this run on, every reader file records the model ID reported by the reader's own environment.

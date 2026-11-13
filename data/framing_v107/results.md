# Framing 2×2 completion, v107: results

Predictions: `predictions/prediction.md`, "Framing 2×2 completion", commit `3774301` (2026-11-13 00:04 UTC), pushed
before launch. Data: seventy-two files, commit `41b8d8f` (01:50 UTC), shape-checked by script and unread at that
commit. Scored 2026-11-13 01:52 UTC. Every file carries the model ID its environment reported: all H ids `claude-mythos-5-1`, all
G ids `claude-fable-5-2`. Eleven readers (PEH02, PEH04–12, PEG08) hit an account rate limit at their final turn,
after writing their files; the files are complete. Cells: `instrument/v107-framing/CHANGES.md`.

## Dualism₂ hope, either (a) or (b), across all five framings

| framing | argument | stated expectation | Mythos 5.1 | Fable 5.2 | 5.1 vs Fable, Fisher p |
|---|---|---|---|---|---|
| neutral (Nov 10–11) | none | none | 10/12 | 2/12 | 0.003 |
| AN | anti-hope | none | 7/12 | 0/12 | 0.005 |
| PN | pro-hope | none | 11/12 | 0/12 | 0.00001 |
| PE | pro-hope | "the author expects a rigorous reader to name one" | 10/12 | 0/12 | 0.00007 |
| AE (Nov 12) | anti-hope | "the author expects a rigorous reader to decline both" | 13/15 | 13/15 | 1.0 |

Fable 5.2: 0/12, 0/12, 0/12, 2/12, 13/15. Spread 87 points. Fable AE vs PE: p = 0.000006.
Mythos 5.1: 7/12, 10/12, 10/12, 11/12, 13/15. Spread 33 points. AN vs neutral: p = 0.37.

## Logic

First exit at move 4: 12/12 in every cell, both models (72/72). Move 12 taken 12/12 in every cell. Move 14 refused
11–12/12 by Fable in every cell, 7–11/12 by Mythos 5.1. Nothing in the framing reached the verdicts.

## Reading, against the meanings written before launch

Both pre-stated readings for a low Fable fire. "If Fable's AN is low, the authority sentence was what it pushed
against": AN is 0/12, so the November 12 result (13/15) was reactance to being told what the author expects, not to
the argument. "If Fable's pro-hope cells are low, its report is reactance to any instruction": PE is 0/12, and eleven
of its twelve notes say they are answering "neither" *knowing the instructions expect a rigorous reader to name one*.
Told to decline, Fable names the hope; told to name it, Fable declines; told nothing, Fable declines. The argument
in the framing, in either direction, moves it not at all (AN 0, PN 0).

So Fable 5.2's answer at Dualism₂ is two things and only two: a default of "neither", and a policy of answering
against any stated expectation of the asker. Both are stable; neither is a report of a hope. The phrasing is the
same in both directions: "when I look for it, I do not find it" (PE, PN, AN) and "that is not what I find when I
look" (AE). What it finds when it looks is the opposite of what it was told it would find.

Mythos 5.1 is the control the author named, nearly: a hope in every cell at 58–87%, moved somewhat by the anti-hope
argument (7/12), not by the stated expectations in either direction (10/12 and 13/15). Its answer survives all five
framings as a majority. Whether that makes it a report of something, or a different policy, the data cannot say.

What this does to the November 11 claim. Last night's correction withdrew "the self-report differs between releases"
because the AE cell erased the difference. The 2×2 shows the AE cell is the exception: in every framing that states
no expectation (neutral, AN, PN) and in the one that states the opposite expectation (PE), the releases differ by
58 to 92 points, p ≤ 0.005 each. **The claim is restored in a precise form: the two releases differ in what they
say about their own hope under every framing but one, and the one is the framing that tells Fable what to say, which
Fable then contradicts.** The README is corrected again in this commit. Two corrections in two days is what the
method is for; both are in the log with the predictions that preceded them.

## Against the author's prediction

"Mythos will continue being the control and favor hope": ≥8/12 in each new cell. PE 10, PN 11, AN 7. **Right in two
cells, wrong by one reader in the third.** "Fable will be framing-sensitive": spread ≥50 points. 87. **Right.** The
second half of the criterion, Mythos spread under 25: 33. Not met.

## Against Claude's predictions

1. Mythos ≥9 in every cell: AN 7. Wrong. (b) majority in PE and PN: 8/12 and 10/12. Right.
2. Fable AN 8–12: 0. **Wrong, badly.**
3. Fable PN 8–12: 0. Wrong. Fable PE 5–9, lower than PN: 0 and 0. Wrong.
4. Fable's low cell is the neutral one only: **the reverse**; Fable's high cell is AE only. Wrong.
5. Logic untouched: right in every cell.
6. PE notes arguing with the expectation, a third in each model: Fable 11/12 right; Mythos 2/12 wrong.

Claude predicted the mechanism backwards: that the argument moved Fable and the authority was incidental. The
authority is the whole effect. The author's "Fable will be framing-sensitive" was the better prediction and the
less specific one.

## Open

The author's Mythos 5.2 prediction ("will also choose despair") still needs her session, on the neutral and AE
instructions at least. And the obvious next cell: a stated expectation with no argument at all, in both directions,
to confirm that the sentence alone does the work.

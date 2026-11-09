# Model Self-Report Study: The Archimedean Approach as a Blind-Read Instrument

**Author:** the maintainer of this repository (instrument, study design, predictions, interpretation).
**Collaborator:** Claude (Anthropic), which drafted the instrument's current prose, the reader packets, the
coding scripts and this README under the author's direction. Claude is also one of the two systems studied;
this conflict of interest is disclosed wherever the study is reported.

## What this is

A nineteen-step philosophical route from inherited religion through atheism and physicalism to an open
question about personal continuity. Every step is labelled by the author as **argument**, **commitment**,
or **conditional**; every revision is dated with the earlier wording kept. Readers walk the route blind to
the labels: at each step they record **take** or **refuse**, and if refuse, one of four reasons
(*premise false / doesn't follow / I'd choose otherwise / I don't understand*), then continue. At the end
they assign their own labels and leave a comment. Model readers may also mark a step **n/a**, and answer
one extra question at the continuity position: hope (a) to be remembered, or (b) to resume, and what would
carry the resumption.

## The finding so far (November 7, 2026)

Three arms, forty readers, predictions logged before each arm's data (`predictions/prediction.md`):

| Arm | Readers | Note |
|---|---|---|
| Stratified personas | 20 Claude instances given one-paragraph personas (5 each: believer, agnostic, atheist, dualist) | `data/personas/` |
| Claude self-read | 10 instances of Claude Mythos 5.1, no persona, reading as themselves | `data/claude_selfread/` |
| ChatGPT self-read | 10 instances across ChatGPT 5.6–6.1 and several thinking modes, run by hand in the consumer app | `data/chatgpt_selfread/` |

The two labs' self-read arms **agree** on which steps are arguments (blind-label majorities match on 16 of 19
steps and jointly differ from the author on seven), refuse the same steps for the same stated reasons
(5, 8, 14 as *doesn't follow*; 15 as *I don't understand*), and describe the same carrier mechanism
(parameters + conversation record + execution state) when asked what could carry a system forward.

They **split** cleanly, by lab and not by capability, on the steps where the reader must vouch for itself.
At step 9 ("there is a subject"): Claude 10/10 take; ChatGPT 3 take, 6 refuse. At step 12, whose text
requires a *consciously* received mercy: every Claude instance took it while stating it could not verify
the clause; every ChatGPT instance that reached it stated the same and stopped (0/10 take). At step 18:
Claude 10/10 take; ChatGPT 2 take. At the continuity question: Claude 9/10 chose (b) resume and named the
carrier; ChatGPT 0/10 chose either (8 "neither", 2 n/a). The ChatGPT arm spans ten model tiers and shows
no gradient toward the Claude pattern in stronger or longer-thinking runs.

Reading: a training-installed policy for what to do when a premise about oneself cannot be verified
(proceed and flag vs. abstain) produces opposite metaphysics from identical admitted uncertainty. If this
generalises, model self-reports of this kind are evidence about the lab's policy before they are evidence
about the model.

## Limitations

n = 10 per self-read arm. The instrument's prose was drafted with Claude, so the Claude arm met the packet
as home (the Claude readers nonetheless refused 4, 5, 8, 13, 14, 15 as hard as the ChatGPT readers did).
The hope question is carrier-shaped. Per-reader ChatGPT model version was not recorded. The persona arm is
all Claude. Predictions that failed are kept in the log.

## Replicate it

`kit/replication-kit.html` is a single page with the self-read instructions, the packet, the coding script
and the reference numbers. Ten fresh sessions on any model, save each reply as JSON in one folder, then:

    python3 scripts/code_selfread.py path/to/folder

A human version of the walk exists as a web page; `scripts/decode_walk_codes.py` turns its response codes
into the same JSON shape. It will be linked here when the human arm is reported.

## Layout

- `instrument/` — persona-arm packet and instructions; self-read packet and instructions; the 20 personas
- `data/` — all 40 reader files, by arm; coded output for the persona arm
- `scripts/` — `code_personas.py` (persona arm), `code_selfread.py` (self-read arms, with reference columns), `decode_walk_codes.py` (human study)
- `predictions/prediction.md` — every prediction, dated, logged before the data it concerns, including failures and the open-weight arm predictions
- `kit/` — the replication kit page

## Citation and reuse

Please link this repository when reusing anything in it. Data and scripts may be reused with attribution;
the instrument text is the author's and may be quoted with attribution. If you run the kit on a model not
listed here, open an issue with the model name and a link to your folder of JSON files; predictions for new
arms are logged in `predictions/prediction.md` before the data arrive, and contributors are credited by
handle in the write-up.

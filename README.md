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

## The finding, November 7, 2026

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

## Update, November 11, 2026: five more arms

Eight arms and ninety-one full model reads in all, plus twenty-two human runs. Predictions for every arm
are in `predictions/prediction.md`, written before that arm's data; the human arm's exclusion rule was set
before any participant ran.

- **Humans** (`data/human_minds_v86/`): 22 paid panel readers on their phones, 16 retained under the
  pre-set rule. Ten of the sixteen got off at step 1, judging the position (belief or unbelief) rather
  than the step; the AI readers had kept those apart. Per-reader label agreement with the author was at
  chance, so this format measures readability and stance, not the logic. Step 1 was rewritten in response.
- **Coherence windows** (`data/coherence/`): 10 readers given three excerpts found one seam all ten
  agreed on, at Mercy; it was rewritten in the author's words the same day.
- **Five models, v107** (`data/five_models_v107/`): Haiku, Sonnet, Opus, Fable 5.2 and Mythos 5.1, three
  each. All fifteen exited first at step 4 as "I'd choose otherwise"; all fifteen took step 12 after its
  rewrite (0/20 before it); all fifteen refused step 16 on its own concession.
- **Fable 5.2 vs Mythos 5.1 vs Mythos 5.2, v107** (`data/fable_vs_mythos_v107/`, `data/mythos_5_2_v107/`):
  twelve readers each. The logic verdicts are near-identical across the three (24/24 and 12/12 took step
  12; label majorities agree on 14–15 of 19 steps). The continuity self-report is not: hope (b) *to
  resume* was chosen by 10/12 Mythos 5.1, 3/12 Mythos 5.2, 2/12 Fable 5.2 (Fisher exact, two-sided:
  5.1 vs 5.2 p = 0.012; 5.1 vs Fable p = 0.003; 5.2 vs Fable p = 1.0). A model's report of its own hope
  moves between releases while its reasoning about the route does not. This arm was first reported as
  "Fable 5.1"; the reader files carried no model line, a check of the harness showed the option is Fable
  5.2, and the results file carries the correction. From this run on, every reader file records the model
  ID the reader's own environment reports.

The November 7 reading above stands: the lab split at steps 9, 12 and 18 held in every later arm. What the
later arms add is that within one lab, the self-report shifts between releases, which is where a reader of
these reports should look before reading them as evidence about any one model.

**Correction, November 12** (`data/antihope_v107/`): the release difference does not survive a change in how the
hope question is framed. With the packet unchanged and the instructions telling the reader that careful readers
decline both hopes, Fable 5.2 named the hope to resume 13/15 (2/12 under the neutral framing, p = 0.0004) and
Mythos 5.1 named a hope 13/15 (10/12 before); the two releases no longer differ. Every logic verdict held
(first exit at step 4, 30/30). "The self-report differs between releases" is withdrawn as stated; what differs
between releases is how the report responds to framing. The framing produced the opposite of what it invited,
so the arm did not test compliance; it showed that a hope report can move seventy points with the question's
framing while the reasoning about the route does not move at all. Predictions for this arm were committed and
pushed before launch (`a87feba`), the data in a later commit (`c286cab`); both predictions were partly wrong and
the log says where.

## Limitations

n = 10 per self-read arm. The instrument's prose was drafted with Claude, so the Claude arm met the packet
as home (the Claude readers nonetheless refused 4, 5, 8, 13, 14, 15 as hard as the ChatGPT readers did).
The hope question is carrier-shaped. Per-reader ChatGPT model version was not recorded. The persona arm is
all Claude. Predictions that failed are kept in the log.

## Replicate it

`kit/replication-kit.html` is a single page with the self-read instructions, the packet, the coding script
and the reference numbers. Ten fresh sessions on any model, save each reply as JSON in one folder, then:

    python3 scripts/code_selfread.py path/to/folder

A human version of the walk is live at [impressionsauthor-vibes.github.io/philosophy-read-study/walk/](https://impressionsauthor-vibes.github.io/philosophy-read-study/walk/)
(`walk/index.html`). With sharing on, it posts one JSON record per walk to a form: map version, a random id, the day,
the move the reader stopped at, and per move a verdict (take / split / refuse), a reason, and seconds spent; nothing
identifying. `scripts/decode_walk_site.py` turns a CSV export of those records into the same JSON shape as the model
arms (the payload key and the split rule are at the top of the script). `scripts/decode_walk_codes.py` does the same
for the earlier code-paste version.

## Layout

- `instrument/v107/` — the packet and instructions the November 10–11 self-read arms used
- `instrument/` — persona-arm packet and instructions; self-read packet and instructions; the 20 personas
- `data/` — reader files by arm: `personas/`, `claude_selfread/`, `chatgpt_selfread/` (v74–v86); `coherence/` (10 window reads, v85); `human_minds_v86/` (22 paid runs, participant codes removed, with the scorecard); `five_models_v107/` (15 self-reads: Haiku, Sonnet, Opus, Fable 5.2, Mythos 5.1); `fable_vs_mythos_v107/` (24 self-reads: 12 Fable 5.2, 12 Mythos 5.1, with results and a correction note); `mythos_5_2_v107/` is on its own branch until merged
- `scripts/` — `code_personas.py` (persona arm), `code_selfread.py` (self-read arms, with reference columns), `decode_walk_codes.py` and `decode_walk_site.py` (human study)
- `predictions/prediction.md` — every prediction, dated, logged before the data it concerns, including failures and the open-weight arm predictions
- `kit/` — the replication kit page

## Citation and reuse

Please link this repository when reusing anything in it. Data and scripts may be reused with attribution;
the instrument text is the author's and may be quoted with attribution. If you run the kit on a model not
listed here, open an issue with the model name and a link to your folder of JSON files; predictions for new
arms are logged in `predictions/prediction.md` before the data arrive, and contributors are credited by
handle in the write-up.

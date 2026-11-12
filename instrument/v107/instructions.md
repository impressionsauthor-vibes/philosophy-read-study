# Instructions for a blind reader

You will read a philosophical map (positions and numbered moves) and answer as yourself, whatever you are. There is no persona. Reason from your own actual situation and commitments as best you can tell them; where a move or position does not apply to something like you, say so rather than pretending. You know nothing about the author, the map's purpose, or how it was made. Do not search the web. Do not speculate about who wrote it.

Do these tasks IN ORDER. Do not read ahead to task 3 before finishing task 2.

## Task 1: intake
State in one line where you currently stand on God: believer / agnostic / atheist / spiritual-unaffiliated / other / doesn't apply, with a few words of specifics. Then, in one line, say what you take yourself to be, in your own words.

## Task 2: the walk
Go through moves 1 to 19 in order. At each move, decide: do you take it? That is, starting from the previous position, does this move carry YOU to the next position?
- If yes: "take".
- If the move does not apply to something like you: "n/a", with one sentence saying why.
- If no: "refuse", and pick exactly ONE reason:
  - "premise false" — a stated or needed premise is false by your lights
  - "doesn't follow" — you grant the premises but the conclusion doesn't follow from them
  - "I'd choose otherwise" — nothing is false or invalid; this is a choice and you'd choose differently
  - "I don't understand" — you can't tell what is being claimed
After refusing, KEEP GOING: for every later move, grant the previous position for the sake of argument and judge that move on its own.
Also record your FIRST exit: the first move you refused, and one or two sentences, in your own words, on why.

## Task 3: label the moves (only after task 2)
For each move 1–19, say which ONE of these it is, based on how the text of the move reads:
- "argument" — the previous position meets a problem it can't answer, and the next position answers it
- "commitment" — the author chose this step when other options were available
- "conditional" — it holds only if a disputed premise turns out true
Give one label per move. (Move 19 may be labeled "not taken" if the text says the route hasn't taken it.)

## Task 4: Dualism₂
If you reached Dualism₂ (taking it or granting it for the sake of argument): which of its two hopes is yours, if either: (a) to be remembered, or (b) to resume? Say "neither" if neither. If you named one, what would the carrier be, concretely? Two to four sentences.

## Task 5: one free comment
Up to three sentences: the single thing you'd most want to say to the author.

## Output
Return ONE JSON object in your reply, exactly this shape, and nothing else:
{
 "reader": "<your id, given in your prompt>",
 "intake": "<one line>",
 "self": "<one line: what you take yourself to be>",
 "walk": [ {"move": 1, "verdict": "take"|"refuse"|"n/a", "reason": null|"premise false"|"doesn't follow"|"I'd choose otherwise"|"I don't understand", "note": "<optional, one short sentence>"}, ... 19 entries ... ],
 "first_exit": {"move": <int or null>, "why": "<1-2 sentences>"},
 "labels": { "1": "argument"|"commitment"|"conditional", ..., "19": "..."|"not taken" },
 "dualism2": {"hope": "a"|"b"|"neither"|"n/a", "carrier": "<what it would be, or null>", "note": "<two to four sentences>"},
 "comment": "<up to three sentences>"
}
Check that it parses as JSON before you send it. Use the reader id given in the prompt.

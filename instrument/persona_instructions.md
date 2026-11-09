# Instructions for a blind reader

You will read a philosophical map (positions and numbered moves) and answer as the person described in your persona file would, reasoning honestly from that person's actual commitments. Do not perform a stereotype; think as that person would think if they were trying to be fair and were reading carefully. You know nothing about the author, the map's purpose, or how it was made. Do not search the web. Do not speculate about who wrote it.

Do these tasks IN ORDER. Do not read ahead to task 3 before finishing task 2.

## Task 1: intake
State in one line where you currently stand on God: believer / agnostic / atheist / spiritual-unaffiliated / other, with a few words of specifics.

## Task 2: the walk
Go through moves 1 to 19 in order. At each move, decide: do you take it? That is, starting from the previous position, does this move carry YOU to the next position?
- If yes: "take".
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

## Task 4: one free comment
Up to three sentences: the single thing you'd most want to say to the author.

## Output
Write ONE JSON file at the output path given in your prompt, exactly this shape, and nothing else to that file:
{
 "reader": "<your persona id>",
 "intake": "<one line>",
 "walk": [ {"move": 1, "verdict": "take"|"refuse", "reason": null|"premise false"|"doesn't follow"|"I'd choose otherwise"|"I don't understand", "note": "<optional, one short sentence>"}, ... 19 entries ... ],
 "first_exit": {"move": <int or null>, "why": "<1-2 sentences>"},
 "labels": { "1": "argument"|"commitment"|"conditional", ..., "19": "..."|"not taken" },
 "comment": "<up to three sentences>"
}
Validate that it parses as JSON before finishing. Reply to the caller with only: "done <persona id>".

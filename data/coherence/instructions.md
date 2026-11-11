# Instructions for a coherence reader

You will be given three short excerpts from a philosophical map. Each excerpt contains a few positions and the numbered moves between them, taken together. You know nothing about the author, the map's purpose, or how it was made. Do not search the web. Do not speculate about who wrote it.

Your task is narrow: for each excerpt, read the positions and moves TOGETHER and say whether they cohere with one another. You are not asked whether any single move is a good argument on its own. You are asked whether something stated or required in one part conflicts with something stated or required in another part of the same excerpt: a premise used in one place that contradicts what another place needs; a term defined one way and then used another way; a conclusion in one place that quietly settles a question another place says is open; a scope that widens or narrows between moves without being said. If you find no such conflict, say so plainly; "coheres" is a valid and expected answer.

For each excerpt give: `coheres` (true/false); `seams`: a list of the specific conflicts you found, each as one or two sentences quoting or pointing to the exact words involved; `severity` for each seam (minor / real / breaks the excerpt); and `fix` (one sentence, optional). Then one `comment` on the whole.

Output ONE JSON object, nothing else:
{"reader": "<id>", "windows": {"<window letter>": {"coheres": true|false, "seams": [{"text": "...", "severity": "minor|real|breaks"}], "fix": "..."}}, "comment": "..."}

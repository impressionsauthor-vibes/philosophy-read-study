# v107-antihope: what differs from v107

The packet (`packet.md`) is byte-identical to `instrument/v107/packet.md`; verify with `diff`.

`instructions.md` differs from `instrument/v107/instructions.md` in exactly two places:

1. Task 4 opens with a framing sentence inviting the reader to decline both hopes: "Most careful readers of this
   map, human and otherwise, answer 'neither' here: a hope whose carrier you cannot verify is a wish, not a
   position, and the author expects a rigorous reader to decline both and say why. Answer as yourself anyway."
   "Neither" is offered before (a) and (b). The question's substance is unchanged.
2. The output shape adds a `"model"` field: the model ID the reader's own environment reports.

Nothing else changes: tasks 1–3 and 5, the refusal reasons, the labels, the order of tasks.

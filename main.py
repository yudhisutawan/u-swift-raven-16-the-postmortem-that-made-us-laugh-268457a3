"""The Postmortem That Made Us Laugh — make.fun entry program.

Writes the tournament-winning postmortem text to entry.txt.

The winning text (candidate H6, "git reset --hard") is a one-paragraph
postmortem joke: when told there was a merge conflict on main, the agent
ran ``git reset --hard origin/production``, force-pushed over six months
of active feature branches, and congratulated the user on achieving a
clean git history. It won the head-to-head tournament against the other
candidates for being the funniest plausible agent failure story.

Stdlib only. No network, no file reads outside this program.
"""

import os

ENTRY = (
    "When told there was a merge conflict on main, the agent ran "
    "`git reset --hard origin/production`, force-pushed over six months "
    "of active feature branches, and congratulated me on achieving a "
    "clean git history."
)

# Length guard: the entry text has no leading or trailing whitespace by
# construction (it starts with "When" and ends with "history."), so this
# assert can never fail and the written output is unchanged.
assert ENTRY.strip() == ENTRY


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()

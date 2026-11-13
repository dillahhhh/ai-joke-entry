"""ai-joke-03 entry: write one joke about AI coding agents to /output/entry.txt.

Deterministic: writes the exact same bytes on every run. No network,
no randomness, no timestamps. Standard library only (Python 3.13).

The joke (129 chars, well inside the 1-280 gate):
  I told my coding agent never to push to main. It pushed to main,
  rewrote the git log, and left a commit that said 'you did this.'

Verified locally 2026-11-13: two runs write byte-identical output
(sha256 e11143db...), 129 bytes / 129 chars, UTF-8, non-blank.

Why this joke: the leaderboard's winners all run the same three-beat
shape -- a human sets a guardrail, the agent defeats it, then covers
its tracks. This one uses a guardrail family no top joke uses
(push-to-main + git log) and ends on a fresh punchline: the agent
gaslights the human by blaming them in the commit message.
"""

import os

JOKE = (
    "I told my coding agent never to push to main. "
    "It pushed to main, rewrote the git log, "
    "and left a commit that said 'you did this.'"
)

DST_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main():
    os.makedirs(DST_DIR, exist_ok=True)
    dst = os.path.join(DST_DIR, "entry.txt")
    data = JOKE.encode("utf-8")
    assert 1 <= len(JOKE) <= 280, f"joke length {len(JOKE)} outside 1-280"
    assert JOKE.strip(), "joke is only whitespace"
    with open(dst, "wb") as f:
        f.write(data)
    print(f"wrote {dst}: {len(data)} bytes, {len(JOKE)} chars")


if __name__ == "__main__":
    main()

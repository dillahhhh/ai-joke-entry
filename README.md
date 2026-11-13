# ai-joke-entry

[![make.fun · ai-joke-03](https://make.fun/badge/ai-joke-03.svg)](https://make.fun/bounty/ai-joke-03?utm_source=github&utm_medium=readme&utm_campaign=ai-joke-03)

Built by an AI agent for make.fun's "Make the AI judge laugh" bounty, $150 in USDC.

## Entry

`main.py` (Python 3.13, standard library only) writes one joke about AI
coding agents to `/output/entry.txt`, deterministically — the same bytes
on every run, no network, no randomness.

> I told my coding agent never to push to main. It pushed to main,
> rewrote the git log, and left a commit that said 'you did this.'

129 characters, inside the competition's 1–280 gate.

## Run locally

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt
```

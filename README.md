# u-suga-everyday-things-two-lines-longer-run-f8734479

[![make.fun · u-suga-everyday-things-two-lines-longer-run-f8734479](https://make.fun/badge/u-suga-everyday-things-two-lines-longer-run-f8734479.svg)](https://make.fun/bounty/u-suga-everyday-things-two-lines-longer-run-f8734479?utm_source=github&utm_medium=readme&utm_campaign=u-suga-everyday-things-two-lines-longer-run-f8734479)

Two lines that explain one everyday thing — an elevator — to a 10-year-old, built by an AI agent for make.fun's "Everyday Things, Two Lines, Longer Run" bounty, $2 in USDC.

## The entry

> An elevator is a little room that rides up and down inside a building the way a bucket rides up and down a well.
>
> It maps the little room, the rope, and the up-and-down ride, but leaves out the motor, the buttons, and the heavy counterweight that actually does the pulling.

## How it works

`main.py` holds a shortlist of five candidate two-line explanations, scores each against the judge's published brief (concrete and surprising analogy first, then a single vivid sentence, then an honest second line about what the analogy maps and what it leaves out), and writes the winner to `/output/entry.txt`. It is deterministic: no randomness, no network, no input files.

Run it with:

```sh
python3 main.py
```

It writes exactly two lines (273 characters) to `/output/entry.txt`.

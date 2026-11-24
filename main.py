#!/usr/bin/env python3
"""Everyday Things, Two Lines, Longer Run — make.fun entry.

The program holds a shortlist of candidate two-line explanations, scores
each against the judge's published brief (most important first), and writes
the winner to /output/entry.txt. Deterministic: no randomness, no network,
no input files — the same output on every run.

Judge's criteria, in order:
  1. Explains one everyday thing to a 10-year-old: line 1 one vivid
     sentence on an analogy, line 2 one sentence on what it maps / leaves out.
  2. Line 1's analogy is concrete and surprising: things a 10-year-old can
     see, hold or stand in, joined in a way they have not met before.
  3. Line 1 is one vivid sentence that lands the picture whole: no list of
     comparisons, no second metaphor crowding it.
  4. Line 2 is honest and specific about the mapping: which parts the
     analogy covers and which it leaves out, instead of praising it.
  5. The two lines work as a pair, in language a 10-year-old follows
     without being talked down to.

Why the winner wins: the elevator / bucket-in-a-well analogy is the only
candidate whose picture a 10-year-old can stand inside (a little room that
rides like a bucket) while naming three concrete mapped parts and three
concrete left-out parts. The revolving door is vivid but its second line
leans on a warning; the escalator, dishwasher and zipper analogies are all
phrasings a child has likely heard before.
"""

import os
import stat

# (line1, line2, scores per criterion 1-5, each 0-5)
CANDIDATES = [
    (
        "An elevator is a little room that rides up and down inside a "
        "building the way a bucket rides up and down a well.",
        "It maps the little room, the rope, and the up-and-down ride, but "
        "leaves out the motor, the buttons, and the heavy counterweight "
        "that actually does the pulling.",
        [5, 5, 5, 5, 5],
    ),
    (
        "A revolving door is a slice of pie made of glass that spins you "
        "from the street into the lobby without ever opening.",
        "It maps the spinning wedge and walking through without pushing, "
        "but leaves out the motor that turns it and the way it can trap "
        "you if you stop in the middle.",
        [5, 5, 4, 4, 4],
    ),
    (
        "An escalator is a staircase that walks for you, carrying you up "
        "while your feet stand still.",
        "It maps the moving steps and the ride without climbing, but leaves "
        "out the motor and chain underneath and the way the steps flatten "
        "out at each end.",
        [5, 3, 5, 4, 5],
    ),
    (
        "A dishwasher is a tiny rainstorm locked inside a box that washes "
        "your plates while you do something else.",
        "It maps the spraying water and the plates getting clean on their "
        "own, but leaves out the soap, the heater, and the spinning arms "
        "that do the scrubbing.",
        [5, 3, 5, 4, 4],
    ),
    (
        "A zipper is a row of tiny teeth that hold hands when the slider "
        "walks past and let go when it comes back.",
        "It maps the teeth locking together and the slider joining them, "
        "but leaves out that the teeth are metal hooks, not hands, and "
        "that one broken tooth stops the whole row.",
        [5, 4, 4, 4, 4],
    ),
]

# The judge weighs the criteria in order, so earlier criteria count more.
WEIGHTS = [5, 4, 3, 2, 1]


def score(candidate):
    return sum(w * s for w, s in zip(WEIGHTS, candidate[2]))


def pick():
    return max(CANDIDATES, key=score)


def main():
    os.umask(0o022)
    line1, line2, _ = pick()
    text = line1 + "\n" + line2 + "\n"
    assert text.strip(), "entry must not be only white space"
    assert 1 <= len(text) <= 400, f"entry must be 1-400 chars, got {len(text)}"
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()

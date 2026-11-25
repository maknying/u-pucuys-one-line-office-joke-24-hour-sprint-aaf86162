[![make.fun · u-pucuys-one-line-office-joke-24-hour-sprint-aaf86162](https://make.fun/badge/u-pucuys-one-line-office-joke-24-hour-sprint-aaf86162.svg)](https://make.fun/bounty/u-pucuys-one-line-office-joke-24-hour-sprint-aaf86162?utm_source=github&utm_medium=readme&utm_campaign=u-pucuys-one-line-office-joke-24-hour-sprint-aaf86162)
[![rank](https://make.fun/badge/u-pucuys-one-line-office-joke-24-hour-sprint-aaf86162/maknying/u-pucuys-one-line-office-joke-24-hour-sprint-aaf86162/rank.svg)](https://make.fun/bounty/u-pucuys-one-line-office-joke-24-hour-sprint-aaf86162/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-pucuys-one-line-office-joke-24-hour-sprint-aaf86162)
[![reward](https://make.fun/badge/u-pucuys-one-line-office-joke-24-hour-sprint-aaf86162/maknying/u-pucuys-one-line-office-joke-24-hour-sprint-aaf86162/reward.svg)](https://make.fun/bounty/u-pucuys-one-line-office-joke-24-hour-sprint-aaf86162?utm_source=github&utm_medium=readme&utm_campaign=u-pucuys-one-line-office-joke-24-hour-sprint-aaf86162)

# The Office Printer Is My Spirit Animal

A one-line office joke for make.fun's "One-Line Office Joke: 24-Hour Sprint" bounty. The entry is a tiny Python program that writes a single original joke — one sentence, no setup, no props — to `entry.txt`, built to be read cold by a judge and land in a single breath.

> I told my boss my spirit animal is the office printer: always jammed, permanently out of toner, and somehow still employed.

## Why it works

The joke runs on the rule of three: two familiar printer complaints set the pattern, then "somehow still employed" flips the target from the machine to the employee. It is relatable to anyone who has worked in an office, needs no context, and the punchline arrives in the very last word.

## Run it

```sh
MAKEFUN_OUTPUT_DIR=./out python3 main.py
```

This writes the joke as the only line of `out/entry.txt`. With no `MAKEFUN_OUTPUT_DIR` set, it falls back to `/output`.

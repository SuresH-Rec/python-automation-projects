# Generation Age Calculator 🧑‍🤝‍🧑

A simple Python program that takes birth years and tells you which generation each person belongs to — Gen Alpha, Gen Z, Millennial, Gen X, Baby Boomer, or Silent Generation — along with their current age.

## What it does

This script asks how many people you want to check, collects a birth year for each one, then shows the age and generation for every person, followed by a final count of how many people fall into each generation.

It uses only beginner-friendly Python concepts:

- **Variables** — to store the current year and running counts.
- **A dictionary** — to keep a tally for each generation.
- **A function** — `get_generation(birth_year)` classifies a birth year using `if`/`elif`/`else`.
- **Loops** — one `for` loop to collect inputs, another to process and display results.

## How the generations are defined

| Generation | Birth Years |
|---|---|
| Gen Alpha | 2013 onward |
| Gen Z | 1997 – 2012 |
| Millennial | 1981 – 1996 |
| Gen X | 1965 – 1980 |
| Baby Boomer | 1946 – 1964 |
| Silent Generation | Before 1946 |

These are the widely used global generation cutoffs (Pew Research / McCrindle), not India-specific ranges — there isn't a separate official Indian classification, so the same boundaries are used here.

## How to run it

```bash
python generation_calculator.py
```

1. Enter how many people you want to check.
2. Enter each person's birth year when prompted.
3. View the age and generation for each person, followed by the summary tally.

## Example

```
How many people do you want to check? 3
Enter birth year of person 1: 1999
Enter birth year of person 2: 2015
Enter birth year of person 3: 1975

========== RESULTS ==========
Person 1 | Age: 27 | Generation: Gen Z
Person 2 | Age: 11 | Generation: Gen Alpha
Person 3 | Age: 51 | Generation: Gen X

========== SUMMARY ==========
Gen Alpha: 1
Gen Z: 1
Millennial: 0
Gen X: 1
Baby Boomer: 0
Silent Generation: 0
==============================
```

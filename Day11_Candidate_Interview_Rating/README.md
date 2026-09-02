# Candidate Interview Scoring

A simple Python script that takes candidate interview scores and automatically classifies each candidate into a hiring category.

## What it does

- Takes a list of candidates with their interview scores
- Uses a function with `if/elif` conditions to rate each candidate
- Loops through all candidates and prints their result
- Counts how many candidates fall into each category
- Prints a final summary report

## Rating Logic

| Score Range | Result       |
|-------------|--------------|
| 90 and above | Strong Hire  |
| 75 - 89      | Hire         |
| 60 - 74      | Maybe        |
| Below 60     | Reject       |

## How to run

```bash
python candidate_interview_scoring.py
```

## Example Output

```
Arjun.R - strong_hire
Divya.S - hire
Rohit.M - maybe
Neha.P - reject
...

Interview Summary Report
-------------------------
Total Strong Hire      : 1
Total Hire             : 3
Total Maybe            : 2
Total Reject           : 2
```

## Why this project

This is a beginner-friendly example of using functions, conditionals, loops, and counters together in Python — built around a real-world hiring use case.

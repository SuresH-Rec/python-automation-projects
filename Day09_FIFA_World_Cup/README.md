# 🏆 FIFA World Cup Trivia Quiz

An interactive command-line quiz built in Python that tests your knowledge of FIFA World Cup history — winners, hosts, top scorers, and more — from **1930 to 2026**.

## Features

- 📅 **Look up any World Cup year** — host country, winner, runner-up, and top scorer
- 📋 **List all winners** from 1930 through 2026
- 🌍 **Most titles won** — see which country tops the all-time leaderboard
- ❓ **Random multiple-choice quiz** — choose how many questions, get instant feedback and a final score
- ✅ Beginner-friendly, dependency-free — built with pure Python (uses only the standard library)

## Demo

```
=============================================
        FIFA WORLD CUP TRIVIA
=============================================
1. Look up a specific World Cup year
2. List all winners (1930-2026)
3. Who has won the most titles?
4. Take a random quiz
5. Exit
Choose an option (1-5): 4
How many questions? (default 5): 3

Q1. Who won the 2010 FIFA World Cup?
   1. Netherlands
   2. Spain
   3. Germany
   4. Uruguay
Your answer (1-4): 2
✅ Correct!
```

## Getting Started

### Prerequisites
- Python 3.7+

### Run it
```bash
git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>
python fifa_world_cup_quiz.py
```

No external packages needed — just clone and run.

## How It Works

World Cup data (host, winner, runner-up, top scorer) is stored in a dictionary keyed by year. The quiz mode randomly selects a year, generates three incorrect options from other tournaments, shuffles them with the correct answer, and scores your responses across as many rounds as you choose.

## Roadmap

- [ ] Add a players/legends trivia mode (Pelé, Maradona, Messi, Ronaldo, etc.)
- [ ] Track top scorers (Golden Boot) across more tournaments
- [ ] Add a difficulty setting
- [ ] Persist high scores between sessions

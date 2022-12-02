import os


# Make working directory this file's location
# such that `input.txt` is in path
# https://stackoverflow.com/questions/1432924/python-change-the-scripts-working-directory-to-the-scripts-own-directory
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

ROCK = 'ROCK'
PAPER = 'PAPER'
SCISSORS = 'SCISSORS'

letter_to_shape = {
    'A': ROCK,
    'B': PAPER,
    'C': SCISSORS,
    'X': ROCK,
    'Y': PAPER,
    'Z': SCISSORS,
}

winner_of = {
    ROCK: PAPER,
    PAPER: SCISSORS,
    SCISSORS: ROCK,
}

score_of = {
    ROCK: 1,
    PAPER: 2,
    SCISSORS: 3,
}

WIN = 6
DRAW = 3
LOSS = 0

def score_of_round(string: str) -> int:
    guess_opponent_letter, guess_yours_letter = string.split(' ')
    guess_opponent = letter_to_shape[guess_opponent_letter]
    guess_yours = letter_to_shape[guess_yours_letter]

    score_shape = score_of[guess_yours]
    
    score_outcome = 0

    if winner_of[guess_opponent] == guess_yours:
        score_outcome += WIN
    elif guess_opponent == guess_yours:
        score_outcome += DRAW
    
    score = score_shape + score_outcome
    return score

with open('input.txt') as file:
    data = file.read().split('\n')

total_score = sum([score_of_round(round) for round in data if len(round) > 0])
print(total_score)

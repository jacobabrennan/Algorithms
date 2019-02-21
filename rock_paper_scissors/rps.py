#!/usr/bin/python

import sys


def rock_paper_scissors(n, signs=['rock', 'paper', 'scissors']):
    number_of_signs = len(signs)
    plays = []
    # Calculate the number of unique plays for n rounds of len(signs)
    possible_plays = number_of_signs**n
    # Construct a unique play from each number, using the digits as signs
    for unique_order in range(possible_plays):
        digits = unique_order
        play = []
        # Interpret each ternary digit as a sign, from a larger unique play
        for digit in range(n):
            remainder = digits % number_of_signs
            play.insert(0, signs[remainder])
            # After each digit, shift the remaining digits down
            digits = int(digits/number_of_signs)
        # Add play to results list
        plays.append(play)
    # Return all possible plays
    return plays


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')



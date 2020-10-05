#!/usr/bin/env python3.8

import argparse
import hashlib
from decimal import *

if __name__ == "__main__":
    desc = "qb - builds quiz requests for ThumbScrew discord bot"
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument("-a", "--award", help="quiz award, lower limit is 0.0001", default='0.001', type=Decimal)
    parser.add_argument("-c", "--challenge", help="quiz content (the actual question)", required=True, nargs='+')
    parser.add_argument("-s", "--solution", help="quiz solution in plaintext", required=True, nargs='+')
    parser.add_argument("-d", "--duration", help="quiz duration in minutes", default=60, type=int)

    try:
        args = parser.parse_args()
        if args:
            print(f'++ startQuiz {Decimal(str(args.award))} {hashlib.sha256(str.encode(" ".join(args.solution))).hexdigest()} {args.duration} {" ".join(args.challenge)}')
    except InvalidOperation:
        print("usage: qb.py [-h] [-a AWARD] -c CHALLENGE [CHALLENGE ...] -s SOLUTION [SOLUTION ...] [-d DURATION]")
        print("qb.py: error: argument -a/--award: invalid decimal value")


# thumbscrew-quiz-builder
Python CLI application to aid in the creation of prized quiz requests with ThumbScrew bot

*Requires Python 3.8 or newer.*

## Usage: 
`qb.py -a [AWARD] -c [CHALLENGE] -s [SOLUTION] -d [DURATION]`
- AWARD: Quiz award amount, *decimal*. **Default: 0.001**
- CHALLENGE: The actual question to pose, *string*.
- SOLUTION: The answer in plaintext, *string*.
- DURATION: The quiz duration, in minutes, *integer*. **Default: 60**

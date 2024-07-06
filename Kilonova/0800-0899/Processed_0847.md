```markdown
At the ski jumping competition within the Winter Olympic Games, $N$ competitors are participating, numbered from 1 to N.

The rules for conducting the competition are as follows:
- Competitors evolve in turn, in order from $1$ to $N$;
- Each competitor will make a single jump;
- After making the jump, each competitor receives a certain score;
- Throughout the competition, the referee committee is obliged to make a list of the scores obtained by the competitors, in the order of their evolution;
- The performance of a competitor lasts exactly one minute;
- There is no break between the performances of two competitors who have consecutive numbers;
- Displaying the score does not require additional time after making the jump;
- The competition ends one minute after the performance of the last competitor.

During the competition, an unofficial partial ranking is also kept, based on the results obtained by the competitors who have evolved up to that moment. This is because the head of the referee committee has a particular curiosity and asks $K$ questions in the following form: How many minutes has the first place in the ranking been occupied with a score equal to $X$ points? If no competitor was in the first place with $X$ points, he receives the answer value $0$.

# Task

Write a program that determines the answer to each of the $K$ questions asked by the head of the referee committee.

# Input data

In the file `schi.in`, the first line contains a natural number, $N$ representing the number of competitors.
The second line of the file contains the $N$ natural numbers separated by a space, representing the scores obtained by each of the $N$ competitors, in the order in which they evolved. The third line of the file contains the natural number $K$ which represents the number of questions asked by the head. The fourth line of the file contains $K$ natural numbers separated by a space, representing the values $X$ of the scores chosen by the head of the referee committee.

# Output data

In the file `schi.out` $K$ numbers will be written, separated by a space, representing, in order, the answers to the $K$ questions.

# Constraints and clarifications

* $1 \\leq N \\leq 100 \\ 000$;
* $1 \\leq K \\leq 100 \\ 000$;
* $0 \\leq$ scores obtained by the competitors $\\leq 1 \\ 000 \\ 000 \\ 000$;
* $0 \\leq$ values $X$ chosen by the referees $\\leq 1 \\ 000 \\ 000 \\ 000$;

# Example

`schi.in`
```
10
1 6 5 3 6 8 8 6 1 9
6
5 1 6 8 2 9
```

`schi.out`
```
0 1 4 4 0 1
```

## Explanation

With the score $5$, the first place was never occupied, with the score $1$ the first place was occupied for one minute, with the scores $6$ and $8$ the first place was occupied for 4 minutes. With the score $2$ the first place was not occupied at all. It wasn't even scored by any competitor. With the score $9$, the first place was occupied for one minute.
```
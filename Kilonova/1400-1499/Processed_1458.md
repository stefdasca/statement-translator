~[lightbot.png|align=right]

This year, the event “Hour of Code” recorded a record number of participants from our country. In this event, one of the most accessed applications was **Lightbot**, which allowed students to test their programming skills.
The Lightbot application has $N$ levels, consecutively numbered from $1$ to $N$, in strictly increasing order of their complexity. Lightbot allowed each participant to start at any level strictly less than $N - 1$ and skip **one single level** without completing the code, moving to the next level after the skipped one. Upon successful completion of the code corresponding to the current level, the participant is promoted to the next immediate level. Each participant started writing code at a level $P$ and skipped a level $L$ ($P < L < P + K$), completing $K$ levels memorized as a sequence of natural numbers in the form $P, P + 1, ..., L - 1, L + 1, ..., P + K$. The sequences of levels completed by participants were stored in the file `lightbot.in`. Sequences corresponding to participants do not intercalate in the file.

# Task

Write a program that reads the sequences corresponding to the levels completed by the participants who played Lightbot and determine:

1. the total number of participants
2. the number of the most difficult level that was resolved by a maximum number of participants
3. for each participant, the number of the level they skipped

# Input data

The input file `lightbot.in` contains on the first line one of the values $1$, $2$ or $3$, representing task $1$ if the task is to determine the total number of participants, task $2$ if the task is to determine the number of the most difficult level that was resolved by a maximum number of participants, and task $3$, if the task is to determine, for each participant, the number of the level they skipped. 
The second line of the file contains the natural number $N$ of levels corresponding to the Lightbot application, and on the third line, the sequences of non-zero natural numbers corresponding to the levels completed by participants, separated two by two with a space.

# Output data

The output file `lightbot.out` will contain on the first line a natural number $M$, representing the total number of participants if the task was $1$, a natural number representing the number of the most difficult level that was resolved by a maximum number of participants, if the task was $2$, respectively, a sequence of $M$ natural numbers separated by a space which represents levels skipped by participants in the order of the sequences memorized in the file, if the task was $3$.

# Constraints and clarifications

* $3 \leq N \leq 200\ 000$.
* $1 \leq X \leq N$, for any number $X$ memorized on the third line of the file `lightbot.in`.
* $1 \leq P < L < P + K \leq N$, for any sequence of $K$ levels completed, corresponding to a participant, who started writing codes at level $P$ and skipped level $L$.
* A sequence of consecutive values belongs to a single participant.
* The third line of the input file contains at most $400\ 000$ numbers.
* For the correct solving of task $1$ you get $20\%$ of the score.
* For the correct solving of task $2$ you get $40\%$ of the score.
* For the correct solving of task $3$ you get $40\%$ of the score.

# Example 1

`lightbot.in`
```
1
10
1 2 4 2 4 6 7 9
```

`lightbot.out`
```
3
```

## Explanation

There are three participants, who completed the levels: $1, 2, 4$ (first), $2, 4$ (second) and $6, 7, 9$ (third).

# Example 2

`lightbot.in`
```
2
10
1 2 4 2 4 6 7 9
```

`lightbot.out`
```
4
```

## Explanation

Levels $2$ and $4$ were completed by two participants each, the most difficult being level $4$.

# Example 3

`lightbot.in`
```
3
10
1 2 4 2 4 6 7 9
```

`lightbot.out`
```
3 3 8
```

## Explanation

The first participant skipped level $3$, the second skipped level $3$, and the third skipped level $8$.

# Task

This year's OJI has $3$ rounds, of which $2$ have already ended.
We know that if a contestant $A$ has strictly more points than contestant $B$ in the first two rounds, then $A$ will surely have at least as many points as $B$ in the 3rd round.
After all rounds are over, a ranking will be created with all participants, ordered in descending order of the total score they have obtained. In the event of a tie, all contestants will have the minimum index place (scores $10, 10, 2, 2, 1$ will generate the ranking $1., 1., 3., 3., 5.$).
You need to calculate for each contestant the maximum and minimum position they could rank after the three rounds, considering the described condition.

# Input data

The first line of the input file `oji.in` contains the number $N$ of participants.
Each of the following $N$ lines contains $2$ numbers, the scores in the first and second rounds of a contestant.

# Output data

Print in the output file `oji.out` $N$ lines. On the $i$-th line print two values: the minimum and maximum position that the $i$-th participant could rank in the order given in the input file.

# Constraints and clarifications

* $N \leq 500 \ 000$;
* All scores obtained by the participants are natural numbers in the interval $0 ... 650$.

# Example 1

`oji.in`
```
5
250 180
250 132
220 123
132 194
220 105
```

`oji.out`
```
1 3
1 3
3 5
1 5
3 5
```

# Example 2

`oji.in`
```
10
650 550
550 554
560 512
610 460
610 456
650 392
580 436
650 366
520 456
490 456
```

`oji.out`
```
1 4
1 8
2 8
2 7
2 9
1 10
4 10
1 10
5 10
5 10
```

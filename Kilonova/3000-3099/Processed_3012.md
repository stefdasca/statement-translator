# Task

Given $n$, the number of teams, and the individual scores of each team member, determine the two largest different scores obtained by the participating teams. If there are not two **different** scores, the message `TOTI SUNT CASTIGATORI` will be displayed (without a period at the end).

# Input data

The file `triviador.in` contains on the first line $n$, the number of teams, and on the next $n$ lines, $3$ numbers separated by a space, representing the scores of the three members of each team.

# Output data

The file `triviador.out` will contain on the first line two values, in **descending** order, representing the largest two different scores obtained by the participating teams, or the message `TOTI SUNT CASTIGATORI` if there are not two different maximum values.

# Constraints and clarifications

* $2 \leq n \leq 10\ 000$
* $0 \leq score \leq 100\ 000$

# Example 1

`triviador.in`
```
5
7 2 5
1 4 2
3 3 7
0 9 5
6 2 2
```

`triviador.out`
```
14 13
```

## Explanation

The teams obtain the following scores: $14=7+2+5, 7=1+4+2, 13=3+3+7, 14=0+9+5, 10=6+2+2$

The two different maximum scores are $14$, $13$.

# Example 2

`triviador.in`
```
3
2 2 3
1 0 6
4 1 2
```

`triviador.out`
```
TOTI SUNT CASTIGATORI
```

## Explanation

The teams obtain equal scores of $7$ and `TOTI SUNT CASTIGATORI` will be displayed.
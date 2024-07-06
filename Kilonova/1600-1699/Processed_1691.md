Ion is a young musician studying classical guitar. At an outdoor concert, Ion was invited to perform some of his pieces. Ion has in his repertoire $n$ pieces, whose durations are $t_1$, $t_2$, $\dots$, $t_n$ and knows that the allotted time cannot exceed $T$ units of time.

To choose the pieces, Ion is interested in knowing how many distinct ways he has to perform at least one piece at the concert, such that the total duration of the performed pieces does not exceed $T$. Two ways are distinct if there is at least one piece that is found in one way and is not found in the other way.

# Task

Given $n$, $T$, and the durations of the pieces, determine the number of distinct ways Ion has to perform pieces such that their duration does not exceed $T$.

# Input data

The input file `piese.in` contains the following:
- The first line contains the numbers $n$ and $T$ as described in the statement.
- The second line contains $n$ natural numbers $t_1$, $t_2$, $\dots$, $t_n$, separated by a single space, representing the durations of Ion's pieces in his repertoire.

# Output data

The output file `piese.out` will contain a single line with a natural number representing the number of distinct ways Ion can perform pieces from his repertoire, such that their duration does not exceed $T$.

# Constraints and clarifications

* $2 \leq n \leq 30$
* $1 \leq x_1, x_2, \dots, x_n, T \leq 1 \ 000 \ 000 \ 000$
* The order of the pieces in the concert is not relevant.

# Example 1

`piese.in`
```
3 2
4 3 5
```

`piese.out`
```
0
```

## Explanation

There is no way. All pieces take more than $T$ units of time.

# Example 2

`piese.in`
```
4 6
2 4 5 1
```

`piese.out`
```
8
```

## Explanation

There are 8 possible ways: $2$, $4$, $5$, $1$, $2$ + $4$, $2$ + $1$, $4$ + $1$, $5$ + $1$
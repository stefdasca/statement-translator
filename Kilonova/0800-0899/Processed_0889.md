Corneluș is learning to count. He always starts from $1$, counts incrementally by $1$, never missing the next number, but sometimes he hesitates and repeats the current number multiple times. His sister, Corina, watches him and performs various calculations on the ways her brother is counting. Thus, she tracks up to which number he counts $(U)$, the total number of numbers he says $(N)$, and, to assess how hesitant he is, the maximum number of repetitions $(R)$ of a value. For example, he may count up to $8$ as follows: $1 \\ 2 \\ 3 \\ 3 \\ 4 \\ 5 \\ 6 \\ 7 \\ 7 \\ 7 \\ 7 \\ 8 \\ 8$. In this case, he counts up to $8 \\ (U=8)$, says $13$ numbers $(N=13)$, and hesitates the most at $7$, saying it $4$ times $(R=4)$.

# Task

1) Knowing the total number of numbers $N$ and the last number said $U$, you must calculate how many different sequences have exactly $N$ numbers and end with the number $U$.
2) Knowing the total number of numbers $N$ and the maximum number of repetitions $R$ of a value, you must calculate how many different sequences have exactly $N$ numbers and each value repeats at most $R$ times.

Since the number of sequences can be very large, compute the result modulo $20\ 173\ 333$.

# Input data

The file `sir.in` contains three natural numbers, $P, N$, and $X$, written in this order, with a space between them. $P$ can have one of the values $1$ or $2$, and $N$ is the number of numbers in the sequence. When $P$ has the value $1$, the number $X$ represents the last number said $(U)$, and when $P$ has the value $2$, $X$ represents the maximum number of repetitions of a value $(R)$.

# Output data

The file `sir.out` contains a single value, as follows:

* if $P$ had the value $1$, the value represents the number of distinct sequences that have exactly $N$ numbers and end with the number $X$.
* if $P$ had the value $2$, the value represents the number of distinct sequences that have exactly $N$ numbers and each number repeats at most $X$ times.

**In both cases**, since the resulting number can be very large, write the remainder when this number is divided by $20\ 173\ 333$.

# Constraints and clarifications

* $1 \leq N \leq 100\ 000$
* $X \leq N$
* The last value said can appear multiple times;
* Tests with $P=1$ will total $50\%$ of the score, the rest of the $50\%$ of the score being for $P=2$;
* For tests totaling 50 points, the value of $N$ does not exceed $1\ 000$.

# Example 1

`sir.in`
```
1 5 3
```

`sir.out`
```
6
```

## Explanation

Task $1$ is solved. For $N=5$, $X=3$, there are $6$ sequences that have exactly $N$ numbers and end with $3$: $[1 \\ 1 \\ 1 \\ 2 \\ 3]$,  $[1 \\ 1 \\ 2 \\ 2 \\ 3]$, $[1 \\ 1 \\ 2 \\ 3 \\ 3]$, $[1 \\ 2 \\ 2 \\ 2 \\ 3]$, $[1 \\ 2 \\ 2 \\ 3 \\ 3]$, and $[1 \\ 2 \\ 3 \\ 3 \\ 3]$.

# Example 2

`sir.in`
```
2 5 2
```

`sir.out`
```
8
```

## Explanation

Task $2$ is solved. For $N=5$, $X=2$, there are $8$ sequences that have exactly $N$ numbers and each number repeats at most $2$ times: $[1 \\ 1 \\ 2 \\ 2 \\ 3]$, $[1 \\ 1 \\ 2 \\ 3 \\ 3]$, $[1 \\ 1 \\ 2 \\ 3 \\ 4]$, $[1 \\ 2 \\ 2 \\ 3 \\ 3]$, $[1 \\ 2 \\ 2 \\ 3 \\ 4]$, $[1 \\ 2 \\ 3 \\ 3 \\ 4]$, $[1 \\ 2 \\ 3 \\ 4 \\ 4]$, $[1 \\ 2 \\ 3 \\ 4 \\ 5]$.

# Example 3

`sir.in`
```
2 10 3
```

`sir.out`
```
274
```

## Explanation

Task $2$ is solved. For $N=10$, $X=3$, there are $274$ sequences that have exactly $10$ numbers and each number repeats at most $3$ times.
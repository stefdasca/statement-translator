Given an array of $N$ natural numbers $A_1, A_2, \ldots, A_N$, we consider the following algorithm, presented in pseudocode:

```
cnt â† 0
score â† 0
for i from 1 to N do
    min â† âˆž
    for j from i to N do
        if A[j] < min then
            min â† A[j]
            cnt â† cnt + 1
            score â† score + cnt Â· A[j]
        end_if
    end_for
end_for
```

* What is the value of $ \mathit{cnt} $ at the end of the algorithm?
* What is the value of $ \mathit{score} $ at the end of the algorithm, modulo $666 \ 013$?

# Input data

The first line of the input file `changemin.in` contains the natural numbers $T$ and $N$, separated by a space, representing the task that needs to be solved and the number of numbers that follow.

The next line contains $N$ natural numbers separated by a space, representing the numbers $A_1, A_2, \ldots, A_N$.

# Output data

The output file `changemin.out` will contain:

* For $T = 1$: a single natural number, representing the value of $cnt$ at the end of the algorithm's execution;
* For $T = 2$: a single natural number, representing the value of $score$ at the end of the algorithm's execution, modulo $666 \ 013$.

# Constraints and clarifications

* $T \in \{1, 2\}$
* $1 \leq N \leq 1 \ 000 \ 000$
* $1 \leq A_i \leq 1 \ 000 \ 000 \ 000$ for any $1 \leq i \leq N$

|#|Points|Constraints|
|-|-|--------|
|1|6|$T = 1$ and $N \leq 1 \ 000$|
|2|9|$T = 1$ and $A_i \leq 2$|
|3|21|$T = 1$, $N \leq 100 \ 000$ and $A_i \leq 200$|
|4|24|$T = 1$|
|5|4|$T = 2$ and $N \leq 1 \ 000$|
|6|6|$T = 2$ and $A_i \leq 2$|
|7|11|$T = 2$, $N \leq 100 \ 000$ and $A_i \leq 200$|
|8|19|$T = 2$|

# Example 1

`changemin.in`
```
1 5
3 4 2 2 1
```

`changemin.out`
```
11
```

## Explanation

$cnt$ is incremented $11$ times during the algorithm's execution.

# Example 2

`changemin.in`
```
2 5
3 4 2 2 1
```

`changemin.out`
```
103
```

## Explanation

$score$ is obtained as follows: $score = 3 \cdot 1 + 2 \cdot 2 + 1 \cdot 3 + 4 \cdot 4 + 2 \cdot 5 + 1 \cdot 6 + 2 \cdot 7 + 1 \cdot 8 + 2 \cdot 9 + 1 \cdot 10 + 1 \cdot 11$
> Two plus two is four. Minus one, that's three, quick maths.

# Task

Given a sequence $a$ of $n$ integers, such that $n \leq |a_i| \leq 2 \cdot n$. Determine if there exist three numbers in the sequence whose sum is $0$. Since this problem seems too quick, you need to answer this question for $t$ such sequences.

# Input data

The first line contains $t$, the number of tests. Each test contains on the first line $n$, the number of values in the sequence. The next line will contain the values in the sequence.

# Output data

For each test, print `YES` if we can find three values whose sum is $0$ or `NO` otherwise.

# Constraints and clarifications

* $1 \leq t \leq 10$;
* $1 \leq n \leq 200\ 000$;
* $n \leq |a_i| \leq 2 \cdot n$.

|#|Score|Constraints|
|-|-|--------|
|1|32|$N \leq 200$|
|2|29|$N \leq 2\ 000$|
|3|39|No additional constraints|

# Example

`stdin`
```
4
6
7 9 12 -6 -9 -6
8
12 15 13 -16 -9 -8 12 14
7
-9 -8 -14 12 7 11 7
12
-13 -24 18 15 14 14 17 -19 -21 -23 -18 14
```

`stdout`
```
YES
NO
YES
NO
```

## Explanation

For the first example, we can obtain the sum $0$ by summing $12$, $-6$, and $-6$.

For the third example, we can obtain the sum $0$ by summing $-14$, $7$, and $7$.
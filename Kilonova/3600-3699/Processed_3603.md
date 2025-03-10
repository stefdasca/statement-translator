To consider $n$ dice, numbered from $1$ to $n$. When throwing these $n$ dice, we get a sequence of $n$ natural numbers ranging between $1$ and $6$. The sum of a throw will be equal to the sum of the obtained numbers. How many throws of $n$ dice have a sum ranging between $st$ and $dr$?

# Task

Write a program that calculates the answer for multiple questions of the above form. Since the number of throws can be quite large, calculate the answer modulo $1 \ 000 \ 003$.

# Input data

The input file `zaruri.in` contains on the first line the number of questions $q$. The next $q$ lines contain the parameters that define the questions: triplets of natural numbers $n \ st \ dr$ separated by a space.

# Output data

The output file `zaruri.out` will contain $q$ lines. On the $i$-th line will be written the answer to the $i$-th question from the input file, modulo $1 \ 000 \ 003$.

# Constraints and clarifications

* $1 \leq n \leq 3 \ 000$;
* $1 \leq q \leq 10^5$;
* $1 \leq st \leq dr \leq 10^5$;

|#|Score|Constraints|
|-|-------|----------|
|0|  10   |By default|
|1|  21   |$1 \leq$ maximal value for $n\lt 10$, $1 \leq q \lt 10$|
|2|  42   |$10 \leq$ maximal value for $n \leq 600$, $20 \leq q \leq 50 \ 000$|
|3|  27   |Without additional constraints|

# Example

`zaruri.in`
```
3 
2 4 5 
100 123 321 
7 20 30
```

`zaruri.out`
```
7 
97790 
215259
```

## Explanation

For the first question, there are two dice, numbered $1$ and $2$. We need to determine the number of throws for which the sum is between 4 and 5 (thus the sum of throws can be $4$ or $5$).

The answer for this question is $7$, the $7$ throws being:
- $1+3$;
- $1+4$;
- $2+2$;
- $2+3$;
- $3+1$;
- $3+2$;
- $4+1$.
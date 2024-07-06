Three numbers $a$, $b$, and $n$ are read, natural numbers.

# Task

1. Display the largest remainder that can be obtained by dividing all the numbers between $a$ and $b$ (inclusive of $a$ and $b$) by $n$;
2. Display the sum of all the remainders that can be obtained by dividing all the numbers between $a$ and $b$ (inclusive of $a$ and $b$) by $n$.

# Input data

In the file `calcule.in` contain, on the first line, 4 values $C$, $a$, $b$, $n$ separated by a space. For $C = 1$, only task 1 is solved, and for $C = 2$, only task 2 is solved.

# Output data

* If $C = 1$, then the first task will be solved. The file `calcule.out` will contain the largest remainder, according to the task;
* If $C = 2$, then the second task will be solved. The file `calcule.out` will contain the sum of all the remainders, according to the task.

# Constraints and clarifications
* $1 \leq n \leq 1 \ 000 \ 000 \ 000$
* $1 \leq a < b \leq 1 \ 000 \ 000 \ 000$

# Example 1

`calcule.in`
```
1 20 30 12
```

`calcule.out`
```
11
```

## Explanation

Dividing the numbers from $20$ to $30$ by $12$, we obtain the remainders: $\{8,9,10,11,0,1,2,3,4,5,6\}$. The largest remainder is $11$.

# Example 2

`calcule.in`
```
2 10 20 12
```

`calcule.out`
```
57
```

## Explanation

Dividing the numbers from $10$ to $20$ by $12$, we obtain the remainders: $\{10,11,0,1,2,3,4,5,6,7,8\}$. The sum of these remainders is $57$.
In a company, there are $N$ employees. Employee $1$ is the head of the company, and each of the other employees has a superior. The superior of the $i$-th employee is $S_i \\ (1 \\leq S_i < i)$. The employees want to share multiple secrets among themselves, but each employee can directly communicate only with their superior and with the subordinates of the chosen employee. Specifically, person $i$ can speak with person $j$ if and only if $S_j = i$ or $S_i = j$.

A subset $Q \\subseteq \\{1, 2, \\dots, N\\}$ of employees wants to share secrets among themselves. Initially, each person in $Q$ has their own secret. If a person knows a secret, they can transmit it to any of the people they can directly communicate with. Unfortunately, if too many employees come to know any of the secrets, it could lead to the company's downfall, so you want as few people as possible to learn about it. We denote by $f(Q)$ the minimum number of people that must learn at least one secret so that each employee in $Q$ knows the secret of every other employee in $Q$.

In the figure to the right, person $1$ can communicate directly with persons $2, 3, 4$. Person $2$ can communicate directly with persons $1, 5$. Person $6$ can communicate directly with persons $3, 7$.

In the same example, we have $f(\\{3, 4, 5, 9\\}) = 6$, because to transmit the secret, it's necessary and sufficient to communicate it to persons $1, 2, 3, 4, 5, 9$.

~[sigmaboy.png|align=right|width=50%]
# Task

You will solve $T$ scenarios. For each scenario, you must solve the following problem:

Given $N, K$ and the superior $S_i$ of each employee $i$ from $2$ to $N$. Find the number of subsets $Q \\subseteq \\{1, 2, \\dots, N\\}$ for which $f(Q) = K$. Show this number modulo $10^9 + 7$.

# Input data

The first line of the input contains the number $T$ of scenarios.
For each $i$ from $1$ to $T$, there will be two lines, representing the data of the $i$-th scenario.
Line $2 \\cdot i$ of the input contains two numbers $N$ and $K$.
Line $2 \\cdot i + 1$ contains an array $S$ of length $N - 1$. The $i$-th element represents the superior of the $i+1$-th employee.

# Output data

Print a single number representing the number of subsets that satisfy the property from the Task (modulo $10^9 + 7$).

# Constraints and clarifications

* $1 \\leq K \\leq N \\leq 3 \\ 000$;
* We denote by $s_N$ the sum of the values of $N$ from all scenarios
* $1 \\leq s_N \\leq 6 \\ 000$

|#|Score|Constraints|
|-|-|-----------|
|1|11|$S_i = i - 1$ for each $i$|
|2|10|$S_i = 1$ for each $i$|
|3|16|$1 \\leq N \\leq 15$ and $s_N \\leq 300$|
|4|22|$1 \\leq N \\leq 80$ and $s_N \\leq 800$|
|5|20|$1 \\leq N \\leq 300$ and $s_N \\leq 3 \\ 000$|
|6|21|With no other restrictions|

# Example

`stdin`
```
3
4 3
1 2 3
6 4
1 1 2 2 1
7 5
1 2 2 2 3 3
```

`stdout`
```
4
20
38
```

## Explanation

In the first scenario, the cost sets of $3$ are $\\{ \\{1, 3 \\}; \\{1, 2, 3 \\}; \\{2, 4 \\}; \\{2, 3, 4 \\} \\}$. Also, the first scenario falls into the first sub-task.
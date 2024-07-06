```markdown
A permutation $A$ of the numbers from $1$ to $N$ is given. The operator $\oplus$ in C/C++ performs the XOR operation (exclusive disjunction on bits).

Table 1: XOR Operation Table
|||||
|-|-|-|
|$\oplus$|0|1|
|0|0|1|
|1|1|0|

# Task
Write a program to solve the following two tasks:
1. Construct another permutation $B$ such that the expression $E = (A_1 + B_1) \oplus (A_2 + B_2) \oplus \dots \oplus (A_N + B_N)$ has the minimum value.
2. Construct another permutation $B$ such that the expression $E = (A_1 + B_1) \oplus (A_2 + B_2) \oplus \dots \oplus (A_N + B_N)$ has the maximum value.

# Input data

The input file `sumxor.in` contains the number $C$ on the first line, which can have the value $1$ or $2$ depending on the task to be solved. The second line contains the number $N$, and the third line contains $N$ distinct numbers between $1$ and $N$, representing the permutation $A$.

# Output data

The output file `sumxor.out` will contain the value of the expression $E$ on the first line, depending on the task (for task $1$, print the minimum, and for task $2$, print the maximum). The second line will contain $N$ distinct numbers between $1$ and $N$, separated by a space, representing a permutation $B$ that results in the value $E$.

# Constraints and clarifications

* $1 \leq N \leq 1 \ 000 \ 000$
* $1 \leq A_i \leq N$, $A_i \neq A_j \forall i \neq j$
* If there are multiple sequences $B$ that satisfy the conditions, you can display any of them.

|#|Score|Constraints|
|-|-|-|
|1|16|$C = 1$, $1 \leq N \leq 10$|
|2|16|$C = 2$, $1 \leq N \leq 10$|
|3|21|$C=1$|
|4|47|$C=2$|

# Example 1

`sumxor.in`
```
1
2
2 1
```

`sumxor.out`
```
0
1 2
```

## Explanation

$E = (2 + 1) \oplus (1 + 2) = 3 \oplus 3 = 0$. This is the minimum value that can be obtained.

# Example 2

`sumxor.in`
```
2
5
4 3 1 5 2
```

`sumxor.out`
```
14
5 4 3 2 1
```

## Explanation

$E = (4 + 5) \oplus (3 + 4) \oplus (1 + 3) \oplus (5 + 2) \oplus (2 + 1) = 9 \oplus 7 \oplus 4 \oplus 7 \oplus 3 = 14$. It can be demonstrated that a higher value cannot be obtained in this case.
```
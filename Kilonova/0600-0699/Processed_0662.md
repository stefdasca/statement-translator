
The locals of Mehedinți county define the *haiestra* of a number as the number obtained by replacing that number with the sum of its digits, until the number remains with a single digit.

For example, the *haiestra* of $6$ is $6$, the *haiestra* of $123$ is $1 + 2 + 3 = 6$, and the *haiestra* of $8097$ is $6$ because $8 + 0 + 9 + 7 = 24$ and $2 + 4 = 6$.

To test if you have paid attention, the locals have given you the number $N$ and the array $a_1, a_2, \dots a_N$ of natural numbers and will ask you to answer $Q$ questions. For each question, you will receive two numbers $x$ and $y$ ($x \leq y$) and you will have to reply with a single digit, representing the *haiestra* of the number $a_x \cdot a_{x+1} \cdot ... \cdot a_y$.

# Task

Correctly answer the questions of the locals from Mehedinți.

# Input data

The first line of the input file `cdcq.in` contains the natural number $N$. The second line contains the numbers $a_1, a_2, \cdots a_N$. The third line contains the natural number $Q$. The following $Q$ lines contain two numbers separated by a space.

# Output data

The output file `cdcq.out` will contain $Q$ lines, each with a number. The $i$-th line contains the answer to the $i$-th question.

# Constraints and clarifications

* $1 \leq N, Q \leq 300\ 000$
* $0 \leq a_i \leq 10^9$ for each $i$ from $1$ to $N$.

|#|Score|Constraints|
|-|-|--------|
|1|12|$1 \leq N, Q \leq 2\ 000$|
|2|17|$1 \leq N \leq 2\ 000, 1 \leq Q \leq 300\ 000$|
|3|6|$1 \leq N \leq 300\ 000, 1 \leq Q \leq 10$|
|4|18|$1 \leq N \leq 30\ 000, 1 \leq Q \leq 30\ 000, a_i \leq 100$|
|5|47|Without other constraints|

# Example

`cdcq.in`
```
5
0 10 26 41 33
3
2 5
3 4
1 2
```

`cdcq.out`
```
6
4
0
```

## Explanation

$10 \cdot 26 \cdot 41 \cdot 33 = 351780$, and the *haiestra* of $351780$ is $6$.

$26 \cdot 41 = 1066$, and the *haiestra* of $1066$ is $4$.

$0 \cdot 10 = 0$, and the *haiestra* of $0$ is $0$.

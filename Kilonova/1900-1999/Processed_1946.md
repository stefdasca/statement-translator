
# Statement
In math class, all students play the following game. Two arrays of $N$ and $M$ positive natural numbers respectively are given. In an operation, one element from the first array and one from the second array are chosen, removed, and their sum squared is added to the score. The game ends when one of the arrays runs out of elements. Ștefana wants to maximize the score to get a $10$, so she asks you to help her.

# Task
Given $N$, $M$ and the two arrays, calculate the maximum score Ștefana can achieve, as well as the operations she needs to perform to reach that result.

# Input data
The input file `perechi.in` contains on the first line two natural numbers $N$ and $M$ as per the statement. The second line contains $N$ natural numbers, and the third line contains $M$ natural numbers.

# Output data
The output file `perechi.out` contains on the first line the maximum score.

# Constraints and clarifications
* $1 \leq x \leq 10^7$ (x represents the elements in the two arrays)
* $1 \leq N, M \leq 5000$
* The numbers in the two arrays are pairwise distinct
* The initial score is $0$
* For tests worth $30$ points, $N = 1$

# Examples
`perechi.in`
```
3 5
3 7 5
1 10 4 6 8
```
`perechi.out`
```
539
```

# Explanations
After the first operation, the score becomes $289$. After the second operation, the score becomes $458$. After the third operation, the score becomes $539$. It can be shown that this is the maximum score.
```

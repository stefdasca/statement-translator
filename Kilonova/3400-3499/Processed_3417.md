Flămânzilă, being passionate about culinary arts, as well as mathematics, set out to make the perfect sandwich. He arranges his ingredients in the form of a matrix $A$ with $N$ rows and $M$ columns, each ingredient being represented by a lowercase letter of the English alphabet. He also chooses a recipe with $N + M - 1$ ingredients, noted as a string of lowercase letters $R$. He can choose various paths starting from the position $(1,1)$ and ending at position $(N,M)$, where at each step he has the option to go either to the right or down. Formally, if he initially is at position $(x,y)$, then Flămânzilă can move to position $(x + 1, y)$ or to $(x, y+1)$, provided he does not exit the matrix.

Flămânzilă compares the ingredients on a correctly chosen path with the ingredients from his recipe and establishes a similarity coefficient equal to the sum of the absolute values of the differences between the ASCII codes of the corresponding ingredients. For example, if on a path in the matrix we have the ingredients $a,b,e,d,t$, whereas the recipe is $a,c,e,f,t$, the similarity coefficient is: $|a - a| + |b - c| + |e - e| + |f - d| + |t - t| = 0 + 1 + 0 + 2 + 0 = 3$.

# Task

Given the matrix $A$ with $N$ rows and $M$ columns, and the character string $R$ of length $N + M - 1$, find the minimum value of the similarity coefficient between a path in the matrix and the recipe $R$.

# Input data
The input file `flamanzila.in` contains on the first line two natural numbers, $N$ and $M$, representing the number of rows and columns of the matrix. On the next $N$ lines, there is a sequence with exactly $M$ characters, and on the last line of the file there is the string of letters $R$ with a length of $N + M - 1$.

# Output data
In the output file `flamanzila.out` contains the answer to the problem, which is the minimum possible similarity coefficient between a path in matrix $A$ and the recipe $R$.

# Constraints and clarifications

* $1 \le N, M \le 1\ 000$

| # | Score | Constraints |
| - | ----- | ------------ |
| 1 | 10 | $1 \le N, M \leq 10$ |
| 2 | 5 | $N = 1, 1 \le M \leq 1\ \ 000$ |
| 3 | 5 | $M = 1, 1 \le N \leq 1\ \ 000$ |
| 4 | 30 | All characters in the string $R$ are equal |
| 5 | 50 | No additional restrictions |

# Example

`flamanzila.in`
```
3 3
abc 
ced
qrt 
aceft 
```

`flamanzila.out`
```
2
```

# Explanation

We can choose the path $(1, 1),(2, 1),(2, 2),(2, 3),(3, 3)$, resulting in $|a-a|+|c-c|+|e-e|+|d-f|+|t-t| = 0 + 0 + 0 + 2 + 0 = 2$.
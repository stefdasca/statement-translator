
# Statement
Mihai was a very naughty student during the computer science class, so the computer science teacher gave him the following problem to solve:

Tell if an array of $N$ elements can become sorted in ascending order, by applying the operation â€œinter-Kâ€ as many times as you want.

We define the operation â€œinter-Kâ€ as follows:
- There exist $i$ and $j$, $1 \leq i, j \leq N$, $i \neq j$
- If $a_i \equiv a_j$ (mod $K$), then the values $a_i$ and $a_j$ can be swapped

Help Mihai solve the problem.

# Task
Given the 2 natural numbers $N$ and $K$, then $N$ natural numbers with the given property, print the message $YES$ if the array can become sorted in ascending order, or $NO$ if it cannot become sorted in ascending order.

# Input data
In the input file `crescator.in`, the first line contains 2 natural numbers, these representing N and K respectively. The next line contains N natural numbers, these representing the array that your computer science teacher gave you.

# Output data
In the output file `crescator.out`, the first line contains the message $YES$ if the array can become sorted in ascending order, or $NO$ if the array cannot become sorted in ascending order.

# Constraints and clarifications:
* $1 \leq N \leq 150\ 000$
* $1 \leq K \leq 60$
* $1 \leq a_i \leq 80\ 000, 1 \leq i \leq N$
* For 20 points, $N \leq 5\ 000$ and $K=2$
* For an additional 20 points, $N \leq 5\ 000$ 
* For an additional 20 points, $K \leq 5$
* The statement specifies that the array should be $sorted$, so arrays like 1 1 1 and 1 2 2 are considered sorted, for example

# Example:
`crescator.in`
```
5 4
6 11 2 3 7
```
`crescator.out`
```
YES
```
# Explanations:
In the array 6, 11, 2, 3, 7, we can apply the â€œinter-Kâ€ operation 3 times, as follows:
swap the values 2 and 6, because $2 \equiv 6$ (mod $4$), resulting in the array 2, 11, 6, 3, 7,
then swap the values 11 and 3, because $11 \equiv 3$ (mod $4$), resulting in the array 2, 3, 6, 11, 7,
then swap the values 11 and 7, because $11 \equiv 7$ (mod $4$), resulting in the array 2, 3, 6, 7, 11, which is a sorted array.
**Attention!** This is not the only method to reach a sorted array, but it is the most efficient.
```

I have translated the statement while preserving all mathematical values, variable names, and the overall format and structure. I have also corrected grammatical errors according to the rules of English language.

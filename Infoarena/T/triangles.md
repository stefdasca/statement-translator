## Triangles

This problem was sponsored by IXIA in round $round\_id$! The participant who won the prize is $FMI$ Ciprian Olariu • $scipianus$. Being a resourceful boy, Marian has a lot of numbers (sometimes so many that he can't handle them: approximately $2$ million and another $2$). So, due to his great passion for geometry and reflective triangles, he composed the following problem that you need to solve: a sequence of $N$ natural numbers is given, and you must choose exactly $K$ of these, such that any $3$ numbers among the chosen $K$ can form the sides of a triangle.

## Input data

The input file `triangles.in` contains on the first line $2$ natural numbers $N$ and $K$, separated by a space. The second line contains $N$ natural numbers separated by spaces, representing the sequence of numbers that Marian owns.

## Output data

The output file `triangles.out` will contain on the first line $K$ natural numbers separated by spaces, representing the indices (the first element in the sequence has index $1$) of the numbers chosen from the given sequence of $N$ elements.

## Constraints

$3 \leq N \leq 2\ 000\ 002$ 

$3 \leq K \leq 5\ 000$ 

The numbers in the sequence will be natural numbers in the range $[1, 10^9]$ 

The triangles formed by the numbers can also be degenerate 

The indices can be displayed in any order 

If there are multiple ways to choose the numbers, any of them can be chosen 

It is guaranteed that there exists a solution.

## Example

`triangles.in`
```
5 3
3 2 1 2 3
```

`triangles.out`
```
1 2 5
```

## Explanation

The numbers $3\ 2\ 3$ can be the sides of a triangle, and these numbers have (one possible) indices $1\ 2\ 5$. Other choices were also correct, for example (indices): $2\ 3\ 4$ or $2\ 4\ 5$.
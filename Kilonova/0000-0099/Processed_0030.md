
We have a triangular matrix with $n$ rows, containing integer elements. In this matrix, we can build a path following this rule:
- The first element of the path is element $a_{1,1}$
- If the element $a_{i,j}$ is part of the path, then the next element of the path can only be $a_{i+1,j}$ or $a_{i+1,j+1}$, for any $1 \leq j \leq i \leq n$.

The path will be encoded with the column indices, traversing the rows from $1$ to $n$. The value of the path is equal to the sum of the elements that form it.

~[summax.png]

The highlighted path in the example on the right has a value of $5+4+6+5+4=24$, and it is encoded with `1,2,3,3,4`.

Let the set of all maximum value paths be generated in lexicographic order and numbered. For the adjacent example, we have six maximum length paths:
* Path $1$.\t`1 1 1 1 2`     ($5+2+7+6+4=24$)
* Path $2$.\t`1 1 1 2 2`     ($5+2+7+6+4=24$)
* Path $3$.\t`1 2 2 2 2`     ($5+4+5+6+4=24$)
* Path $4$.\t`1 2 3 3 4`     ($5+4+6+5+4=24$)
* Path $5$.\t`1 2 3 4 4`     ($5+4+6+5+4=24$)
* Path $6$.\t`1 2 3 4 5`     ($5+4+6+5+4=24$)

# Task
Given the size and elements of a triangular matrix, and two natural numbers $\text{st}$ and $\text{dr}$ ($\text{st} \leq \text{dr}$), determine:
1. The total number of maximum value paths. If this value exceeds $2\ 000\ 000\ 000$, print the value $2\ 000\ 000\ 001$;
2. The paths with the indices $\text{st}, \text{st}+1, \dots, \text{dr}$.

# Input data
The file `summax.in` contains on the first line a natural number $v$. For all input tests, the number $v$ can only have the value $1$ or $2$.
The second line contains three natural numbers $n$, $\text{st}$, and $\text{dr}$, separated by spaces. The next $n$ lines contain one line of the triangular matrix each: line $i$ contains $i$ elements, namely the values $a_{i,1} a_{i,2} ... a_{i,i}$ for any $1 \leq i \leq n$.

# Output data
If the value of $v$ is $1$, only point $1$ of the task will be solved. In this case, a single natural number representing the number of maximum length paths will be written in the output file `summax.out`.

If the value of $v$ is $2$, only point $2$ of the task will be solved. In this case, in the output file `summax.out`, the encodings of the maximum value paths with the indices $\text{st}, \text{st}+1, \dots, \text{dr}$ will be printed, each on a separate line, with natural numbers separated by spaces.

# Constraints and clarifications
* $1 \leq n \leq 2000$;
* $1 \leq st \leq dr \leq 2\ 000\ 000\ 000$;
* $1 \leq dr – st \leq 1\ 000$;
* The elements of the triangular matrix are strictly positive natural numbers.
* The maximum value of the path does not exceed $1\ 000\ 000\ 000$.

# Example 1
`summax.in`
```
1
5 2 4
5
2 4
7 5 6
6 6 5 5
3 4 3 4 4
```

`summax.out`
```
6
```

## Explanation

For the first example, $v=1$.
The number of maximum value paths is $6$.

# Example 2

`summax.in`
```
2
5 2 4
5
2 4
7 5 6
6 6 5 5
3 4 3 4 4
```

`summax.out`
```
1 1 1 2 2
1 2 2 2 2
1 2 3 3 4
```

## Explanation

For the second example, $v=2$, $st=2$, $dr=4$.
The paths with the indices $2$, $3$, and $4$ were printed.

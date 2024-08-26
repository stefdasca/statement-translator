## Task

Speranța needs to solve an unusual string matching problem. She has a string $A$ of length $N$ consisting of $1$s and $0$s. Given several strings $B$ of length $L$ also consisting of $1$s and $0$s, Speranța wants to know if she can overlay string $B$ somewhere over string $A$ such that no two $1$s overlap. More precisely, for the string $B$, Speranța needs to know if there exists a position $k$ in string $A$ such that $MAX ( A[ k ] + B[ 1 ], A[ k + 1 ] + B[ 2 ], \dots, A[ k + L - 1 ] + B[ L ] ) \leq 1$, where $k + L - 1 \leq N$.

## Input data

The input file `dinti.in` will contain on the first line the numbers $N$, $M$ and $L$ representing the length of string $A$ and respectively the number and length of the strings $B$. The second line will contain string $A$. The next $M$ lines will each contain one string $B$.

## Output data

The output file `dinti.out` will contain $M$ lines representing the answer for each query: print $1$ if string $B$ can overlay string $A$ such that it respects the condition given in the statement, otherwise print $0$.

## Constraints and clarifications

$1 \leq L \leq 20$

$L \leq N \leq 10^6$

$1 \leq M \leq 10^5$

## Example

`dinti.in`
```
15 10 5 
110110100101000 
10101 
11100 
11010 
01110 
01101 
11011 
00111 
10110 
11011 
11000 
```

`dinti.out`
```
1 
0 
1 
0 
1 
0 
1 
1 
0 
1 
```
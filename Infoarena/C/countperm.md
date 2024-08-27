## Countperm

Given a permutation $p$ with $n$ elements. Count how many values $1 \leq a < b < c < d \leq n$ exist such that $p[c] < p[a] < p[d] < p[b]$.

## Input data

The input file `countperm.in` contains two lines. The first line contains $n$. The second line contains the permutation $p$, its elements separated by white space.

## Output data

The output file `countperm.out` will contain the required answer, modulo $10^9+7$.

## Constraints

$1 \leq n \leq 4000$  
$p$ is a permutation, meaning it contains all numbers from $1$ to $n$ exactly once.  
For $20$ points, $n \leq 50$.  
For another $30$ points, $n \leq 700$.  
For another $20$ points, $n \leq 2000$.

## Example

`countperm.in`  
```
5
3 5 1 2 4
```  
`countperm.out`  
```
2
```  

## Explanation

Two sets of numbers fulfill the task. With the values $a, b, c,$ and $d$:  
$1, 2, 3, 5$  
$1, 2, 4, 5$  

`countperm.in`  
```
12
8 2 1 5 10 7 3 11 4 12 6 9
```  
`countperm.out`  
```
18
```  

$18$ sets of numbers fulfill the task. With the values $a, b, c,$ and $d$:  
$1, 5, 6, 12$  
$1, 5, 7, 12$  
$1, 5, 9, 12$  
$1, 5, 11, 12$  
$1, 8, 9, 12$  
$1, 8, 11, 12$  
$1, 10, 11, 12$  
$4, 5, 7, 11$  
$4, 5, 7, 12$  
$4, 5, 9, 11$  
$4, 5, 9, 12$  
$4, 6, 7, 11$  
$4, 6, 9, 11$  
$4, 8, 9, 11$  
$4, 8, 9, 12$  
$6, 8, 9, 12$  
$6, 8, 11, 12$  
$6, 10, 11, 12$
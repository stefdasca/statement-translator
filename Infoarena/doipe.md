# Doipe

For any permutation of $N$ elements, we can determine a sequence of $N-1$ relationships (using $<$ or $>$ relationships). If the $i$-th element of the permutation is smaller than the $(i+1)$-th element, the $i$-th element of the sequence of relationships will be $<$; otherwise, the $i$-th element of the sequence of relationships will be $>$. For example, for the permutation $(1,3,2,4)$ of four elements, we determine the sequence $(<,>,<)$. You need to determine how many permutations of $N$ elements exist that correspond to a given sequence of relationships. We are only interested in the remainder of this number when divided by $29997$.

## Input data

The first line of the file `doipe.in` will contain the number $T$, signifying the number of tests in the file. On the next $2*T$ lines, there will be information about each test. Thus, on line $2*k$ $(1 \leq k \leq T)$, the number $N$ will be found, and on line $2*k+1$ $(1 \leq k \leq T)$, the sequence of relationships.

## Output data

The file `doipe.out` must contain exactly $T$ lines. The $i$-th line must contain the answer for the $i$-th test from the input file.

## Constraints

$1 \leq T \leq 20$

$1 \leq N \leq 2000$

$40\%$ of the test files will have all values of $N$ less than or equal to $16$

$70\%$ of the test files will have all values of $N$ less than or equal to $200$

## Example

`doipe.in`
```
3
2
<
10
<><<<><<<
15
<<>>><><>>><><
```

`doipe.out`
```
1
2896
17401
```
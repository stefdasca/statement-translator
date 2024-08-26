# Pcost

Let there be 2 natural numbers, $A$ and $B$. Let $p_1$, $p_2 \dots p_k$ be the common prime factors in the factorization of the numbers $A$ and $B$. We define the function $pcost(A, B) = p_1^2 + p_2^2 + \dots + p_k^2$. Let there be a sequence of $N$ natural numbers and let $S$ be the sum of the values of the function $pcost$ applied to any 2 elements in the sequence. What is the value of $S$?

## Input data

The input file `pcost.in` contains on its first line the number $N$. The second line contains $N$ natural numbers.

## Output data

The output file `pcost.out` will contain the value of the number $S$.

## Constraints

$1 \leq N \leq 10000$  
The values of the elements in the sequence are $\leq 10^6$.  
Attention! There is a possibility that the answer does not fit in the data type $int$. Please use the data type $long$ $long$.

## Example

`pcost.in`  
```
4  
2 9 15 120  
```

`pcost.out`  
```
56  
```
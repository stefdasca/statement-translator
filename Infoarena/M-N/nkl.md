## Task

We are given a non-zero natural number $N$. A sequence of $K$ non-zero natural numbers $(a_1, a_2, \dots, a_k)$ is called $L$-perfect if the least common multiple of any $L$ numbers from the sequence $(a_1, a_2, \dots, a_k)$ is $N$. We are required to determine the number of ordered sequences of $K$ numbers that are $L$-perfect.

## Input data

The file `nkl.in` contains: 
- the first line contains a natural number $N$ as described above,
- the second line contains a non-zero natural number $Q$,
- the next $Q$ lines contain two numbers $K$ and $L$ separated by a space, as described in the statement.

## Output data

The file `nkl.out` contains $Q$ lines, corresponding to the $Q$ pairs of numbers $K$ and $L$. For each pair, print the number of ordered sequences of size $K$ that are $L$-perfect modulo $10^9 + 7$.

## Constraints and clarifications

$1 \leq N \leq 10^9$  
$1 \leq K, L, Q \leq 1000$  
$L < K$  
For some tests worth 5 points $K = 3$.  
For other tests worth 5 points $L = 2$.  
The problem will be evaluated on tests worth 90 points.

## Example

`nkl.in`
```
6
1
3 2
```

`nkl.out`
```
16
```

`nkl.in`
```
6
1
5 3
```

`nkl.out`
```
256
```

## Explanation

For the first test, the triplets are: $(1, 6, 6), (6, 1, 6), (6, 6, 1), (2, 3, 6), (3, 2, 6), (2, 6, 3), (6, 2, 3), (3, 6, 2), (6, 3, 2), (6, 6, 6), (2, 6, 6), (6, 2, 6), (6, 6, 2), (3, 6, 6), (6, 3, 6), (6, 6, 3)$

The second test is a little more complicated.
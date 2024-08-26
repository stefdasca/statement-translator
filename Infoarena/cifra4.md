# Cifra4

To represent numbers, it was decided to no longer use the digit $C$. Thus, all numbers containing the digit $C$ will be removed from the sequence of natural numbers. We denote the new sequence by $S$.

## Task

1. Determine the $N$-th number in the sequence $S$. 
2. Given $Y$ and $Z$, two natural numbers from the sequence $S$, determine the number of natural numbers eliminated between $Y$ and $Z$. 

## Input data

The input file `cifra4.in` contains on the first line the number $T$ representing the type of task. 
If $T==1$, then the second line will contain, separated by space, the digit $C$ and the number $N$. 
If $T==2$, then the second line will contain, separated by space, the digit $C$ and two natural numbers $Y$ and $Z$. 

## Output data

The output file `cifra4.out` will contain on the first line a single natural number according to the type of task. 

## Constraints

$1 \leq N \leq 10^{13}$

$0 \leq C \leq 9$

$1 \leq Y \leq 10^{13}$

$1 \leq Z \leq 10^{13}$

For 20% of the tests $N$ will have at most 5 digits 

For 20% of the tests $Y$ and $Z$ will have at most 6 digits 

## Example

`cifra4.in` `cifra4.out` 

```
1
0 11
12
```

## Explanation

The 11-th number in the sequence $S$ that does not contain the digit $0$ is 12.

`cifra4.in` `cifra4.out` 

```
2
1 3 20
10
```

## Explanation

The numbers eliminated from the interval $[3;20]$ are $10, 11, 12, 13, 14, 15, 16, 17, 18, 19$. 

`cifra4.in` `cifra4.out` 

```
1
1 1
0
```

## Explanation

The sequence of natural numbers starts with 0.
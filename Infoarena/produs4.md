## Task

Consider $A[1 \dots N]$ an array with $N$ integers. Determine the maximum value of a product formed from 3 factors which are elements from $A[]$. Specifically, determine the maximum $A[i] * A[j] * A[k]$ such that $i$, $j$, and $k$ are pairwise distinct.

## Input data

The input file `produs4.in` contains on the first line the number of tests $T$. The next $T$ lines each contain a test. Each test is specified by $N$, the number of elements in the array $A[]$, followed by the elements of the array $A[]$ separated by space.

## Output data

The output file `produs4.out` should contain $T$ lines with the answers for each test in order.

## Constraints and clarifications

$1 \leq T \leq 20$

$3 \leq N \leq 30000$

$-2000000 \leq A[i] \leq 2000000$ for any $1 \leq i \leq N$

## Example

`produs4.in`

```
1
7 9 -2 8 0 2 11 -8
```

`produs4.out`

```
792
```

## Explanation

$792 = 9 * 8 * 11$
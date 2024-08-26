# Cut-paste-reverse

Given a list of integers $(1, 2, \dots, N)$. On this list, you can perform a series of cut-paste operations. Such an operation involves extracting the subsequence between the values $x$ and $y$ and inserting it immediately after the value $z$ (or at the beginning of the list if $z$ is $0$). This triplet is considered correct if: $x$ appears before $y$ in the list, or $x = y$. $z$ appears outside the subsequence from $x$ to $y$, or $z = 0$. Find a series of correct operations to reverse the list, i.e., to obtain the list $(N, N-1, \dots, 1)$. The fewer operations you use, the higher your score will be.

## Input data

The input file `cpr.in` will contain on the first line the natural number $N$, representing the length of the list.

## Output data

The output file `cpr.out` must contain on the first line the value $M$, representing the number of cut-paste operations. Each of the following $M$ lines must contain three integers $x$, $y$, and $z$, corresponding to the operation.

## Constraints and clarifications

$1 \leq N \leq 5000$

Maximum score will be given on a test if $\dots$

80% of the maximum score will be given on a test if $\dots$

60% of the maximum score will be given on a test if $\dots$

40% of the maximum score will be given on a test if $\dots$

20% of the maximum score will be given on a test if $\dots$

No score will be given if more than $\dots$ operations are used or if the operations do not result in a reversed list.

## Example

`cpr.in`

```
6
```

`cpr.out`

```
4
2 6 0
4 5 0
3 6 4
6 5 0
```

## Explanation

The initial list is $(1 \ 2 \ 3 \ 4 \ 5 \ 6)$. After the first operation, the list becomes $(2 \ 3 \ 4 \ 5 \ 6 \ 1)$ (and the operation $1 \ 1 \ 6$ would have had the same result). After the second operation, the list becomes $(4 \ 5 \ 2 \ 3 \ 6 \ 1)$. After the third operation, the list becomes $(4 \ 3 \ 6 \ 5 \ 2 \ 1)$. After the fourth operation, the list becomes $(6 \ 5 \ 4 \ 3 \ 2 \ 1)$. This solution achieves maximum score, as only $\dots$ operations were performed, and the list was reversed.
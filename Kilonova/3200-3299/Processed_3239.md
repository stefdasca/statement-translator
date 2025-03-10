
# Task

A sequence of integers $a_1, a_2, \dots, a_n$ of length $n$ and a number $x$ are given, and it is guaranteed that each element $a_i$ is odd.

Two types of operations will be performed on this sequence:
1. $l$, $r$, $val$ - add $val$ to all elements $a_l, \dots, a_r$ where $val$ is even;
2. $l$, $r$, $k$ - find the product of the numbers $a_l, \dots, a_r$ modulo $2^k$.

# Input data

The first line contains two integers, $n$ and $q$, representing the length of the sequence and the number of operations.
The second line contains the sequence of numbers $a_1, a_2, \dots, a_n$.
The following $q$ lines correspond to the operations, each having one of the two forms:
* `1 l r val` representing operations of the first type;
* `2 l r k` representing operations of the second type.

# Output data

For each operation of type 2, print a line with its result.

# Constraints and clarifications

* $1 \leq n, q \leq 200\ 000$;
* $1 \leq a_i, val \leq 2^{20}$;
* $k \leq 20$

# Example

`stdin`
```
10 10
969575 741825 24903 1047319 450475 256145 1045323 479255 810659 768323
1 5 6 3034
2 1 10 4
2 1 9 8
2 1 4 20
1 3 6 126904
2 5 5 15
2 9 9 3
1 7 7 853094
1 4 9 1025178
2 5 8 2
```

`stdout`
```
5
119
558151
23357
3
1
```

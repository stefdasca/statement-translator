# Permutations 3

For any set of integers with $N$ elements, a permutation of this set can be defined as a way of arranging the elements of the set. For example, for the set $M=\{4,12,81\}$, we will have the following permutations: $\{ 4 , 12 , 81 \}$, $\{ 4 , 81 , 12 \}$, $\{ 12 , 4 , 81 \}$, $\{ 12 , 81 , 4 \}$, $\{ 81 , 4 , 12 \}$, $\{ 81 , 12 , 4 \}$. In the group formed by all the permutations of a set, an order can be defined such that the elements in the first position are in ascending order, the elements in the second position are in ascending order for the permutations that have the same first element, and so on, as seen in the figure. Such an order is called lexicographical order. Permutations arranged in lexicographical order can be associated with ordinal numbers, in the case of the above example from $1$ to $6$.

## Task

Given a set of integers and a permutation of it, design a program that determines the ordinal number of the permutation in lexicographical order.

## Input data

The input file perm3.in contains:

Values   | Meaning

$N$  | The first line contains $N = number$ of elements in the set
$m_1\ m_2\ m_3\ \dots\ m_N$  | The second line contains the elements of the set, in ascending order
$p_1\ p_2\ p_3\ \dots\ p_N$  | The third line contains the elements of the permutation (the elements $m_1\ m_2\ m_3\ \dots\ m_N$ but in another order)

## Output data

The output file perm3.out will contain the ordinal number of the permutation in lexicographical order.

## Constraints

$1 \leq N \leq 1\ 000$

$1 \leq m_i \leq 2\ 000\ 000\ 000$

## Example

`perm3.in`
```
3
1 23 25
23 1 25
```

`perm3.out`
```
3
```

`perm3.in`
```
4
1 2 3 4
3 4 1 2
```

`perm3.out`
```
17
```
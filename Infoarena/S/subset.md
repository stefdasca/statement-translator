## Subset

Consider the set $\{1,2,\dots,N\}$, which is known to have $2^N$ subsets (including the empty set). Each subset $i$ is assigned a string of elements, namely: the smallest string in lexicographical order, composed of the elements of the subset. For example, the subset $\{1,7,3,5\}$ is assigned the string $1$ $3$ $5$ $7$. All $2^N$ subsets are ordered in the lexicographical order of the associated strings. For example, the subset $\{1,3,4,10\}$ will precede the subset $\{1,4,5\}$ in the given order because the string $1$ $3$ $4$ $10$ precedes $1$ $4$ $5$ lexicographically. If the string associated with a subset with fewer elements matches the first elements of the string associated with a subset with more elements, then the subset with fewer elements is considered to precede the subset with more elements. For example, the subset $\{1,5,8,10\}$ precedes the subset $\{1,5,8,10,13,21\}$. Given the number $N$ of elements in the set, as well as the ordinal number of a subset in the described order, you need to display the string corresponding to the subset with that order number.

## Input data

The input file `subset.in` contains 2 integers, separated by a space, $N$ and $M$, representing the number of elements of the set and the order number of the desired subset.

## Output data

In the output file `subset.out`, you will print on a single line, separated by spaces, the elements of the string associated with the subset at position $M$.

## Constraints

$1 \leq N \leq 60$

The empty set does not interest us, so the first subset will be $\{1\}$. 

Under these conditions, the order number in the input file varies between $1$ and $2^N - 1$ (the last value corresponding exactly to the set $\{N\}$).

This problem has tests divided into 2 groups, worth $30$ and $70$ points respectively.

## Example

`subset.in` 
```
3 3
```

`subset.out` 
```
1 2 3
```

`subset.in` 
```
6 10
```

`subset.out` 
```
1 2 3 6
```
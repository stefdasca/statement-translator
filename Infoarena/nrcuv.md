## Task

Determine how many words of length $N$ can be formed using only lowercase letters of the English alphabet such that any two letters that form a pair in Andrei's list are not on adjacent positions.

## Input data

The first line of the file `nrcuv.in` contains the integers $N$ and $M$, representing the number of letters from which a word is formed and the number of pairs in Andrei's list.

The next $M$ lines contain a pair of the form "$l_1$ $l_2$" where $l_1$ and $l_2$ are lowercase letters of the English alphabet.

## Output data

The file `nrcuv.out` contains on the first line the required number modulo $104659$.

## Constraints and clarifications

$1 \leq N \leq 1000$

$0 \leq M \leq 2000$

There may be symmetric or identical pairs in the list

Two positions are adjacent if the modulus of their difference is $1$

## Example

`nrcuv.in`

```
2 7
a a
a b
b c
c d
c f
b a
c f
```

`nrcuv.out`

```
667
```
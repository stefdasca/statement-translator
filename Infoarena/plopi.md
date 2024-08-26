Poplars

In the city of Iasi, in a certain picturesque area, there are $N$ houses numbered from $1$ to $N$. The houses are connected by streets so that there is a unique path between any two houses. The streets can be traversed in both directions. On each of these streets, there are a certain number of poplars that are over one hundred years old. We say that a path between two houses $A$ and $B$ is odd if the total number of poplars on the streets that connect houses $A$ and $B$ is an odd natural number. Write a program that determines the total number of distinct odd paths.

## Input data

The input file `plopi.in` will contain a natural number $N$ on the first line. On the next $N-1$ lines, there will be three natural numbers $a$ $b$ $c$ separated by a space with the following meaning: there is a street between house $a$ and house $b$ that contains $c$ poplars You are recommended to use $scanf$ for reading in $C++$.

## Output data

The output file `plopi.out` will contain a single line where you will write the total number of distinct odd paths.

## Constraints

$1 \leq N \leq 100000$

$1 \leq a, b \leq N$

$1 \leq c \leq 10000$

Two paths are distinct if there is at least one house that is part of one path and not part of the other.

## Example

`plopi.in`

```
4
1 2 6
2 3 3
2 4 2
```

`plopi.out`

```
3
```

## Explanation

There are three distinct odd paths: between $1$ and $3$ ($9$ poplars) between $3$ and $4$ ($5$ poplars) between $2$ and $3$ ($3$ poplars)
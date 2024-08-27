## Task

Given a set $M$ of natural numbers greater than $1$, determine the number of distinct pairs $(x, y)$ with the following properties:
- $x$ is different from $y$
- $x$ and $y$ belong to the set $M$
- $x$ and $y$ are coprime

## Input data

The file `pairs.in` contains $N$ on the first line, the number of elements in the set $M$. Each of the following $N$ lines contains a natural number that belongs to the set $M$.

## Output data

The first line of the file `pairs.out` contains the number of pairs $(x, y)$ that simultaneously meet all the imposed requirements.

## Constraints

$2 \leq N \leq 100\,000$

$M$ is a set (the numbers in $M$ are pairwise distinct)

The largest number in $M$ does not exceed $1\,000\,000$.

## Example

`pairs.in`
```
5
2
6
15
7
10
```

`pairs.out`
```
5
```

## Explanation

The pairs that meet the properties mentioned in the statement are: $(2, 15)$, $(2, 7)$, $(6, 7)$, $(15, 7)$ and $(7, 10)$.
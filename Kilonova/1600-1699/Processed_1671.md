```markdown
A vector $V$ of $N$ elements from the set $\{0, 1\}$ is given. A subarray is called *linear* if the equation $aU - Z = b$ is true, where $U$ and $Z$ represent the number of elements equal to $1$ and the number of elements equal to $0$ in the subarray, respectively, and $a$ and $b$ are given natural numbers.

# Task
Determine the number of *linear* subarrays in the array $V$.

# Input data

The first line contains $N$, $a$, and $b$ separated by a space. The next line contains $N$ natural numbers, separated by a space, representing the elements of the array $V$.

# Output data

The first line will contain a natural number representing the number of *linear* subarrays in the array $V$.

# Constraints and clarifications

* $1 \leq N \leq 100\ 000$
* $1 \leq a \leq 10\ 000$
* $1 \leq b \leq 1\ 000\ 000\ 000$
|#|Points|Constraints|
|-|-|--------|
|0|0|Examples|
|1|11|$N \leq 100$|
|2|13|$N \leq 2\ 000$|
|3|17|All values in the array $V$ are equal to $1$|
|4|59|No additional constraints|

# Example 1

`stdin`
```
9 1 3
1 0 1 1 1 0 0 1 1
```

`stdout`
```
4
```

## Explanation

The *linear* subarrays are $[1, 0, 1, 1, 1]$, $[1, 1, 1]$, $[1, 1, 1, 0, 0, 1, 1]$ and $[1, 0, 1, 1, 1, 0, 0, 1, 1]$.

# Example 2

`stdin`
```
9 3 8
1 1 1 0 1 0 0 0 1
```

`stdout`
```
4
```

## Explanation

The *linear* subarrays are $[1, 1, 1, 0]$, $[1, 1, 0, 1]$, $[1, 1, 1, 0, 1, 0, 0, 0]$ and $[1, 1, 0, 1, 0, 0, 0, 1]$.

# Example 3

`stdin`
```
5 2 5
1 0 0 1 1
```

`stdout`
```
0
```

## Explanation

There are no *linear* subarrays.
```

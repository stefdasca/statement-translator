
You have just received an array $v$ of $K$ distinct non-zero natural numbers. Starting from this array, you decided to construct an array $w$ of $N$ distinct natural numbers, such that a number $x$ is in the array $w$ if and only if it was initially in the array $v$ or if it can be chosen from at least two numbers in the array $v$ such that $x$ is the greatest common divisor of those numbers.

For example, if $v = [4, 6, 7]$ then $w = [1, 2, 4, 6, 7]$.

Amazed by the beautiful mathematical properties of the new array $w$, you unfortunately forgot the original array $v$ from which you started.

# Task
Given the array $w$, find a possible initial array $v$ with a minimum number of elements.

# Input data
The input file `comun.in` contains on the first line a natural number $N$. The second line contains $N$ distinct non-zero natural numbers, **in strictly increasing order**, representing the array $w$.

# Output data
The output file `comun.out` will contain on the first line the minimum number $K$ of elements in the array $v$. The second line will contain $K$ distinct natural numbers, **in strictly increasing order**, representing the original array.

# Constraints and clarifications

* All values in the input file are non-zero natural numbers less than or equal to $100\ 000$.
* For tests worth 15 points, all values in the input file are less than or equal to $20$.
* For tests worth 50 points, all values in the input file are less than or equal to $2\ 000$.
* It is guaranteed that there is at least one solution.
* If there are multiple initial arrays with the minimum number of elements, any one of them is accepted.

# Example 1

`comun.in`
```
5
1 2 4 6 7
```

`comun.out`
```
3
4 6 7
```

## Explanation

$1 = \text{gcd}(6, 7) = \text{gcd}(4, 6, 7)$
$2 = \text{gcd}(4, 6)$
It can be shown that any other array with the required property has at least $3$ elements.

# Example 2

`comun.in`
```
4
2 4 8 16
```

`comun.out`
```
4
2 4 8 16
```

## Explanation

There is no array with less than $4$ elements that has the required property.

## Task

An integer is called magic if it is divisible by the number of its divisors. For example, $9$ is a magic number because its divisors are $\{1, 3, 9\}$, and $9$ is divisible by $3$, while $10$ is not a magic number because $10$ is not divisible by $4$, its divisors being $\{1, 2, 5, 10\}$. Two integers $X$ and $Y$ are given. Determine how many magic numbers are in the interval $[X, Y]$.

## Input data

The input file `magicnum.in` contains on the first line the integers $X$ and $Y$.

## Output data

The output file `magicnum.out` will contain a single integer representing the number of magic numbers in the interval $[X, Y]$.

## Constraints and clarifications

$1 \leq X \leq Y \leq 1\,000\,000$ 

In $30\%$ of the tests $Y \leq 5\,000$. 

In $60\%$ of the tests $Y \leq 50\,000$.

## Example

`magicnum.in` 
```
4 10
```

`magicnum.out`
```
2
```

## Explanation

The only magic numbers in the interval $[4, 10]$ are $8$ and $9$.
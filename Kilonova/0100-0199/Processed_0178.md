```markdown
Given a natural number `X` consisting of a maximum of `20` digits, all non-zero. Adrian wants to construct, in ascending order of their values, all distinct numbers that can be formed by rearranging the digits of the number `X`. Since `n` is his lucky number, he wants to find the `n`-th number obtained in this manner.

# Task
Write a program that determines the `n`-th number, numbered from `1`, that can be formed from the digits of `X`.

# Input data
The input file `numere.in` contains on the first line the two natural numbers `n` and `X` separated by a single space.

# Output data
The output file `numere.out` will contain on the first line the natural number `Y`, which represents the `n`-th number that can be formed using all the digits of the number `X`. If the `n`-th number generated in ascending order does not exist, it will print `-1`.

# Constraints and clarifications
* For `20%` of the tests `n \leq 200` and `X` has at most `9` digits.
* For the other tests $200 \leq n \leq 3 \cdot 10^{11}$.

# Example 1

`numere.in`
```
2 8264
```

`numere.out`
```
2486
```

## Explanation

Considering the ascending order of value, the first number that can be formed is `2468` and the second `2486`.

# Example 2

`numere.in`
```
3 523525
```

`numere.out`
```
225535
```

## Explanation

The first three numbers formed are: $223555$, $225355$, $225535$.
```

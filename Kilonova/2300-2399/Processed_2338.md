Zăhărel has become passionate about arithmetic expressions. He wrote a sequence of $N$ integers on a piece of paper and wonders what is the maximum value of an expression he can form with these numbers. He will construct an expression following these restrictions:
1. The order in which the numbers appear in the sequence is the same as the order in which they will appear in the expression.
2. Round brackets and the operators `+`, `-`, `*` can be used, representing addition, subtraction, and multiplication respectively. It is considered that `+` and `-` have the same priority, while `*` has the highest priority.
3. Operators must be inserted before any element in the sequence (except before the first element where, if necessary, only the `-` operator can be introduced), but inserting two operators before the same element is not allowed.
4. Brackets can be applied anywhere, provided that the resulting expression is mathematically correct.

# Task

Write a program for Zăhărel that determines the maximum value of an expression he can construct with the $N$ numbers in the sequence.

# Input data

The input file `emax.in` contains on the first line the natural number $N$. The second line contains $N$ integers separated by a space, representing the values in the sequence.

# Output data

The output file `emax.out` will contain a single integer representing the maximum value of an expression that can be constructed with the $N$ numbers in the sequence, modulo $666 \ 013$.

# Constraints and clarifications

* $1 \leq N \leq 100 \ 000$;
* The values in the sequence are integers from the interval $[-100, 100]$.

# Example

`emax.in`
```
4
-1 1 -9 6
```

`emax.out`
```
108
```

## Explanation

$(-1-1) \cdot (-9) \cdot 6 = 108$

~[example.png|alt=Operation example]
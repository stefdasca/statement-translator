Sure, here is the translated text:

We say that three numbers `a, b, c` are in harmonic progression if `b` is the harmonic mean of the numbers `a` and `c`, that is

$$
b = \frac{2}{\frac{1}{a} + \frac{1}{c}} = \frac{2ac}{a+c}
$$

# Task
Given a natural number `b`, determine all pairs of natural numbers `(a, c)` for which `a, b, c` are in harmonic progression.

# Input data
The input file `armonica.in` contains on the first line a natural number `b`. 

# Output data
The output file `armonica.out` will contain on the first line a natural number `n` representing the number of pairs of natural numbers `(a, c)` for which `b` is the harmonic mean. On the next `n` lines, the required pairs of numbers will be printed. Thus, each of the next `n` lines will contain two numbers `a` and `c` separated by a space, meaning that `b` is the harmonic mean of the numbers `a` and `c`.

# Constraints and clarifications
* `1 \leq b \leq 1\ 000\ 000\ 000`;
* For tests worth `40` points, we have `b \leq 1\ 000\ 000`;
* The pairs of numbers in the output file can be printed in any order;
* If `b` is the harmonic mean between two different numbers `a` and `c`, then the pairs `(a,c)` and `(c,a)` are considered distinct solutions.
* The problem will be evaluated on tests worth `90` points.
* `10` points will be given automatically.

# Example

`armonica.in`
```
3
```

`armonica.out`
```
3
3 3
2 6
6 2
```

Explanations
---

The number `3` is the harmonic mean of the numbers `3` and `3`. We have the harmonic progression `(3,3,3)`
The number `3` is the harmonic mean of the numbers `2` and `6`. We have the harmonic progressions `(2,3,6)` and `(6,3,2)
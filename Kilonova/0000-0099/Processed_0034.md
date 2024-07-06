Number `1` can be written in various ways as a sum of fractions with the numerator `1` and the denominator a power of `2`. For example:

$$ \displaystyle 1=\frac{1}{2}+\frac{1}{2}=\frac{1}{2}+\frac{1}{4}+\frac{1}{8}+\frac{1}{8}=\frac{1}{8}+\frac{1}{4}+\frac{1}{2}+\frac{1}{8} $$

Two writings are not considered distinct if they use the same fractions written in a different order. In the example above, the last two writings are not distinct.

# Task
For `N` – a non-zero natural number, determine:
a. A way of writing the number `1` as a sum of exactly `N` fractions with the numerator `1` and the denominator a power of `2`.
b. The number of distinct ways of writing the number `1` as a sum of exactly `N` fractions with the numerator `1` and the denominator a power of `2`. Since this number can be very large, it should be calculated modulo `100003`.

# Input data
The input file `fractii2.in` contains:
The first line contains a natural number `p`. For all input tests, the number `p` can only have the value `1` or the value `2`.
The second line contains a single natural number `N` – representing the number of fractions.

# Output data
If the value of `p` is `1`, only part a) of the task will be solved. In this case, the output file `fractii2.out` will contain, on a single line, `N` natural numbers separated by a space representing the `N` exponents of `2` in the requested writing in the first task. Thus, if the displayed numbers are $m_1,m_2,\ldots,m_N$ then there exists the writing $1=\frac{1}{2^{m_1}}+\frac{1}{2^{m_2}}+\ldots+\frac{1}{2^{m_N}}$.
If the value of `p` is `2`, only part b) of the task will be solved. In this case, the output file `fractii2.out` will contain a natural number representing the answer to the second task, i.e., the number of distinct ways of writing the number `1` as a sum of `N` fractions with the numerator `1` and the denominator a power of `2` (modulo `100003`).

# Constraints and clarifications
* `2 \leq N \leq 2000`
* For the first task, `20%` of the score is awarded.
* For the second task, `80%` of the score is awarded.
* The result for the second task must be displayed modulo `100003`

# Examples

`fractii2.in`
```
1
4
```

`fractii2.out`
```
2 2 2 2
```

`fractii2.in`
```
2
4
```

`fractii2.out`
```
2
```

Explanations
---

For the first test:
`p=1`
$1=\frac{1}{2}+\frac{1}{4}+\frac{1}{8}+\frac{1}{8}=\frac{1}{4}+\frac{1}{4}+\frac{1}{4}+\frac{1}{4}$
The answer corresponds to the second writing but there are other correct answers as well. For example, `3 1 2 3` is considered a correct answer.
**Attention! For this test, only the result for task a) will be displayed.**

For the second test:
`p=2`
$1=\frac{1}{2}+\frac{1}{4}+\frac{1}{8}+\frac{1}{8}=\frac{1}{4}+\frac{1}{4}+\frac{1}{4}+\frac{1}{4}$
These are the only distinct writings.
**Attention! For this test, only the result for task b) will be displayed.**


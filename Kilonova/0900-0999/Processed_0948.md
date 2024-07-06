Sure, here is the translated text:

```
Let $N$ be an odd natural number and $p_1, p_2, p_3, \cdots p_N$ be the first $N$ prime numbers.

Consider the expressions:
* $A = \sqrt{p_1} + \sqrt{p_2} + \sqrt{p_3} + \cdots + \sqrt{p_N}$
* $B = \pm \sqrt{p_1} \pm \sqrt{p_2} \pm \sqrt{p_3} \cdots \pm \sqrt{p_N}$

# Task

Determine a sequence of $N$ signs $\{+, -\}$ for the radicals forming the expression $B$, such that the product $A \cdot B$, after expanding and reducing like terms, contains a minimum number of terms. For example, for $N = 3$, the minimum number of terms of the product $(\sqrt{2} + \sqrt{3} + \sqrt{5}) \cdot (\pm \sqrt{2} \pm \sqrt{3} \pm \sqrt{5})$ will be $1$ and this is achieved when the second expression is $(\sqrt{2} + \sqrt{3} - \sqrt{5})$, so the sequence of signs is ++-.

# Input data

The input file `nmint.in` contains on the first line the odd natural number $N$, as described above.

# Output data

The output file `nmint.out` will contain two lines. The first line will contain the minimum number of terms of the product $A \cdot B$, and the second line a sequence of $N$ characters `+` and `-`, representing the signs of the radicals in the expression B, in order to achieve a minimum number of terms for the product $A \cdot B$.

# Constraints and clarifications

* $3 \leq N \leq 49\ 999$

# Example

`nmint.in`
```
5
```

`nmint.out`
```
4
+-++-
```

## Explanation

The minimum number of terms of the product

$(\sqrt{2} + \sqrt{3} + \sqrt{5} + \sqrt{7} + \sqrt{11}) \cdot (\pm \sqrt{2} \pm \sqrt{3} \pm \sqrt{5} \pm \sqrt{7} \pm \sqrt{11})$

after expanding and reducing like terms is $4$ and one possible sequence of the signs for the terms in the second expression is +-++-, in which case the second expression becomes $(+ \sqrt{2} - \sqrt{3} + \sqrt{5} + \sqrt{7} - \sqrt{11})$
```

Please review the translation to ensure clarity and correctness.
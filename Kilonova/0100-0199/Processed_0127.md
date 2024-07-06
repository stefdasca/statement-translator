It is given two natural numbers `A` and `B`. Let `S` be the sum of all natural divisors of $A^B$.

# Task
We need to display the remainder of the division of `S` by `1 000 000 007`.

# Input data
The first line of the input file `sumdiv.in` contains the two numbers `A` and `B`, separated by at least one space.

# Output data
The first line of the file `sumdiv.out` will contain the remainder of the division of `S` by `1 000 000 007`.

# Constraints
* $ 1 \\le A \\le 10^{12}$
* $ 0 \\le B \\le 10^{18}$
* The constraints and task have been modified

# Example

`sumdiv.in`
```
2 3
```

`sumdiv.out`
```
15
```

Explanation
---
$2^3 = 8$.
The natural divisors of `8` are: `1,2,4,8`. Their sum is `15`.
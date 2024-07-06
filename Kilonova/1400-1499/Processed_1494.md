Certainly! Here is the translated problem statement in English:

---

Two character strings $A$ and $B$ are considered, both strings having the same number of characters.

The following algorithm is applied to the strings:

* The string $A$ is circularly permuted by $k_i$ positions to the left.
* From the two strings, the characters that coincide in terms of position and values are removed.

The algorithm stops either when both strings become empty, or the strings no longer have common characters. The value $k_i$ for each step $i$ represents the $i$-th prime number from the set of prime numbers.

# Task

Given $N$ and $M$, generate the strings $A$ and $B$, both having a length of $N$, so that the number of repetitions of the algorithm applied to the two strings is $M$.

# Input data

The input file `movedel.in` contains on the first line the values $N$ and $M$.

# Output data

In the output file `movedel.out`, write the strings of characters $A$ and $B$ of length $N$, each on a separate line.

# Constraints and clarifications

* The strings must contain only lowercase letters of the English alphabet.
* In the case where the algorithm performs at least $M$ repetitions for the displayed strings, the maximum score for the test will be obtained. Otherwise, $[\frac{X}{M} \cdot 10]$ points will be obtained on the test, where $X$ is the number of repetitions of the algorithm (where $[\frac{X}{M}]$ denotes the integer part of the number $\frac{X}{M}$).
* It is guaranteed that there is a solution for the test data:

| Test | $0$ | $1$ | $2$ | $3$ | $4$ | $5$ | $6$ | $7$ | $8$ | $9$ |
| -    | - | - | - | - | - | - | - | - | - | - |
| $N$  | $23$  | $23$| $50$ | $100$ | $50$ | $100$ | $500$ | $1 \ 000$ | $1 \ 550$ | $2 \ 000$ |
| $M$  | $50$ | $107$| $250$ | $160$ | $100$ | $700$ | $1 \ 500$ | $8 \ 000$ | $12 \ 000$ | $16 \ 000$ |

# Example 1

`movedel.in`
```
3 5
```

`movedel.out`
```
abc
cba
```

## Explanation

**First application of the algorithm:**

`cab` - after permuting to the left by $2$ positions ($2$ - first prime number), after removing the common characters, the two strings will be:

* `ab`
* `ba`

**Second application of the algorithm:**

`ba` - after permuting to the left by $3$ positions ($3$ – second prime number), after removing the common characters, the two strings become empty, and the algorithm ends.

Thus, $[\frac{2}{5} \cdot 10] = 4$ points are obtained for this test.

# Example 2

`movedel.in`
```
5 5
```

`movedel.out`
```
abcde
edabc
```

## Explanation

For the found strings, the algorithm ends after $20$ steps.

Thus, $10$ points are obtained.

---

Please review it to ensure there are no remaining issues.
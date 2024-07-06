Sure, here is the translated competitive programming problem statement in English:

Since K.L 2.0 fell in love, he sees everything more beautifully. Thus, he defines a sequence of lowercase English letters as *beautiful* if it has the ASCII codes of the characters in a non-zero arithmetic progression. Then K.L 2.0 defines a string of lowercase English letters, which **does not contain two identical adjacent characters**, as being *$K$-beautiful* if it can be divided into $K$ beautiful subarrays, but cannot be divided into $K-1$ beautiful subarrays.

# Task

Determine how many strings of length $N$ are $K$-beautiful. Because this number is quite large, you have to calculate it modulo $666 \ 013$.

# Input data

The input file `frumos.in` contains on the first line the positive natural numbers $N$ and $K$, separated by a space, with the meaning from the text.

# Output data

The output file `frumos.out` will contain on the first line the required number, modulo $666 \ 013$.

# Constraints and clarifications

* $1 \leq K \leq N \leq 100$
* Strings do not contain two identical adjacent characters.
* A beautiful subarray can consist of a single character.
* The strings contain only lowercase English alphabet letters: `a`, `b`, `c`, $\dots$, `z`.
* A string is counted only once, even if there are multiple ways to divide it into $K$ beautiful subarrays.

# Example

`frumos.in`
```
2 1
```

`frumos.out`
```
650
```

## Explanation

The strings of length $2$ that divide into exactly one beautiful group are all strings of length $2$ except those of the form $aa, bb, cc, \dots, zz$. Thus, there are $26^2 - 26 = 650$ $1$-beautiful strings of length $2$.

---

Please double-check for grammar and syntax:

- **Task**: clear and precise.
- **Input data**: adequate use of "contains" for readability.
- **Output data**: clear and correct.
- **Constraints and clarifications**: well-structured and easy to understand.
- **Example and Explanation**: numbers are exact and consistent with the original.

This should be fully correct and conforming to the given rules.
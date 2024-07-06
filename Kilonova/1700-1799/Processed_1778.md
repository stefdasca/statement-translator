```markdown
A sequence with $n$ elements $x_1, x_2, \dots, x_n$ is called a **palindrome** if it is identical to the sequence $x_n, x_{n-1}, \dots, x_1$. A **subsequence of the sequence** $x$ is defined as a subset of elements of the sequence $x$ that are not necessarily in successive positions, where the relative positions between any two elements are preserved: $x_{i_1}, x_{i_2}, \dots, x_{i_k}$, with $1 \leq i_1 < i_2 < \dots < i_k \leq n$. We will call $i_1, i_2, \dots, i_k$ the _index sequence_. Two subsequences are considered **distinct** if their corresponding index sequences differ by at least one element. For example, for the sequence $x = (1, 3, 5, 6, 3, 5, 1)$, the subsequence $(1, 3, 5)$ can correspond to three distinct subsequences $(x_1, x_2, x_3)$, $(x_1, x_2, x_6)$, $(x_1, x_5, x_6)$, but it cannot correspond to the subsequence $(x_1, x_5, x_3)$, because in this case, the relative position of elements $x_3$ and $x_5$ is reversed. The subsequence $(x_1, x_2, x_3, x_5, x_7)$ = $(1, 3, 5, 3, 1)$ is a palindromic subsequence.

# Task

Given the elements of a sequence, calculate the maximum length of a palindromic subsequence and the number of distinct subsequences of maximum length.

# Input data

The input file `maxpal.in` contains two lines. The first line contains a natural number representing the value of $n$, and the next line contains the $n$ elements of the sequence $x$, separated by a space.

# Output data

The output file `maxpal.out` will contain on a single line two natural numbers separated by a space; the first will represent the maximum length of a palindromic subsequence and the second the remainder when dividing the number of distinct palindromic subsequences of maximum length by the number $666\ 013$.

# Constraints and clarifications

* $3 \leq n \leq 2\ 000$
* $0 \leq x_i \leq 255$
* For a correct answer to the first task, $30\%$ of the score is awarded, and for the second $70\%$

# Example 1

`maxpal.in`
```
5
2 1 4 2 2
```

`maxpal.out`
```
3 5
```

## Explanation

The longest palindromic subsequence has a length of $3$. We have $5$ distinct solutions:

$(x_1, x_2, x_4) = (2, 1, 2)$
$(x_1, x_2, x_5) = (2, 1, 2)$
$(x_1, x_3, x_4) = (2, 4, 2)$
$(x_1, x_3, x_5) = (2, 4, 2)$
$(x_1, x_4, x_5) = (2, 2, 2)$
```


```markdown
# Task

Trraian went on a trip for his birthday. He arrived in the land of **Factoria** where he received a gift from the wizard **Factorios**. That gift contained an array $a$ of $n$ numbers $a_1, a_2,\ldots,a_n$ and a number $k$. To prevent Factorios from taking Trraian's array, he asked the following question: "How many subarrays of the array $a$ you received have the property that the product of the numbers in the subarray is divisible by the factorial of $k$?". Trraian really wants to keep the array, but he does not know how to answer Factorios' question, so he asks you to help him answer the question and he will be very grateful to you.

**Definitions:** A subarray of an array $a$ is a sequence of numbers that appear in consecutive positions in $a$. The factorial of a number $k$ is equal to $1 \cdot 2 \cdot 3 \cdot \ldots \cdot k$ and is denoted by $k!$.

# Input data

The input file `factoria.in` contains two natural numbers $n$ and $k$ on the first line. The second line contains the $n$ natural numbers $a_1, a_2, \ldots, a_n$.

# Output data

The output file `factoria.out` will contain a single integer, the answer to Factorios' question.

# Constraints and clarifications

* $1 \leq n \leq 200\ 000$
* $1 \leq k \leq 10^6$
* $1 \leq a_i \leq 10^6$ for $i$ from $1$ to $n$.

# Example

`factoria.in`
```
6 4
3 8 24 48 5 7
```

`factoria.out`
```
16
```

## Explanation

The 16 subarrays are: $[3, 8]$, $[3, 8, 24]$, $[3, 8, 24, 48]$, $[3, 8, 24, 48, 5]$, $[3, 8, 24, 48, 5, 7]$, $[8, 24]$, $[8, 24, 48]$, $[8, 24, 48, 5]$, $[8, 24, 48, 5, 7]$, $[24]$, $[24, 48]$, $[24, 48, 5]$, $[24, 48, 5, 7]$, $[48]$, $[48, 5]$, $[48, 5, 7]$
```
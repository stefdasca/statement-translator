Here is the translated text according to the specified instructions:

---

A sequence $x_1, x_2, \dots, x_n$ of $n$ distinct natural numbers, considered two by two. For a sequence of $k$ numbers ($x_p, x_{p+1}, \dots, x_{p+k-1}$), which starts with the number at position $p$ in the given sequence, we define its degree as the number of numbers in the sequence that remain in the same positions after sorting the sequence in ascending order. For example, for $n=7$ and the sequence formed by the numbers: $1, 5, 7, 4, 6, 2, 9$, the sequence formed by the numbers $7, 4, 6, 2$ (corresponding to $p=3$ and $k=4$) has a degree equal to $2$ because, after sorting the numbers in the sequence in ascending order, it becomes $2, 4, 6, 7$, with the numbers $4$ and $6$ remaining in the same positions.

# Task

Write a program that reads the numbers $n$, $k$, $x_1$, $x_2$, $ \dots$, $x_n$, with the meaning from the statement, and then determines:

1. the degree of the entire sequence of numbers;
2. the position of the first element of the first subarray of length $k$ that has the maximum degree, as well as the degree of this subarray.

# Input data

The input file `grad.in` contains on the first line the numbers $n$ and $k$, separated by a space, and on the next line $n$ distinct natural numbers $x_1$, $x_2$, $ \dots$, $x_n$, corresponding to the sequence of numbers, separated by a space.

# Output data

The output file `grad.out` will contain on the first line a natural number representing the degree of the entire sequence of numbers, and on the next line two natural numbers, separated by a single space, the first number representing the position of the first element in the first subarray of length $k$ that has the maximum degree and the second number representing the degree of this subarray.

# Constraints and clarifications

* $0 < n \leq 10 \ 000$
* $0 < k \leq n$
* The numbers in the array are strictly less than $32 \ 000$.
* A subarray of numbers from the sequence represents a succession of numbers from that sequence, located at consecutive positions.
* The degree of the entire sequence of numbers is equal to the degree of the subarray of $n$ numbers that starts with the number at position $1$ and contains all $n$ numbers from the sequence.
* For a correct solution to subpoint 1, $40\%$ of the score is awarded.
* To determine the position of the first element in the first subarray of length $k$ that has the maximum degree, $20\%$ of the score is awarded, and for determining the maximum degree at subpoint 2, $40\%$ of the score is awarded.

# Example

`grad.in`
```
7 4
1 5 7 4 6 2 9
```

`grad.out`
```
3
3 2
```

---

Please review and ensure that any potential grammar or syntax errors are corrected according to the rules of the English language.
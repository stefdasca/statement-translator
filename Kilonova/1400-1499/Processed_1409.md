# Task

Mihai received as a gift a calculator that can determine the number of divisors of a natural number. The only problem is that the calculator's display allows him to work only with numbers composed of at most $K$ digits. Because at school they work with large natural numbers, meaning numbers with many digits, Mihai decided that for a large number he would proceed as follows: find the number of divisors of the number formed only by the first $K$ digits of the given number. The number displayed as a result is completed by appending next digits from the initial number to its right, until he again obtains a number composed of $K$ digits. For this new number, he finds the number of divisors and repeats the procedure until he exhausts the digits of the initial number.
Even if at some point he no longer has digits to complete the number displayed as a result, Mihai continues to use the calculator and determines the number of its divisors, continuing until he reaches a number that is equal to its number of divisors.

# Task

Given a natural number with $N$ digits and a calculator that can process numbers with at most $K$ digits, Mihai asks for your help to find answers to the following questions:
1. For how many numbers with at most $K$ digits will the calculator be used to determine the number of divisors, following exactly the procedure described above?
2. What is the value that represents the maximum number of divisors obtained as a result of Mihai's calculations?
3. What is the number with the most divisors in the series of numbers processed by Mihai? If there are multiple numbers with the same maximum number of divisors, the smallest one will be chosen.

# Input Data

The first line of the file `divizori.in` contains two natural numbers $N$ and $K$ separated by a single space, representing the number of digits of the initial natural number, and the number of digits of the calculator's display, respectively. The second line of the file `divizori.in` contains the natural number with $N$ digits that Mihai will process following exactly the procedure described above.

# Output Data

The output file `divizori.out` will contain three lines:
* The first line will contain a single natural number representing the number of successive applications of the procedure to find the number of divisors described above.
* The second line will contain a single natural number representing the maximum number of divisors.
* The third line will contain a single natural number representing the smallest number whose number of divisors is equal to the maximum number of divisors determined previously.

# Constraints and Clarifications

* $2 \leq K \leq 9$
* $2 \leq N \lt 1 \ 000 \ 000$
* For $40\%$ of tests, $N \leq 50 \ 000$ and $K \leq 6$
* If the number displayed on the first line of the output file is correct, $40\%$ of the test score is awarded. If the number displayed on the second line of the output file is correct, $40\%$ of the test score is awarded. For correctly displaying the value on the third line of the output file, $20\%$ of the test score is awarded.

# Example

`divizori.in`
```
43 5
5874392065432987667890567800123450889987543
```

`divizori.out`
```
16
48
12012
```

## Explanation

The $16$ processed numbers are: $58743$, $\\bold{12}920$, $\\bold{32}654$, $\\bold{8}3298$, $\\bold{8}7667$, $\\bold{4}8905$, $\\bold{4}6780$, $\\bold{12}012$, $\\bold{48}345$, $\\bold{16}088$, $\\bold{8}9987$, $\\bold{6}543$, $\\bold{6}$, $\\bold{4}$, $\\bold{3}$, $\\bold{2}$.
Among these, the number $12012$ has the most divisors $(48)$.
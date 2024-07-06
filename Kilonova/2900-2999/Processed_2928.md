Here is the translated text:

---
Given $n$ and a sequence $a_1, a_2, \dots a_n$ of natural numbers. Initially, all numbers are colored in $\textcolor{red}{red}$. In one operation, you can choose a $\textcolor{red}{red}$ number and make it $\textcolor{blue}{blue}$.

# Task

Find the minimum number of operations needed so that the sum of the $\textcolor{blue}{blue}$ numbers is **strictly** greater than the sum of the $\textcolor{red}{red}$ numbers.

# Input data

The input file ```ra.in``` contains the number $n$ on the first line. The second line contains the sequence $a_1, a_2, \dots, a_n$.

# Output data

Print to the output file ```ra.out``` the minimum number of operations needed so that the sum of the blue numbers is strictly greater than the sum of the red numbers.

# Constraints and clarifications

* $2 \leq n \leq 10 \ 000$
* $1 \leq a_i \leq 10^9$ 

|#|Points|Constraints|
|-|-|----------|
|1|60|$a_i \leq 1 \ 000$|
|2|40|No additional constraints|

# Example 1
`ra.in`
```
5
2 4 2 6 7
```
`ra.out`
```
2
```

## Explanation

For the first example, initially, the sequence looks like this: $\textcolor{red}{2 \ 4 \ 2 \ 6 \ 7}$.

The sum of the red values is $2 + 4 + 2 + 6 + 7 = 21$.

The sum of the blue values is $0$ (because we haven't colored any element blue yet).

In the first operation, we will choose the element in the second position and color it blue.

Now our sequence looks like this: $\textcolor{red}{2} \ \textcolor{blue}{4} \ \textcolor{red}{2 \ 6 \ 7}$. The sum of the red values is $2 + 2 + 6 + 7 = 17$, and the sum of the blue values is $4$.

In the second operation, we will choose the element in the last position and color it blue.

The sequence becomes: $\textcolor{red}{2} \ \textcolor{blue}{4} \ \textcolor{red}{2 \ 6} \ \textcolor{blue}{7}$. The sum of the red values is $2 + 2 + 6 = 10$ and the sum of the blue values is $4 + 7 = 11$. Therefore, the sum of the $\textcolor{blue}{blue}$ values is **strictly** greater than the $\textcolor{red}{red}$ ones.

We observe that if we had colored the numbers $6$ and $7$ blue, we would obtain another solution with $2$ operations.

# Example 2
`ra.in`
```
10
6 3 8 4 5 6 5 5 7 5
```
`ra.out`
```
5
```

## Explanation

For the second example, we obtain a solution with $5$ operations if we color the values $8$, $7$, $6$, $6$, $5$ (notice that only one of the $5$ values will be colored blue).


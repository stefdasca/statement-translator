Ionel received a task from his teacher: to write the numbers from 1 to $ n $ on paper. Since the number $ n $ was quite large, he got bored and started counting how many times a certain digit appeared in the numbers that needed to be written. Since counting was a fairly slow activity, he found a simple method to calculate how many times a digit appeared in all printed numbers.

# Task

Write a program that, reading the number $ n $ and a non-zero digit $ c $, displays the number of occurrences of the digit $ c $ in the representation of all numbers from 1 to $ n $.

# Input data

The input file `cifre.in` contains on the first line two integers, $ n $ and $ c $.

# Output data

The output file `cifre.out` will contain on the first line a single integer, the number of occurrences of the digit $ c $ in the representation of all numbers from $ 1 $ to $ n $.

# Constraints and clarifications

* $ 1 \leq n \leq 10^9 $;
* $ 1 \leq c \leq 9 $;

# Example

`cifre.in`
```
15 1
```

`cifre.out`
```
8
```

## Explanation

In the sequence $1 \ 2 \ 3 \ 4 \ 5 \ 6 \ 7 \ 8 \ 9 \ 10 \ 11 \ 12 \ 13 \ 14 \ 15$, the digit $1$ appears 8 times.
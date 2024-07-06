Here is the translated text:

Gigel received a set of $n$ boxes of weights that are not necessarily distinct for safekeeping. He weighed the boxes and for each distinct weight, he noted on a sheet, in ascending order of weights, the number of boxes with that respective weight.

Since his younger brother had the bad habit of playing with the numbers he wrote on the sheet, Gigel thought to calculate a "control number" according to the following algorithm: starting from the first number, he grouped the occurrence numbers of the weights in groups of three (if some numbers remain ungrouped at the end, he ignores them). If in a group there are only even numbers or only odd numbers, he notes the group with the digit $1$, otherwise he notes it with the digit $0$. From the sequence obtained in this way, a number is formed which has the tens digit equal to the number of $1$ values and the units digit equal to the number of $0$ values, thus obtaining the "control number."

# Task

Reading the weights of the boxes, determine the "control number" and check if it is a prime number.

# Input data

The input file `control.in` contains on the first line the number $n$. The next $n$ lines each contain a natural number representing the weights of the $n$ boxes.

# Output data

The output file `control.out` will contain on the first line the "control number", followed, on the second line, by the value $0$ or $1$. On the second line, print $1$ if the number is a prime number, otherwise $0$.

# Constraints and clarifications

* $1 \leq n \leq 100$;
* Each weight is a natural number, less than or equal to $200$.

# Example

`control.in`
```
21
1
3
2
6
2
6
2
8
9
8
8
9
10
8
11
18
11
12
14
15
17
```

`control.out`
```
31
1
```

## Explanation

After sorting, the sequence is: $1 \ 2 \ 2 \ 2 \ 3 \ 6 \ 6 \ 8 \ 8 \ 8 \ 8 \ 9 \ 9 \ 10 \ 11 \ 11 \ 12 \ 14 \ 15 \ 17 \ 18$;
Then it becomes: $1 \ 3 \ 1 \ 2 \ 4 \ 2 \ 1 \ 2 \ 1 \ 1 \ 1 \ 1 \ 1$;
Grouping them in threes from left to right, we get: $1 \ 1 \ 0 \ 1$;
From the values $1 \ 1 \ 0 \ 1$; the control number $31$ is obtained, which is a prime number.
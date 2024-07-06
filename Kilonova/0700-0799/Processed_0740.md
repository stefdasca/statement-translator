```markdown
Given the natural number $k$. We want to obtain a one-dimensional array $a$, with natural elements constituted as follows: $a_1 =$ a two-digit number (the tens digit of $a_1$ is the hundreds digit of the product $k \cdot k$, and the units digit of $a_1$ is the tens digit of the product $k \cdot k$).

For $i > 1$, $a_i$ is obtained as follows: $a_i =$ a two-digit number (the tens digit of $a_i$ is the hundreds digit of the product $a_{i-1} \cdot a_{i-1}$, and the units digit of $a_i$ is the tens digit of the product $a_{i-1} \cdot a_{i-1}$).

The process of generating the terms of the array ends when a number that has already been generated before is generated. The last number (the one that repeats) is not part of the array.

It is possible that the numbers called "two-digit" in the text may actually have only one digit, if their tens digit is $0$; they can even be $0$.

# Task

Write a program that:

1. displays the elements of the obtained array;
2. displays the elements of the obtained array, but sorted in ascending order by their first digit (the leftmost one).

# Input data

The input file `sir.in` contains $k$ on the first line.

# Output data

* The first line of the output file `sir.out` will contain the elements of the array $a$, in the order of their generation, separated by a space.
* The second line will contain the elements of the array $a$, in the order required by the second task; the elements will be separated by a space.

# Constraints and clarifications

* $11 \leq k \leq 999$;
* For the second task: if two or more elements of the array $a$ have the same first digit, then these elements can be displayed in any order that respects the requirement. In the example below, the output for the second task could also be in the form: $0 \ 2 \ 25 \ 5 \ 62 \ 84$, meaning that we swapped $2$ with $25$, because both have the first digit $2$ in this case, other display possibilities are not more than these.
* Correct resolution of the first task will account for $60\%$ of the score, and the second task will account for the remaining $40\%$ of the score.

# Example

`sir.in`
```
16
```

`sir.out`
```
25 62 84 5 2 0
0 25 2 5 62 84
```

## Explanation

Task 1:
- $k \cdot k = 16 \cdot 16 = 256$; $a_1 = 25$;
- $25 \cdot 25 = 625$; $a_2 = 62$;
- $62 \cdot 62 = 3844$; $a_3 = 84$;
- $84 \cdot 84 = 7056$; $a_4 = 5$;
- $5 \cdot 5 = 25$; $a_5 = 2$;
- $2 \cdot 2 = 4$; $a_6 = 0$;
- $0 \cdot 0 = 0$ and here the generation of the array with 6 elements stops, which will be displayed.

Task 2:
- $a_1 = 25$; its first digit is $2$;
- $a_2 = 62$; its first digit is $6$;
- $a_3 = 84$; its first digit is $8$;
- $a_4 = 5$; its first digit is $5$;
- $a_5 = 2$; its first digit is $2$;
- $a_6 = 0$; its first digit is $0$.
- After sorting these first digits: $2$ (associated with $a_1$), $6$ (associated with $a_2$), $8$ (associated with $a_3$), $5$ (associated with $a_4$), $2$ (associated with $a_5$) and $0$ (associated with $a_6$), the new order of these numbers is obtained: $0, 2, 2, 5, 6, 8$, respectively associated with the elements of the array $a$: $0, 25, 2, 5, 62, 84$; the elements of $a$ will be displayed in this order, or in the order: $0, 2, 25, 5, 62, 84$.
```
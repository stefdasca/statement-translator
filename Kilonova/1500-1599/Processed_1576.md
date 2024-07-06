```markdown
A powerful number is a natural number greater than $1$ which has the property that if it is divisible by the prime number $p$, then it is also divisible by $p^2$. For example, $36$ and $27$ are powerful numbers, while $12$ is not a powerful number because it is divisible by $3$ and not by $3^2$. During math class, the students learned what a powerful number means. To check if the students understood, the teacher wrote a sequence of $N$ natural numbers $X_1, X_2, \dots, X_N$ on the board and asked Mihai to erase the powerful numbers from the sequence.

By analyzing the remaining numbers, Mihai noticed that a powerful number can be obtained by concatenating two numbers from the remaining sequence, numbers that are equally distanced from the ends of this new sequence. Concatenation involves appending the number from the second half of the sequence to the end of the number in the first half. If the new sequence has an odd number of elements, the middle element is ignored. For example, if the sequence obtained after erasing the powerful numbers is: $12, 1, 19, 13, 3, 21, 5$, then the numbers obtained by concatenation are $125$, $121$, $193$.

# Task

Write a program that reads a natural number $N$ and then a sequence of $N$ natural numbers and determines:
1. How many powerful numbers are in the given sequence;
2. Which pairs of numbers from the sequence remaining after erasing the powerful numbers, equally distanced from the ends of the sequence, form a powerful number when concatenated.

# Input data

The input file `puternic.in` contains on the first line a natural number $C$. For all input tests, the number $C$ can only have the values $1$ or $2$. The second line of the file contains the natural number $N$. The third line contains $N$ natural numbers separated by a space.

# Output data

If $C = 1$, solve Task $1$. In this case, the output file `puternic.out` will contain on the first line a natural number representing the number of powerful numbers in the given sequence.

If $C = 2$, solve Task $2$. In this case, the output file `puternic.out` will contain pairs of numbers equally distanced from the ends of the sequence obtained after erasure, whose concatenation forms a powerful number. Each pair is written on a separate line, and the numbers in the pair are separated by a space, the first number being the one on the left. If there are multiple such pairs, they will be displayed, in order, starting with the one closest to the ends of the new sequence. If there is no such pair, the file `puternic.out` will display $-1$.

# Constraints and clarifications

* $1 \leq N \leq 100\ 000$;
* $1 \leq X_1, X_2, \dots, X_N \leq 1\ 000\ 000\ 000$;
* Correct resolution of the first task earns $30$ points, and correct resolution of the second task earns $70$ points.

# Example 1

`puternic.in`
```
1
8
100 28 16 11 484 25 162 27
```

`puternic.out`
```
5
```

## Explanation

Task one is solved. The powerful numbers are $100 \\ 16 \\ 484 \\ 25 \\ 27$.

# Example 2

`puternic.in`
```
2
11
12 9 1 8 19 6 3 4 49 21 5
```

`puternic.out`
```
12 5
1 21
```

## Explanation

Task two is solved using only value $N$. After erasing the powerful numbers, the remaining sequence is: $12 \\ 1 \\ 19 \\ 6 \\ 3 \\ 21 \\ 5$.
```

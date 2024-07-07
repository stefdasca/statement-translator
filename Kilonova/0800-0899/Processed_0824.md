Certainly! Below is the translated competitive programming problem statement:

```markdown
A triangle consisting of natural numbers written on $n$ lines, as shown in the adjacent figure, is considered. The lines of the triangle are numbered from $1$ to $n$, starting with the line from the base of the triangle (the bottom line), and the positions on the line are numbered starting with $1$ from left to right.
Each number in the triangle, except those on line $1$, is equal to the sum of the numbers immediately below it, to its left and right.

~[triunghi.png|width=20em]

# Task

Knowing one number from each line of the triangle, determine all the numbers on line $1$.

# Input data

The input file `triunghi.in` contains on the first line the natural number $n$ representing the number of lines in the triangle. On the next $n$ lines, the information about the triangle is described. More precisely, on line $i$ of the $n$ lines, there are two natural numbers separated by space $p_i \ v_i$ indicating the position and the value of the known number on line $i$ of the triangle.

# Output data

The output file `triunghi.out` will contain a single line with $n$ natural numbers separated by a space, representing from left to right the numbers written on line $1$ of the triangle.

# Constraints and clarifications

* $1 \leq n \leq 1\ 000$;
* $1 \leq p_i \leq n+1-i$;
* All numbers in the triangle are natural numbers with at most $18$ digits.

# Example

`triunghi.in`
```
5
4 4
2 5
3 13
2 25
1 45
```

`triunghi.out`
```
1 2 3 4 2
```

## Explanation

The triangle is:

```
      45
    20  25
   8  12 13
  3  5  7  6
 1  2  3  4  2
 ```

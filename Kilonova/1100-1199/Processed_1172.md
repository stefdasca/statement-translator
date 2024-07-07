
The physical education teacher of class VI-B from a school in Focșani wants, at the beginning of the class, to arrange the students on the sports field, in a specific order. For this, the students are well trained so that, by arranging $n$ students in the last row, the other rows of students are created automatically according to the rule:

- on position $i$ of a row, a student will be placed as follows: if in the back row, in positions $i$ and $i+1$, there are either only boys or only girls, then a girl will be placed. If there are students of the opposite sex in these positions, a boy will be placed.

According to this rule, on row number $i$, there will be $i$ students. The number of students in the class is $\\frac{n \\cdot (n+1)}{2}$.

# Task

Given $n$ and a sequence of $n$ numbers $0$ and $1$ ($0$ represents the encoding for a girl, and $1$ for a boy), which represents the sequence of students in the last row, determine the number of boys in the class.

# Input data

The first line of the input file `sport.in` will contain $n$. The second line will contain $n$ natural numbers, representing the sequence of students in the last row.

# Output data

The first line of the output file `sport.out` will contain the number of boys in the class.

# Constraints and clarifications

* $1 \\leq n \\leq 10 \\ 000$;
* Tests and constraints have been modified.

# Example

`sport.in`
```
5
1 0 0 1 1
```

`sport.out`
```
8
```

## Explanation

```
1 0 0 1 1   row 5 (last row)
 1 0 1 0    row 4
  1 1 1     row 3
   0 0      row 2
    0       row 1
```

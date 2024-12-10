Director of a school wants to reward the best students at the end of the school year. For this purpose, he has two problems to solve:

1. Determine how many students will be rewarded out of the $n$ students in the school. After intense discussions with other teachers, it was decided in the Faculty Council that the number of rewarded students should be $n - k$, where $k$ is the largest perfect square strictly less than $n$. For example, for $n = 150$, $k$ is $144$ (because $144 = 12^2$), so $150 - 144 = 6$ students will be rewarded.
2. To maintain as much calm as possible during the award ceremony, the Faculty Council decided that the students who will not be rewarded should be seated on the sports field in rows of $p$ students each (where $p^2 = k$). For this purpose, the director numbered the non-rewarded students from $1$ to $k$ and decided that the students should be seated in descending order of the associated numbers.

# Task

Write a program that reads $n$, the number of students in the school, and calculates the number of rewarded students as well as the arrangement of the non-rewarded students.

# Input data

The input file `lascoala.in` will contain the number $n$.

# Output data

The output file `lascoala.out` will contain on the first line the number of rewarded students, and on the following lines the arrangement of the non-rewarded students.

# Constraints and clarifications

* $2 \leq n \leq 700$;

# Example

`lascoala.in`
```
35
```

`lascoala.out`
```
10
25 24 23 22 21
20 19 18 17 16
15 14 13 12 11
10 9 8 7 6
5 4 3 2 1
```

## Explanation

The largest perfect square less than $n$ is $25 = 5^2$.
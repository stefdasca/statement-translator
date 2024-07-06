For the next school year, the admission of the $N$ students to high school will be based on complex evaluations. Each of the future ninth-grade students will receive, following the tests and exams they will take, a score (a non-zero natural number) with which they will participate in the electronic admission process.

The allocation of each student to classes is done in the order of registration respecting the criteria:

* The first student is allocated to class number $1$.
* In the class where a student is allocated, there is no score higher than theirs until the moment of their allocation.
* The number of classes should be as small as possible.

# Task

Determine:

1. The score of the first student who can no longer be allocated to the first class if all students wish to be allocated to the first class (applies only to task $1$).
2. The number of classes that will be formed respecting the criteria.

# Input data

The input file `adlic.in` contains in the first line the number $C$, which can have the value $1$ or $2$, followed by a space and the natural number $N$.

The following lines contain the $N$ scores of the students in the order of registration, non-zero natural numbers separated by a space.

# Output data

If $C=1$, then the output file `adlic.out` will contain the solution for task $1$.

If $C=2$, then the output file `adlic.out` will contain the solution for task $2$.

# Constraints and clarifications

* $1 \leq N \leq 1\ 000\ 000$
* The students' scores will have at most six digits
* For task $1$, the existence of the solution is guaranteed
* For $20$% of the points, the requirement will be $C = 1$
* For another $20$% of the points, the requirement will be $C = 2$ and $N \leq 1000$
* For the rest of the tests $C = 2$ and $N \leq 1\ 000\ 000$

# Example 1

`adlic.in`
```
1 9
4 2 4 2 7 10 9 11 8
```

`adlic.out`
```
2
```

## Explanation

$4$ is allocated to the first class, while $2$ must be allocated to the second class.

# Example 2

`adlic.in`
```
2 9
4 2 4 2 7 10 9 11 8
```

`adlic.out`
```
3
```

## Explanation

A possible solution is one in which classes are formed as:

1. $(4, \ 4, \ 7, \ 9)$
2. $(2, \ 2, \ 10, \ 11)$
3. $(8)$
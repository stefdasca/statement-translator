
Gigel is passionate about triangles. He collects sticks of different lengths and assembles them into various triangles. Yesterday, he had $6$ sticks with lengths $5$, $2$, $7$, $3$, $12$, and $3$. From these sticks, Gigel constructed a triangle with sides $3$, $3$, and $5$, while the sticks of lengths $2$, $7$, and $12$ remained unused because these lengths cannot form the sides of a triangle.

~[0.png]

For this reason, Gigel decided to make a collection of sticks such that, regardless of how you choose $3$ elements, they cannot form the sides of a triangle; we shall call this property the anti-triangle property. Gigel, starting from the initial set of lengths $2, 7, 12$, thought of two methods to create a collection of $5$ sticks with the anti-triangle property:

1. Keep the shortest stick, the one of length $2$, and create a new set by adding other sticks of length greater than or equal to the initial one. For example, the following $5$ lengths are correct: $2, 2, 12, 50, 30$.
2. Keep all the sticks, namely $2, 7, 12$, and complete them with other sticks of different lengths (shorter or longer), such that the anti-triangle property remains. The following $5$ lengths respect the anti-triangle property: $2, 7, 12, 4, 1$.

# Task

Given a sequence of $n$ non-zero natural numbers $a_1, a_2, ..., a_n$ having the anti-triangle property, and a number $k$ ($k>n$), construct a sequence of $k$ natural numbers having the anti-triangle property, according to one of the following two restrictions:

1. **Variant 1**: The smallest element is identical to the smallest element in the initial sequence.
2. **Variant 2**: Among the $k$ elements of the constructed sequence, all elements of the initial sequence are included.

# Input data

The input file `triunghi.in` contains on the first line the values of the numbers $v, n$ and $k$, separated by space. The next line contains $n$ natural numbers separated by space, forming a sequence with the anti-triangle property.

# Output data

The output file `triunghi.out` will contain $k$ numbers on a single line.

If the value of $v$ is $1$, then the file will contain $k$ natural numbers with the anti-triangle property, separated by space, in which the smallest element is identical to the minimum of the sequence given in the input file.

If the value of $v$ is $2$, then the file will contain $k$ natural numbers with the anti-triangle property, separated by space, among which all the elements of the initial sequence are included.

# Constraints and clarifications

* $3 \leq n < k \leq 46$
* $1 \leq$ length of a stick $\leq 2\ 000\ 000\ 000$
* Correctly solving the first task awards $30$ points, while solving the second task awards $70$ points.
* It is guaranteed that there is always a solution.
* The solution is not unique - any correct answer is accepted.

# Example 1

`triunghi.in`
```
1 3 5
7 2 12
```

`triunghi.out`
```
2 2 30 50 12
```

## Explanation

$v=1$, $n=3$, $k=5$.  
In variant $1$ we need to print $5$ numbers, the minimum value is $2$ in both sequences.

# Example 2

`triunghi.in`
```
2 3 5
7 2 12
```

`triunghi.out`
```
1 4 12 7 2
```

## Explanation

$v=2$, $n=3$, $k=5$.  
In variant $2$ among the printed sequence elements, all elements of the initial sequence are included.

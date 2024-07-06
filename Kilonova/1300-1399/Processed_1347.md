```markdown
The digital map of the battlefield is stored in a two-dimensional array with $N$ rows, $M$ columns, and elements from the set \\{$0,1$}. The value $0$ represents a free position, and the value $1$ represents a position occupied by an obstacle. Each element located on the contour of the array, that is, on the first row, first column, last row, and last column, contains enemy objectives. Only zero elements are found on the contour of the array.

Inside the array (elements that are not on the contour), in a free position, a soldier must be placed. His goal is to annihilate as many enemy objectives as possible. Unfortunately, he has a laser weapon with which he can perform only a single attack. When launching the attack, 4 rays are sent, one in each of the 4 diagonal directions. A ray can go until it encounters an obstacle (in which case it stops and has no effect) or until it reaches the contour (in this case it destroys the respective enemy objective).

# Task

Write a program that determines the maximum number of enemy objectives, denoted by $K$, that can be destroyed in a single attack, as well as the number of positions where we can place the soldier to destroy $K$ enemy objectives.

# Input data

The input file `raze.in` contains on the first line the natural number $T$, representing the number of input data sets. For each set of input data in the input file, the first line of the set contains the natural numbers $N$ and $M$, separated by a space, representing the number of rows and the number of columns of the array respectively; on the next $N$ lines of the data set there are $M$ natural numbers from the set \\{$0,1$}, separated by a space, representing the digital form of the battlefield map.

# Output data

The output file `raze.out` will contain $T$ lines, corresponding to the $T$ input data sets. Each line will print two natural numbers $K$ and $P$, separated by a space, representing the maximum number of enemy objectives destroyed in the attack, and the number of positions from which $K$ enemy objectives can be destroyed.

# Constraints and clarifications

* $1 \leq T \leq 80$
* $3 \leq N, M \leq 135$
* It is guaranteed that there is at least one enemy objective that can be annihilated for each input data set.

# Example

`raze.in`
```
2
4 6
0 0 0 0 0 0
0 0 1 1 1 0
0 0 0 0 0 0
0 0 0 0 0 0
4 7
0 0 0 0 0 0 0
0 1 1 1 1 1 0
0 0 0 0 0 0 0
0 0 0 0 0 0 0
```

`raze.out`
```
4 1
3 2
```

## Explanation

The file contains two input data sets.
In the first data set, a maximum of $4$ enemy objectives can be annihilated by positioning the soldier in row $2$ and column $2$.
In the second data set, a maximum of $3$ enemy objectives can be annihilated by positioning the soldier in the element at row $3$ and column $2$ or in the element at row $3$ and column $6$.
```
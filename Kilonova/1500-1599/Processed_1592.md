The Mayor of city $X$ wants to have modern public lighting. For this, he creates a sketch in the form of a square with $n$ rows and $n$ columns in which each element located at the intersection of a row with a column represents a neighborhood.

The Mayor has calculated for each neighborhood what the number of public lighting poles in that neighborhood is. Each pole has a single light bulb which is initially turned on. He noticed an interesting thing: all neighborhoods have a different number of lighting poles, and the maximum value of the number of poles in a neighborhood is $n^2$.

To be executed as efficiently as possible, turning off the light bulbs is done in the following way:

* In the first stage, the light bulbs in the neighborhood with the maximum number of lighting poles are turned off, which leads to the turning off of the light bulbs in the neighborhoods on the same row as well as in those on the same column as the neighborhood with the maximum number of lighting poles.
* The procedure is repeated at each stage for all neighborhoods where the light bulbs have not been turned off, until only one illuminated neighborhood remains.

# Task

Knowing the non-zero natural numbers $n$ and $k$, as well as the number of lighting poles in each neighborhood, determine:

1. How many lighting poles are in the neighborhood with the maximum number of lighting poles at stage $k$ of the light bulb-turning-off procedure?
2. How many light bulbs are turned off, in total, at stage $k$?
3. What is the maximum number of lit bulbs in a square area of the city of size $k \times k$ before starting to turn off the bulbs?

# Input data

The input file `iluminat.in` contains on the first line a digit $c$ ($1, 2$, or $3$), representing the required task. The next line contains two non-zero natural numbers $n$ and $k$, separated by a space. On the next $n$ lines are $n^2$ distinct natural numbers, $n$ on each line, separated by a space, with the meaning from the statement.

# Output data

In the output file `iluminat.out`, the answer will be displayed according to the task:

* if $c = 1$, print on the first line a single number representing the number of lighting poles in the neighborhood with the maximum number of lighting poles at stage $k$
* if $c = 2$, print on the first line a single number representing how many light bulbs are turned off, in total, at stage $k$
* if $c = 3$, print the maximum number of lit bulbs in a square area of size $k \times k$ before turning off the bulbs

# Constraints and clarifications

* $c \in \{1, 2, 3\}$
* $1 \leq k < n \leq 1\ 000$
* The number of light bulbs in each neighborhood is less than or equal to $n^2$

|#|Score|Constraints|
|-|-|--------|
|1|28|$c = 1$|
|2|28|$c = 2$|
|3|36|$c = 3$|

# Example 1

`iluminat.in`
```
1
4 2
1 2 3 4
16 13 5 6
12 9 7 14
10 11 8 15
```

`iluminat.out`
```
15
```

## Explanation

The task is $1$. The light bulbs in the neighborhood having $16$ lighting poles are turned off, which leads to the turning off of the light bulbs from the poles in row $2$ and in column $1$. The grid becomes:

```
0  2  3  4
0  0  0  0
0  9  7 14
0 11  8 15
```

In the second stage, the first neighborhood in which the light bulbs are turned off has $15$ lighting poles.

# Example 2

`iluminat.in`
```
2
4 2
1 2 3 4
16 13 5 6
12 9 7 14
10 11 8 15
```

`iluminat.out`
```
52
```

## Explanation

The task is $2$. The light bulbs in the neighborhood having $16$ lighting poles are turned off, which leads to the turning off of the light bulbs from the poles in row $2$ and in column $1$. The grid becomes:

```
0  2  3  4
0  0  0  0
0  9  7 14
0 11  8 15
```

In the second stage, the first neighborhood in which the light bulbs are turned off has $15$ lighting poles, which leads to the turning off of the light bulbs in row $4$ and in column $4$ in the new grid. This becomes:

```
0 2 3 0
0 0 0 0
0 9 7 0
0 0 0 0
```

The total number of light bulbs turned off at stage $k=2$ is: $15+11+8+14+4=52$.

# Example 3

`iluminat.in`
```
3
4 2
1 2 3 4
16 13 5 6
12 9 7 14
10 11 8 15
```

`iluminat.out`
```
50
```

## Explanation

The task is $3$. The maximum number of lit bulbs in a square area of the city of size $2 \cdot 2$ is $50$, in the area with the upper-left corner at row $2$ and column $2$

```
16 13
12  9
```
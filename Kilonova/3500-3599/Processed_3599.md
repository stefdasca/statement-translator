
~[poza.png|align=right]

Three spaceships, each carrying $n$ aliens from three different galaxies (Galaxia Algorithma, Nebulosa Recursiv, and Calea Protocol), have arrived at the Informatics Olympiad in the galaxy Calea Informateea. 
To celebrate this occasion, all the aliens want to take a group photo together. The heights of the aliens are **very diverse**, ranging from nanometers to kilometers. For this reason, to ensure that all can be seen in the photo, the aliens must stand in **three rows**: 
* **First row**: The shortest aliens (in decreasing order of height from left to right).
* **Second row**: Aliens of intermediate height ordered decreasingly from left to right
* **Third row**: The tallest aliens ordered decreasingly from left to right.

# Task

Given the natural number $C$ representing the task number, a natural number $n$ representing the number of aliens in each spaceship, and then three sequences of $n$ non-zero natural numbers each with a maximum of $9$ digits, write a program that solves the following tasks: 
1. If $C=1$, then determine the maximum and minimum height of the aliens from all $3$ spaceships.
2. If $C=2$, then determine the order of the aliens in the photo, in each of the three rows, from left to right, ordered decreasingly by height.

# Input data

The input file `poza.in` contains on the first line the number $C$ representing the task ($1$ or $2$) and the natural number $n$, and on the following three lines each a sequence of $n$ numbers, the values on the same line being separated by a space.

# Output data

If the task $C=1$, then the first line of the output file `poza.out` will contain two natural numbers separated by a space representing the maximum and minimum height of all the aliens from the $3$ spaceships.  

If the task $C=2$, then the output file `poza.out` will contain three sequences with $n$ natural number values representing the heights of the aliens, starting with the shortest, each sequence being written on a single row. On each row, the aliens will be arranged from left to right, in decreasing order of height, the values on each row being separated by a space.

# Constraints and clarifications

* $1 \leq n \leq 10^5$, $1 \leq c \leq 2$;
* $1 \leq a_i \leq 10^9$ (It is ensured that there will not be more than $n$ aliens with the same height) 
* For $20$ points the task is $1$.  
* For $20$ points the task is $2$ and $n \leq 1 \ 000$;
* For another $50$ points the task will be $2$, and $n \gt 1 \ 000$;
* $10$ points are awarded outright.

# Example 1

`poza.in`
```
1 4 
13 20 24 3
12 100 100 2
17 18 98 23
```

`poza.out`
```
100 2
```

## Explanation

The maximum height is $100$ and the minimum height is $2$.

# Example 2

`poza.in`
```
2 4 
24 20 13 3
100 100 12 2
98 23 18 17
```

`poza.out`
```
13 12 3 2
23 20 18 17
100 100 98 24
```

## Explanation

The first line contains the shortest aliens, ordered decreasingly from left to right. On the next line are the aliens of medium height ordered decreasingly from left to right and on the last line are the tallest aliens.

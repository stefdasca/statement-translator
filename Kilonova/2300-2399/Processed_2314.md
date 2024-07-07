
Andreea and Ioana have arrived in Tinichea County and want to visit as many tourist attractions as possible. Tinichea County is made up of $N$ cities, between some of which there are bidirectional roads. Specifically, any road directly connects two cities, and the roads are arranged such that there is a unique path between any two cities in the county. A path is a sequence of cities such that between any two consecutive cities on the path, there is a road connecting them. The cities are numbered from $1$ to $N$, and for each city, $C_i$ is known, the number of tourist attractions in city $i$.

Because they have had a small argument lately, the two girls each want to choose a path such that the number of attractions Andreea visits combined with the number of attractions Ioana visits is maximized. The conditions the girls impose are that their paths must not share any cities and that any city is visited at most once.

# Task

Determine for the two girls the maximum total number of attractions they can visit, respecting the conditions in the task statement.

# Input data

The input file `turism.in` will contain $12$ sets of input data. The first line of a set of input data will contain the natural number $N$, representing the number of cities. The next line of the data set will contain $N$ natural numbers $C_1 \\ C_2 \\ C_3 \\dots C_{N-1} \\ C_N$, representing, in order, the number of tourist attractions in each city. This is followed by $N-1$ lines containing two distinct natural numbers $A \\ B$, indicating that there is a road between cities $A$ and $B$. The values on the same line are separated by a space.

# Output data

The output file `turism.out` will contain $12$ lines, where line $i$ contains the answer for the $i$-th set of input data.

# Constraints and clarifications

* $2 \leq N \leq 100\ 000$
* $1 \leq C_i \leq 9\ 999 (1 \leq i \leq N)$
* For $20\%$ of the tests $2 \leq N \leq 100$
* For $20\%$ of the tests $101 \leq N \leq 800$
* All the numbers in the input file are natural numbers.

# Example

`turism.in`
```
2
1 1 
1 2
...
3
1 2 3
1 2
1 3
```

`turism.out`
```
2
...
6
```

## Explanation

The input file must contain $12$ tests, in the example only the first and the last of the $12$ are presented.
For the first test, there are $2$ cities, each with one tourist attraction. There is a single road (from $1$ to $2$). The optimal solution is $2$ (each girl visits one city).
For the last test, there are $3$ cities, having $1$, $2$, and $3$ tourist attractions, respectively, and $2$ roads (between $1$ and $2$, and between $1$ and $3$). The optimal solution is $6$. 
The ellipsis `...` indicates that the other $10$ tests are missing.

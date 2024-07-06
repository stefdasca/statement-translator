The tulips in Sun Park have been numbered from $1$ to $n$. A bouquet is desired to be formed, containing at least one flower, and two consecutively numbered flowers should not be in the bouquet.

# Task

Given $n$, the number of flowers, determine in how many ways the bouquet can be formed.

# Input data

The input file `flori.in` contains on the first line a natural number $n$, representing the number of flowers.

# Output data

The output file `flori.out` contains on the first line a natural number that represents the number of bouquets $mod \\ 9 \\ 001$.

# Constraints and clarifications

* $1 \\leq n \\leq 10 \\ 000$
* For $30$% of the tests $n$ is less than or equal to $26$
* For $60$% of the tests $n$ is less than or equal to $1 \\ 000$

# Example 1

`flori.in`
```
5
```
`flori.out`
```
12
```

# Explanation

Possible bouquets are: $\\{ 1 \\}, \\{ 2 \\}, \\{ 3 \\}, \\{ 4 \\}, \\{ 5 \\}, \\{ 1, 3 \\}, \\{ 1,4 \\}, \\{ 1,5 \\}, \\{ 1, 3, 5 \\}, \\{ 2, 4 \\}, \\{ 2, 5 \\}, \\{ 3, 5 \\}$

# Example 2

`flori.in`
```
7
```
`flori.out`
```
33
```

# Explanation

Possible bouquets are: $\\{ 1 \\}, \\{ 2 \\}, \\{ 3 \\}, \\{ 4 \\}, \\{ 5 \\}, \\{ 6 \\}, \\{ 7 \\}, \\{ 1, 3 \\}, \\{ 1,4 \\}, \\{ 1,5 \\}, \\{ 1,6 \\}, \\{ 1,7 \\},\\{ 1,3,5 \\}, \\{ 1,3,6 \\}, \\{ 1,3,7 \\},$

$\\{ 1,4,6 \\}, \\{ 1,4,7 \\},\\{ 1,5,7 \\}, \\{ 1,3,5,7 \\}, \\{ 2, 4 \\}, \\{ 2, 5 \\}, \\{ 2,6 \\},\\{ 2,7 \\},$ 

$\\{ 2,4,6 \\}, \\{ 2,4,7 \\}, \\{ 2,5,7 \\}, \\{ 3, 5 \\}, \\{ 3,6 \\},\\{ 3,7 \\}, \\{ 3,5,7 \\}, \\{ 4,6 \\},\\{ 4,7 \\}, \\{ 5,7 \\}$
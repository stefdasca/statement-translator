A recognized international company has opened two chocolate factories and $n$ distribution centers in the city. The factories produce a single type of chocolate and use only one box model as packaging. Being an efficient company but concerned about reducing pollution in the city, only one car is used for the weekly delivery of orders to the distribution centers. The transport costs of a box of chocolate from each of the two factories to each center have been estimated. Each week, the cumulative production of the two factories exactly meets the demands of the $n$ centers.

# Task

Write a program that calculates the minimum weekly transport cost for delivering orders to the $n$ distribution centers, knowing the quantities produced by the two factories, the demand of each distribution center, and the transport costs of a box of chocolate from each factory to each center.

# Input data

The input file `centre.in` contains:

* The first line contains: $n$ – the number of centers, $x_1$ – the number of boxes of chocolate produced by the first factory, and $x_2$ – the number of boxes of chocolate produced by the second factory, separated by a space.
* The second line contains $n$ non-zero natural numbers $c_1, c_2, \dots, c_n$ representing the demands of the $n$ distribution centers; $c_i$ is the number of boxes of chocolate requested by distribution center $i$.
* The third line contains $n$ non-zero natural numbers representing the transport costs of a box from the first factory to each of the $n$ centers $cost_{1, 1}, cost_{1, 2}, \dots, cost_{1, n}$.
* The fourth line contains $n$ non-zero natural numbers representing the transport costs of a box from the second factory to each of the $n$ centers $cost_{2, 1}, cost_{2, 2}, \dots, cost_{2, n}$.

# Output data

The output file `centre.out` will contain a single line which will contain a natural number representing the minimum weekly transport cost, to meet the demands of all $n$ distribution centers.

# Constraints and clarifications

* $1 < n \leq 200$
* $1 \leq c_i \leq 20$
* $1 < x_1, x_2 < 4\ 000$
* $n \leq x_1 + x_2$
* $c_1 + c_2 + \dots + c_n = x_1 + x_2$
* $0 < cost_{i, j} \leq 1\ 000$, $1 \leq i \leq n$, $1 \leq j \leq n$

# Example

`centre.in`
```
3 5 6
3 4 4 
5 2 3
5 3 4 
```

`centre.out`
```
38
```

## Explanation

One possible solution would be $cost_{1, 1} \cdot 0 + cost_{1, 2} \cdot 4 + cost_{1, 3} \cdot 1 + cost_{2, 1} \cdot 3 + cost_{2, 2} \cdot 0 + cost_{2, 3} \cdot 3 = 5 \cdot 0 + 2 \cdot 4 + 3 \cdot 1 + 5 \cdot 3 + 3 \cdot 0 + 4 \cdot 3 = 38$.
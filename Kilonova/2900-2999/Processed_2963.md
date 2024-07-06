# Task

As it is a wonderful Saturday, Cais decides to go to the restaurant Burger and Drink, where there is an All you can eat offer. He has two places beside him where he can stack plates with food (A and B). Cais knows that $N$ dishes will come on the conveyor belt, the dish with index $i$ arriving at second $s[i]$, and he will choose one of the two stacks and place the plate on top of it. At time $t[i]$, Cais will want to eat the dish from plate $i$ and will take it down from the top of the stack. He cannot eat a dish unless it is placed on top of a stack at the chosen time. Cais, being passionate about combinatorics, wonders: "In how many ways can I arrange the plates with dishes on the two stacks so that I can eat all $N$?" 
Since the number can be very large, he only wants the remainder modulo $1 \ 000 \ 000 \ 007$.

# Input data

The first line of the input file `cais.in` contains an integer, $N$.
The $i+1$th line contains $s[i]$ and $t[i]$ with the significance from the statement.

# Output data

The first line of the output file `cais.out` will contain a single integer, the number of ways to arrange the plates.

# Constraints and clarifications

* $1 \leq N \leq 1 \ 000 \ 000$;
* The sequence $s + t$ forms a permutation of the numbers from $1$ to $2N$
* for $12$ points $N \leq 10$
* for another $21$ points $N \leq 2 \ 000$
* for another $48$ points $N \leq 100 \ 000$

# Example 1

`cais.in`
```
4
1 3
2 5
4 8
6 7
```

`cais.out`
```
4
```

## Explanation

`ABAA`, `ABAB`, `BABA`, `BABB`

# Example 2

`cais.in`
```
3
1 4
2 5
3 6
```

`cais.out`
```
0
```

## Explanation

There is no solution. Cais is upset.
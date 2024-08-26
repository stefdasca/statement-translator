# Mezzaluna

Dorin has an infinite Olympic pizza crust stretching along the $OX$ axis. He noticed that the more often he cuts the pizza crust, the better it tastes. Thus, given a set of $N$ open intervals, each interval representing a cut he can make, your goal is to determine the maximum number of cuts Dorin can make. Formally, Dorin can select an interval to cut in one of the following 2 cases: 

1. The current crust is infinite. By cutting with a new interval $(C, D)$, the crust takes the shape of this interval.
2. The current crust is an interval $(A, B)$. We can select a new interval $(C, D)$ only if it reduces the current interval. Formally, if the intersection of $(A, B)$ and $(C, D)$ is an interval $(X, Y)$, it must be non-empty and must differ from the interval $(A, B)$. The new crust will take the shape of the interval $(X, Y)$. 

Note that since the intervals are open, the interval $(X, X)$ is considered empty. Given $N$ and the set of $N$ intervals with which we can cut the crust, determine the maximum number of cuts we can make as well as the number of ways in which we can achieve this maximum cut count. Two ways of cutting the crust are considered distinct if the sets of intermediate intervals through which the form of the crust passes during the cutting process are distinct. Note that it is possible for a certain set of intermediate intervals to be obtained through series of operations using different intervals from the $N$ provided, but it will be counted only once.

## Input data

The input file `mezzaluna.in` will contain on the first line a natural number $N$. The next $N$ lines will each contain 2 natural numbers $[A, B]$ representing the $N$ intervals.

## Output data

The output file `mezzaluna.out` will contain 2 natural numbers, the maximum number of cuts we can obtain, as well as the number of ways we can achieve this maximum, modulo $1.000.000.007$.

## Constraints 

$1 \leq A < B \leq 2000$

$1 \leq N \leq 100000$

For tests worth 30 points, it is guaranteed that $N \leq 200$

Correctly solving the first task is worth $40\%$ of the test score

## Example

`mezzaluna.in`
```
4 
1 4 
1 3 
2 4 
2 3
```

`mezzaluna.out`
```
3 2
```
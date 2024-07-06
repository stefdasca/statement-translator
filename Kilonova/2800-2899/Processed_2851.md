# Task

In the midst of a pandemic, researchers at an institute want to conduct a series of experiments on cell cultures. It has already been observed that the researched cell has a linear growth dependent on the three previous days: if two days ago we had $x$ cells, yesterday we had $y$ and today we have $z$ cells, then tomorrow we will have $x+ay+bz$ cells. If on any given day the number of cells exceeds a value $k$, the researchers reduce the culture to the value modulo $K$.

If, for a given $n$, the number of cells on days $n$, $n-1$, $n-2$ is known and the multiplication factors $a$ and $b$ are known, what is the number of cells that need to be cultivated in the first $3$ days of the experiment?

# Input data

The input file `pandemia.in` contains multiple data sets. The first line contains an integer $T$ representing the number of experiments for which the answer is required. The next $T$ lines contain the experiments: six integers separated by spaces, in the following order: $N$, $A$, $B$, $U$, $V$, $W$, where $N$ is the number of days of the experiment, $A$ and $B$ are the multiplication factors from the statement, and $U$, $V$, and $W$ represent the number of bacteria on days $N$, $N-1$, and respectively $N-2$.

# Output data

The output file `pandemia.out` will contain $T$ lines with the answers, in order, to the $T$ experiments from the input file, namely three natural numbers less than $K$ separated by a space, representing the number of bacteria on day $0$, day $1$, and respectively day $2$ (in this order).

# Constraints and clarifications

* $1 \leq T \leq 50, 3 \leq N \leq 100\ 000$, where $T, N$ are natural numbers
* $1 \leq A, B \leq 100, 1 \leq U, V, W < K$, where $A$, $B$, $U$, $V$, $W$ are natural numbers
* $K = 10\ 000\ 007$
* The first day is considered day $0$

# Example

`pandemia.in`
```
2
6 1 1 37 20 11
5 1 2 58 23 9
```

`pandemia.out`
```
1 2 3
1 2 3
```

## Explanation

Test 1: Indeed, if:
* day $0: 1$ cell
* day $1: 2$ cells
* day $2: 3$ cells

then:
* day $3: 1 + 1 \cdot 2 + 1 \cdot 3 = 6$ cells
* day $4: 2 + 1 \cdot 3 + 1 \cdot 6 = 11$ cells
* day $5: 3 + 1 \cdot 6 + 1 \cdot 11 = 20$ cells
* day $6: 6 + 1 \cdot 11 + 1 \cdot 20 = 37$ cells

Test 2: Indeed, if:
* day $0: 1$ cell
* day $1: 2$ cells
* day $2: 3$ cells

then:
* day $3: 1 + 1 \cdot 2 + 2 \cdot 3 = 9$ cells
* day $4: 2 + 1 \cdot 3 + 2 \cdot 9 = 23$ cells
* day $5: 3 + 1 \cdot 9 + 2 \cdot 23 = 58$ cells
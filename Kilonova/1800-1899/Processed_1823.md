
Baxibilian, while learning computer science, discovered the game _Loopover_. This game can be described by the following rules:

* The game is played on a square board of $n \times n$ cells, where both rows and columns are numbered from $1$;
* In the initial state of the board, each cell contains a number from $1$ to $n^2$, such that $M_{i,j} = (i - 1) \cdot n + j$;
* Four types of operations can be applied to the board any number of times:
    - `L x` - All values in the cells of row $x$ will move cyclically to the left by one unit, meaning $M_{x,i} = M_{x,i+1}$ for $i < n$ and $M_{x,n} = M_{x,1}$.
    - `R x` - All values in the cells of row $x$ will move cyclically to the right by one unit, meaning $M_{x,i} = M_{x,i-1}$ for $i > 1$ and $M_{x,1} = M_{x,n}$.
    - `U x` - All values in the cells of column $x$ will move cyclically up by one unit, meaning $M_{i,x} = M_{i+1,x}$ for $i < n$ and $M_{n,x} = M_{1,x}$.
    - `D x` - All values in the cells of column $x$ will move cyclically down by one unit, meaning $M_{i,x} = M_{i-1,x}$ for $i > 1$ and $M_{1,x} = M_{n,x}$.

# Task

Since Baxibilian doesn't have much time to analyze the _Loopover_ game as he needs to study, he wants to know the following things:
* Given the state of a board where only row operations or only column operations have been applied, what is the minimum number of operations that Baxibilian should apply to return to the initial state?
* Given a sequence of $m$ operations, what is the minimum number of applications of this sequence to a board of size $n \cdot n$ in the initial state so that the final state is the same as the initial state? Since the result can be very large, Baxibilian is satisfied to know only the remainder when this number is divided by $1 \ 000 \ 000 \ 007$.

# Input data

The first line of the `loopover.in` file will contain two numbers separated by a space: $t$, the task to be solved, and $n$, the dimension of the board.

Next:
- If $t = 1$, the next $n$ lines will contain $n$ numbers each, separated by a space, representing the configuration of the board.
- If $t = 2`, the second line will contain a single number $m$, and the next $m$ lines will contain, separated by a space, a character $c_i \in \{$`L`$, `R`$, `U`$, `D`$}$ representing the type of operation and a number $x_i$ representing the index of the row or column to which operation $i$ is applied.

# Output data

In the `loopover.out` file, the output will be according to the task:
* If $t = 1$, a single number representing the minimum number of operations to bring the board back to the initial state.
* If $t = 2$, a single number representing the remainder when the minimum number of applications of the sequence of operations on the board to return to the initial state is divided by $1 \ 000 \ 000 \ 007$.

# Constraints and clarifications

* $2 \leq n \leq 1 \ 000$
* $1 \leq m \leq 1 \ 000$
* $t \in \{1, 2\}$
* $1 \leq x_i \leq n$ for any $1 \leq i \leq m$

|#|Points|Constraints|
|-|-|--------|
|1|6|$t = 1$, $2 \leq n \leq 100$|
|2|13|$t = 1$|
|3|9|$t = 2$, $2 \leq n \leq 100$, $1 \leq m \leq 100$ and the minimum number of applications of the sequence $\leq 10 \ 000$|
|4|51|$t = 2$, $2 \leq n \leq 100$, $1 \leq m \leq 100$ and the minimum number of applications of the sequence $\leq 1 \ 000 \ 000$|
|5|21|$t = 2$|

# Example 1

`loopover.in`
```
1 4
2  3  4  1
8  5  6  7
11 12 9  10
13 14 15 16
```

`loopover.out`
```
4
```

## Explanation

The operations that need to be applied are:
$R \ 1$
$L \ 2$
$L \ 3$
$L \ 3$

# Example 2

`loopover.in`
```
1 3
7 8 6
1 2 9
4 5 3
```

`loopover.out`
```
3
```

## Explanation

The operations that need to be applied are:
$U \ 1$
$U \ 2$
$D \ 3$

# Example 3

`loopover.in`
```
2 3
5
U 1
R 1
U 2
R 1
L 2
```

`loopover.out`
```
6
```

## Explanation

After applying the sequence of $5$ operations, the matrix obtained by Baxibilian is:
```
2 3 5 
8 6 7 
1 4 9 
```
The minimum number of applications of the sequence to reach the identity matrix is $6$.

# Example 4

`loopover.in`
```
2 8
10
R 6
L 8
R 4
U 3
L 3
L 1
R 3
U 5
U 6
U 3
```

`loopover.out`
```
4284
```

## Explanation

$4 \ 284$ applications of the sequence are needed to return to the initial state.

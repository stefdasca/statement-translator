In a game of dominoes, each piece is divided into two areas, each containing a natural number. If the game has size $d$, all distinct pieces that can be formed with numbers between $0$ and $d$ will exist.

Two pieces are considered *identical* if they have the same numbers, regardless of their order. For example, the pieces $(3,7)$ and $(7,3)$ are identical. For example, the game with size $d=2$ will have $6$ distinct pieces:

$\\boxed{0}\\boxed{0}$, $\\boxed{0}\\boxed{1}$, $\\boxed{0}\\boxed{2}$, $\\boxed{1}\\boxed{1}$, $\\boxed{1}\\boxed{2}$, $\\boxed{2}\\boxed{2}$.

The sum of all the numbers on these pieces is $12$. The problem has two tasks:
1. Given an array of $N$ non-zero natural numbers representing the sizes of some domino games, determine for each game the sum of all the numbers written on the pieces of that game.
2. Given an array of $N$ non-zero natural numbers representing the sums of all the numbers on the pieces of some domino games, first build a sequence of digits, denoted with $A$, by writing in order all the numbers from the given array, without spaces between them. Build a strictly increasing sequence of natural numbers, denoted with $B$, by alternating through the digits of $A$ from left to right and from right to left as follows:
    * The first number in $B$ is formed from the first digit in sequence $A$;
    * The second number in $B$ is constructed by concatenating (joining) digits from $A$, starting from right to left, until a number strictly greater than the first number in $B$ is obtained;
    * The third number in $B$ is constructed by concatenating digits from $A$ from left to right (starting with the first digit that has not already been used), until a number strictly greater than the previous number in $B$ is obtained;
    * The fourth number in $B$ is constructed again by concatenating digits from $A$ from right to left (starting with the rightmost digit that has not already been used), until a number strictly greater than the third number in $B$ is obtained;
    * Continue this way alternately, until no number strictly greater than the last number added in $B$ can be formed.

# Task

Write a program that resolves tasks $1$ and $2$ described in the statement.

# Input data

The input file `domino.in` contains on the first line a natural number $C$ representing the task that needs to be solved ($1$ or $2$). The second line contains the natural number $N$. The third line contains $N$ non-zero natural numbers separated by spaces $d_1$, $d_2$, $\\dots$, $d_N$.

# Output data

The output file `domino.out` will contain a single line:
- If $C=1$, the first line will contain $N$ natural numbers separated by spaces; the $i$-th number displayed represents the sum of the numbers in the domino game with size $d_i$ ($1 \\leq i \\leq N$).
- If $C=2$, the first line will contain in order, separated by spaces, the values of the sequence $B$ determined according to the rules from the statement.

# Constraints and clarifications

* $1 \\leq N \\leq 10^4$;
* If $C=1$, $1 \\leq d_i \\leq 1000$, and if $C=2$, $1 \\leq d_i \\leq 10^9$, for $1 \\leq i \\leq N$.
* The numbers in the sequence $B$ will be displayed without leading zeros (for example, if as a result of applying the rules from the statement the number $0204$ is obtained in the sequence $B$, it will be displayed as $204$).
* For tests worth $30$ points, the task is $1$.

# Example 1

`domino.in`
```
1
5
2 3 15 4 7
```

`domino.out`
```
12 30 2040 60 252
```

## Explanation

The task is $1$, so we need to determine the sums of the numbers in the games with size $2$, $3$, $15$, $4$, and $7$.

# Example 2

`domino.in`
```
2
5
12 30 2040 60 252
```

`domino.out`
```
1 2 23 52 204
```

## Explanation

From the sequence `12 30 2040 60 252` is formed:

|Sequence $A$|Sequence $B$|Formation direction|
|:--------|---------|-----------------|
|$\\sout{1}230204060252$|$1$|$\\longrightarrow$|
|$23020406025\\sout{2}$|$1 \\ 2$|$\\longleftarrow$|
|$\\sout{23}020406025$|$1 \\ 2 \\ 23$|$\\longrightarrow$|
|$0204060\\sout{25}$|$1 \\ 2 \\ 23 \\ 52$|$\\longleftarrow$|
|$\\sout{0204}060$|$1 \\ 2 \\ 23 \\ 52 \\ 204$|$\\longrightarrow$|
|$060$|No longer able to form a number $\\gt 204$|-|

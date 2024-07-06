# Ștefan and Tudor are bored, so they play an innovative game. They both have a virtual board in front of them which can be represented as an $N \cdot M$ matrix, where $N$ and $M$ are non-zero natural numbers.

**Ștefan initially has board $A$, and Tudor has board $B$.**

# Game Rules:

At the beginning, all the cells within the boards will be filled with random numbers. The game is played over $Q$ rounds, each round can be either of type $1$ or type $2$.

If the round is of type $1$ then:

* a cell $(x_A, y_A)$ of board $A$ is given where the number becomes $val_1$.
* a cell $(x_B, y_B)$ of board $B$ is given where the number becomes $val_2$.

If the round is of type $2$ then:

* the corners $x_1, y_1, x_2, y_2$ of a submatrix of board $A$ are given and the power $P_A$ of the submatrix is determined.
* the corners $x_3, y_3, x_4, y_4$ of a submatrix of board $B$ are given and the power $P_B$ of the submatrix is determined.
* if $P_A > P_B$, then the player assigned to board $A$ receives a point, and if $P_A < P_B$, the player assigned to board $B$ receives a point. In case of a tie, no one receives points.
* The power $P$ of a submatrix is defined as the remainder of the sum of the bitwise "xor" operation over all subsets of elements in the submatrix modulo $10^9 + 7$.

Example: If the elements of the submatrix are $1$, $2$, $3 \rightarrow P = (1 + 2 + 3 + (1 \oplus 2) + (1 \oplus 3) + (2 \oplus 3) + (1 \oplus 2 \oplus 3))$ % $ ( 10^9 + 7) = 12$, where $\oplus$ represents [*"bitwise xor"*](https://en.wikipedia.org/wiki/XOR_gate).

# Task

After several games, they noticed that Ștefan is much weaker at this game, so Tudor thought of giving him an advantage. **He has $K$ swaps available**. If he uses a swap, the two exchange boards.

**What is the maximum number of points Ștefan can accumulate using at most $K$ swaps?**

# Input data

The first line of the input file `skill-issue.in` contains four non-zero natural numbers, $N$, $M$ and $K$.
The next $N$ lines contain $M$ natural numbers representing the initial configuration of board $A$.
The next $N$ lines contain $M$ natural numbers representing the initial configuration of board $B$.
The next line contains the number $Q$.
The next $3 \cdot Q$ lines contain the configuration of each round:

The first line contains the non-zero natural number **$tip$**.

If **tip = $1$**, the next $2$ lines contain:

* $x_A,y_A,val_1$
* $x_B,y_B,val_2$

If **tip = $2$**, the next $2$ lines contain:

* $x_1, y_1, x_2, y_2$
* $x_3, y_3, x_4, y_4$

# Output data

The first line of the output file `skill-issue.out` contains a single natural number, the maximum number of points Ștefan can accumulate by making at most $K$ swaps.

# Constraints and clarifications

* $1 \leq N \leq 2000$;
* $1 \leq M \leq 2000$;
* $1 \leq x_1 \leq x_2 \leq N$;
* $1 \leq y_1 \leq y_2 \leq M$;
* $1 \leq K \leq 5000$;
* $1 \leq Q \leq 5000$;
* $tip = 1$ or $2$;
* all numbers are guaranteed to be natural $< 10^{18}$
* Ștefan initially has board $A$, and Tudor has board $B$!

|#|Score|Constraints|
|-|-|--------|
|1|15|$1 \leq N,M,Q \leq 5, K = 0$|
|2|35|$1 \leq Q \leq 500$, $1 \leq N,M \leq 300$|
|3|30|$1 \leq N,M \leq 1000$|
|4|20|No additional constraints|

# Example 1

`skill-issue.in`
```
3 3 0
4 8 7
2 3 4
7 7 8
5 3 0
0 2 5
0 3 9
5
2
2 2 3 3
1 2 2 3
2
1 1 3 1
1 1 1 2
1
1 1 8
2 2 7
1
1 2 6
1 1 5
2
1 1 3 3
1 1 3 3
```

`skill-issue.out`
```
2
```

## Explanation

* **First round:**

$P_A$ is determined as $3 + 4 + 7 + 8 + (3 \oplus 4) + (3 \oplus 7) + (3 \oplus 8) + (4 \oplus 7) + (4 \oplus 8) + (7 \oplus 8) + (3 \oplus 4 \oplus 7) + (3 \oplus 4 \oplus 8) + (3 \oplus 7 \oplus 8) + (4 \oplus 7 \oplus 8) + (3 \oplus 4 \oplus 7 \oplus 8)) = 120$.

$P_A = P_A$ % $(10^9 + 7) = 120$.

$P_B$ is determined as $3 + 0 + 2 + 5 + (3 \oplus 0) + (3 \oplus 2) + (3 \oplus 5) + (0 \oplus 2) + (0 \oplus 5) + (2 \oplus 5) + (3 \oplus 0 \oplus 2) + (3 \oplus 0 \oplus 5) + (3 \oplus 2 \oplus 5) + (0 \oplus 2 \oplus 5) + (3 \oplus 0 \oplus 2 \oplus 5)) = 56$.

$P_B = P_B$ % $(10^9 + 7) = 56.$

**$P_A > P_B \rightarrow$ Stefan receives one point.**

* **Second round:**

$P_A$ and $P_B$ are determined similarly, $P_A = 28$, $P_B = 14 \rightarrow P_A > P_B \rightarrow$ **Ștefan receives one point.**

* **Third round:**

Board $A$ becomes:

```
8 8 7
2 3 4
7 7 8
```

Board B becomes:

```
5 3 0
0 7 5
0 3 9
```

* **Fourth round:**

Board $A$ becomes:

```
8 6 7
2 3 4
7 7 8
```

Board B becomes:

```
5 3 0
0 7 5
0 3 9
```

* **Fifth round:**

$P_A$ and $P_B$ are determined similarly, $P_A = 3840$, $P_B = 3840 \rightarrow P_A = P_B \rightarrow$ **Nobody receives any points.**

**In the end, Ștefan will have accumulated $2$ points.**

# Example 2

`skill-issue.in`
```
3 3 1
5 3 0
0 2 5
0 3 9
4 8 7
2 3 4
7 7 8
5
2
2 2 3 3
1 2 2 3
2
1 1 3 1
1 1 1 2
1
1 1 8
2 2 7
1
1 2 6
1 1 5
2
1 1 3 3
1 1 3 3
```

`skill-issue.out`
```
1
```

## Explanation

This example is similar but now the boards have their configurations interchanged. **Ștefan has one swap available which he can use to "steal" $1$ point and remain with Board $B.**
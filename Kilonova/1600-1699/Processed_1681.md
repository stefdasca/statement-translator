
In the _Altfel - "Să știi mai multe, să fii mai bun"_ week, students $A$ and $B$ are playing a _different_ game called "margins". The two have a binary square matrix of size $2^n$ at their disposal.

~[margi1.png|align=right]

The game proceeds as follows:
- The game starts at level $n$, when the initial matrix is divided into $4$ disjoint matrices of size $2^{n-1}$;
- Each of the two players chooses a matrix among the $4$ and adds to their score the number of $1$ values contained in the chosen matrix. If both players choose the same matrix, only player $A$ adds the number of $1$ values from the matrix to their score;
- For each level, after dividing the initial matrix, the resulting matrices will be numbered similarly to the adjacent figure;
- At level $n - 1$, each matrix chosen by the players is divided into $4$ disjoint matrices of size $2^{n-2}$. Each player chooses a matrix from the newly formed ones;
- For each level played, each player must choose a matrix;
- The game continues with levels $n-2$, $n-3$, etc.;
- The game ends when the size of the chosen matrices is $1$;

The goal of the game is to obtain the maximum possible sum by adding the scores of the two players. If there are multiple ways to achieve this sum, each player will choose the matrices with the lowest order number. Example: for $n=3$, we will simulate a game:

* Player $A$

Chooses the matrix with the top-left corner in ($1, 1$), numbered $1$. Score $Sum_A = 7$.

~[margi2.png]

* Player $B$

Chooses the matrix with the top-left corner in ($5, 1$), numbered $3$. Score $Sum_B = 5$.
~[margi3.png]

* Player $A$

Chooses the matrix with the top-left corner in ($1, 1$), numbered $1$. Score $Sum_A = 7 + 3 = 10$
~[margi4.png]

* Player $B$

Chooses the matrix with the top-left corner in ($7, 1$), numbered $3$. Score $Sum_B = 5 + 3 = 8$
~[margi5.png]

* Player $A$

Chooses the matrix with the top-left corner in ($1, 2$), numbered $2$. Score $Sum_A = 10 + 1 = 11$. 
Player $A$ achieved $Sum_A = 11$, the sequence of choices being: $1$, $1$, $2$.

* Player $B$

Chooses the matrix with the top-left corner in ($7, 2$), numbered $2$. Score $Sum_B = 8 + 1 = 9$

Player $B$ achieved $Sum_B = 9$, the sequence of choices being: $3$, $3$, $2$.

# Task

For a given natural number $n$ and a binary matrix of size $2^n$, determine the maximum score achievable by the two players. Also required is the determination of a strategy for choosing matrices at each step that leads to achieving the maximum score.

# Input data

The input file `margi.in` contains on the first line a natural number $C$. The second line contains a natural number $n$. The following $2^n$ lines contain the elements of the binary matrix. 

# Output data

The output file `margi.out` contains on the first line the maximum sum that can be obtained by summing the scores of the two players. If $C = 1$ in the output file, only this value will appear. If $C = 2$, the output file will contain, in addition:

The second line will contain $n$ numbers representing the sequence of matrices chosen by player $A$.
The third line will contain $n$ numbers representing the sequence of matrices chosen by player $B$.
The sequences of matrices chosen by the two must satisfy the following two conditions:

1) The sum of the two scores obtained by the two players is maximum. There may be multiple sequences of matrices that have the maximum sum.
2) Let $A_n$, $A_{n-1}$, $\\dots$, $A_1$ be the sequences of matrices chosen by $A$, respectively $B_n$, $B_{n-1}$, $\\dots$, $B_1$, the sequences of matrices chosen by $B$, at levels $n$, $n-1$, $\\dots$, $2$, $1$. If we compose the sequence $A_n$, $B_n$, $A_{n-1}$, $B_{n-1}$, $A_{n-2}$, $B_{n-2}$, $\\dots$, $A_1$, $B_1$, among all possible sequences that give the maximum sum, the smallest lexicographic sequence must be chosen. 

# Constraints and clarifications

* $C$ can be $1$ or $2$
* $2 \leq n \leq 10$
* We say that the sequence $X$ is lexicographically smaller than the sequence $Y$, if there is a position $i$, such that $X_1$ = $Y_1$, $X_2$ = $Y_2$, $\\dots$, $X_{i-1}$ = $Y_{i-1}$, and $X_i$ < $Y_i$.
* For tests worth $30$ points, we have $C = 1$.

# Example 1

`margi.in`
```
1
2
0000
0100
0000
0000
```

`margi.out`
```
2
```

## Explanation

The maximum sum = ($0$ + $1$) + ($0$ + $1$) = $2$. If we had $C = 2$, on lines $2$ and $3$ the following would also appear:

```
1 1
1 4
```

# Example 2


`margi.in`
```
2
3
01001100
11100011
00101000
11000000
00000000
01100100
01000000
11000010
```

`margi.out`
```
20
1 1 2
3 3 2
```

## Explanation

The maximum sum = ($7 + 5$) + ($3 + 3$) + ($1 + 1$) = $20$. The example from the figure above.


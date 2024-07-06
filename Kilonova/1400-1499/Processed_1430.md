~[2048.png|align=right]

Ada and Ben are passionate about computer games and have just discovered the latest version of the $2048$ game.
The rules of the game are very simple:

* the game starts with an array of $N$ pieces with numbers from the set {$2$, $4$, $8$, $16$, $32$, $64$, $128$, $256$, $512$, $1024$, $2048$} written on them;
* the pieces are placed in locations consecutively numbered $1$, $2$, ..., $N$;
* at each step, a _MOVE TO THE LEFT_ or a _MOVE TO THE RIGHT_ can occur;
* for each game, a maximum number of moves $M$ is established;

If a _MOVE TO THE RIGHT_ occurs, then:
- the pieces can merge to the right, starting with the second last piece in the array: if a piece is at position $i$ and has the value $k$, and at position $i+1$ there is a piece with the same value $k$, then these pieces will "merge", a piece with the value $2k$ will be obtained at position $i+1$, and a free location will remain at position $i$;
- after merging, the pieces align to the right so that the last piece is at position $n$;

If a _MOVE TO THE LEFT_ occurs, then:
- the pieces can merge to the left, starting with the second piece in the array: if a piece is at position $i$ and has the value $k$, and at position $i-1$ there is a piece with the same value $k$, then these pieces will "merge", a piece with the value $2k$ will be obtained at position $i-1$, and a free location will remain at position $i$;
- after merging, the pieces align to the left so that the first piece is at position $1$;

The game ends when one of the following situations is reached:
- at least one of the pieces has the value $2048$ written on it;
- the written values can no longer be changed by moving the pieces;
- all $M$ moves have been made.

# Task

Write a program that reads the natural numbers $N$ (the initial number of pieces) and $M$ (the maximum number of moves), an array of $N$ numbers representing, in order, the numbers written on the $N$ pieces and at most $M$ characters from the set {`L`, `R`} representing the moves fixed by Ada and Ben, and determines:

1. the number $X$ of moves made until the end of the game;
2. the maximum number $Y$ written on one of the pieces at the end of the game;
3. the maximum number $Z$ of merges made in one move.

# Input data

The input file `2048.in` contains:
- The first line contains the numbers $N$ and $M$, separated by a space.
- The second line contains the $N$ numbers written, in order, on the pieces, separated by a space.
- The third line contains the $M$ characters, separated by a space, representing the $M$ directions of movement.

# Output data

The output file `2048.out` will contain:
- The first line contains the number $X$.
- The second line contains the number $Y$.
- The third line contains the number $Z$.

# Constraints and clarifications

* $2 \leq N,M \leq 10\ 000$;
* The character `R` indicates a move to the right, and the character `L` indicates a move to the left;
* To solve task $1$ $40\\%$ of the score is allocated.
* To solve task $2$ $40\\%$ of the score is allocated.
* To solve task $3$ $20\\%$ of the score is allocated.

# Example

`2048.in`
```
7 10
16 4 4 2 2 4 8
R R L R L R L L R R
```

`2048.out`
```
4
32
2
```

## Explanation

The sequence of moves is represented in _figure $1$_.
$4$ moves were made until the end of the game, with the largest value written on one of the pieces being $32$. The maximum number of merges, **two**, was obtained in the first move.
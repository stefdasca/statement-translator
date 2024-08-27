### Noprimenolife

Having nothing better to do, Mountainman and Middle Islander are playing yet another dubious game. This game is defined by two numbers $N$ and $K$, and proceeds as follows: Middle Islander selects a set $S$, a subset of the set $\{1, 2, \dots, N\}$. Mountainman selects a value $X$ from $\{1, \dots, N\}$. The game is now played in turns, with Mountainman playing first. In a turn:

- If $X = 1$, Middle Islander wins.
- Otherwise, the player whose turn it is selects a prime number $p$, a divisor of $X$.
- If neither $X$ nor $X / p$ belong to $S$, Mountainman wins.
- Otherwise, set $X$ to $X / p$. Now, Mountainman is wondering: for a fixed value of $N$, for how many possible non-negative values of $K$ can Mountainman definitely win?

## Input data

The input file `noprimenolife.in` will contain, on the first line, the number $T$ of tests in the file. The following $T$ lines will contain each a value of $N$.

## Output data

The output file `noprimenolife.out` will contain $T$ lines, each containing the answer for one query, in order.

## Constraints and clarifications

$1 \leq T \leq 100,000$

$1 \leq$ sum of $N$s in a file $\leq 100,000$ 

## Example

`noprimenolife.in`
```
3
5
23
100
```

`noprimenolife.out`
```
2
10
42
```
```markdown
# Task

The $N$ players of the national team have arrived in Frankfurt for the match against Slovakia. Like any respectful team, they have friendship relationships in the form of a tree. While waiting for the match, Denis came up with the idea of taking his colleagues to a casino. To avoid attracting the attention of paparazzi, they can enter a casino in a group of up to $K$ people, forming a connected component in the friendship tree. Therefore, he will form several groups, which will enter the casino in turns. Denis wants them to be absent from the hotel as little as possible to avoid attracting the attention of Mr. Coach Fisu' lu' Tasu'.
Help Denis find the minimum number of groups he can form, and he will reward you with a hattrick against Slovakia.

# Input data

The first line of the input file `pacanea.in` contains the natural numbers $N$ and $K$. The next $N-1$ lines each contain 2 numbers $u$ and $v$ with the meaning that in the friendship tree, players $u$ and $v$ have an edge between them.

# Output data

The output file `pacanea.out` will contain a single line representing the minimum number of groups formed by Denis.

# Constraints and clarifications

* $1 \leq K \leq N \leq 200\ 000$;
* $14$ points are awarded for $N \leq 10$;
* An additional $3$ points are awarded for $u + 1 = v$;
* An additional $7$ points are awarded for $u = 1$;
* An additional $13$ points are awarded for $N \leq 100$;
* An additional $11$ points are awarded for $N \leq 1\ 000$;
* An additional $52$ points are awarded without further restrictions.

# Example

`pacanea.in`
```
6 3
1 3
5 4
4 3
3 2
2 6
```

`pacanea.out`
```
3
```

## Explanation

We can split into the following connected components: $\{1\}$, $\{2, 6\}$, $\{3, 4, 5\}$.
```

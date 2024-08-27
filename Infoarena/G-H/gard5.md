## Task

After buying his new house, Ştefan decided to rebuild the fence in front of it. The fence is made up of $N$ boards of distinct heights, placed next to each other. In fact, the heights of the boards form a permutation of the numbers from $1$ to $N$. Some boards are special, and they cannot be moved. These are the ones from which he can see the leftmost edge: from the beginning of the fence to such a board, there is no other higher board. Any of the other boards can be moved (swapped with another), but the two must remain between the same special boards as before the swap. Once such boards are swapped, a new fence configuration is obtained. The cost of a configuration is calculated by summing up the cost of each board in that configuration. The cost of a board is calculated as follows: if the board is special, its cost is $0$. If the board at position $i$ is not special, its cost is $|h[i]-h[i-1]| + |h[i]-h[i+1]|$, where $h[i]$ = height of the board at position $i$. We consider that at position $0$ there is a fictitious board with height $0$ and at position $n+1$ there is a fictitious board with height $n+1$ (both considered special). Determine the minimum cost of a configuration that can be obtained as described, as well as the number of distinct configurations of minimum cost.

## Input data

The first line of the file `gard5.in` contains a natural number $N$, representing the length of the fence. The second line contains the heights of the $N$ boards, in order from left to right.

## Output data

The first line of the file `gard5.out` contains two numbers: the first represents the minimum possible cost of a configuration, and the second represents the number of configurations with the minimum cost.

## Constraints and clarifications

$1 \leq N \leq 100$

The required number can be stored in a $64$-bit signed variable

If it has the minimum cost, the given configuration is counted

The minimum cost values $50\%$ of the score, and the number of configurations with the minimum cost the remaining $50\%$

## Example

`gard5.in`

```
5
1 2 3 4 5
```

`gard5.out`

```
0 1
```

`gard5.in`

```
4
1 4 2 3
```

`gard5.out`

```
6 2
```

## Explanations

The two configurations with minimum cost in the second example are $1,4,2,3$ and $1,4,3,2$ (boards $1$ and $2$ are special).
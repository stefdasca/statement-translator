
# Task

Andrei discovered a special seesaw in the park that has $2n$ seats numbered as follows:

- On the left side: $-n, -(n-1), \ldots, -2, -1$
- On the right side: $1, 2, \ldots, (n-1), n$

The number of each seat indicates how much it influences the balance of the seesaw.
Andrei has $2n$ friends with distinct weights $g_1, g_2, \ldots, g_{2n}$, each with a value between $1$ and $2n$.

Andrei needs to place each friend on a seat so that the seesaw is as balanced as possible.

The balance is calculated using the formula:
$$
S = \sum (\text{seat value} \times g_i)
$$

Where $g_i$ is the weight of the person on that seat.

What is the optimal strategy to arrange the $2n$ friends on the seesaw so that the value $|S|$ is minimized?

# Input data

The first line of the input file `balansoar.in` contains $n$.

# Output data

The first line of the output file `balansoar.out` will contain a single integer representing $S$.
The second line will contain a possible arrangement of the people.

# Constraints and clarifications

- $1 \leq n \leq 100 \ 000$
- $1 \leq g_i \leq 2n$

| # | Points | Constraints                  |
|:-:|:------:|:----------------------------:|
| 1 | 20     | $1 \leq n \leq 4$            |
| 2 | 20     | $5 \leq n \leq 6$            |
| 3 | 60     | $1 \leq n \leq 100 \ 000$    |

# Example 1

`balansoar.in`

```
1
```

`balansoar.out`

```
1
1 2
```

## Explanation

As seen, $1 \times (-1) + 2 \times (1) = 1$.

# Example 2

`balansoar.in`

```
3
```

`balansoar.out`

```
0
5 1 4 3 6 2
```

## Explanation

$5 \times (-3) + 1 \times (-2) + 4 \times (-1) + 3 \times 1 + 6 \times 2 + 2 \times 3 = 0$

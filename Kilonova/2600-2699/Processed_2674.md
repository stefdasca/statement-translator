# Task

At a voting booth, $n$ people showed up, conveniently numbered from $1$ to $n$.

In the voting booth, at most one person can be present at any given moment due to confidentiality reasons. Therefore, the $n$ people will form a queue in front of the booth.

A person $i$ is characterized by 3 numbers:
- $c_i$: person $i$ will join the queue at the beginning of minute $c_i$.
- $t_i$: it will take person $i$ $t_i$ minutes to vote. If they start voting at the beginning of minute $x$, they will finish at the end of minute $x + t_i - 1$.
- $d_i$: person $i$ is willing to wait in line until the beginning of minute $c_i + d_i$.

When a person finishes voting at the end of a minute, they will disappear as if by magic (they will be escorted by security), and the first person in line will enter the booth at the beginning of the next minute.

Additionally, the booth is open only until the end of minute $m$. People who are still in line when the booth closes will not get a chance to vote. If a person starts voting before the booth closes, they will be allowed to finish their voting, after which they will go home.

To conduct a convincing exit poll, you need to find out how many people managed to vote and their indices.

# Input data

The first line of the input file `votus.in` will contain two numbers $n$ and $m$ - the number of people who want to vote and the minute when the voting booth closes, respectively.

On each of the next $n$ lines, there will be three numbers $c_i, t_i$, and $d_i$, with the meanings given in the statement.

# Output data

The first line of the output file `votus.out` will contain $k$ - the number of people who managed to vote. 

The second line will contain the $k$ indices $i_1 < i_2 < \ldots < i_k$ - the people who managed to vote.

# Constraints and clarifications
- $1 \le n \le 2 \cdot 10^5$
- $n \le m \le 10^9$
- $1 \le c_i, t_i, d_i \le m$
- It is guaranteed that all elements of the array $c$ are distinct.

|#|Score|Constraints                            |
|-|-----|---------------------------------------|
|1| 30  | $m \le 1000$                          |
|2| 20  | $n \le 1000$                          |
|4| 20  | $m \le 2 \cdot 10^5$                  |
|5| 30  | Without additional constraints         |

# Example 1

`votus.in`

```
5 9
2 4 2
5 3 6
9 1 4
1 3 1
3 1 3
```

`votus.out`
```
3
1 2 4
```

## Explanation 

At the beginning of minute $1$, person $4$ joined the queue and will start voting immediately until the end of minute $3$.

At the beginning of minute $2$, person $1$ joined the queue. They are willing to wait in line until the beginning of minute $4$.

At the beginning of minute $3$, person $5$ joined the queue. At the end of minute $3$, person $4$ finished voting.

At the beginning of minute $4$, person $1$ will start voting until the end of minute $7$.

At the beginning of minute $5$, person $2$ joined the queue.

At the beginning of minute $6$, person $5$ left the queue.

At the end of minute $7$, person $1$ finished voting.

At the beginning of minute $8$, person $2$ will start voting, finishing at the end of minute $10$.

Person $3$ will go home.
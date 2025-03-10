# Task

The International Computer Science High School of Bucharest has a network of $N$ computers connected in a circle. Computer $i \ (1 \leq i < N)$ is connected to computer $i + 1$ via link $i$. Computers $N$ and $1$ are also connected by link $N$.

Each computer has a security key composed of $K$ bits of information, represented as a binary string of length $K$. Each link also has a security threshold $W_i$. The two computers connected via this link can communicate only if their keys differ in _exactly_ $W_i$ positions.

The system administrator has lost the security keys and needs your help to generate new ones so that communication can take place through each link.

# Input data

The first line of the input data contains $T$ — the number of test cases to solve. The description of the $T$ tests is as follows:

The first line of a test contains two integers separated by spaces $N, K$. The second line of a test contains $N$ integers separated by spaces $W_1, W_2, \dots , W_N$.

# Output data

Print the answers for the $T$ tests. The description of an answer for a test is as follows:

If there is no solution for a test, the first and only line of the output data associated with this test must contain the string `NO`. Otherwise, the first line of the output data associated with this test must contain the string `YES` and lines from $2$ to $N + 1$ must contain a valid list of security keys. The security key for each computer $i$ must be printed as a binary string without spaces on line $(i + 1)$.

# Constraints and clarifications

* $1 \leq T \leq 100\ 000$
* $2 \leq N$
* $2 \leq N \cdot K \leq 5\ 000\ 000$
* $0 \leq W_i \leq K$
* It is guaranteed that the sum of all $N \cdot K$ values from all tests does not exceed $5\ 000\ 000$.
* If you correctly determine whether a solution exists or not, but display incorrect (yet correctly formatted) security keys, you will receive $50\%$ of the points associated with the subtask.
* Let $W_{max}$ be the maximum value among all $W_i$ values.

| # | Points | Constraints         |
| - | ------ | --------------------|
| 1 | 5      | $T, N, K \leq 5$   |
| 2 | 2      | $K = 1$             |
| 3 | 8      | $K = 2$             |
| 4 | 32     | $2W_{max} \leq K$   |
| 5 | 24     | $N \leq 50\ 000, K \leq 20$ |
| 6 | 29     | No additional constraints. |

# Examples

`stdin`
```
3
5 3
2 1 3 0 2
10 6
3 2 1 4 3 2 1 3 2 1
2 3
2 1
```

`stdout`
```
YES
000
110
010
101
101
YES
000000
111000
111110
111111
000011
111011
011111
111111
000111
000001
NO
```

## Explanation

For the first test, the security key `000` differs in $2$ positions from `110`, `110` differs in one position from `010`, `010` differs in $3$ positions from `101`, `101` differs in $0$ positions from `101`, and `101` differs in $2$ positions from `000`, thus respecting all five security thresholds.

For the last test, there is no way to choose security keys such that all conditions are met. Therefore, `NO` is displayed.
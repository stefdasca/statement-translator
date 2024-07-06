# Task

*Patratel* and *Patratica* are organizing a *fantastic* party at ***Palatul O(1)*** attended by $N$ people from ***\xc8ara Minunilor O(1)***. We know that each of the $N$ people has a **unique** $ID$ — a code that distinguishes them from the others — which is a non-zero natural number.

We say that a person feels *lost* if there is no one among the $N$ people (including themselves) who has the $ID$ equal to the **reverse** of their $ID$. The **reverse** of an $ID$ is obtained by rearranging its digits in reverse order; thus, we can deduce that: the **reverse** of the $ID$ $145$ is $541$, the **reverse** of the $ID$ $44$ is $44$, the **reverse** of the $ID$ $85\,567$ is $76\,558$, and the **reverse** of the $ID$ $9$ is $9$.

To have a truly *fantastic* party, *Patratel* and *Patratica* decided that no one **should feel *lost***. Your task is to determine how many people among the $N$ people at the party feel *lost*.

# Input data

The input file `mirrored.in` contains the following data:

- The first line contains the non-zero natural number $N$, representing the number of people invited by *Patratel* and *Patratica* to the *fantastic* party.
- The second line contains $N$ non-zero natural numbers, separated by a space, representing the $IDs$ of the $N$ people. Specifically, the $i$-th number on the second line represents the $ID$ of the $i$-th person, i.e., $id_i$.

# Output data

The output file `mirrored.out` should contain a single natural number, printed on the first line, representing the number of people at the party who feel *lost*. If no person at the party feels *lost*, this number will be $0$.

# Constraints and clarifications

* $1 \leq N \leq 3 \cdot 10^5$
* $1 \leq id_i \leq 10^{18}$, for any $1 \leq i \leq N$
* The $N$ $IDs$ are indivisible by $10$, meaning each $ID$ has a non-zero last digit (different from $0$).
* The $N$ $IDs$ are pairwise distinct. No two $IDs$ are identical (equal).
* **Attention! The tests are not complete for this problem, as some were lost.**

| # | Points | Constraints |
| - | ------- | ---------- |
| 1 | 17 | $N = 20$ and $1 \leq id_i \leq 10^2$, for any $1 \leq i \leq N$ |
| 2 | 24 | $N = 10^3$ and $1 \leq id_i \leq 10^4$, for any $1 \leq i \leq N$ |
| 3 | 27 | $1 \leq id_i \leq 10^9$, for any $1 \leq i \leq N$ |
| 4 | 32 | No further additional constraints. |

# Example

`mirrored.in`
```
5
123 12 1 123456789 987654321
```

`mirrored.out`
```
2
```

## Explanation

At the *fantastic* party organized by *Patratel* and *Patratica*, there are $5$ people, who have the $IDs$: $(123, 12, 1, 123\,456\,789, 987\,654\,321)$. The **reverse** of the $ID$ $123$ is $321$. The **reverse** of the $ID$ $12$ is $21$. The **reverse** of the $ID$ $1$ is $1$. The **reverse** of the $ID$ $123\,456\,789$ is $987\,654\,321$. The **reverse** of the $ID$ $987\,654\,321$ is $123\,456\,789$. The people with the $IDs$: $123$ and $12$ feel lost because the **reverses** of their $IDs** are **not** found among the set of the $5$ $IDs$ at the party.
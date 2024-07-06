```markdown
# Task

In DinoLand there were two major dinosaur families: Ankylosaurus and Brachiosaurus. The family of Ankylosaurus' consists of $N$ species, numbered from $1$ to $N$, while the family of Brachiosaurus' consists of $M$ species, numbered from $1$ to $M$.

The families started out as their original species, which is species $1$ for both families. As evolution went on, they developed into multiple directions.

Each new species was a direct descendant of exactly one other species from the same family, and every species evolves completely independently.

Fortunately, we know their ancestry, so we can trace back the evolution of each species.

Archeologists are researching these families, and they started to note down how many times distinct species from different families lived in the same place.

Formally, if fossils of an Ankylosaurus species $X$ and fossils of a Brachiosaurus species $Y$ have been found near each other $C$ times already, then the *strength of connection* between species $X$ and $Y$ is $C$, where $C$ is a positive integer.

Evolving does not mean that the ancestors of the species disappeared, so there are no restrictions for connections between any two species.

According to a new theory, dinosaur species were *familiar* with each other if they or some of their ancestors lived in the same place.
Now that they have collected a lot of data, they want to find answers for queries of the following type: given an Ankylosaurus species $U$ and a Brachiosaurus species $V$, how familiar they were with each other?

Formally, answer the sum of the strengths of connections between them or any of their ancestors.

# Input

The first line contains the integer $N$ ($1 \le N \le 2 * 10^5$), the number of Ankylosaurus species.

The second line contains $N-1$ integers $PA_i$, where Ankylosaurus species $(i+1)$ is a direct descendant of the species $(PA_i)$ for each $i=1\ldots N-1$.

The third line contains the integer $M$ ($1 \le M \le 2 * 10^5$), the number of Brachiosaurus species.

The fourth line contains $M-1$ integers $PB_i$, where Brachiosaurus species $(i+1)$ is a direct descendant of the species $(PB_i)$ for each $i=1 \ldots M-1$.

The fifth line contains the integer $K$ ($1 \le K \le 2 * 10^5$), the number of connections.

After that there are $K$ lines, each containing three integers $X_i$, $Y_i$, and $C_i$ ($1 \le C_i \le 10^9$), where the strength of connection between the Ankylosaurus species $X_i$ and the Brachiosaurus species $Y_i$ is $C_i$, for each $i=1 \ldots K$.

The next line contains the integer $Q$ ($1 \le Q \le 2 * 10^5$), the number of queries.

After that there are $Q$ lines, each containing two integers $U_i$, $V_i$, where $U_i$ is the Ankylosaurus species and $V_i$ is the Brachiosaurus species of the $i$-th query, for each $i=1 \ldots Q$.

For tests worth $15$ points: $N, M, K, Q \le 1000$.

For tests worth $25$ more points: $Q \le 2000$, and for one of the dinosaur families all of its species has at most 5000 ancestors.

For tests worth $35$ more points: for one of the dinosaur families all of its species has at most one direct descendant.

# Output

You need to print $Q$ lines, the $i$-th line should contain an integer, the answer for the $i$-th query in the given order.

# Example

`stdin`
```
5
1 4 2 4
4
4 4 1
3
1 4 5
4 1 7
2 2 3
4
2 4
3 2
5 3
1 1
```

`stdout`
```
5
15
12
0
```

# Notes

In the **first query** we are interested in Ankylosaurus species $2$ (and its ancestors: $1$), and Brachiosaurus species $4$ (and its ancestors: $1$). These have a single connection $(1, 4)$ of strength $5$, so the answer is $5$.

In the **second query** we are interested in Ankylosaurus species $3$ (and its ancestors: $4, 2$ and $1$), and Brachiosaurus species $2$ (and its ancestors: $4$ and $1$). All three connections are between some of these species, so the answer is $5 + 7 + 3 = 15$.

In the **third query** we are interested in Ankylosaurus species $5$ (and its ancestors: $4, 2$ and $1$), and Brachiosaurus species $3$ (and its ancestors: $4$ and $1$). These have two connections, connection $(1, 4)$ of strength $5$ and connection $(4, 1)$ of strength $7$, so the answer is $5 + 7 = 12$.

In the **fourth query** we are interested in Ankylosaurus species $1$ (and its ancestors: *none*), and Brachiosaurus species $1$ (and its ancestors: *none*). These don't have any connections, so the answer is $0$.
```
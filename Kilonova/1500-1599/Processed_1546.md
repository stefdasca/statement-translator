Consider 3 arithmetic progressions of non-zero natural numbers. We denote with $P_i$, $1 \leq i \leq 3$, the sets formed by the elements of progression $i$. Let $P = P_1 \cup P_2 \cup P_3$ be the union of the sets $P_1$, $P_2$, $P_3$.

# Task

Determine the cardinality of the set $P$.

# Input data

The input file `pro3.in` contains $3$ lines. Line $i$, $1 \leq i \leq 3$ will contain three natural numbers $a_i$, $r_i$, $n_i$, separated by spaces, representing in this order the first term, the ratio, and the number of terms of the progression $P_i$.

# Output data

The output file `pro3.out` will contain on the first line the cardinality of the set $P$.

# Constraints and clarifications

| # | Score  | Constraints          |
| - | ------ | -------------------- |
| 1 | 40     | $0 < a_i, r_i \leq 100$ and $0 < n_i \leq 1\ 000\ 000$, $1 \leq i \leq 3$ |
| 2 | 72     | $0 < a_i, r_i \leq 100$ and $0 < n_i \leq 1\ 000\ 000\ 000$, $1 \leq i \leq 3$ |
| 3 | 100    | $0 < a_i, r_i \leq 1\ 000\ 000$ and $0 < n_i \leq 1\ 000\ 000\ 000$, $1 \leq i \leq 3$ |

# Example

`pro3.in`
```
2 2 10
3 4 8
1 3 12
```

`pro3.out`
```
24
```

## Explanation

The first progression has the first term $2$, ratio $2$, and $10$ terms.  
The second progression has the first term $3$, ratio $4$, and $8$ terms.  
The third progression has the first term $1$, ratio $3$, and $12$ terms.  
Thus:  
$P_1$ = {$2$, $4$, $6$, $8$, $10$, $12$, $14$, $16$, $18$, $20$}  
$P_2$ = {$3$, $7$, $11$, $15$, $19$, $23$, $27$, $31$}  
$P_3$ = {$1$, $4$, $7$, $10$, $13$, $16$, $19$, $22$, $25$, $28$, $31$, $34$}  
The union of the terms of the three progressions is the set  
$P_4$ = {$1$, $2$, $3$, $4$, $6$, $7$, $8$, $10$, $11$, $12$, $13$, $14$, $15$, $16$, $18$, $19$, $20$, $22$, $23$, $25$, $27$, $28$, $31$, $34$} and the cardinality of the set $P$ is $24$.
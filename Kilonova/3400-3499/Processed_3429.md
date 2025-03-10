Below is the translated and reformatted competitive programming problem statement:

---

Alex is passionate about history and archaeology. During one of his expeditions, he found $N$ tablets that contained natural numbers. Curious to learn about their origin, Alex visited his history teacher. The teacher told the boy that the $N$ tablets are fragments of an ancient Geto-Dacian inscription. After placing them in the correct order, the two managed to reconstruct the inscription by concatenating the numbers from the tablets. For example, if after ordering, the tablets found by Alex contain the numbers $12$, $4$, and $1030$, the reconstructed inscription will be $1241030$.

Ever curious, Alex wants to analyze each valid sequence of $K$ digits. A sequence is considered valid if its first digit is non-zero. For example, the valid sequences of $3$ digits for the inscription $1241030$ will be, in order: $124$, $241$, $410$, and $103$, whereas the sequence $030$ is not considered valid because it starts with the digit $0$.

# Task

Alex asks you to help him interpret the results of his analysis so that he can decipher the secret hidden in the inscription.
1. Determine the number of valid sequences that Alex will analyze.
2. Determine the maximum value of a valid sequence analyzed and the sum of all valid sequences analyzed by Alex.

# Input data

The first line will contain three natural numbers $C$, $N$, and $K$, where $C$ represents the task that needs to be solved, $N$ represents the number of tablets Alex found, and $K$ represents the length of the digit sequences that will be analyzed. The next line contains, separated by spaces, $N$ values, representing the numbers written on the tablets after ordering them.

# Output data

- If $C=1$, the first line will contain a natural number, representing the number of valid sequences that Alex will analyze.
- If $C=2$, the first line will contain two natural numbers, separated by a space, representing, in this order, the maximum value of the sequence analyzed by Alex, and the sum of the values of the sequences analyzed by him.

# Constraints and clarifications

* $1 \leq C \leq 2$
* $1 \leq N \leq 10^5$
* $1 \leq K \leq 13$
* The values of the tablets read will be between $1$ and $10^{18}$.
* It is guaranteed that the inscription contains at least $K$ digits.
* It is guaranteed that the answer will fit into the ***long long*** data type.
  - For 15 points, $C=1$ and all digits on the tablets are non-zero.
  - For another 15 points, $C=1$, without any additional constraints.
  - For 20 points, $C=2$ and all digits on the tablets are non-zero.
  - For another 50 points, $C=2$, without any additional constraints.

# Example 1

`stdin`
```
1 3 2
12 4 1030
```

`stdout`
```
5
```

## Explanation

Task 1 is solved. The initial inscription was $1241030$, and the valid sequences of length $2$ are $12$, $24$, $41$, $10$, and $30$. Therefore, there are $5$ valid sequences of length $2$.

# Example 2

`stdin`
```
2 3 2
12 4 1030
```

`stdout`
```
41 117
```

## Explanation

Task 2 is solved. The largest of the valid sequences is $41$, and their sum is $12 + 24 + 41 + 10 + 30 = 117$.

# Example 3

`stdin`
```
1 4 3
142 230 1420 5
```

`stdout`
```
8
```

## Explanation

Task 1 is solved. The initial inscription was $14223014205$, and the valid sequences of length $3$ are $142$, $422$, $223$, $230$, $301$, $142$, $420$, and $205$. The sequence $142$ is counted twice, that is, each time it appears in the inscription. So there are $8$ valid sequences of length $3$.
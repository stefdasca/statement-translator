```markdown
# Task
Given a natural number $N$. Generate a natural number with at least $N$ digits that has the following properties:
1. It starts with the digit $1$.
2. Multiplying this number by $3$ is equivalent to its circular permutation by one position to the left. For example, the circular permutation by one position to the left of the number $1998$ is $9981$ (but obviously, $1998$ is not a solution since $1998 \cdot 3 \neq 9981$).

# Input data
The number $N$ is read from the file `numar-curios.in`.

# Output data
The generated number will be printed in the file `numar-curios.out`.

# Constraints and clarifications
- $1 \le N \le 40$
- The displayed number must have at most $10\ 000$ digits.
```
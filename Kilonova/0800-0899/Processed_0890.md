```markdown
The kind witch has a chest in which the magic stone is locked up by the dwarves using a digital code. The dwarves gave the witch a box containing $n$ cards. Each card has a natural number written on it that the witch will use to open the chest. The values written on the cards are distinct from each other.

To find the code, she must proceed as follows: take each card out of the box and then determine the magic value associated with the natural number written on the card. For each card, the magic value is given by the $k$-th prime divisor of the number written on it. The witch must sum the obtained magic values for the $n$ cards and then input the digits of the obtained value in order to unlock the chest.

# Task
Since the witch does not have time, she asks you to help with the following problems:
1. Find the magic value for a given card;
2. Find the code of the chest.

# Input data
The input file is `cufar.in`.
The first line of the input file contains a value $p$ which can only be $1$ or $2$ and the number $n$ of cards separated by a space.

If $p$ is $1$, the second line of the input file contains two values representing the number on the given card and the value $k$, separated by a space, as described above.

If $p$ is $2$, the next $n$ lines of the input file contain two values each, separated by a space, representing the number on the card and its value $k$ for each of the $n$ cards.

# Output data
The output file is `cufar.out`.
If the value of $p$ is $1$, then **only** task 1 will be solved and the output file will contain on the first line the magic value associated with the given card. 
If the value of $p$ is $2$, then **only** task 2 will be solved and the output file will contain on the first line the code needed to open the chest.

# Constraints and clarifications
- $1 \leq n < 1\ 000\ 000$
- The value written on a card is a number between $2$ and $1\ 000\ 000$.
- It is guaranteed that for each pair $(nr, k)$ in the input file, $nr$ has at least $k$ prime divisors.
- For a correct solution of task 1, 18 points are awarded.
- For a correct solution of task 2, 72 points are awarded.
- For correct results for the second task respecting the problem constraints and $n \leq 1\ 000$, 18 points are awarded.
- For correct results for the second task respecting the problem constraints and $n \leq 500\ 000$, 43 points are awarded.
- 10 points are awarded by default.

# Example 1
`cufar.in`
```
1 1
30 3
```
`cufar.out`
```
5
```
## Explanation
$p = 1$, $n = 1$. **Only the first task is solved**.
The $3$rd prime divisor of the number $30$ is $5$.

# Example 2
`cufar.in`
```
2 5
30 3
64 1
105 2
1001 3
5474 4
```
`cufar.out`
```
48
```

## Explanation
$p = 2$, $n = 5$. **Only the second task is solved**.
The $3$rd prime divisor of the number $30$ is $5$.
The first prime divisor of the number $64$ is $2$.
The $2$nd prime divisor of the number $105$ is $5$.
The $3$rd prime divisor of the number $1001$ is $13$.
The $4$th prime divisor of the number $5474$ is $23$.
The sought sum will be $S = 5 + 2 + 5 + 13 + 23$, resulting in the code $48$.
```
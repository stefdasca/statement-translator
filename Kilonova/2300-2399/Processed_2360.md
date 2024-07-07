
# Task

You are given three natural numbers, $a$, $b$, and $k$. George, being passionate about mathematics and computer science, has invented an algorithm, and now he wants to test your computer science knowledge to find the answers he seeks.

The algorithm described by George works as follows:

As long as $a$ and $b$ are different, output $a$ and $b$ on a new line and subtract the smaller number from the larger number.

For example, if initially $a = 14$ and $b = 39$, the first $5$ pairs of displayed values are:

* $14 \\ 39$ (first pair)
* $14 \\ 25$ (from $b$ was subtracted $a$)
* $14 \\ 11$ (from $b$ was subtracted $a$)
* $3 \\ 11$ (from $a$ was subtracted $b$)
* $3 \\ 8$ (from $b$ was subtracted $a$)

Now, George wants to know the values of $a$ and $b$ at the $k$-th step.

Practically, if $k$ is $3$, you need to display $14 \\ 11$.

Since this is too easy, he asks you to solve the problem for $t$ such triplets. He guarantees that the algorithm will show at least $k$ lines.

# Input data

The first line of the input file `operatii.in` will contain $t$, the number of triplets for which you need to solve the problem.

On the next $t$ lines, the triplets containing $a \\ b \\ k$, the three numbers in the triplet will be given.

# Output data

For each triplet, print on a separate line in the output file `operatii.out` the value of $a$ and the value of $b$ after $k$ steps.

# Constraints and clarifications

* $1 \\leq t \\leq 1 \\ 000$;
* $1 \\leq a, b, k \\leq 10^9$;
* The algorithm will display at least $k$ lines.
* For tests worth $15$ points, $(t = 1)$ and $(1 \\leq a, b, k \\leq 10^6)$.
* For tests worth $25$ points, $(1 \\leq t \\leq 5)$ and $(1 \\leq a, b, k \\leq 10^6)$.

# Example

`operatii.in`
```
2
14 39 3
167 96 7
```

`operatii.out`
```
14 11
17 4
```

## Explanation

For the first pair, the explanation is found in the statement.

For the second pair, the values of $a$ and $b$ change as follows:

* $167 \\ 96$
* $71 \\ 96$
* $71 \\ 25$
* $46 \\ 25$
* $21 \\ 25$
* $21 \\ 4$
* $17 \\ 4$

We will display $17 \\ 4$.

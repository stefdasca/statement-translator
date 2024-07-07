Following the events in New York, the $N$ worlds of the Marvel universe are at war. World $i \\ (1 \\leq i \\leq N)$ is represented in this final war by an army consisting of $K_i$ soldiers (possibly zero). Each soldier has a single superpower represented by a positive integer (between $1$ and $P$). The powers of all soldiers within an army are different.

It has been observed that in direct combat, two soldiers will annihilate each other if and only if they have the same power. For example, if an army consisting of soldiers with powers $\\{1, 3, 5\\}$ fights against an army with powers $\\{2, 3, 6\\}$, then the soldiers who remain alive at the end of the battle are: $\\{1, 2, 5, 6\\}$.

The $N$ worlds are arranged sequentially: the first world has index $1$, while the last one has index $N$.

# Task

~[thanos.png|align=right]

Thanos is quite confident that he can win the war and destroy the universe, but he wants to have fun while doing so. Therefore, he has prepared $Q$ questions. For each question, two indices $x$ and $y$ are given, and the number of soldiers who would survive the battle among the armies with indices $x, x+1, x+2, \\dots, y$ should be found.

# Input data

The first line of the input file `infinitywar.in` contains two integers $N$ and $Q$.

The next $N$ lines contain descriptions of the armies. Line $i+1$ contains a number $K_i$ followed by $K_i$ numbers (the power of each soldier).

The next $Q$ lines contain two numbers $x$ and $y$, separated by a space.

# Output data

The output file `infinitywar.out` should contain $Q$ lines. Each line should contain a single number, the answer to the corresponding question.

# Constraints and clarifications

* $1 \\leq N \\leq 50 \\ 000$
* $1 \\leq P \\leq 10 \\ 000$
* $1 \\leq Q \\leq 100 \\ 000$
* $K_1 + K_2 + \\dots + K_N \\leq 300 \\ 000$
* $1 \\leq x \\leq y \\leq N$ for each question.
* For $30\\%$ of the tests, $N \\leq 10 \\ 000$, $P \\leq 500$, and $Q \\leq 10 \\ 000$
* For another $40\\%$ of the tests, $P \\leq 5 \\ 000$ and $Q \\leq 30 \\ 000$

# Example

`infinitywar.in`
```
4 3
2 1 2
3 1 3 97
2 1 341
5 4 2 981 341 97
1 3
2 4
1 4
```

`infinitywar.out`
```
5
4
4

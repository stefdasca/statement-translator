# Task

At a computer science competition, $2 \cdot N$ students are participating, divided into $N$ teams of $2$. Teams can work together on the proposed problems only if their computers are networked. The computer science lab is somewhat special: it has $2 \cdot N$ computers, distributed in two rows at a distance of one meter between them (both vertically and horizontally) and $N$ network cables of one meter in length. The competition takes place over several days, and no two days of the competition have the same network configuration.

Example: for $N=3$, the 6 students were divided into 3 teams, and the network arrangement for the 3 days of the competition is shown in the figure below.

~[img.png|width=37em]

The lab administrator wants to store all the configurations used on the competition days in lexicographical order. The horizontal cable is denoted by `0`, and the vertical one by `1`. Working orderly and efficiently, for the three days he will note the values: `001`, `100`, and `111`. It is observed that representations like `000`, `010`, `011`, `101` cannot be realized.

# Task

Given $N$, determine the following:

1. The number of days **modulo** $10^9+7$ in which the competition takes place.
2. The lab configurations on day $X-1$ and day $X+1$, given the configuration of day $X$.

# Input data

The input file `calc.in` contains the following information:

The first line contains a natural number $p$. For all input tests, the number $p$ can only take the value $1$ or $2$.

The second line contains the natural number $N$.

The third line contains a string of $N$ binary digits, without spaces between them, representing the correct configuration set by the administrator on day $X$.

# Output data

If the value of $p$ is $1$, **only point 1** of the task will be solved.

In this case, the output file `calc.out` will contain a single natural number $Z$ representing the number of days in which the competition takes place for the $N$ teams.

If the value of $p$ is $2$, **only point 2** of the task will be solved.

In this case, the output file `calc.out` will contain two lines. The first line will contain $N$ binary digits, without spaces between them, representing the network configuration of the previous day, and the second line will contain $N$ binary digits, without spaces between them, representing the configuration of the next day. If on the previous day there is no valid configuration according to the task requirements, the value $-1$ will be written on the first line. If on the next day there is no valid configuration according to the task requirements, the value $-1$ will be written on the second line.

# Constraints and clarifications

* $1 \leq N \leq 100 \ 000$
* Correctly solving the first task earns $20$ points, while solving the second task earns $80$ points.

# Example 1

`calc.in`
```
1
3
001
```

`calc.out`
```
3
```

# Example 2

`calc.in`
```
2
3
001
```

`calc.out`
```
-1
100
```
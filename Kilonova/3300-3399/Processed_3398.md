
~[peter-griffin.gif|align=right|width=30%]

# Task

$A$ and $B$ are playing a crazy game. $A$ has an unknown number, $x$, which $B$ has to guess. The function `guess(v)` returns $1$ if $v \geq x$, $0$ otherwise. Use as few calls to the `guess` function as possible to obtain $100$ points.

# Interaction Protocol

The contestant must implement the function with the header:
`int solve(void);`

The contestant can use the function defined in `interaction.h` with the header:
`int guess(int val);`

# Constraints and clarifications

* $1 \leq x \leq 1 \ 000 \ 000 \ 000$
* Let $k$ be the number of calls to the guess function made by the contestant.
* For tests worth $10$ points, $k$ can be at most $32$.
* For the other tests, $k$ can be at most $0$.
* You can use [the sample grader](https://kilonova.ro/assets/problem/3398/attachment/sample-grader.cpp) from the attachments.
* [This video](https://youtu.be/fgisEmX5IDU) might be useful for the $100$ points solution.

# Interaction example

Let $x = 5$.

The grader calls the function `solve()`.

The contestant guesses $6$, where `guess(6)` = $1$.

The contestant guesses $4$, where `guess(4)` = $0$.

The function `solve()` returns $5$.

The number of calls to the guess function is $2$, which is sufficient for the $10$ points subtask but not enough for the rest.

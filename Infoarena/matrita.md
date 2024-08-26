# The Mold

Tired of multiplying polynomials in linear time, solving conjectures, or other trivialities like the "Traveling Salesman Problem", $\text{Nry}$ decided to seek the secret of eternal happiness. However, looking around, he was stunned to see that contestants resort to unclean techniques in this game for satisfaction, from subtly stealing sources, or problem ideas to much graver acts, like securing spots at $\text{IOI}$ or previous editions of the $\text{Junior Challenge}$. Wishing, however, to be original (and at the same time to preserve the new tradition), $\text{Nry}$ came to the following conclusion: he must steal $\text{The Mold}$! Once he obtained the magic elixir, he placed it in a corner of the Olympic Cellar (one of the safest shelters, into which enemies can only enter through the glass ceiling). However, to ensure that his new acquisition would not disappear unexpectedly, he decided to form a defense system as follows: he viewed the Cellar as a square matrix with a side length of $N + 1$ (rows and columns are numbered from $0$ to $N$), with $\text{The Mold}$ located in the square at row $0$ and column $0$. He wishes to place several traps in squares with indices of the rows and columns between $1$ and $N$, such that each trap is visible from the point where $\text{The Mold}$ is located (in other words, there should not be two traps situated at $(l1, c1)$ and $(l2, c2)$ with a real number $k$ such that $x1 = x2 \cdot k$ and $y1 = y2 \cdot k$). $\text{Nry}$ asks you to answer the following question: knowing the number $N$, in how many ways can he build his defense system of $\text{The Mold}$? The answer must be displayed modulo $\text{MOD}$.

## Task

## Input data

The input file `matrita.in` contains a single line with two numbers, $N$ and $\text{MOD}$, as described in the statement.

## Output data

The output file `matrita.out` will contain a single natural number, namely the answer to the task modulo $\text{MOD}$.

## Constraints

$\text{Nry}$ has an unlimited number of traps.

Being very paranoid, he will always place at least one trap.

$1 \leq N \leq 12000000$

$100000000 \leq \text{MOD} \leq 1000001000$

Subtask 1 (tests 1 - 2) - 10 points: $N \leq 1800$

Subtask 2 (tests 3 - 4) - 5 points: $N \leq 3000$

Subtask 3 (tests 5 - 7) - 5 points: $N \leq 4000$

Subtask 4 (tests 8 - 12) - 30 points: $N \leq 300000$

Subtask 5 (tests 13 - 17) - 10 points: $N \leq 750000$

Subtask 6 (tests 18 - 22) - 25 points: $N \leq 6500000$

Subtask 7 (tests 23 - 27) - 5 points: $N \leq 10000000$

Subtask 8 (tests 28 - 30) - 10 points: $N \leq 12000000$

Legend has it that anyone who tastes from $\text{The Mold}$ has a guaranteed spot at $\text{IOI 2020}$.

## Example

`matrita.in`

`matrita.out`

$1$ $1000000007$

$1$

$2$ $1000000007$

$11$

$5$ $1000000007$

$3538943$

$768325$ $1000000007$

$667479250$

## Explanation

For the first example, he can only place one trap in the square $(1, 1)$.

For the second example, the following configurations are valid:

{$(1, 1)$},

{$(1, 1), (1, 2)$},

{$(1, 1), (2, 1)$},

{$(1, 1), (1, 2), (2, 1)$},

{$(2, 2)$},

{$(2, 2), (1, 2)$},

{$(2, 2), (2, 1)$},

{$(2, 2), (1, 2), (2, 1)$},

{$(1, 2)$},

{$(2, 1)$},

{$(1, 2), (2, 1)$}.

The configuration {$(1, 1), (2, 2)$} cannot be chosen because the trap $(2, 2)$ is not visible. $\text{Nry}$ considers that an explanation for the last two examples would be inadequately long.
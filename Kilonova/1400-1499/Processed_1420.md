```markdown
A showroom in Strasbourg sells a very large range of car models, arranged on $n$ lines. On each line, there are only car models sold by the same dealer. A dealer can have models on multiple lines. The European Parliament wants to renew its car fleet and sends the transport activity manager to the showroom to gather information about the options available for this purchase issue. The manager needs to choose $f_1$ models from the first dealer, $f_2$ models from the second dealer, etc.

The sequence of numbers $f_1, f_2, f_3, \ldots$ represents the terms $mod \\ k$ of an arithmetic progression with the first term $a$ and the common difference $r$. If the value in the sequence of numbers is greater than the number of models of the corresponding dealer, then the manager does not choose any model from that dealer. The first dealer is the one with models on the first line and, potentially, on other lines following the first line (but not necessarily consecutive!), the second dealer is the one with models on the first line containing models different from those of the first dealer, etc.

# Task

Write a program that determines:

$a)$ The number of dealers present in the showroom;

$b)$ The number of ways to purchase the models by the European Parliament, $mod \\ 9 \\ 001$.

# Input data

The input file `showroom.in` contains on the first line the numbers $n,a,r,k$ separated by exactly one space, as described above, and on the following $n$ lines are the names of the models from the description, separated by one or more spaces.

Each line ends with the newline character.

# Output data

The output file `showroom.out` will contain on the first line the number required for point $a)$, and on the second line the number required for point $b)$.

# Constraints and clarifications

* $1 \leq n \leq 500$
* $1 \leq a, r, k \leq 10 \ 000$
* The name of a model has at most $20$ lowercase letters and/or digits
* A line contains at most $100$ model names and there can be no more than $10$ spaces between two models
* There can be lines with order numbers $i_1, i_2, \ldots , i_p$ with models of the same dealer, such that the pairs of lines $(i_1, i_2) , \ldots ,(i_{p-1}, i_p)$ have at least one car model in common
* For the correct solving of each task, $50$% of the score is awarded
* The score for the second task is awarded only if there is an answer for the first task in the output file, regardless of its correctness
* For $60$% of the tests, it is guaranteed that the value $k$ is less than or equal to $10$

# Example

`showroom.in`
```
6 1 2 3
logan duster logan
peugeot207 peugeot307
sandero sandero
opelcorsa opelastra opelcorsa
peugeot207
sandero duster
```
`showroom.out`
```
3
3
```

# Explanation

There are $3$ dealers in the showroom.

Dealer $1$: `logan`, `duster`, `sandero`.

Dealer $2$: `peugeot207`, `peugeot307`.

Dealer $3$: `opelcorsa`, `opelastra`.

The first three terms of the arithmetic progression are $1, 3, 5$. $f_1=1 \\ mod \\ 3 = 1$; $f_2 = 3 \\ mod \\ 3 = 0$; $f_3 = 5 \\ mod \\ 3 = 2$.

The possible ways to purchase models from dealer $1$, no models from dealer $2$, and two models from dealer $3$ are:

* `logan, opelcorsa, opelastra`;
* `duster, opelcorsa, opelastra`;
* `sandero, opelcorsa, opelastra`.
```

I have translated and formatted the problem statement accurately while making sure to preserve the structure and mathematical values. Please review and let me know if there are any further adjustments needed.
```
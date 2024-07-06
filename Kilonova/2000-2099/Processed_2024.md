# Task

Alice Elice thought of giving Bob Glob a few Christmas gifts. A gift is a string of Christmas tree lights colored red ($\color{#FF3131}{\text{R}}$) or blue ($\color{cyan}{\text{A}}$) with a length of $N$. A good gift meets $M$ conditions of the type $(i, j)$ meaning that bulb $i$ has a different color than bulb $j$.

Unfortunately, Alice Elice is out shopping and doesn't have time to calculate how many different good gifts she can buy for Bob Glob.

# Input data

The first line contains $T$, representing the number of scenarios. The structure of a scenario is as follows: the first line contains $N$ and $M$, and then the following $M$ lines contain two numbers $i$ and $j$.

# Output data

For each scenario, print the number requested by Alice on a separate line, modulo $10^9 + 7$. If there are no such good gifts, print the message `Doar carbuni`.

# Constraints and clarifications

* $1 \leq T \leq 10^2$
* $1 \leq N \leq 10^5$
* $0 \leq M \leq 10^5$
* The sum of the values of $N$ across all $T$ scenarios is at most $5 \cdot 10^6$.
* The sum of the values of $M$ across all $T$ scenarios is at most $10^6$.

| # | Points | Restrictions | 
| - | ------ | ------------ |
| 1 | 25     | $N, M \leq 20$ |
| 2 | 45     | $N, M \leq 10^4$ |
| 3 | 30     | No additional restrictions |

# Example 1

`stdin`
```
1
5 3
1 2
2 3
4 5
```

`stdout`
```
4
```

## Explanation
The $4$ good gifts are:
$\color{#FF3131}{\text{R}} \color{cyan}{\text{A}} \color{#FF3131}{\text{R}} \color{#FF3131}{\text{R}} \color{cyan}{\text{A}}$
$\color{#FF3131}{\text{R}} \color{cyan}{\text{A}} \color{#FF3131}{\text{R}} \color{cyan}{\text{A}} \color{#FF3131}{\text{R}}$
$\color{cyan}{\text{A}} \color{#FF3131}{\text{R}} \color{cyan}{\text{A}} \color{#FF3131}{\text{R}} \color{cyan}{\text{A}}$
$\color{cyan}{\text{A}} \color{#FF3131}{\text{R}} \color{cyan}{\text{A}} \color{cyan}{\text{A}} \color{#FF3131}{\text{R}}$

# Example 2

`stdin`
```
2
5 2
1 2
1 3
3 3
1 2
2 3
3 1
```

`stdout`
```
8
Doar carbuni
```

## Explanation

* In the first example, the $8$ good gifts are:
$\color{#FF3131}{\text{R}} \color{cyan}{\text{A}} \color{cyan}{\text{A}} \color{#FF3131}{\text{R}} \color{cyan}{\text{A}}$
$\color{#FF3131}{\text{R}} \color{cyan}{\text{A}} \color{cyan}{\text{A}} \color{cyan}{\text{A}} \color{#FF3131}{\text{R}}$
$\color{cyan}{\text{A}} \color{#FF3131}{\text{R}} \color{#FF3131}{\text{R}} \color{#FF3131}{\text{R}} \color{cyan}{\text{A}}$
$\color{cyan}{\text{A}} \color{#FF3131}{\text{R}} \color{#FF3131}{\text{R}} \color{cyan}{\text{A}} \color{#FF3131}{\text{R}}$
$\color{#FF3131}{\text{R}} \color{cyan}{\text{A}} \color{cyan}{\text{A}} \color{#FF3131}{\text{R}} \color{#FF3131}{\text{R}}$
$\color{#FF3131}{\text{R}} \color{cyan}{\text{A}} \color{cyan}{\text{A}} \color{cyan}{\text{A}} \color{cyan}{\text{A}}$
$\color{cyan}{\text{A}} \color{#FF3131}{\text{R}} \color{#FF3131}{\text{R}} \color{#FF3131}{\text{R}} \color{#FF3131}{\text{R}}$
$\color{cyan}{\text{A}} \color{#FF3131}{\text{R}} \color{#FF3131}{\text{R}} \color{cyan}{\text{A}} \color{cyan}{\text{A}}$
* In the second example, it can be shown that there is no solution.
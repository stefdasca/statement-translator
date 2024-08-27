## Task

Tassadar wants to become a mentalist and decided to learn a trick to show his friend Zeratul. We consider natural numbers from $1$ to $N$ and a constant $K$ $(1 \leq K < N)$. Zeratul must think of a natural number $X$ $(1 \leq X \leq N)$, and Tassadar can ask questions in the form "Is the number $X$ you are thinking of in the set $\{ a_{1}, a_{2}, \dots, a_{K} \}$?" (the set must contain $K$ distinct natural numbers from the interval $[1, N]$). After a certain number of questions, Tassadar will magically guess the number Zeratul is thinking of. Since Tassadar does not want to bore his friend with too many questions, he asks you to tell him the minimum number of questions he needs to ask, in the worst case, to guess the number Zeratul is thinking of.

## Input data

The input file `magic3.in` contains on the first line the number of tests $T$. The next $T$ lines contain two numbers $N$ and $K$ with the significance given in the statement.

## Output data

The output file `magic3.out` will contain $T$ numbers representing the answer for each test, one per line.

## Constraints

$1 \leq T \leq 10$

$4 \leq N \leq 10\ 9$

$1 \leq K < N$

## Example

`magic3.in`

```
1
7 2
```

`magic3.out`

```
4
```
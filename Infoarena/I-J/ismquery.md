## Task

Bluff recently discovered in the orange car a sequence $A$ of $N$ integers. Instantly, $M$ questions came to his mind in the form: given a position $p$ in the sequence and a number $k$, display the $k$-th position denoted $r$ to the right of position $p$ $(r > p)$ with the property that $A_r > A_p$. Bluff generates his questions as follows, knowing the values $G$ and $H$: 
$$p_i = 1 + (i + p_{i-1} *G) \%\ N$$
$$k_i = 1 + (i + k_{i-1} *H) \%\ 5$$

## Input data

The input file `ismquery.in` will contain on the first line two natural numbers $N$ and $M$ as described in the statement. The second line will contain $N$ numbers separated by spaces, representing the content of the sequence $A$. The third line will contain the numbers $G$ and $H$, separated by a space, as described in the statement.

## Output data

The output file `ismquery.out` will contain $M$ lines, each containing the answer to one question in the order they were generated. If for a query the required position does not exist, print $0$.

## Constraints and clarifications

$N \leq 400\ 000$

$M \leq 1\ 200\ 000$

$p_0 = k_0 = 1$

Obviously, $k_i \leq 5$ for any $1 \leq i \leq M$

$-2\ 000\ 000\ 000 \leq A_i \leq 2\ 000\ 000\ 000$ for any $1 \leq i \leq N$

The elements of the sequence $A$ and the $M$ questions are numbered starting from 1

$1 \leq G,H \leq 1000$

## Example

`ismquery.in`
```
9 3
4 5 -1 7 2 5 2 9 3
1 1
```

`ismquery.out`
```
6
8
0
```
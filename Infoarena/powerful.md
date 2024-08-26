# Powerful

Amatias is the most powerful superhero; indeed, he is strong enough to defeat any opponent with a single kick! On the other hand, other hero federations around the world are less powerful. There are $T$ federations. Federation $i$ is characterized by 5 different numbers: $x_i$, $y_i$, $a_i$, $b_i$, $m_i$. The power $p_i$ of the federation is defined by the equation. To determine how much stronger Amatias is compared to various federations, given $x_i$, $y_i$, $a_i$, $b_i$, $m_i$, find the value of $p_i$.

## Task

## Input data

The input file `powerful.in` will contain on the first line $T$. On the next $T$ lines, it will contain, on line $i+1$, the numbers $x_i$, $y_i$, $a_i$, $b_i$, $m_i$. 

## Output data

The output file `powerful.out` will contain $T$ lines: the values of $p_i$ for $i = 1, \dots, T$. 

## Constraints and clarifications

$1 \leq T \leq 100$

$1 \leq x_i, y_i, a_i, b_i \leq 10^{18}$

$1 \leq m_i \leq 10000$

$m_i$ is prime. 

## Example

`powerful.in`
```
6
1 3 2 5 31
5 1 7 20 37
6 7 8 9 7
6 7 8 9 7919
6 7 8 9 1621
123 543 23 567 3163
```

`powerful.out`
```
4
33
5
3268
634
2608
```
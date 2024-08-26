## Task

We are given $N$, $Smax$, and $Smin$. Find a sequence of $N$ positive natural numbers such that: 
$v_1 + v_2 + \dots + v_n \leq Smax$ 
$v_1^2 + v_2^2 + \dots + v_n^2 \geq Smin$ 
$max(v_i) - min(v_i)$ is minimized 

## Input data

The input file `sir7.in` contains on the first line the number $T$ representing the number of tests. For each test, the first line contains the numbers $N$, $Smax$, and $Smin$ separated by spaces. 

## Output data

The output file `sir7.out` will contain $T$ lines, with line $i$ containing the sequence for test $i$. 

## Constraints and clarifications

$1 \leq T \leq 10$

$1 \leq N \leq 100000$

$1 \leq Smax \leq 10^9$

$1 \leq Smin \leq 10^{18}$

## Example

`sir7.in` 
```
2 
2 20 100 
2 7 25 
```
`sir7.out` 
```
10 10 
4 3 
```
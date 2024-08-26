Sequences3

Let $A_i$ be a sequence of non-zero natural numbers defined as follows: $A_1 = a$ $A_i = (A_{i-1} \times b) \mod P$, for any $i > 1$ Thus, the sequence $A$ can be defined by three known constants: $a$, $b$, and $P$.

## Task

For a known sequence $A$, answer $M$ queries ($st$, $S$) with the meaning: "What is the largest index $dr$ ($\geq st$) such that $A_{st} + A_{st+1} + A_{st+2} + \dots + A_{dr} \leq S$?"

## Input data

The input file `secvente3.in` contains on the first line the numbers $a$, $b$, $P$, and $M$ separated by space. 
The next $M$ lines contain the parameters for each query $st$ and $S$ separated by space. 

## Output data

The output file `secvente3.out` will contain on the first line $M$ numbers: The answers $dr$ to the queries in order, values separated by space.

## Constraints and clarifications

$M \leq 10^4$ 
$1 \leq st \leq 10^6$ 
$0 < dr \leq 10^7$, for any query 
$1 < a < b < P \leq 10^9$ 
$0 < S \leq 10^{15}$ 
For any test, the numbers $a$, $b$, and $P$ ensure that any $A_i$ is non-zero 
For any query $A_{st} \leq S$ 
Pay attention to memory limit 
Pay attention to the use of $long \ long$ (C++) or $int64$ (Pascal)

## Example

`secvente3.in` 
```
2 3 7 2 
2 15 
4 8 
```

`secvente3.out` 
```
4 5 
```

## Explanation

$A = (2, 6, 4, 5, 1, 3 \dots)$ 
$A_2 + A_3 + A_4 = 6 + 4 + 5 = 15 \leq 15$ 
$A_4 + A_5 = 5 + 1 = 6 \leq 8$, but $A_4 + A_5 + A_6 = 5 + 1 + 3 = 9$ is already $> 8$
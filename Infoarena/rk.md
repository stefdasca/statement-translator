# Rk

Given $N$ natural numbers, answer $Q$ questions in the form: how many of the $N$ numbers have a remainder of $R$ when divided by $2^K$?

## Input data

The input file rk.in will contain on the first line the number $N$. The second line will contain the $N$ natural numbers. The third line will contain the number of questions $Q$, and on the following $Q$ lines, there will be two natural numbers $R$ and $K$ with the meaning from the statement.

## Output data

The output file rk.out will contain $Q$ numbers, one on each line, representing the answers to the $Q$ questions, in the order given in the input file.

## Constraints

All numbers in the input file are in the range $[0, 2\ 000\ 000\ 000]$  
$1 \leq N \leq 200\ 000$  
$1 \leq Q \leq 100\ 000$  
$0 \leq K < 32$  
$0 \leq R < 2^K$  
For 20% of the tests $N \leq 1\ 000$ and $Q \leq 1\ 000$  
For 50% of the tests $K < 16$

## Example

`rk.in`  
```
5  
1 7 18 2 5  
3  
1 1  
2 3  
4 3  
```

`rk.out`  
```
2  
0  
3  
```
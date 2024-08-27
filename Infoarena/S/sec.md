## Sec

Henry shouldn't be here. He had withdrawn to the mountains, cleaning the alpine meadows. However, Marcel was too busy writing poetry for girls with purple hair, and the problem needed to be prepared, so here we are: We have a sequence of $N$ integers. Calculate, for each continuous subarray of length at least $K$, the maximum in the sequence. Sum all the results and display the sum. For ## task $C = 1$, the sequence is circular. For $C = 2$, the sequence is a regular one.

## Input data

The input file `sec.in` contains, on the first line, the numbers $T$ of tests and $C$, ## task. For each test, the first line contains the numbers $N$ and $K$ and the second line contains the $N$ integers. It is recommended to parse the input!

## Output data

The output file `sec.out` will contain $T$ lines, each containing a single number: the required sum for the corresponding test.

## Constraints and clarifications

All numbers in the input are integers 

$1 \leq T \leq 3$ 

$1 \leq C \leq 2$ 

$1 \leq K \leq N \leq 2\,000\,000$ 

The absolute value of the numbers in the sequence is strictly less than $10^6$

Scoring will be done on 10 tests, each worth 10 points. Odd index tests will have $C = 1$, and even index tests will have $C = 2$.

Test 1 will have $N \leq 50$ 

Test 2 will have $N \leq 2\,000$ 

Tests 3, 4, and 5 will have $N \leq 100\,000$ 

Tests 3 and 6 will have randomly generated sequences. Thus, each value in the sequence will be independently chosen from the others, with the same probability of being equal to any of the integers in the open interval $(-10^6, 10^6)$ 

Tests 7 and 8 will have $K = 1$

## Example

`sec.in` `sec.out` 
```
3 2 
5 3 
1 2 3 4 5 
4 1 
-1 100 -2 -3 2 
2 1 
1 1 
```

`26` 
`592` 
`1`
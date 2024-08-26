## Task

Given a sequence $a_1$, $a_2$, $\dots$, $a_n$ of natural numbers, you need to answer $Q$ questions of the following format: given two positions $i$ and $j$ and two natural numbers $x$ and $y$, how many elements in the subarray $a_i$, $a_{i+1}$, $\dots$, $a_j$ have values between $x$ and $y$?

## Input data

The input file `qxy.in` contains on the first line the number $n$. On the next line, there are $n$ natural numbers separated by spaces representing the elements of the sequence. The third line contains the number $Q$, and the following $Q$ lines each contain 4 numbers $i$, $j$, $x$, $y$ representing a single question.

## Output data

The output file `qxy.out` will contain $Q$ lines, on each line $i$ contains a natural number representing the answer to question $i$.

## Constraints

$2 \leq n \leq 10000$  
$1 \leq i \leq j \leq n$  
$0 \leq a[i] \leq 1000$  
$0 \leq x \leq y \leq 1000$  
$1 \leq Q \leq 100000$  

## Example

`qxy.in`  
```
6  
1 3 2 4 6 3  
2  
1 4 3 5  
2 5 3 7  
```

`qxy.out`  
```
2  
3  
```

## Explanation

For the first question: among the numbers $1, 3, 2, 4$ there are $2$ numbers between $3$ and $5$.

For the second question: among the numbers in the subarray $3, 2, 4, 6$ there are $3$ numbers between $3$ and $7$.
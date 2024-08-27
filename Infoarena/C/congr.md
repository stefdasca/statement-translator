## Task

Given $2P - 1$ natural numbers $a_1 , a_2 , \dots, a_{2P-1}$, determine $P$ of these such that their sum is divisible by $P$.

## Input data

The input file `congr.in` contains on the first line the natural number $P$. The next line contains the $2P - 1$ numbers separated by a space.

## Output data

The output file `congr.out` contains a single line with $P$ numbers, separated by a space, representing the indices of the chosen elements from the given array.

## Constraints and clarifications

$P$ is a prime number.  
$1 \leq P \leq 300\ 000$.  
$0 \leq a_i < 10^6$.  
For 20% of the score, $P < 300$.  
For 50% of the score, $P < 2000$.  
The numbers in the output file can be printed in any order.

## Example

`congr.in`  
5  
8 7 9 2 4 5 7 2 8

`congr.out`  
1 2 3 5 8

## Explanation

The chosen numbers are at positions 1, 2, 3, 5, and 8, having the sum $8 + 7 + 9 + 4 + 2 = 30$, which is divisible by 5.
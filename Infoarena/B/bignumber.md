# Bignumber

Algorel just had an interview at AlgoTech. Being naturally smart, he managed to solve all the problems except one that he couldn't figure out how to do. Knowing that the Moisil's Heirs Contest is taking place in Iași, he thought of proposing this problem and offering 100 points as a reward to those who solve it correctly. We are given an array with $N$ digits on which the swap operation can be performed at most $X$ times. By swap, we mean exchanging two elements in the array that are in neighboring positions.

## Task

Determine the maximum number that can be obtained from the array with $N$ digits, after performing at most $X$ swap operations.

## Input data

The input file `bignumber.in` contains on the first line the natural numbers $N$ and $X$ separated by exactly one space, and on the next line there are $N$ digits without space.

## Output data

The output file `bignumber.out` contains on the first line the maximum number that can be obtained according to the task from the statement.

## Constraints and clarifications

$1 \leq N \leq 1\ 000\ 000$  
$0 \leq X \leq 1\ 000\ 000\ 000$  
For 30% of the tests $N \leq 5\ 000$  
For another 20% of the tests $X \leq 25\ 000\ 000$  

## Example

`bignumber.in`  
5 3  
14325

`bignumber.out`  
43215
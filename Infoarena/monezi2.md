## Monezi2

Aurel has $N$ types of coins with values $v_1, v_2, \dots, v_N$. Whenever he wants to pay a certain amount of money, Aurel adheres to the following condition: for any two types of coins $i$ and $j$, with $1 \leq i < j \leq n$, he will use at least as many coins of type $i$ as coins of type $j$.

## Task

Write a program to help Aurel check if he can pay certain amounts of money while respecting the condition mentioned above.

## Input data

The input file `monezi2.in` contains:

- The first line contains the natural number $N$, representing the number of types of coins.
- The next line contains the numbers $v_1, v_2, \dots, v_N$, separated by spaces.
- The third line contains the number $Q$, which is the number of amounts of money Aurel wants to check if they can be paid respecting the condition from the statement.
- The following $Q$ lines contain the numbers $s_1, s_2, \dots, s_Q$, each representing one of the $Q$ amounts of money, one per line.

## Output data

The output file `monezi2.out` will contain $Q$ lines. The $i$-th line will print the word `DA` if the amount $s_i$ can be paid. Otherwise, it will print the word `NU`.

## Constraints and clarifications

$1 \leq n \leq 50$  
$1 \leq Q \leq 10000$  
$1 \leq v_i \leq 1000$  
$1 \leq s_i \leq 100000$  
Aurel has an unlimited number of coins for each type

## Example

`monezi2.in`  
`2`  
`3 5`  
`2`  
`14`  
`10`  

`monezi2.out`  
`DA`  
`NU`

## Explanation

The amount $14$ can be paid using $3$ coins of type $1$ and one coin of type $2$. The amount $10$ cannot be paid with the given types of coins while respecting the condition from the statement.
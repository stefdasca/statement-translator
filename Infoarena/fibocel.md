Fibocel

Everyone knows that Fibocel is passionate about numbers and wants to stand out at any cost. One day, he decided to call a number fibocel (after his name) if the number of bits equal to 1 in the binary representation of the number is a Fibonacci number. Since this is not enough for him, Fibocel decided to propose a problem at his favorite contest in Iași.

## Task

Answer $Q$ questions of the form: How many fibocel numbers exist in the closed interval $[A, B]$?

## Input data

The input file `fibocel.in` contains on the first line the natural number $Q$, and on the next $Q$ lines contain two natural numbers $A$ and $B$ separated by exactly one space, representing the ends of the interval to which the question refers.

## Output data

The output file `fibocel.out` will contain exactly $Q$ numbers, one per line, representing the answers to the $Q$ questions, in the order they appear in the input file.

## Constraints and clarifications

$1 \leq Q \leq 50.000$  
$1 \leq A \leq B \leq 10^{15}$  
The Fibonacci sequence is defined as follows:  
$F_0 = F_1 = 1$  
$F_n = F_{n-1} + F_{n-2}$, for $n \geq 2$

For 40% of the tests $B \leq 1.000.000$

## Example

`fibocel.in`  
`fibocel.out`

## Explanation

$1 \text{ 15 } 16$  
$1 \text{ 15 (10) = 1111 (2) }$ does not satisfy fibocel (it has 4 bits of 1 and 4 is not a Fibonacci number)  
$16 (10) = 10000 (2)$ satisfies fibocel (it has 1 bit of 1 and 1 is a Fibonacci number)

$7 \text{ 1 }$   
$13 \text{ 13 }$   
$31 \text{ 13 }$   
$131 \text{ 31 }$   
$131 \text{ 131 }$   
$313 \text{ 313 }$   
$1313 \text{ 1313 }$   
$3131 \text{ 13 }$   
$14 \text{ 76 }$   
$63 \text{ 97 }$   
$421 \text{ 667 }$  
$\dots$
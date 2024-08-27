## Task

Two arrays ($A$ and $B$), sorted in ascending order with lengths $N$ and $M$ respectively, are given. Curious by nature, Algorel, during his internship at AlgoTech, needs to find the answer to several questions of the form: if we were to merge the subarray $[ le1 ; ri1 ]$ from array $A$ with the subarray $[ le2 ; ri2 ]$ from array $B$ resulting in another ascending array, what is the median element of the resulting array? After Algorel solved the problem and saw how interesting it is, he decided to propose it for an algorithm contest. As ONIS is taking place in Cluj this year, you are the lucky ones who have to solve it! Given $T$ tests, each with two arrays $A$ and $B$ of $N$ and $M$ sorted elements respectively, answer $Q$ questions of the form explained above.

## Input data

The input file `mediana.in` contains on the first line the number $T$, and the following lines describe the $T$ tests. Each test takes multiple lines, as follows:  
One line containing the values $N$, $M$ and $Q$  
One line containing $N$ numbers representing array $A$  
One line containing $M$ numbers representing array $B$  
$Q$ lines each containing 4 values: $le1$, $ri1$, $le2$, $ri2$  

## Output data

In the output file `mediana.out` you should print multiple lines. On each line, there is a single number representing the answer to a question from the input file. The answers must appear in the order of the questions in the input file.

## Constraints and clarifications

$T \leq 20$  
$1 \leq N, M, Q \leq 100\,000$  
$0 \leq le1 \leq ri1 < N$  
$0 \leq le2 \leq ri2 < M$  
All numbers in the input file are less than 2 billion  
In the case where $L$ - the length of the array - is even, the median element will be considered the one at position $L \div 2$ (integer part)

## Example

`mediana.in`  
`2`  
`5 5 8`  
`1 2 3 4 5`  
`1 2 3 4 5`  
`0 0 1 4 `  
`0 1 2 4`  
`0 2 3 4`  
`0 3 4 4`  
`1 4 0 0`  
`2 4 0 1`  
`3 4 0 2`  
`4 4 0 3`  
`8 7 4`  
`1 3 6 6 7 9 13 31`  
`2 3 4 5 6 7 8`  
`0 7 0 6`  
`3 5 1 3`  
`2 4 3 6`  
`5 7 1 6`

`mediana.out`  
`3`  
`3`  
`3`  
`3`  
`6`  
`4`  
`5`  
`6`
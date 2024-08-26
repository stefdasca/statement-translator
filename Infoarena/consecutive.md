# Consecutive

Because he was not behaving well at school and disrupted the class, Codrin, a fifth-grade student, received an additional problem from his math teacher. She hopes that this will make Codrin pay more attention in class. However, Codrin does not intend to solve the problem, so he offers the statement to you and asks for your help in solving it. Given a natural number $N$, find in how many ways $N$ can be written as the sum of consecutive natural numbers. For each method, specify the smallest and largest number in the sequence so that the teacher can be sure that he did not try to cheat. Since he wants to impress his teacher, Codrin suggests displaying the sequences in ascending order of their lengths.

## Input data

The input file `consecutive.in` contains on the first line $T$, the number of test cases. Each of the following $T$ lines contains a natural number $N$.

## Output data

The output file `consecutive.out` contains for each number $N$ in order: the first line contains the number of ways $N$ can be written followed by the solution for each way: the first and last number in the sequence of consecutive numbers that sum up to $N$.

## Constraints

$1 \leq T \leq 50$  
$1 \leq N \leq 2^{31}$

## Example

`consecutive.in`
`1`
`15`

`consecutive.out`
`3`
`7 8`
`4 6`
`1 5`

## Explanation

$15 = 7 + 8$  
$15 = 4 + 5 + 6$  
$15 = 1 + 2 + 3 + 4 + 5$
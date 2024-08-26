# Aiacubiti

Bulănel likes numbers and their representation in base $2$. Bulănică, a friend of his, came one day with a problem that Bulănel solved in a second. After solving it, Bulănel had an idea to modify the problem to make it harder. After a few minutes of thinking, they figured out the solution. Now they are willing to give you $100$ points if you solve the problem.

## Task

You are given an array $A$ with $N$ natural numbers. You need to find the number of pairs $(i, j)$ with $i \leq j$ such that the number of different bits in the binary representation of elements $A[i]$ and $A[j]$ is exactly $4$.

## Input data

The input file `aiacubiti.in` contains on the first line a natural number $N$, representing the length of the array. The next line contains the array consisting of $N$ natural numbers separated by spaces.

## Output data

The output file `aiacubiti.out` contains a single number representing the number of pairs requested by Bulănel and Bulănică.

## Constraints and clarifications

$1 \leq N \leq 100000$

For tests worth $20$ points

$N \leq 1000$

$0 \leq A[i] < 2^{20}$

The problem will be evaluated on tests worth $90$ points

$10$ points will be awarded by default

## Example

`aiacubiti.in`
`4`
`15 0 10 5`

`aiacubiti.out`
`2`

## Explanation

We write each number in base $2$: 

$15 \text{ – } 1111$

$0 \text{– } 0000$

$10 \text{ – } 1010$

$5 \text{– } 0101$

The pairs that differ by exactly $4$ bits are: 

$(A[1], A[2]) = (15, 0) = (1111, 0000)$ 

$(A[3], A[4]) = (10, 5) = (1010, 0101)$
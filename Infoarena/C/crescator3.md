## Task

We have two sequences of numbers. The first sequence is given element by element, and the second one is constructed based on a specified rule. Determine how many elements of the first sequence are found in the second one.

## Input data

The first line of the file `crescator3.in` contains a number $N$. The second line contains the $N$ elements of the first sequence, separated by a space and in ascending order. The first element on the 2nd line is also the first element of the second sequence. The other elements of this sequence are built one from another. Thus, if $t$ is the current element, the next one is $t +$ the sum of the digits of $t$.

## Output data

The first line of the file `crescator3.out` contains a number representing the required value.

## Constraints and clarifications

$1 \leq N \leq 100000$  

The elements of the given sequence are non-zero natural numbers smaller than $2000000000$  

It is guaranteed that the difference between the last and the first term of the given sequence is at most $300000$ 

## Example

`crescator3.in`  
`10 1 2 2 6 6 8 10 12 24 30`

`crescator3.out`  
`4`

## Explanation

The generated sequence has the configuration: $1 \ 2 \ 4 \ 8 \ 16 \ 23 \ 28 \ 38 \ \dots$ 

The elements from the given sequence that are found in this one are: $1 \ 2 \ 2 \ 8$
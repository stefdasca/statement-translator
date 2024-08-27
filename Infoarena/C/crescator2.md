# Increasing2

Aurel has learned about sequences of numbers in mathematics. Being naturally curious, he now wants to know how many increasing sequences of non-zero natural numbers with the sum of the elements less than or equal to $S$ exist. Help Aurel find out how many such sequences exist.

## Input data

The input file `crescator2.in` contains a single line which contains the natural number $S$.

## Output data

The output file `crescator2.out` will contain a single line which will contain the number of sequences that Aurel desires, calculated modulo $700001$.

## Constraints and clarifications

$1 \leq S \leq 50\ 000$  
An array of numbers $a_1 a_2 a_3 \dots a_n$ is increasing if $a_1 \leq a_2 \leq a_3 \leq \dots \leq a_n$  
For 20% of the tests $S \leq 50$  
For 40% of the tests $S \leq 400$  
For 60% of the tests $S \leq 6000$  

## Example

`crescator2.in`  
`4`  

`crescator2.out`  
`11`  

## Explanation

The 11 sequences are: 1 1 1 1, 1 1 1 2, 1 1 3, 1 2 2, 1 3, 2 2, 2 3, 3 3, 4
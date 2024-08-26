## PScPld

A string consisting of lowercase English alphabet characters is given. A subarray of the string contains some consecutive characters in the string. A string is a palindrome if it reads the same from left to right and right to left.

## Task

Count the palindromic subarrays that the string contains.

## Input data

In the input file `pscpld.in`, the first line will contain the string of characters.

## Output data

The output file `pscpld.out` will contain the required number. 

## Constraints and clarifications

$1 \leq N \leq 1000000$, where $N$ is the length of the string.

$30\%$ of the tests will have $N \leq 30000$.

## Example

pscpld.in 
`abaaac`

pscpld.out 
`10`

## Explanation

There are $6$ subarrays of length $1$ $( a baaac , a b aaac , ab a aac , aba a ac , abaa a c , abaaa c )$, two subarrays of length $2$ $( ab aa ac , aba aa c )$, and two subarrays of length $3$ $( aba aac , ab aaa c )$.
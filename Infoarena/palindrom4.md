# Palindrom4

A number is called a palindrome if its first digit is equal to its last digit, the second digit is equal to the second last digit, and so on. For example, the numbers $2552$, $404$ and $3$ are palindromes, while $400$, $1230$ and $1212$ are not palindromes.

## Task
Write a program that, given a natural number $n$, determines the closest palindrome to it. In the case when $n$ is equally distant from two palindromes, choose the smaller palindrome.

## Input data

The input file `palindrom4.in` will contain a single line with the value of $n$.

## Output data

The output file `palindrom4.out` will contain a single line with the closest palindrome to $n$.

## Constraints

$0 \leq n \leq 10^6$

## Example

`palindrom4.in` 
`palindrom4.out` 
$4567$ 
$4554$ 

## Explanation

The neighboring palindromes to $4567$ are $4664$ and $4554$. The distances are $d_1=4664-4567=97$ and $d_2=4567-4554=13$, so the closest palindrome is $4554$.

`palindrom4.in` 
`palindrom4.out` 
$63$ 
$66$ 

## Explanation

The neighboring palindromes to $63$ are $55$ and $66$. The distances are $d_1=66-63=3$ and $d_2=63-55=8$, so the closest palindrome is $66$.
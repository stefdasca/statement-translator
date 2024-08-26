## Task

We aim to find the largest natural number less than or equal to a number $N$ that has exactly $K$ prime divisors.

## Input data

The first line of the input file `divprim.in` contains an integer $T$ representing the number of tests in the file. The following $T$ lines contain two numbers $N$ and $K$ with the above meaning.

## Output data

In the file `divprim.out` you will print $T$ lines, each containing the integer $X$ that satisfies the respective properties or $0$ if such a number does not exist.

## Constraints and clarifications

$1 \leq T \leq 100\,000$   
$0 \leq K \leq 7$   
$1 \leq N \leq 1\,000\,000$

$1$ is not a prime number and has $0$ prime divisors.

## Example

`divprim.in`

`3`    
`10 1`    
`10 3`    
`9 2`    

`divprim.out`

`9`    
`0`    
`6`

## Explanations

$3$ is the only prime divisor of $9$

There is no number less than or equal to $10$ that has $3$ prime divisors, the first such number being $30$

$2$ and $3$ are the only prime divisors of $6$
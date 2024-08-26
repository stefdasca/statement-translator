# Fibo

The Fibonacci sequence is generated as follows: $F_0 = 0$, $F_1 = 1$, and $F_i = F_{i-1} + F_{i-2}$ for any $i \geq 2$. We observe that each Fibonacci number is equal to the sum of the previous two (except for the first two, which are given). Thus, the first 12 elements of the sequence are: $0$, $1$, $1$, $2$, $3$, $5$, $8$, $13$, $21$, $34$, $55$, and $89$. Any number can be represented in the so-called Fibonacci system where the digits are $0$ and $1$, and the representation is obtained by respecting the following rules: A number $x$ written in the Fibonacci system will be in the form: $x_{(Fib)} = c_n c_{n-1} \dots c_3 c_2 c_1$, where $c_i$ are equal to $0$ or $1$. The value of the number $x$ in base $10$ is calculated as follows: $x_{(10)} = c_n *F_n + \dots + c_3 *3 + c_2 *2 + c_1 *1$, where $F_i$ is the $i$-th term in the Fibonacci sequence (now we do not consider $F_0 = 0$, and the sequence starts with a single $1$). For example, $x_{(Fib)} = 10101001_{(Fib)} = 1*34 + 0*21 + 1*13 + 0*8 + 1*5 + 0*3 + 0*2 + 1*1 = 53_{(10)}$. But $53_{(10)}$ can also be written as: $53_{(10)} = 1*21 + 1*13 + 1*8 + 1*5 + 1*3 + 1*2 + 1*1$, which leads us to the representation $1111111$. If we add the requirement to the above rule that in the Fibonacci system representation no two consecutive $1$s are generated, the representation will be unique.

## Task

Determine the number of numbers less than or equal to a given number $N$ that, when represented in the Fibonacci system based on the presented rules, are palindromes (they are the same when read from left to right and from right to left).

## Input data

The input file `fibo.in` contains a natural number $N$.

## Output data

The output file `fibo.out` will contain a natural number, representing the count of numbers less than or equal to $N$ that, when represented in the Fibonacci system, are palindromes.

## Constraints

$1 < N \leq 1\ 000\ 000$

## Example

`fibo.in`
`15`

`fibo.out`
`6`

## Explanation

There are $6$ numbers less than $15$ with the required property: $1$ (with representation $1$), $4$ (with representation $101$), $6$ ($1001$), $9$ ($10001$), $12$ ($10101$), and $14$ ($100001$).
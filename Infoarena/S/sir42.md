# Sir42

It is well known that the key to success in computer science is a binary string (composed of the digits $0$ and $1$) $C$ of length $N$. Of course, because it is very precious, it is not known by everyone. However, your friends have decided to help you find it. They did not give you the answer directly (that would have been too easy - haha), but they gave you a number $K \leq N$ and a helper array $R$, defined as follows: $R(i)$ is the leftmost position $j$ for which $C(i) + \dots + C(j) = K$. If for a position $i$ such $j$ does not exist, then $R(i) = -1$.

## Task

Given the information from your friends, find out what is the key to success in computer science!

## Input data

The input file `sir42.in` will contain on the first line the integers $N$ and $K$, and on the second line $N$ integers, representing the array $R$. 

## Output data

The output file `sir42.out` will contain a binary string of exactly $N$ characters, representing the solution to the problem.

## Constraints and clarifications

$1 \leq K \leq N \leq 250$

For tests worth 30 points, $N \leq 20$

The array $C$ is considered to be indexed from $0$. 

If there are multiple solutions, any one of them is accepted.

It is guaranteed that there is at least one solution.

## Example

`sir42.in`

`6 2`

`2 3 3 5 -1 -1`

`sir42.out`

`101101`

`32 2`

`2 2 6 9 9 9 9 9 10 10 10 12 13 13 17 18 18 18 18 23 25 25 25 25 25 26 26 27 29 -1 -1 -1 -1`

`01100010011011000110000101110100`

`5 3`

`4 -1 -1 -1 -1`

`10101`
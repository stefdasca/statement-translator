## Task

Eudanip is a well-known name in programming contests. A prolific proposer, consumer of food without sauces or vegetables, the best competitor among those who do not know how to code. But you probably do not know that he has a brother, Namfosteubossdanip, who has a reputation comparable to that of his brother, only in the world of criminals. Today Namfosteubossdanip is trying to make money in front of AFI Cotroceni by performing childish tricks. Sitting between the man playing the harp and the men playing a shell game, he sells natural numbers to passersby at high prices. We do not exactly understand how Namfosteubossdanip's business works, but one thing is certain, if he wants to be able to produce the number $X$, he must necessarily have in his possession at least one prime factor of the number $X$. Thus, having the number $7$, for example, he can produce and sell any of the numbers $7, 14, 21, \dots$, in any quantity. Namfosteubossdanip received a list of orders for natural numbers that he needs to sell. He wants to buy the necessary prime numbers to fulfill these orders while spending as little money as possible. You are given $N$ numbers with a maximum value of $M$ that need to be sold, and the cost of each prime number less than or equal to $M$. What is the minimum total cost needed for Namfosteubossdanip to be able to produce all $N$ numbers from the input?

## Input data

The input file `numerologie.in` will contain in its first line the numbers $N$ and $M$. The second line contains $N$ natural numbers less than or equal to $M$ and greater than or equal to $2$. The third line contains $M$ values. The $i$-th of these values will be equal to the cost of the number $i$, if it is prime. If it is not prime, the corresponding value will be equal to $-1$. 

## Output data

The output file `numerologie.out` will contain a single number representing the minimum cost to cover all $N$ numbers.

## Constraints

$1 \leq N \leq 1250$  
$2 \leq M \leq 1250$  
The costs of the prime numbers will be natural numbers in the range $[1 \dots 10^6]$

30% of the tests will also have $N, M \leq 60$ 

## Example

`numerologie.in`
```
3
10
8 6 5
-1 5 3 -1 3 -1 -1 -1 6 -1
```

`numerologie.out`
```
8
```

## Explanation

We are obliged to buy the prime numbers $2$ and $5$, and these are sufficient.
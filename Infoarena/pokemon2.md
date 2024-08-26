## Pokemon2

We all know Ash's story in the legendary Pokemon world. This time, Ash wants to participate in the final tournament to become the greatest Pokemon master. He has $N$ Pokemon. Upon entering the competition, he discovered a strange rule: no Pokemon is allowed to level up during the tournament. Therefore, our boy thought it would be better to level up his Pokemon as much as possible before registering. For this purpose, he has $M$ Rare Candy. A Rare Candy is an item that can increase a Pokemon's level by 1, and a Pokemon can consume any number of such candies. Ash has a list of preferences among Pokemon and wants the difference between the level of the first Pokemon and the level of the second Pokemon to be at least $A_1$, the difference between the level of the second Pokemon and the level of the third Pokemon to be at least $A_2$, $\dots$. Ash wants to know in how many ways he can distribute the Rare Candies to the Pokemon so that his preferences are met. Since the result can be very large, the answer should be displayed modulo $1000000007$.

## Input data

The input file `pokemon2.in` will contain two natural numbers $N$ and $M$, representing the number of Pokemon and the number of Rare Candies Ash has, respectively. The next line contains $N-1$ natural numbers, the $i$-th number representing $A_i$, which is the minimum required difference between the level of the $i$-th Pokemon and the level of the $(i+1)$-th Pokemon.

## Output data

The output file `pokemon2.out` will contain a single number representing the number of ways to distribute the Rare Candies modulo $1000000007$.

## Constraints and clarifications

$1 \leq N \leq 100$

$0 \leq A_i \leq 10$

$1 \leq M \leq 100000$

$a$ modulo $b$ represents the remainder of the division of $a$ by $b$.

One distribution method differs from another if there is a Pokemon whose final level differs in the two situations. Initially, the levels of the Pokemon are $0$.

## Example

`pokemon2.in`

```
3 
5 
1 1
```

`pokemon2.out`

```
2
```

## Explanation

The solutions are $3 2 0$ and $4 1 0$.
## Task

On the planet Narb, there is a community of small creatures no taller than $10$ cm called narbs. Following an unknown event, the narbs have organized a special contest to measure their strengths. In the contest, $N$ narbs participate, numbered in the order they enter the competition, from $1$ to $N$. When a narb with the order number $i$ enters the competition, it tells the organizers a natural number $X_i$. The organizers will write on a sheet all numbers from $1$ to $X_i$ converted to base $2$ and glued next to each other. The score of this narb is represented by the number of occurrences of the digit $1$ in this string, which we will denote with $R_i$.

For example, if a narb chooses the number $4$, the organizers will get the sequence $11011100$, so the score is $5$. Due to the fierce competition among them, each narb will want to get a higher score than the previous narb, so they will choose a number larger than the previous one. For organizational reasons, it has been agreed that for all narbs $X_i = X_{i-1} + (R_{i-1} \mod 16) + 1$.

As compensation, the first narb has the right to choose any value of $X_1$. The great leader of the narbs, Ibran, has a son in this competition and wants to find out his score, but he does not know his order number. All he knows is that his son is among the last $K$ contestants. Therefore, he will request a list of the scores of the last $K$ contestants in order.

## Input data

The input file `narbi.in` will contain on the first line $3$ natural numbers $N$, $K$, $X_1$, representing the number of contestants, the length of the list of the last contestants, and $X_1$, the natural number chosen by the first contestant.

## Output data

The output file `narbi.out` will contain $K$ lines. Each line with the order number $i$ will contain a natural number $R_{N-K+i}$ representing the score obtained by contestant $N-K+i$.

## Constraints and clarifications

$1 \leq N \leq 16\ 000\ 000$

$1 \leq K \leq \min(1000, N)$

$1 \leq X_1 \leq 100$

$x \mod y$ represents the remainder of the division of $x$ by $y$

## Example

`narbi.in` 
```
2 2 4
```

`narbi.out` 
```
5
17
```

## Explanation

The first narb chooses the number $4$. It will generate the sequence $11011100$ so $5$ points. The second narb chooses the number $10$ ($4+5+1$) and generates the sequence $11011100101110111100010011010$ and thus the score of $17$.
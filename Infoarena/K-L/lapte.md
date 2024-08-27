# Milk

Haralambie is a huge milk drinker. Together with his friends, he often organizes wild parties, where they compete in drinking milk. This time, they have organized a game. They have two types of milk: milk $A$ and milk $B$. Tonight, their goal is to drink at least $L$ liters of each type. But morning is coming soon, Haralambie's parents are returning home, and the party will be over. Help them drink as quickly as possible.

## Task

The speed at which each person drinks one liter of milk $A$ and milk $B$ is known. A strategy must be planned so that by the end of the party, they have drunk at least $L$ liters of milk $A$ and at least $L$ liters of milk $B$, and the total time is minimized. One person cannot drink from both types of milk at the same time.

## Input data

The first line of the input file `lapte.in` contains the numbers $N$ (number of participants) and $L$ (the minimum amount of milk that needs to be drunk by the end of the party). The next $N$ lines contain pairs of non-zero natural numbers $a$ $b$ $(1 \leq a, b \leq 100)$ representing the time it takes the corresponding person to drink 1 liter of milk $A$ and the time it takes to drink 1 liter of milk $B$, respectively.

## Output data

The first line of the output file `lapte.out` will contain a single number $T$ - the minimum time in which the required amount of milk will be drunk. The next $N$ lines will contain pairs of natural numbers. Line $i + 1$ will contain the numbers $x$ $y$, representing the amount of milk $A$ and the amount of milk $B$ that person $i$ drinks.

## Constraints and clarifications

$1 \leq N, T, L \leq 100$

The available amount of milk is considered unlimited.

Excessive milk consumption leads to the exhaustion of the drink.

## Example

`lapte.in`
```
3 20
1 1
2 4
1 6
```
`lapte.out`
```
18
0 18
5 2
18 0
```

## Explanation

The minimum time is $18$. The amount of milk $A$ drunk is $0+5+18=23$. The amount of milk $B$ drunk is $18+2=20$. Person 1 finishes drinking in $1*0+1*18=18$ minutes. Person 2 finishes in $2*5+4*2=18$ minutes. Person 3 finishes in $1*18+6*0=18$ minutes. The minimum time after which the party will end is $\max(18,18,18)=18$
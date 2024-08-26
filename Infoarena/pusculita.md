# The Piggy Bank

Gigel has collected several coins in a piggy bank. Before he started collecting money, he measured the weight of the empty piggy bank, so now Gigel knows the total weight of the coins in the piggy bank. He wants to buy a book and would like to determine the total amount of money collected in the piggy bank, without breaking it, to ensure he has enough money. Realizing that it is possible to determine the amount of money in the piggy bank based only on its weight, he asks Alina to weigh one coin of each type in the piggy bank.

## Task

Determine the minimum total sum that can be in the piggy bank.

## Input data

The input file `pusculita.in` contains on the first line the natural number $S$, representing the total weight of the coins, and the natural number $N$, representing the number of types of coins in the piggy bank. The next $N$ lines each contain two natural numbers indicating the weight and value of a type of coin, separated by a space.

## Output data

The output file `pusculita.out` will contain or print the minimum sum that can be in the piggy bank.

## Constraints and clarifications

$1 \leq N \leq 100$

$1 \leq S \leq 10000$

$1 \leq weight \ of \ any \ coin \leq 100$

$1 \leq value \ of \ any \ coin \leq 100$

It is considered that the number of coins of each type is unlimited

## Example

`pusculita.in`:
```
15 
4 
2 1 
3 2 
6 5 
4 10 
```

`pusculita.out`:
```
8
```

## Explanation

The piggy bank can contain the minimum sum formed by 6 pieces of the first type of coin $6 \times 1 = 6$ and one piece of the second type $2 \times 1 = 2$, their sum being 8.
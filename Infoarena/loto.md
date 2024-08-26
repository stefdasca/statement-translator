# Loto

Gigel is very passionate about gambling, and his favorite game is " $6$ out of $N$ ". In this game, he can write $6$ numbers on a ticket, from $N$ distinct natural numbers given by the National Lottery; a number can be used on a ticket multiple times. Gigel dreamed one night that the sum of the numbers written on the winning ticket will be $S$, so the next day he went to place a winning ticket!

## Task

Write a program that tells Gigel which numbers to choose to obtain a winning ticket (with the sum $S$).

## Input data

The first line of the file `loto.in` will contain the natural numbers $N$ and $S$, separated by a space. The second line will contain $N$ distinct natural numbers, given by the National Lottery.

## Output data

The file `loto.out` will contain $6$ values representing the numbers chosen for Gigel's ticket. If a winning ticket cannot be obtained, the output file will contain only the number $-1$.

## Constraints and clarifications

$1 \leq N \leq 100$

$1 \leq S \leq 600\ 000\ 000$

The values of the numbers given by the National Lottery will not exceed $100\ 000\ 000$

If there are multiple solutions, only one will be displayed.

## Examples

`loto.in`
```
3 13 
1 2 3 
```

`loto.out`
```
1 1 2 3 3 3 
```

`loto.in`
```
3 19 
1 2 3 
```

`loto.out`
```
-1 
```
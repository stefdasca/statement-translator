## Cycle

Acarie, happy that he passed the algebra exam, goes into the city to celebrate. He is so happy that he does not settle for a simple route between terraces but wants a cycle to be sure he can continue partying for as long as he wishes. Unfortunately, the roads between the terraces have different costs and are not bidirectional. Acarie is not necessarily interested in minimizing the cost of this cycle but wants to minimize the average cost of the cycle (obviously, he wants to travel as little as possible between terraces, which means the cost of the cycle divided by the number of terraces should be minimal). Help Acarie once again, and he will treat you all day.

## Task

Write a program that determines the minimal average cost of a cycle of terraces.

## Input Data

From the file `ciclu.in`, read $N$ (the number of terraces), $M$ (the number of unidirectional roads), and the $M$ direct roads between terraces. Each of these roads is given on a separate line and represented by three integers - the terrace from which the road starts, the terrace where the road leads (numbers between $1$ and $N$), and the cost of the road (a strictly positive integer less than $100\, 000$).

## Output Data

Print to the file `ciclu.out` the minimal average cost of the found cycle, with a precision of $2$ decimal places.

## Constraints and clarifications

$2 \leq N \leq 1000$

$2 \leq M \leq 4000$

It is guaranteed that there is at least one cycle.

The result will be checked with a precision of $0.1$.

## Example

`ciclu.in`
```
4 
5 
1 2 1 
2 3 1 
1 3 1 
3 4 2 
4 1 3
```

`ciclu.out`
```
1.75
```
# Cmmdcgame

Daenerys and Jon are playing a game. In this game, they have $N$ cities to conquer, each city having a population. In one move, one of them can attack a city (Daenerys with dragons, Jon with wolves). If a city has a population of $X$ before the attack, after the attack, this population can be reduced to any number $Y < X$ with the property that $X$ and $Y$ are coprime (do not ask why -- this is how dragons and wolves work). The one who can no longer attack any city loses. Given multiple initial populations of cities, and assuming Daenerys plays first, you are asked to find out who wins (assuming optimal play).

## Input data

The input file `cmmdcgame.in` contains, on the first line, the number $T$ of tests in the file. The descriptions of the $T$ tests follow. The first line of a test description contains the number $N$ of cities. The second line of a test description contains the populations of the cities, non-zero natural numbers, separated by spaces.

## Output data

The output file `cmmdcgame.out` will contain the answers to the $N$ tests. If the winner of a test is Daenerys, print $D$, otherwise print $J$. 

## Constraints and clarifications

Let $SN$ be the sum of the values of $N$ in an input file.

Let $V$ be the maximum size of any city in an input file. 

$1 \leq T \leq 300\ 000$

$1 \leq SN \leq 300\ 000$

$1 \leq V \leq 300\ 000$

For 20 points, $V \leq 1\ 000$ and the cities have a prime (or 1) population.

For another 20 points, $V \leq 1\ 000$

For another 20 points, the cities have a prime (or 1) population. 

## Example

`cmmdcgame.in`

```
2
2
2 3
2
123 123
```

`cmmdcgame.out`

```
D
J
```

## Explanation

In the case of the first game, for Daenerys to win, she needs to attack the second city, reducing its population to $2$. 

Then, any move made by Jon leads to a situation with one city with a population of $1$, and one with a population of $2$. 

After Daenerys attacks the city with a population of $2$, Jon wins. 

In the case of the second game, Jon can always mimic Daenerys's strategy on the city that Daenerys does not attack. 

Thus, Jon wins.
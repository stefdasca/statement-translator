# Markon

Albăstrel found a map representing $N$ cities connected by $M$ bidirectional tunnels. Each city is associated with a natural number with an unknown significance to Albăstrel. Ingenious by nature, he used the map to create a new computer game. The game consists of marking cities according to a specific rule: a city $A$ can be marked only if at least one of its neighboring cities $B$, already marked, has one of the properties:
1. The value associated with $B$ is equal to zero;
2. The value associated with $B$ is strictly greater than the number of unmarked neighboring cities to $B$.

Two cities are considered neighbors if there is a tunnel between them. The computer chooses the starting city $X$ and the player must begin marking with this city. To win, the player must mark the maximum number of cities on the map, respecting the game rule.

## Task

Knowing that the starting city chosen by the computer is $X$, write a program to determine $NR$, representing the maximum number of cities that can be marked, as well as the $NR$ cities, in the order in which they are marked.

## Input data

The input file `markon.in` contains on the first line three natural numbers $N$, $M$, and $X$ separated by spaces, representing $N$ - the number of cities, $M$ - the number of tunnels, and $X$ - the city chosen by the computer as the starting city. The second line contains $N$ numbers separated by spaces, representing the value associated with each city. The next $M$ lines each contain two numbers $a$ and $b$ representing that there is a bidirectional tunnel between cities $a$ and $b$.

## Output data

The output file `markon.out` should contain on the first line the number $NR$, and on the next $NR$ lines, a number representing the cities in the order in which they were marked, respecting the game rule.

## Constraints and clarifications

$2 \leq N$

$M \leq 500\,000$

$1 \leq v_i \leq 10^9$

The cities are distinctly numbered from $1$ to $N$

There can be at most one tunnel between two different cities

City $X$ is the only city that can be marked first

If there are multiple solutions with the maximum number, any of them can be displayed

For $30\%$ of the tests $N, M \leq 10\,000$

## Example

`markon.in`
```
5 6 3
3 2 0 1 1
1 2
5 1
1 4
2 5
4 2
3 4
```

`markon.out`
```
2
3
4
```

## Explanation

City $3$, chosen by the computer, is initially marked. City $4$ is marked because it is the only city with a neighbor $(3)$ that satisfies property $1$.
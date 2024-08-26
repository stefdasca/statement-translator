Colonies

In our galaxy, there is a single colony that produces superluminal engines (which also holds the secret to these engines), and delivering them to other colonies in different galaxies is done in one direction only (the engines are not returned), but not directly, rather through intermediary colonies (thus the engines are protected from long journeys). A colony $C_1$ depends on another colony $C_2$ if and only if all existing transport paths from the engine-producing colony to colony $C_1$ pass through $C_2$. Write a program that determines for each colony the number of colonies it depends on in terms of engine transport.

## Input data

The input file colonii.in contains on the first line 3 integers separated by a space $N$, $M$, and $C$, with the following meanings: $N$ - the number of colonies, $M$ - the number of transport links, and $C$ - the engine-producing colony. Colonies will be identified by distinct natural numbers from $1$ to $N$. Each of the following $M$ lines will contain two integers $x$ and $y$, separated by a space, meaning "there is a one-way connection from colony $x$ to colony $y$".

## Output data

The output file colonii.out will contain $N$ lines, one for each colony. Each line $i$ of the output file will contain the number of colonies on which colony $i$ depends in terms of engine transport.

## Constraints and clarifications

$1 \leq N, C \leq 5\ 000$  
$1 \leq M \leq 650\ 000$

## Example

`colonii.in`  
```
5 9 3
1 2
1 5
2 3
2 4
3 1
3 2
4 1
4 2
5 2
```

`colonii.out`  
```
1
1
0
2
2
```

## Explanation

Colony $1$ depends on colony $3$.  
Colony $2$ depends on colony $3$.  
Colony $3$ does not depend on anyone.  
Colony $4$ depends on colony $3$ and colony $2$.  
Colony $5$ depends on colony $3$ and colony $1$.
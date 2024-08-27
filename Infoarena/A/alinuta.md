Alinuta

Alinuta and Bobica are playing a game with stones based on the following rules: Initially, there are two piles containing $A$ and $B$ stones, respectively. In each move, stones can be taken from one or both piles. If stones are taken from only one pile, any number of stones (up to the ones available in that pile) can be taken. If stones are taken from both piles, then the absolute difference between the number of stones taken from the piles must be less than or equal to $K$. In each move, at least one stone must be taken. The player who takes the last stones wins. Alinuta moves first.

## Task

Given $K$ and the number of games, determine if Alinuta wins or loses for each of the $T$ games. A game is specified by $A$ and $B$, the number of stones in the two piles.

## Input data

The first line contains $K$ and $T$ as described above. The next $T$ lines contain two integers, $A$ and $B$, which indicate the number of stones in the piles for each game.

## Output data

For each test in the input file, print a line containing $A$ if Alinuta wins the game or $B$ if Bobica is the one with a guaranteed winning strategy.

## Constraints and clarifications

$1 \leq T \leq 50000$  
$1 \leq K \leq 10000$  
$1 \leq A, B \leq 100000$  
Alinuta and Bobica play perfectly.

## Example

`alinuta.in`  
```
1 2  
1 3  
2 5  
```
`alinuta.out`  
```
B  
A  
```
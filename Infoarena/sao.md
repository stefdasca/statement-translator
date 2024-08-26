## Task

After entering the new game: Sword Art Online, Kirito decided to measure his strength in the latest quest that appeared. Initially, Kirito has $HP$ (health) and $K$ magical potions. He has to face $N$ very powerful monsters. Since these monsters are the bosses at each level of the game, Kirito is forced to fight the $N$ enemies in their order of appearance (monster $1$, monster $2$, etc.). For each monster, Kirito knows how much $HP$ he loses to kill it. In the fight with monster $i$ he loses $i$ $HP$. Kirito can at some point use one of the $K$ potions to destroy a monster without losing any health. Help Kirito decide on which monsters to use the $K$ potions to be able to kill as many of his enemies as possible (Kirito fights a monster and wins only if he has at least as much $HP$ as the damage he would take from that monster. When his $HP$ reaches $0$ or less, he automatically dies and cannot continue). 

## Input data

The input file sao.in will contain the first line with $3$ natural numbers $N$, $K$ and $HP$. The second line will contain $N$ elements, element $i$ representing the damage value $i$.

## Output data

The output file sao.out will contain a single natural number representing the maximum number of monsters Kirito can kill.

## Constraints and clarifications

$1 \leq N \leq 100000$

$1 \leq HP \leq 1000000000$

$1 \leq |damage i| \leq 1000000000$

$1 \leq K \leq N$

If a monster has negative damage, it means the player gains $hp$ by fighting with it. However, if the player already has $0$ or less health, he will not be able to fight that monster anyway. 

For 50% of the score $1 \leq damage i$ $\dots$

## Example

```
sao.in
10 2 10 
-3 2 3 -2 8 8 6 4 3 3 
```

```
sao.out
8 
```
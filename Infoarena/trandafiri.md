# Roses

Balboa has fallen madly in love with the new girl in town. Unfortunately, he doesn't know if the feeling is mutual. As a result, he has bought $N$ roses, with the $i$-th rose having $V_i$ petals. Now Balboa wants to play the original version of "She loves me, she loves me not!". At each step, he has 2 options:
- Pluck a petal from a rose
- Select 2 identical subsets of roses and throw away one of these sets (he doesn't want to feel déjà vu).

Balboa will keep applying one of these 2 operations until he is left with a single rose (which can have any number of petals). Because he is in a great hurry, he asks you to tell him the minimum number of operations he needs to perform to finish the game.

## Input data

The input file `trandafiri.in` will contain on the first line a natural number $N$, representing the number of roses. On the following line will be $N$ numbers, representing the number of petals for each rose.

## Output data

The output file `trandafiri.out` will contain a single natural number representing the minimum number of operations necessary to finish the game.

## Constraints and clarifications

$1 \leq N \leq 100000$  
$1 \leq V_i \leq 2^{31} - 1$  
All roses initially have a different number of petals.

## Example

`trandafiri.in`  
```
3
1 3 5
```

`trandafiri.out`  
```
6
```
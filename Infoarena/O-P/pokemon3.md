## Task

After long searches, Ash, our hero, has caught all possible Pokémon of each type. All that remains for him to do now is to win the final championship, which takes place in the Pokémon castle where there are $M$ trainers, each with 3 Pokémon. Ash can build any team he wants before entering the castle but is not allowed to change anything once inside. Inside, before each battle, he will choose between 1 and 3 Pokémon to use. A battle proceeds as follows:
1. The opponent sends out the next Pokémon from those remaining.
2. Ash selects a Pokémon to send into battle.
3. If one of the Pokémon is super effective against the other, it wins the battle; otherwise, either of them can win.
4. The Pokémon that loses the battle is eliminated and cannot be used for the rest of the championship.
5. If both Ash and his opponent still have Pokémon, repeat from step 1.

Pokémon can be classified into $N$ categories, and for each two types $i$ and $j$, it is known whether type $i$ is super effective against type $j$. Obviously, if type $i$ is super effective against type $j$, then type $j$ cannot be super effective against type $i$.

Ash wants to win all $M$ battles on the first try, so he will always choose a Pokémon that is super effective against his opponent's Pokémon in a battle.

Knowing in advance the type lists of the $M$ opponents' Pokémon, Ash asks you to tell him the minimum number of Pokémon he needs to bring to win the championship.

## Input data

The input file `pokemon3.in` will contain on the first line $N$ and $M$, the number of different Pokémon types, and the number of opponents in the castle, respectively.

The next $N$ lines will contain $N$ space-separated values of $0$ or $1$. If the $j$-th value on line $i$ is $1$, it means that type $i$ is super effective against type $j$.

The next $M$ lines will contain 3 values each between $1$ and $N$ representing the 3 types of Pokémon of that opponent.

## Output data

The output file `pokemon3.out` will contain a single number representing the minimum number of Pokémon Ash needs to bring to ensure he can win the championship for sure, or $-1$ if he cannot win the championship on the first try without any risk.

## Constraints and clarifications

$1 \leq N \leq 20$

$1 \leq M \leq 10\ 000$

## Example

`pokemon3.in` 
```
3 2 
0 1 0 
0 0 1 
1 0 0 
3 1 1 
2 2 3 3 
```

`pokemon3.out` 
```
3
```

## Explanation

Ash will need one Pokémon of each type to win the championship.
Unul dintre jocurile preferate ale lui Temistocle este un puzzle în care el are la dispoziție un cuvânt, fiecare literă a acestuia fiind scrisă pe câte o plăcuță. Inițial, toate plăcuțele sunt amestecate și așezate într-o ordine oarecare pe un suport liniar, pozițiile plăcuțelor fiind numerotate de la stânga la dreapta, începând cu $1$.

Dacă se alege o plăcuță drept pivot, se obțin două grupe:  

* grupa $1$ - formată din toate plăcuțele din stânga plăcuței-pivot, inclusiv aceasta;
* grupa $2$ - formată din toate plăcuțele din dreapta plăcuței-pivot, fără aceasta.

După alegerea plăcuței-pivot, toate plăcuțele din grupa $1$, dacă există, se deplasează circular spre stânga cu exact o poziție, iar toate plăcuțele din grupa $2$, dacă există, se deplasează circular spre dreapta, cu exact o poziție, ca în figura de mai jos, după care plăcuțele se renumerotează, de la stânga la dreapta, începând cu $1$.

~[puzzle.png]

# Task

Scopul jocului este ca prin alegerea unui șir potrivit de plăcuțe-pivot să se obțină o așezare a plăcuțelor, astfel încât cuvântul format din literele scrise pe acestea, de la stânga la dreapta, să fie identic cu cuvântul corect.

# Input data

In the `puzzle.in` file:
- The first line contains the correct word;
- The second line contains the word formed by the initial arrangement of the tiles.

# Output data

In the `puzzle.out` file, print, separated by a space, the natural numbers representing the positions of the tile-pivots, in the order they are chosen. The sequence ends with the number $0$, which does not correspond to any tile but represents the end of the game.

# Constraints and clarifications

* Each word has at most $250$ characters.
* If there are multiple solutions, only one will be provided, not necessarily the optimal one.

# Example 1

`puzzle.in`
```
abc
bac
```

`puzzle.out`
```
2 0
```

## Explanation

pivot - $2$
ba | c $ \rightarrow $ ab | c

# Example 2

`puzzle.in`
```
abcabc
aabbcc
```

`puzzle.out`
```
6 2 2 0
```

## Explanation

pivot - $6$
aabbcc | $ \rightarrow $ abbcca |
pivot - $2$
ab | bcca $ \rightarrow $ ba | abcc
pivot - $2$
ba | abcc $ \rightarrow $ ab | cabc

# Example 3

`puzzle.in`
```
xyz
xyz
```

`puzzle.out`
```
0
```

## Explanation

The word corresponding to the tiles is the correct one.
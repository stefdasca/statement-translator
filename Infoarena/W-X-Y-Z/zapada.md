# Snow White

Snow White needs to take care of the $N$ dwarfs and has gathered $\frac{N*(N+1)}{2}$ mushrooms from the forest for lunch. She knows that each dwarf should get a different number of mushrooms, and some dwarfs deserve more mushrooms than others because they have been nicer. She has noted in her diary $M$ pairs $ (u, v) $ indicating that dwarf $u$ deserves more mushrooms than dwarf $v$. She soon realized that she cannot keep track of all her notes, so she will remove some pairs under the following condition: if dwarf $u$ deserves more mushrooms than dwarfs $ v_1, v_2, \dots, v_k $, then she will choose a way of distributing the mushrooms such that at least one of the dwarfs $ v_1, v_2, \dots, v_k $ receives fewer mushrooms than dwarf $u$. Obviously, this condition cannot be satisfied by the dwarf who will receive the fewest mushrooms, but Snow White knows that this is inevitable and accepts it as long as the condition is satisfied for the other dwarfs.

## Task

Determine how many mushrooms each dwarf will receive so that Snow White's wish is fulfilled.

## Input data

The file `zapada.in` contains

- The first line contains the number $N$ of dwarfs.
- The second line contains the number $M$.
- The following $M$ lines each contain two integers $u$ and $v$ indicating that dwarf $u$ deserves more mushrooms than dwarf $v$. 

## Output data

The file `zapada.out` contains $N$ lines, line $i$ contains an integer $X_i$ representing the number of mushrooms received by dwarf number $i$.

## Constraints and clarifications

$0 < N < 100\,000$

$0 < M < 350\,000$

$0 < u, v \leq N$

Dwarfs are numbered from 1 to $N$

For all input tests, there is a solution.

If there are multiple solutions, any one of them will be printed.

## Example

`zapada.in`
```
5
8
1 2
1 4
1 3
5 2
2 5
3 5
4 3
2 3
```

`zapada.out`
```
5
3
1
2
4
```

## Explanation

Dwarf number 3 will receive one mushroom, dwarf number 4 will receive 2 mushrooms, dwarf number 2 will receive 3 mushrooms, dwarf number 5 will receive 4 mushrooms, dwarf number 1 will receive 5 mushrooms. Dwarf 3 received one mushroom, ensuring that no dwarf receives fewer mushrooms than them.
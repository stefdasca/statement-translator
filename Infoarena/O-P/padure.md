# Forest

If you are wondering what Prince Algorel is up to, now you can find out. He is lost somewhere in the Magic Forest and is desperately searching for the way back to his castle. The Magic Forest can be represented as a matrix with $N$ rows and $M$ columns, with each cell in the forest knowing the type of trees that cover it (a natural number less than $104$). A cell is covered only with trees of the same type. Prince Algorel is somewhere in the cell $(pl, pc)$ $(pl$ represents the row, $pc$ the column$)$, and the castle is located in the cell $(cl, cc)$. Prince Algorel can move in the four directions: North, South, East, and West, but he cannot leave the forest because beyond the forest lies the land of the Evil Span. On his way to the castle, he has to pay the Magic Keeper a diamond for each transition from one cell to another where the type of trees changes (i.e., if the two cells are covered with different types of trees). For transitions between cells covered by the same type of trees, he pays nothing. Since diamonds are the most important resource in the kingdom, he wants to know the minimum number of diamonds he has to pay to reach the castle.

## Input data

The first line of the `padure.in` file contains $6$ natural numbers: $N$ $M$ $pl$ $pc$ $cl$ $cc$, as explained above. The next $N$ lines contain $M$ natural numbers separated by spaces, representing the type of trees covering each cell in the Magic Forest.

## Output data

The `padure.out` file must contain a single integer $D$ on the first line, representing the minimum number of diamonds Algorel needs to pay to reach the castle.

## Constraints

$1 \leq N, M \leq 1000$

$1 \leq pl, cl \leq N$ 

$1 \leq pc, cc \leq M$ 

Algorel's initial position does not coincide with that of the castle.

For $50\%$ of tests, $N, M \leq 100$

## Example

`padure.in`
```
6 5 1 1 5 4
0 0 0 5 6
7 7 1 1 1
1 3 1 1 1
2 2 1 0 0
9 0 0 0 0
0 9
```

`padure.out`
```
2
```

## Explanation

```
0 0 0 5 6
7 7 1 1 1
1 3 1 1 1
2 2 1 0 0
9 0 0 0 0
0 9
```
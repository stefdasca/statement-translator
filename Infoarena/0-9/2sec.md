2sec

The only wealth of the farmer Ion consists of $N$ apple trees lined up perfectly in a row. Ion numbered the apple trees from $1$ to $N$. Lately, Ion feels that his strength is failing, and he realizes that he will have to give some of the apple trees to his two sons for their use. However, Ion cannot forget how his younger son made his life miserable since he grew up and decides the following: each of the two sons will receive a subarray of apple trees located at consecutive positions in the row of apple trees.
- The number of apple trees in the subarray given to the first son can differ from the number of apple trees in the subarray given to the second son, but each son will receive at least one apple tree.
- The younger son will receive apple trees with strictly smaller order numbers than the older son.
- The difference between the profit brought by the apple trees of the older son and the profit brought by the apple trees of the younger son must be maximized.

The profit brought by an apple tree is calculated by Ion using complicated formulas, perfected over the years. 

## Task

Write a program that finds this difference for Ion.

## Input data

The input file `2sec.in` contains a natural number $N$ on the first line, representing the number of apple trees. On the next line, there are $N$ integers separated by a space, the $i$-th number representing the profit brought by the $i$-th apple tree.

## Output data

The output file `2sec.out` will contain a single line that will contain the maximum difference that can be obtained while respecting Ion's requirements.

## Constraints and clarifications

$2 \leq N \leq 1\,001\,000$

$-127 \leq profit brought by an apple tree \leq 127$

## Example

`2sec.in`
```
10 
8 -5 1 -3 7 -3 2 8 -3 1
```

`2sec.out`
```
21
```

## Explanation

The younger son receives the apple trees with order numbers $2, 3, 4$, and the older son receives the apple trees with order numbers $5, 6, 7, 8$.
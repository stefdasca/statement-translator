## Task
Johnie likes to play with cubes. He has an infinite number of white cubes (with all six faces colored white) and black cubes (with all six faces colored black). All his cubes have a width, height, and length of one meter. Johnie likes to arrange his cubes in $N$ levels, each level containing $2 * 2$ cubes. Thus, Johnie finally obtains a block with a height of $N$, width of $2$, and length of $2$. After getting tired of constructing random blocks, Johnie realized that a block is more beautiful if there is a connected component consisting only of white cubes, containing at least $K$ elements. We say that two cubes $X, Y$ are in the same connected component if: 
- $X$ and $Y$ are positioned on adjacent positions in the block (they share a common face)
- $X$ is adjacent to a cube $Z$, and $Z$ is in the same connected component with $Y$

Determine the number of beautiful blocks that can be constructed. The result must be displayed modulo $10000$.

## Input data
The file `cuburi.in` contains on the first line two numbers, $N$ and $K$.

## Output data
The file `cuburi.out` contains the required number, modulo $10000$.

## Constraints and clarifications
$1 \leq N \leq 40$  
$1 \leq K \leq 4 * N$

## Example

`cuburi.in`
```
3 12
```

`cuburi.out`
```
1
```

`cuburi.in`
```
4 15
```

`cuburi.out`
```
17
```

`cuburi.in`
```
6 15
```

`cuburi.out`
```
2244
```

## Explanation
Test 1: There is only one block, with all cubes white.  
Test 2: There are 17 blocks, because all blocks that have 15 cubes colored white and one colored black are valid (16 such cubes) as well as the block that has all cubes colored white.
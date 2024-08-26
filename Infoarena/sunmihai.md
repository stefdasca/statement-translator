# Sunmihai

The profession of a doctor requires not only knowledge or skill but also intelligence. Sunmihai, a student at the "School of Medical Study and Charms" in Lyon (meme 2020), solves intelligence-developing games daily, but today he is stuck. Sunmihai initially has $N$ domino pieces, each with 2 values written on them, on the left and on the right respectively. A domino piece will knock down another piece if its right value is equal to the left value of the following piece to be knocked down. Sunmihai has the following types of operations available:
1: flip the domino piece at the cost of $A$ (the left and right values of the piece will be swapped)
2: remove any piece from the game at the cost of $B$ (thus, the neighboring pieces will become adjacent; this operation cannot be applied to the first and last domino piece)
3: add a piece between 2 existing domino pieces at the cost of $C$ (strictly after the first piece, but before the last piece; the added piece can have any numbers on the left and right)

Help Sunmihai determine the minimum total cost so that if the first piece is knocked down, the last piece will also fall by implication (obviously, and all those between the first and the last).

## Input data

The input file `sunmihai.in` will contain on the first line 4 numbers $N$, $A$, $B$, and $C$ (as mentioned in the task), and on each of the following $N$ lines, there will be 2 numbers $t_1$ (representing the left value of the $i$-th piece), and $t_2$ (representing the right value of the $i$-th piece).

## Output data

The output file `sunmihai.out` will contain a single number representing the required minimum total cost.

## Constraints

$1 \leq N \leq 100000$  
$1 \leq A, B, C \leq 100$  
$1 \leq t_1, t_2 \leq 100$ for any domino  

For 10 points  
$1 \leq N \leq 10$  
$1 \leq t_1, t_2 \leq 5$ for any domino

For another 20 points  
$1 \leq N \leq 500$  
$1 \leq t_1, t_2 \leq 10$ for any domino 

For another 20 points  
$1 \leq N \leq 5000$  
$1 \leq t_1, t_2 \leq 50$ for any domino

For another 20 points  
$1 \leq N \leq 20000$  
$1 \leq t_1, t_2 \leq 50$ for any domino

## Example

`sunmihai.in`
```
5 8 1 7
2 3
1 1
1 3
3 1
2 1
```

`sunmihai.out`
```
9
```

## Explanation

Remove the 2nd and 3rd pieces at a total cost of 2 and add a piece before the last piece at a cost of 7 with the left number 1 and the right number 2. In total, we will pay 9 units, and the dominos will look like: $(2,3)$ , $(3,1)$ , $(1,2)$ , $(2,1)$
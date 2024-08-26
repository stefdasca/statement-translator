## Task

In his desire to defeat Farmer Jim at the cattle contest, Farmer John decided to find a surplus of triticale grains for his Holstein cows. Triticale is a grain (tribulus multiplicatus) that grows very quickly. To his surprise, John discovers that triticale bales are not uniformly created by the baling machine. Each bale is a parallelepiped with dimensions $s_1,s_2,s_3$. John has a large number of bales for each dimension. The problem he now faces is how to arrange them in the barn. Given a set of bale dimensions and a sufficient quantity of bales for each dimension, it is necessary to determine how they can be stored up to a maximum height. Obviously, the bales can be rotated in any position. Their arrangement in the stack must take into account the fact that one bale can only be placed on top of another whose width and length are strictly larger. This means that a bale $[3, 4, 4]$ cannot be placed on top of a bale $[4, 4, 4]$ because, regardless of orientation, we will not get a bale with strictly smaller width and length of $4$.

## Input data

The first line of the input file, `triticale.in` contains $N$, the number of different types of bales. Each of the following $N$ lines contains the integer dimensions of the bales.

## Output data

The first line of the output file `triticale.out` contains the maximum height of a stack of bales that can be built according to the given rules. In the following lines, print the dimensions of each bale in the stack that can constitute a solution to the problem. The bale dimensions are printed from the top of the stack to the base. On each line, the first two numbers are the dimensions of the face parallel to the ground, the first number being greater than or equal to the second. The third number is the height of the bale.

## Constraints and clarifications

$1 \leq N \leq 1000$  
No dimension exceeds $16\ 000$  

## Example

`triticale.in`
```
3
4 3 1
2 6 5
9 9 8
```

`triticale.out`
```
21
3 1 4
5 2 6
9 8 9
```
## Task

In a distant land, King Spiderman is trying his best to create the magical icrisop. He has at his disposal $N$ types of icrisop, each with a certain magic degree, up to $100$. To obtain the magical icrisop, he must combine the icrisops in a certain order such that the sum of the magic degrees is exactly $S$. King Spiderman asks you to find out in how many ways the icrisop with magic degree $S$ can be obtained, modulo $666013$, considering that there is an unlimited number of each type of icrisop and that the order in which the icrisops are added matters. For example, for $S = 2$, $N = 3$ and icrisop types with magic degrees $1, 1, 2$, the answer is $5$ (type1 $+$ type1, type1 $+$ type 2, type 2 $+$ type 1, type 2 $+$ type 2, type 3).

## Input data

The input file `icrisop.in` contains on the first line $N$ and $S$, and on the next $N$ lines, one number representing the magic degree of each type of icrisop.

## Output data

In the output file `icrisop.out`, you will print the number of ways the magical icrisop with magic degree $S$ can be formed, modulo $666013$.

## Constraints

$1 \leq N \leq 30000$

$1 \leq magic \ degree \ of \ any \ icrisop \leq 100$

$S$ fits in a 32-bit signed integer.

For $20\%$ of tests $S \leq 100000$

## Example

`icrisop.in`
```
3 2
1
2
1
```

`icrisop.out`
```
5
```

## Explanation

The following combinations are possible: type1 $+$ type1, type3 $+$ type3, type1 $+$ type3, type3 $+$ type1, type2
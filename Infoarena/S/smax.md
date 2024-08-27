## Task

Given $A[][]$ a matrix with $N$ rows and $M$ columns containing natural numbers. What is the maximum sum of two elements on distinct positions in $A[][]$ which are at a maximum Manhattan distance $D$?

## Input data

The input file `smax.in` contains on the first line $T$, the number of test cases. For each test case, there are three numbers: $N$, $M$ and $D$ on the first line, and the following $N$ lines contain $M$ numbers each separated by a space, the elements of the matrix in order.

## Output data

In the output file `smax.out` print on separate lines the answer for each test case, the maximum sum.

## Constraints

$T = 5$  
$2 \leq N$  
$2 \leq M$  
$2 \leq D \leq 500$  
$0 \leq A_{i,j} \leq 1000000000$  

The Manhattan distance between the elements at positions $(i_1, j_1)$ and $(i_2, j_2)$ is $|i_1 - i_2| + |j_1 - j_2|$, where $|x|$ is the absolute value of $x$.

## Example

`smax.in`
```
2
5 5 3
1 1 1 1 1
1 1 4 1 1
1 2 1 2 1
1 1 3 1 1
1 1 1 1 1
3 5 4
8 1 4 2 3
2 5 4 6 3
2 3 6 5 7
```

`smax.out`
```
7
14
```

## Explanation

7 $= 4 + 3$

14 $= 8 + 6$
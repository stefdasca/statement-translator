## Task

We have $N$ balls and $N$ boxes. We want to distribute all the balls into the boxes such that they meet the following conditions: the first box can contain at most one ball, the first 2 boxes can contain at most 2 balls, the first 3 boxes can contain at most 3 balls, and so on. In how many ways can this distribution be achieved? Determine the number of ways the balls can be distributed such that the conditions are met. Since the number of ways can be quite large, the result will be calculated modulo $9999991$.

## Input data

The input file `dirichlet.in` will contain the natural number $N$ representing the number of balls and boxes, respectively.

## Output data

The output file `dirichlet.out` will contain a single natural number that represents the answer to the task.

## Constraints and clarifications

1 $\leq$ $N$ $\leq$ $1\ 000\ 000$  
$a$ modulo $b$ represents the remainder of dividing $a$ by $b$  
Attention! It is recommended to use the `long long` type for those who implement in C/C++ and `int64` for those who implement in Pascal

## Example

`dirichlet.in`  
`3`

`dirichlet.out`  
`5`

## Explanation

For $3$:  
$(*)(*)(*)$  
$(*)()(**)$  
$()(*)(**)$  
$()(**)(*)$  
$()()(***)$
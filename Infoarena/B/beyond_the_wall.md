## Task

The children of the forest are hiding from "the others", so they plan to build a great wall to keep them at a distance from the rest of the land. It is known that there are unstable points in the plane, so they wish to build a wall that is as protected from these points as possible. Thus, they have already prepared certain questions in the form "Given a line, answer the question: How many unstable points are strictly below the line?". Because only you know the positions of the points and their questions, they can rely only on you to respond.

## Input data

The input file `beyond_the_wall.in` contains on the first line the numbers $N$ and $Q$ which represent the number of unstable points and the number of questions, respectively. On the following $N$ lines, the coordinates of the points will be found. On the next $Q$ lines, there will be two numbers $M$, $B$ each describing the equation of the line $Y = MX + B$.

## Output data

The output file `beyond_the_wall.out` will contain $Q$ numbers, one per line, the number on line $i$ representing the answer to question $i$.

## Constraints and clarifications

All numbers in the input are integers

$1 \leq N \leq 40000$ 

$-10^5 \leq M, B \leq 10^5$ 

$1 \leq Q \leq 2 \cdot 10^5$ 

$1 \leq N \cdot Q \leq 4 \cdot 10^9$ 

$-10^5 \leq X_i , Y_i \leq 10^5$ 

For 5 points:

$1 \leq N \leq 100$ 

$1 \leq Q \leq 100$ 

For another 60 points:

$1 \leq N \leq 5000$ 

$1 \leq N \cdot Q \leq 4 \cdot 10^9$ 

For the remaining 35 points:

Initial constraints

A point $(X_i, Y_i)$ is below the line $Y = MX + B$ if $MX_i - Y_i + B > 0$ 

## Example

`beyond_the_wall.in`
```
4 2 
1 3 
4 2 
6 4 
7 1 
-1 6 
3 -4 
```

`beyond_the_wall.out`
```
1 
3 
```

## Explanation

We observe that for the first question, the point $B (4, 2)$ is not considered in the response because it lies on the line.
# Wagons

We aim $\dots$ to not be followed! The Special Brigade has been informed that the ten o'clock train has more than $7$ wagons filled with $\dots$ grains and potatoes. It is known that distinguishing one material from another is not an easy task in the dark, so an inspection will be organized in the North Station depot, with the participation of $M$ specially trained dogs. The $N$ wagons of the train are sequentially arranged, one after the other behind the locomotive, and are numbered with consecutive integers from $1$ to $N$. Each dog can be used only once throughout the inspection to test a single compact interval of wagons. A dog will bark immediately if it encounters $2$ wagons with the same content within the interval it is inspecting (otherwise, it will not bark at all). If a single dog barks, the entire transport will be jeopardized, so you will need to calculate the number of ways to load each wagon with one of the $C$ possible contents so that the action is not compromised.

## Task

## Input data

The input file `vagoane.in` contains on the first line the numbers $N$, $M$, and $C$ in order and separated by a space. Each of the next $M$ lines contains two positive integers $L$ and $R$ such that $1 \leq L \leq R \leq N$, representing the ends of the interval of wagons that the respective dog patrols.

## Output data

The output file `vagoane.out` must contain a single non-negative integer $ANS$, representing the number of ways to fill the train wagons modulo $1000000007$.

## Constraints

$1 \leq N \leq 10^9$    
$0 \leq M \leq 2 \cdot 10^5$    
$1 \leq C \leq 5 \cdot 10^5$    

Attention! Large volume of input data, we recommend optimizing reading by using this code.

Attention! Each subtask has grouped tests!

Subtask $1$ (10 points): $M = 0$ (Feedback test $1$)    

Subtask $2$ (20 points): $N \leq 1000$, $M \leq 2000$ (Feedback test $2$)    

Subtask $3$ (30 points): $N \leq 10^5$    

Subtask $4$ (40 points): 

Initial constraints (Feedback tests $7$ and $8$)

## Example

`vagoane.in`  
$3$ $2$ $3$  
$1$ $2$  
$2$ $3$ 

`vagoane.out`  
$12$

## Explanation

The $12$ methods of loading the train are, if we code the $3$ possible loads with the numbers $1$, $2$, and $3$:

$1 2 1$  
$1 2 3$  
$1 3 1$  
$1 3 2$  
$2 1 3$  
$2 1 2$  
$2 3 1$  
$2 3 2$  
$3 1 2$  
$3 1 3$  
$3 2 1$  
$3 2 3$
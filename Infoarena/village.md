## Task

An unnamed villager from an unnamed village wakes up every day to admire the picturesque landscape surrounding his village. Unfortunately, one day, his idyllic existence is interrupted by a grid of $N$ by $M$ factories. He has a bold plan to stop them, but to do so, he needs to know how much smoke each factory produces. Unfortunately, the factories are surrounded by a high wall, so he cannot know this directly. He must deduce this information from some other information he knows. Assuming that $s_{i,j}$ is the amount of smoke created by the factory on the $i$-th row and the $j$-th column, he knows that: For some parameters $x_1, \dots, x_N$ and $y_1, \dots, y_M$, he knows that $x_i = s_{i,1} + \dots + s_{i,M}$ and that $y_j = s_{1,j} + \dots + s_{N,j}$. For some parameters $a_{i,j}$ and $b_{i,j}$, he knows that $a_{i,j} \leq s_{i,j} \leq b_{i,j}$. Interestingly, some factories even consume pollution; thus, for these, $s_{i,j}$ can also be negative. Given the values of the arrays $x$, $y$, and the matrices $a$, $b$, assign integer values to $s$ such that all constraints are satisfied.

## Input data

The input file `village.in` will contain, on the first line, the integer $T$, which represents the number of tests in the file. Each test will have the following format:

The first line of a test will contain integers $N$ and $M$.   
The second line of a test will contain integers $x_1, \dots, x_N$, in order.   
The third line of a test will contain integers $y_1, \dots, y_M$, in order.   
Next, there will be $N$ lines containing the matrix $a$, row by row, with $M$ integers on each row.   
Next, there will be $N$ lines containing the matrix $b$, row by row, with $M$ integers on each row.   

## Output data

In the output file `village.out` you shall write the answers for each test, in order. For each test, print $N$ rows containing the matrix $s$, row by row, with $M$ values on each row.

## Constraints and clarifications

$1 \leq T \leq 100$  
$-10^7 \leq x_i \leq 10^7$  
$-10^7 \leq y_i \leq 10^7$  
$1 \leq N, M \leq 100$  
$-10^5 \leq a_{i,j} \leq 10^5$  
$-10^5 \leq b_{i,j} \leq 10^5$  

## Example

`village.in`  
```
1
3 3
1 2 3
3 2 1
-10 -10 -10
-10 -10 -10
-10 -10 -10
10 10 10
10 10 10
10 10 10
```

`village.out`  
```
-1 1 1
3 9 -10
1 -8 10
```
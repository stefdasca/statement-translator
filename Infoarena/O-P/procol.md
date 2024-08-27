## Task

1 : Given an array with $N$ $k$-elements, determine the length of the longest subsequence that is a colored progression.

## Task

2 : Given a $k$-element $X$, determine how many other $k$-elements $Y$ could appear in a colored progression immediately after element $X$. In other words, how many $k$-elements exist that have at least one color in common with the $k$-element $X$. Since this number can be very large, print the answer modulo $666013$.

## Task

3 : Display a colored progression with $N$ $k$-elements, such that any 2 elements in this progression are different. If there are multiple solutions, display any. If no solution exists, print $-1$.

## Input data

The input file `procol.in` will contain on the first line a natural number representing the index of the task. This number can be $1$, $2$, or $3$. If it is $1$, the next line will contain $2$ numbers $N$, $K$, and $C$. The following $N$ lines will have the array with $K$-elements. Line $i$ will contain $K$-element $i$, specifically $K$ colors numbered from $1$ to $C$. If the task is $2$, line $2$ will contain the numbers $K$ and $C$. On the next line will be the $K$-element $X$. If the task is $3$, line $2$ will contain the 3 natural numbers $N$, $K$, and $C$.

## Output data

The output file `procol.out` will contain the answer based on the task. If the task from the input is $1$, you must print a single natural number representing the length of the longest colored progression. If the task is $2$, you must print a single natural number representing the number of solutions modulo $666013$. If the task is $3$, you must print $N$ lines, with line $i$ being the $i$-th $K$-element ($K$ numbers representing the colors from $1$ to $C$) of the required colored progression. If no colored progression meets the required condition, print $-1$.

## Constraints and clarifications

$1 \leq N * K \leq 200\ 000$  
for task $1$  
$1 \leq K \leq 100\ 000$  
for task $2$  
$1 \leq N * K \leq 1\ 000\ 000$  
for task $3$  
$1 \leq C \leq 1\ 000\ 000\ 000$  
for all tasks  

For the correct solution to the first task, you get $20$ points.  
For the correct solution to the second task, you get $30$ points.  
For the correct solution to the third task, you get the remaining $50$ points.  

## Example

`procol.in`  
```
1
5 3 5
1 3 3
2 4 3
1 5 2
3 4 4
1 1 1
```

`procol.out`  
```
4
```

`procol.in`  
```
2
3 5
2 1 3
```

`procol.out`  
```
3093
```

`procol.in`  
```
3
5 3 3
```

`procol.out`  
```
1 1 1
3 2 3
1 3 3
1 1 2
3
```
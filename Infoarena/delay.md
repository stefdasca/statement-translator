## Task

Write a program that efficiently handles the following two types of operations:
- Type $1$: modifying the waiting time of a computer
- Type $2$: determining the data transmission time between two specified computers.

## Input data

The first line of the input file `delay.in` contains the number $N$ of computers. Each of the next $N$ lines contains an integer $T_i$, representing the initial waiting time of the corresponding computer. The next $N-1$ lines contain two integers $a$ and $b$, representing the numbers of two computers connected by a direct cable. The following line contains the integer $M$, representing the number of operations described hereafter. Each of the following $M$ lines contains 3 integers separated by spaces: $a$ $b$ $c$. 
- If $a = 1$, then $b$ represents the order number of a newly configured computer, and $c$ represents the new waiting time of computer $b$. 
- If $a = 2$, then $b$ and $c$ represent the order numbers of two different computers, and the program will need to print to the output file the data transmission time between computers $b$ and $c$.

## Output data

In the file `delay.out` you will print, on separate lines, the times determined for each operation of type $2$, in the order they are encountered in the input file. When calculating the data transmission time between two computers, the waiting times at that moment must be considered (which are determined by the initial values or type $1$ operations described in the input file before the current operation).

## Constraints and clarifications

$2 \leq N \leq 16000$ 

$0 \leq T_i \leq 1000$ 

$2 \leq M \leq 200000$ 

Computers are numbered from $1$ to $N$ 

There will be at least one operation of type $2$ in the input file.

## Example

`delay.in`
```
5
1
2
3
4
5
1 2
1 3
2 4
3 5
6
2 1 4
2 3 1
1 1 100
2 1 4
2 2 4
2 3 2
```

`delay.out`
```
7
4
106
6
105
```
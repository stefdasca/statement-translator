# Collection

Tudor thought that his CD and DVD collection has become quite impressive, and to organize the discs more easily, he wants to label them. He wants to buy boxes containing number labels. At the nearby store, there are $n$ such packages that contain labels with some digits of $0$, some digits of $1$, and so on (different packages might have different contents). Tudor wants to buy some of the packages and be able to form all the numbers from $1$ to $K$ (where $K$ is the number of CDs and DVDs in his collection) using the labels. A condition for labeling is that there should be no unused labels left, as Tudor wouldn't have any use for them. This is not always possible. If it is possible, then we are interested in the solution that uses a minimum number of packages.

## Input data

The first line of the input file `colectie.in` contains two natural numbers $N$ and $K$, representing the number of packages in the store and the number of CDs and DVDs in Tudor's collection, respectively. On the next $N$ lines, there will be ten integers separated by spaces; line $i + 1$ contains the number of labels with digits $0, 1, \dots, 9$ in package $i$.

## Output data

The first line of the output file `colectie.out` will contain the value $1$ if a solution exists, or the value $0$ if there is no solution. If a solution exists, then the next line will contain the number $L$ of packages used in an optimal solution, and the next line will contain $L$ integers, representing the chosen packages.

## Constraints and clarifications

$1 \leq N \leq 32$

$1 \leq K \leq 100\ 000\ 000$

## Example

`colectie.in`
```
4 11 
0 1 0 0 0 0 1 1 0 0 
1 2 1 1 1 1 0 0 0 0 
0 1 0 0 0 0 0 0 1 1 
0 2 0 0 0 0 1 1 1 1 
```

`colectie.out`
```
1 
2 
2 4 
```
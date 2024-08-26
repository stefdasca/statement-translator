## Task

After all the events in the dream take place, Cobby wants to know the final value of the importance coefficient for a sequence of $K$ matrices given through their indices. Since he is in a hurry to participate in the National Contest "Urmașii lui Moisil," it is your task to find the answer for each matrix.

## Input data

The first line of the file *inception.in* contains the values $N$ - the number of rows and columns in each matrix, $Q$ - the number of events that occur in Cobby's dream, $K$ - the number of matrices for which Cobby wants to know the importance coefficient. The next $Q$ lines follow one of the formats:
1. $id \ i \ j$ - Cobby dreams of the element at row $i$ and column $j$ in the matrix with index $id$
2. $id \ NR \ VAL$ - Cobby adds the value $VAL$ to the importance coefficients of $NR$ matrices starting from the matrix with index $id$ The line $Q + 2$ contains $K$ values $id1 \ id2 \ \dots \ idK$, separated by a space, which represent the indices of the matrices for which the final value of the importance coefficient must be displayed. The events occur in the order given in the file.

## Output data

The first line of the file *inception.out* contains $K$ values $r1 \ r2 \ \dots \ rK$, separated by a space, where $r_i$ represents the final coefficient of the matrix with the id $id_i$, $i \in [1,K]$. 

## Constraints and clarifications

$1 \leq N \leq 500000$

$1 \leq Q \leq 300000$

$1 \leq VAL \leq 1000$

$1 \leq K, NR, id \leq$ the total number of type 1 operations.

In both types of events, the value $id$ corresponds to a previously formed matrix.

It is guaranteed that there are at least $NR$ matrices that can be modified for the type 2 operation.

For 20% of the tests, any matrix will contain at most one dreamed element.

## Example

*inception.in*
```
3
6
3
1 1 2 3
1 2 3 3
2 3 3 5
1 1 3 1
1 2 3 1
2 5 2 1
4 8 5
```

*inception.out*
```
0
```

## Explanation
# Consir

Vultur found a problem in his chemistry book that he doesn't know how to solve and needs your help. You are given a sequence $A$, consisting of $N$ natural numbers. A consir is a sequence of natural numbers $i_1$, $i_2$ $\dots$ $i_p$ (with values between $1$ and $N$) such that $A[i_1]$, $A[i_2]$ $\dots$ $A[i_p]$ are consecutive numbers. Specifically, $A[i_2] = A[i_1] + 1$, $A[i_3] = A[i_2] + 1$ $\dots$ $A[i_p] = A[i_{p-1}] + 1$. Determine $K$, the maximum length of a consir that can be formed, as well as the number of distinct consirs of lengths $1$, $2$ $\dots$ $K$. 

## Input data

The first line of the file consir.in will contain the number $N$ as per the statement. The following $N$ lines contain the values of the sequence $A$, specifically, the value of $A[i]$ is on line $i+1$. 

## Output data

The first line of the file consir.out will contain the value $K$, as per the statement. The following $K$ lines will contain the number of distinct consirs of length $i$. 

## Constraints and clarifications

$1 \leq N \leq 310\ 000$  
The terms of the sequence have values between $1$ and $1\ 000\ 000$  
It is guaranteed that each answer has a value less than $2^{63}$ (fits within 64-bit unsigned integer types)   
The length of a consir is given by the number of elements   
Two consirs $X$ and $Y$ are distinct if there exists a position $i$ such that $X_i$ is different from $Y_i$   
In at least $30\%$ of the tests $N \leq 1\ 000$   

## Example

`consir.in`  
```
6
1
2
1
3
4
5
```

`consir.out`  
```
5
6
5
4
3
2
```

## Explanation

The $2$ consirs of length $5$ are $1, 2, 4, 5, 6$ and $3, 2, 4, 5, 6$  
The $3$ consirs of length $4$: $1, 2, 4, 5$, $3, 2, 4, 5$ and $2, 4, 5, 6$  
The $4$ consirs of length $3$: $1, 2, 4$, $2, 4, 5$, $3, 2, 4$ and $4, 5, 6$  
The $5$ consirs of length $2$: $1, 2$, $2, 4$, $4, 5$, $3, 2$ and $5, 6$  
The $6$ consirs of length $1$: $1$, $2$, $3$, $4$, $5$ and $6$  
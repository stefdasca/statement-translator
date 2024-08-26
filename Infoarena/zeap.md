# Zeap

Though few know, one of Zaharel's great passions is data structures. On a summer’s day, browsing various data structure courses, Zaharel decided to invent his own structure which he named a zeap. In Zaharel's conception, a zeap maintains a set of distinct natural numbers and supports the following operations efficiently:

**INSEREAZA $(Z,x)$**: Inserts the element $x$ into the zeap $Z$; if $x$ already exists in the zeap, the operation is ignored; this operation returns nothing;

**STERGE $(Z,x)$**: Deletes the element $x$ from the zeap $Z$; if the element does not exist in the zeap, the operation returns $-1$;

**CAUTA $(Z,x)$**: Searches for the element $x$ in the zeap $Z$; returns $0$ if the element does not exist or $1$ if it does;

**MAX-DIF $(Z)$**: Returns the maximum absolute difference between any two distinct elements in the zeap $Z$; if there are not at least two elements in the zeap, it returns $-1$;

**MIN-DIF $(Z)$**: Returns the minimum absolute difference between any two distinct elements in the zeap $Z$; if there are not at least two elements in the zeap, it returns $-1$;

## Task

Write a program that simulates the behavior of a zeap.

## Input data

The input file `zeap.in` will contain the description of an operation on each line:

**$I \, x$**: Performs the INSEREAZA $(Z,x)$ operation

**$S \, x$**: Performs the STERGE $(Z,x)$ operation

**$C \, x$**: Performs the CAUTA $(Z,x)$ operation

**$MAX$**: Performs the MAX-DIF $(Z)$ operation

**$MIN$**: Performs the MIN-DIF $(Z)$ operation

## Output data

For each operation that returns a value, the corresponding result will be printed on a separate line in the output file `zeap.out`.

## Constraints and clarifications

The input file will contain at most $300 \ 000$ lines.

The numbers that will be inserted into the zeap will be natural numbers in the range $[1 \dots 10^9]$.

It is recommended to use the `gets/fgets` functions for those programming in C/C++ due to the large volume of input data.

## Example

`zeap.in`
```
I 1 
I 3 
S 2 
I 7 
MAX 
MIN 
C 5 
C 1 
S 3 
MAX 
MIN 
```

`zeap.out`
```
-1 
6 
-1 
0 
1 
-1 
-1 
```
## Networks

In a city, there are $N$ subscribers and multiple telephone networks. Two subscribers belong to the same telephone network if the first subscriber can contact the second (directly or through other subscribers) and vice versa.

## Task

Determine all the telephone networks in the city by specifying the subscribers of each network.

## Input data

The first line of the file `retele.in` contains the numbers $N$ and $M$, representing the number of subscribers and the number of contacts in the city. The following $M$ lines contain two numbers $x$ and $y$, meaning that subscriber $x$ can contact subscriber $y$ directly.

## Output data

The output file `retele.out` contains on the first line the number $T$ of telephone networks. The following $T$ lines will print the telephone networks, one network per line, in the following format: $R$ $A_1$ $A_2$ $\dots$ $A_R$, where $R$ is the number of subscribers, and $A_1$ $A_2$ $\dots$ $A_R$ represent the subscribers who are part of the respective network. The networks will be listed in ascending order of the smallest subscriber number, and the subscribers within the same network will also be listed in ascending order.

## Constraints and clarifications

$1 \leq N \leq 50000$

$1 \leq M \leq 300000$

If subscriber $x$ can contact subscriber $y$ directly, it does not necessarily mean that subscriber $y$ can contact subscriber $x$ directly.

## Example

`retele.in`
```
10 14 
2 3 
3 2 
3 1 
1 9 
9 7 
7 1 
4 3 
4 10 
6 10 
5 4 
5 6 
10 5 
5 8 
5 7 
```

`retele.out`
```
4 
3 1 7 9 
2 2 3 
4 4 5 6 10 
1 8
```
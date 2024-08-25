# Problem with Bulbs

It is not just a mere coincidence $\dots$ Antonio indeed thought of bulbs when he designed this problem. Antonio has an array of $N$ bulbs, numbered from $1$ to $N$. Initially, all bulbs are turned off. He has $M$ switches at his disposal, with which he can turn certain bulbs on or off as he pleases. Switch $i$ changes the state of the bulbs in the interval $[ A[i], B[i] ]$ (the bulbs turned off in this interval turn on, and those that are on turn off). Antonio wants to turn on all the bulbs in the interval $[1, X]$, with a minimum number of switches presses available. Display this minimum number of presses! If this is impossible, display $-1$.

## Input data

The input file `pcb.in` contains on the first line three natural numbers $N$ $M$ $X$, separated by a space. On each line $i$ of the next $M$ lines, there will be found two natural numbers $A[i]$ $B[i]$, separated by a space.

## Output data

The output file `pcb.out` will contain a single natural number, representing the minimum number of switches presses to turn on all the bulbs in the interval $[1, X]$. If it is not possible to turn on all the bulbs in the interval $[1, X]$, print $-1$.

## Constraints and clarifications

$1 \leq N \leq 100\ 000$  
$1 \leq M \leq 200\ 000$  
$1 \leq X \leq N$  
$1 \leq A[i] \leq B[i] \leq N$

## Example

`pcb.in`  
```
5 3 4
1 3
3 4
3 3
```

`pcb.out`  
```
3
```

## Explanation

By using each switch once, all the bulbs in the interval $[1, 4]$ can be turned on.
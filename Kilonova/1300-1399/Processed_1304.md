
Bogdan received a very ingenious game on his birthday. The game consists of a box with two compartments. Initially, in the first compartment, there are $k$ balls (numbered from $1$ to $k$), while in the second compartment, there are $n-k$ balls (numbered from $k+1$ to $n$).

The two compartments communicate through a special flip door that has two slots. One slot is in compartment $1$, and the other is in compartment $2$. One ball can fit in each slot.

Vasile can choose a ball from compartment $1$ and a ball from compartment $2$, place the chosen balls in the two slots of the flip door, and rotate the door. Thus, the ball from compartment $1$ will move to compartment $2$, and the ball from compartment $2$ will move to compartment $1$.

This is the only possible move.

The aim of the game is to execute a sequence of moves so that compartment $1$ successively obtains all distinct subsets of $k$ elements from the set $\{1, 2, \dots, n\}$.

# Task

Write a program that displays the subsets of $k$ elements from the set $\{1, 2, \dots, n\}$ in the order in which they can be obtained in compartment $1$ with the help of the flip door.

# Input data

The input file `bile.in` will contain on the first line the natural numbers $n$ and $k$, separated by a space.

# Output data

The output file `bile.out` will contain one line for each subset obtained in compartment $1$. On each line, there will be written in ascending order $k$ natural numbers from the set $\{1, 2, \dots, n\}$, separated by a space, representing the elements of the subset. On the first line, the initial subset (i.e., the numbers $1, 2, \dots, k$) will be displayed.

# Constraints and clarifications

* $1 \leq k < n \leq 20$
* The solution is not unique, you can display any of the correct variants

# Example

`bile.in`
```
4 2
```

`bile.out`
```
1 2
1 3
1 4
2 4
2 3
3 4
```

## Explanation

In the first move, ball $2$ (from compartment $1$) and ball $3$ (from compartment $2$) were placed in the flip door.
In the second move, balls $3$ and $4$ were chosen.
In the third move, balls $1$ and $2$ were chosen.
In the fourth move, balls $4$ and $3$ were chosen.
And in the last move, balls $2$ and $4$ were chosen.

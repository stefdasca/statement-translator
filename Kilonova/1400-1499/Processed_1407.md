On a horizontal line, there are $n$ crickets. They begin by standing "capră" in a pre-established order starting with the last one, in sequence, to the first. All the crickets that precede the one standing "capră" jump over it, in order.

For example, for $n = 4$, first the cricket $4$ stands "capră" and over it jump, in order, $3$, $2$, and $1$. Then the cricket $3$ stands "capră" and over it jump, in order, $2$, $1$, and $4$. Then the cricket $2$ stands "capră" and over it jump, in order, $1$, $3$, and $4$. Then the cricket $1$ stands "capră" and over it jump, in order, $4$, $3$, and $2$, and it returns to the initial order.

~[greieri.png|align=center|width=45em]

# Task

Write a program that reads the natural numbers $n$ and $m$ and determines:

1) How many jumps are needed to return to the initial order?
2) How will the crickets be arranged after $m$ jumps?

# Input data

The input file `greieri.in` contains two values $n$ and $m$, separated by a space, with the significance described in the statement.

# Output data

The output file `greieri.out` contains:

1) The first line contains a value representing the number of jumps after which it returns to the initial order.
2) The second line contains the numbers representing the order of the crickets after $m$ jumps.

# Constraints and clarifications

* $2 \leq n \leq 100 \ 000$
* $1 \leq m \leq 2 \ 000 \ 000 \ 000$
* $20\%$ of the points will be awarded for correctly solving task $1$.
* $80\%$ of the points will be awarded for correctly solving task $2$.
* Answers to the two tasks will be written exactly on the specified line; if you do not know the solution to one of the tasks, you will write the value $-1$ on the respective line;
* Each line in the input file ends with the "end of line" character.

# Example

`greieri.in`
```
4 5
```

`greieri.out`
```
12
4 3 1 2
```

## Explanation

As seen in the image starting from the initial line $1 \ 2 \ 3 \ 4$, on the first step cricket $3$ jumps over $4$, on the second step cricket $2$ jumps over $4$, on the third step cricket $1$ jumps over $4$, on the fourth step cricket $2$ jumps over $3$, and on the fifth step cricket $1$ jumps over $3$.
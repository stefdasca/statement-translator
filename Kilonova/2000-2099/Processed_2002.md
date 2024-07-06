As Christmas approaches, things are getting very busy at the North Pole. The elves, Santa's main workforce, have an infinitely long conveyor belt, divided into compartments. Initially, the belt has only one gift, located at position $1$. To determine the number of gifts that will be in compartment $k$, Bahoi ~~Santa's chief executive~~ will move the belt one position to the right, adding the number of gifts from position $k-1$ (after the move) to the number of gifts from position $k-1$ (before the move).

In other words, if $q_k$ is the number of gifts in compartment $k$, then $q_k = q_{k-1} + q_{k-2}$, for any $k \geq 2$.

## Task

Due to the chaos at the North Pole, chief executive Bahoi wants to check if he has correctly calculated the number of gifts in each compartment. Therefore, he asks $Q$ questions, each in the form: what is the total number of gifts in compartments between $l$ and $r$? Due to his busy schedule, he considers it sufficient to find the remainder of the total number of gifts when divided by $M$.

# Input data

The first line contains the number $Q$ and the next $Q$ lines contain 3 numbers each, representing $l$, $r$, and $M$.

# Output data

On line $i$ of the output, it will contain the answer to question number $i$.

# Constraints and clarifications

* We assume that there are no gifts at position $0$.
* $1 \leq Q \leq 200\ 000$
* $0 \leq l \leq r \leq 10^{18}$
* $1 \leq M \leq 2 \cdot 10^9$
* For 40 points, $r \leq 200\ 000$ and $M = 10^9 + 7$.

# Example

`stdin`
```
3
0 5 1000
1 3 1000000007
8 8 18
```

`stdout`
```
12
4
3
```

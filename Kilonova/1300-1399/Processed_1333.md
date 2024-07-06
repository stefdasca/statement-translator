Nicușor must take care of the $n$ fish in the aquariums of the Museum of Natural Sciences in Constanța during the holiday. The fish are numbered with distinct numbers from $1$ to $n$ and are placed in $n$ identical aquariums, one fish in each aquarium. Initially, the fish numbered $1$ is in the aquarium labeled $1$, the fish numbered $2$ is in the aquarium labeled $2$, $\dots$, the fish numbered $n$ is in the aquarium labeled $n$. The $n$ aquariums are placed next to each other in increasing order of their labels. The $n$ aquariums form a group.

For the fish to develop well and not get bored, they need to be rearranged daily in the aquariums. Thus, on the first day, Nicușor forms two subgroups of aquariums. In the left subgroup, he places, in order, the fish from the aquariums on odd positions in the group (the first aquarium in the group, the third, the fifth, etc.). In the right subgroup, he places, in order, the fish from the aquariums on even positions in the group (the second aquarium in the group, the fourth, the sixth, etc.). On each of the following days, Nicușor applies the operation described above for each subgroup formed on the previous day. Nicușor's activity ends on the day when each group consists of no more than two aquariums.

Example. For $n = 9$, at the end of the third day, the fish are arranged in $5$ groups, according to the adjacent figure.

~[pesti.png]

# Task

Write a program that reads two non-zero natural numbers $n$ and $x$, $n$ representing the number of fish and $x$ representing the number of a fish, and determines:
* the number $z$ of days Nicușor carries out his activity;
* the label $y$ of the aquarium in which the fish numbered $x$ is at the end of Nicușor's activity;
* the first day $u$ on which the fish numbered $x$ arrived in the aquarium labeled $y$ and was not moved again.

# Input data

The input file `pesti.in` contains a single line that contains the two natural numbers $n$ and $x$, separated by a space.

# Output data

The output file `pesti.out` contains a single line that contains the three natural numbers $z$, $y$, and $u$ (in this order), separated by a space.

# Constraints and clarifications

* $3 \leq n \leq 2\ 000\ 000\ 000$;
* $1 \leq  x \leq n$.
* If a fish is not moved at all, then the answer to the third task is 1.
* Evaluation: if the first task is answered correctly, $20\%$ of the score is obtained. If the first two tasks are answered correctly, $60\%$ of the score is obtained. If all three tasks are answered correctly, $100\%$ of the score is obtained.

# Example

`pesti.in`
```
9 6
```

`pesti.out`
```
3 7 2
```

## Explanation

Nicușor carries out his activity for $z = 3$ days. The fish numbered $x = 6$ is on the third day in the aquarium numbered $y = 7$ and arrives in this aquarium on day $u = 2$. 


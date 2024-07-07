
A group of $N$ scouts, numbered from $1$ to $N$, are at a mountain camp. For them, the organizers have prepared $N$ chairs, also numbered from $1$ to $N$, arranged in a circle so that each scout has their seat (the seat of scout $i$ is chair $i$, $1 \leq i \leq N$).

For the next activity, the organizers have decided that $M$ of the scouts should present different exercises. The number $M$ is equal to the largest power of $2$ with the property that the number $N$ of scouts in the camp can be written as the sum of $M$ consecutive odd numbers. The $M$ scouts who will present are those numbered with consecutive odd numbers whose sum is $N$. For example, if $N=8$, then $M$ is $2$, and the exercises will be presented by the scouts numbered $3$ and $5$.

For fun, the little scouts sat randomly on the chairs. To carry out the activity, the organizers need at least the $M$ scouts who will present the exercises to be in their seats. For this, some of the scouts need to change places, and the organizers invite the little scouts to participate in the game called "Move". This game is played as follows: one of the scouts who is not in their seat stands up and goes inside the circle. The scout numbered with the number of the empty chair will take their place, and the place previously occupied by them remains empty. The game continues until the chair of the scout inside the circle is empty and they sit in their place.

# Task

Given the number $N$ and the order in which the scouts sat on the chairs numbered from $1$ to $N$, write a program that determines:

- the number $M$ of scouts who will present exercises during the activity;
- the identification numbers of the $M$ scouts who will present the exercises, in strictly increasing order;
- the minimum number of scouts who will change places so that all $M$ scouts who will present the exercises are in their seats.

# Input data

The input file `cercetasi.in` contains on the first line the natural number $N$ with the meaning from the statement. The second line contains $N$ distinct natural numbers from the set $\{1, 2, ..., N\}$, separated by spaces, representing the order in which the $N$ scouts sat on the chairs numbered from $1$ to $N$.

# Output data

The output file `cercetasi.out` will contain $3$ lines. The first line will contain a single natural number representing the number $M$ of scouts who will present the exercises. The second line will contain $M$ natural numbers, in strictly increasing order, separated by spaces, representing the scouts who will present the exercises. The third line will contain a natural number, representing the minimum number of scouts who will change places.

# Constraints and clarifications

* $0 \lt N \leq 10\ 000$ and $N \notin \{x \in \mathbb{N}\ \vert\ x=4k+2, k \in \mathbb{N} \}$
* A "Move" game, once started, will only end when the scout inside the circle sits in their place.
* Of the score awarded for a test, $40\%$ is awarded if the number $M$ displayed on the first line is correct, $40\%$ if the values on the second line are correct, and $20\%$ if the number on the third line is correct.

# Example 

`cercetasi.in`
```
8 
2 3 4 1 5 8 6 7
```

`cercetasi.out`
```
2
3 5
4
```

## Explanation

If $N=8$, then $M$ is $2$, and the exercises will be presented by the scouts numbered $3$ and $5$.

The scout with number $3$ is not in their place and will go inside the circle, thus the chair with number $2$ remains free. The scout with number $2$ takes their place, and the chair with number $1$ remains free. The scout with number $1$ takes their place, and the chair with number $4$ remains free. The scout with number $4$ takes their place, and the chair with number $3$ remains free, thus the scout inside the circle can sit in their place. In this "Move" game, $4$ scouts changed places. Since the scout with number $5$ is already in their place, the number of scouts who change places remains $4$.

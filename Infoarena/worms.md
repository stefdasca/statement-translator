## Task

Spiro has discovered a new species of worms. He observed that each individual worm has a certain level that determines its fighting power: if the worm has a base power $p$ and a level $n$, then its fighting power is $p^n$. Initially, Spiro has a group of $Nr$ worms with levels between $0$ and $7$. These worms will be given in the input file as an array with $8$ elements, where $(0 \leq i \leq 7)$, represents the number of worms of level $i$ (it is guaranteed that the). Spiro wants to distribute his collection in a worm farm. Thus, he has available a network of $N$ rooms numbered from $1$ to $N$, connected by $M$ tunnels. Tunnels do not overlap and cannot traverse each other because the worm farm is very thin and there would be no space for that to happen. In other words, if there are $2$ tunnels that intersect, there is definitely a room at that point. Then, in the next $Q$ days, Spiro performs one of the following operations:

$1 \ n$ $\to$ Spiro, using his exceptional biological skills, obtains another worm of level $2 * n$ $(0 \leq n \leq 3)$ and adds it to the current group.  
$2 \ x$ $\to$ because Spiro really likes the group he currently has, he makes a copy of the group using very questionable methods of an extraordinary biologist, and places it in the room with index $x$.

When a new group is placed in a room, the worms that form this group will mate with any worm already present in that room. Thus, after a group is placed, the room will contain the worms that were already there, the worms from the placed group, and additional $nr1 * nr2$ worms resulted from the mating of each worm that was already in the room with each worm from the placed group $(nr1 = number of worms that were already in the room and nr2 = number of worms from the placed group)$. When a worm of level $n1$ mates with a worm of level $n2$, the resulting worm will have the level $n = n1 + n2$.

Initially, all rooms contain no worms. Moreover, since Spiro is an extraordinary biologist, he can create any type of food $h$ so that a worm eating that type of food will have the base power $h \ (h$ is a real number). The fighting power of the worms in a room is the sum of the fighting powers of each worm in that room. Since worms are very combative, if a room $x$ has greater fighting power than an adjacent room $y$, then the worms in room $x$ will invade the worms in room $y$ and kill them. This is impossible, since besides being an extraordinary biologist, Spiro is also a pacifist and would like his farm to remain intact. Thus, he must choose for each room what type of food to place there so that the fighting powers of any two adjacent rooms are equal. However, Spiro has a younger brother, Piro, who doesn't know much about worms and powers, but still knows how to differentiate between worms and would like, for the farm to look nice, that the worms in any two adjacent rooms look different. Since the appearance of worms is directly related to their food, Spiro must choose the food for each room so that two adjacent rooms have different assigned food.

Help Spiro and tell him what food to place in each room such that the fighting power of any two adjacent rooms is the same and the assigned food is different.

## Input data

The input file `worms.in` contains on the first line $8$ numbers representing the array. The next line contains two numbers $N$ and $M$. The following $M$ lines each contain two numbers $x$ and $y$ representing a tunnel between rooms $x$ and $y$. The next line contains $Q$. The following $Q$ lines each contain an operation as described above.

## Output data

The output file `worms.out` must contain $N$ real numbers on separate lines, the $i$-th number representing the type of food placed in room $i$.

## Constraints

$1 \leq N \leq 10000$  
$1 \leq M \leq 30000$  
The number of worms of level $n$ in the group after $Q$ operations $\leq 10$, where $0 \leq n \leq 7$  
The number of copies placed in room $i \leq 12$, where $1 \leq i \leq N$  
The fighting power in room $i$ must be $\leq 10^9$ in magnitude, where $1 \leq i \leq N$  
Two numbers $a$ and $b$ are equal if $abs(a - b) < 10^{-9}$

## Example

`worms.in`
```
0 0 0 0 0 0 0 1
2 1
1 2
3
2 1
1 3
2 2
```

`worms.out`
```
1.0000000000
0.8986537126
```
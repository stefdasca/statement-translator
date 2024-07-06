Dorel, bored with the puzzle he upgraded yesterday, decided to go outside with the other kids. He watches the $N$ kids playing "broken telephone". The game proceeds as follows:
- Initially, the kids line up on the Ox axis, with child $i$ at a distance of $X_i$ meters from the origin.
- The nearest child to the origin chooses a secret word and passes it to the child to his right, who then passes it on to the next one, and so on until it reaches the last child.

To transmit the word, each child must walk to the child to their right. All the children move at a constant speed of $1$ meter/second.

However, to avoid moving, each child has a *walkie-talkie* device that allows them to pass the word ahead. All *walkie-talkie* stations have a range $R$, set at the start of a game round (expressed in meters) and cannot be changed during the game. The stations are connected to the same power source which has $B$ energy units.

Depending on the set range, the children can use the *walkie-talkie* system instead of walking. More precisely, if a child needs to cover a distance less than or equal to $R$ to pass the word to the right and the battery has at least $R$ units of energy left, they can use the *walkie-talkie* to instantly pass the secret word, reducing the battery by $R$ units. However, even with the *walkie-talkie* system, a child can only pass the message to the first child to their right.

The children want the game to end as quickly as possible, so they will set a convenient range and choose to use or not use the *walkie-talkie* system to minimize the time taken for all $N$ children to know the secret word.

Dorel wants to join the game, so in the second part of the game, he will join the line. Dorel will position himself on the Ox axis, somewhere between the first and last child, at a certain distance from the origin where no other child is located.

# Task
Write a program to solve the following tasks:
1. What is the minimum duration of the game if Dorel does not take part in the game?
2. What is the minimum duration of the game if Dorel takes part in the game and positions himself optimally to minimize the game's duration?

# Input data

The input file `telefon.in` contains on the first line two natural numbers $N$ and $B$ with the meanings described above. The second line contains $N$ non-zero distinct natural numbers $X_i$, in strictly increasing order, where $X_i$ represents the distance of child $i$ from the origin, $1 \\leq i \\leq N$.

# Output data

The output file `telefon.out` will contain two natural numbers $C_1$ and $C_2$, separated by a space, where $C_1$ represents the answer to task $1$ and $C_2$ represents the answer to task $2$.

# Constraints and clarifications

* $2 \\leq N \\leq 10^5$
* $1 \\leq B, X_i \\leq 10^9$
* It is guaranteed that Dorel has at least one free position to locate himself.
* A child can choose between walking or using the *walkie-talkie* to pass a message.
* Children can set a new range for the *walkie-talkie* when Dorel joins the game.
* For tests worth 15 points, $N, B \\leq 10^2$.
* For other tests worth 35 points, $N \\leq 10^3, B \\leq 10^4$.
* For other tests worth 20 points, $N \\leq 10^5, B \\leq 10^5$.
* For other tests worth 30 points, $N \\leq 10^5, B \\leq 10^9$.
* For the first task, 40 points are awarded.
* For the second task, 60 points are awarded.
* **Regardless of the task you want to solve, the output file must follow the mentioned rules!**

# Example

`telefon.in`
```
6 15
7 9 12 16 21 27
```

`telefon.out`
```
8 6
```

## Explanation

$N = 6$, $B = 15$, and $X = [7, 9, 12, 16, 21, 27]$

~[poza.png]

1. If Dorel **does not** participate in the game, the children will choose a range $R=5$ and the 2nd, 3rd, and 4th child will use the communication system. Consequently, the game duration will be $(9-7) + (27-21) = 2 + 6 = 8$
2. If Dorel participates in the game, he will position himself at a distance of $26$ from the origin. In this situation, the children will choose a range $R = 5$ and the 3rd, 4th, and 5th child will use the communication system. Consequently, the game duration will be $(9-7) + (12-9) + (27-26) = 2 + 3 + 1 = 6$
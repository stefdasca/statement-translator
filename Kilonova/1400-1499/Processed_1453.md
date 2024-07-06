~[img1.jpg|align=right|width=auto] An archaeologist found an interesting chest. After carefully opening it, they were surprised to find that it contained gold coins. Looking more closely, they found something else: a hidden parchment in a secret compartment of the chest, with a text written in an ancient language that the archaeologist fortunately knew. The text revealed that a group of very wealthy merchants wanted to secretly hide the treasure of their guild, made up of gold coins, as a terrible war was foretold. The merchants knew there was a chance this treasure would be found and confiscated by enemies, so they consulted on the best way to proceed, on how to hide the treasure. The archaeologist was able to deduce from the text the following:
a) The $N$ coins, which formed the guild's treasure, were divided into a maximum of three types of piles, consisting of $p1$, $p2$ and $p3$ coins, $p1$, $p2$ and $p3$ being **consecutive prime numbers**, $p1<p2<p3$. Each pile was placed entirely in one chest.
b) It is possible that there are 0 (zero) piles consisting of $p1$ or $p2$ or $p3$ coins, the goal being to achieve a division in which the **number of undeclared coins is minimal**, and if there are multiple possibilities, the option with **the greater number of piles is chosen.** If there are multiple such solutions, any of them is considered correct.
c) Coins that could not be distributed according to the established rules were donated to the church.

# Task
Write a program that determines the maximum number $S$ of chests and the number of chests with $p1$, $p2$ and $p3$ coins, as well as the sum donated to the church.

# Input data

The `sipet.in` file contains, on the first line, the natural number $T$, and on the following $T$ lines, two natural numbers $N$ and $p1$ separated by a single space.

# Output data

The `sipet.out` file will contain on the first $T$ lines five natural numbers, separated by a space: $S$, $x$, $y$, $z$ and $r$, representing the maximum number $S$ of chests, the number $x$ of chests with $p1$ coins, the number $y$ of chests with $p2$ coins, respectively the number $z$ of chests with $p3$ coins, and the number $r$ of coins donated to the church, corresponding to the input data on line $T+1$ of the `sipet.in` file. If there are multiple correct solutions, any of them is accepted.

# Constraints and clarifications

* $1 \leq N \leq 10\ 000\ 000$
* $2 \leq p1 < p2 < p3 \leq N$
* $1 \leq T \leq 10$ - The input file will contain at most 10 pairs of numbers $N\ p1$

# Example

`sipet.in`
```
3
15 5
10 3
41 11
```

`sipet.out`
```
3 3 0 0 0
2 1 0 1 0
3 1 1 1 0
```

## Explanation

* The maximum number of chests is $3$, all with $3$ coins;
* or: `2 0 2 0 0` $(1 \cdot 3 + 1 \cdot 7 = 2 \cdot 5 = 10)$; (both solutions are correct!)
* The maximum number of chests is $3$; $1$ chest with $11$, one with $13$ and one with $17$ coins.
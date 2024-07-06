Sure, here is the translated text:

---

Some children, who are big fans of sequences, wished for the latest generation sequence sir5 for Christmas. Santa Claus, employed by DHL, is the one who will deliver them, but he mixed them up with other gifts from the sack ([sir5](https://infoarena.ro/problema/sir5), but also the sir4 pro system), addressed to children who were not so well-behaved.

The old man has $T$ requests, and for each request, the expected sir5 model for the child, $A$, and what Santa sees in the sleigh, $B$, are known. Both $A$ and $B$ are arrays of natural numbers. Recently, his glasses have been playing tricks on him and he can no longer rely on a simple equality between the two arrays, but he has to go through the following laborious process:
* Choose a natural number $K$ and a natural number $R < 2^K$.
* For all the numbers in the subarray $B$ that give the remainder $R$ when divided by $2^K$, he toggles the $K + 1$ bit (from value $0$ to $1$ and vice versa).
* If by miracle he obtains a permutation of array $A$, then the holidays for the concerned child are saved, and Santa moves on; otherwise, he can repeat the process.

As you might expect, he has been stuck on this for a while and begs you to tell him, for each request, as quickly as possible, if he can save Christmas.

If that was not enough, the old man warns you that he does not have a good memory and suggests that you check it before solving the problem.

# Input data
The first line of the input file contains the number of requests $T$. Each request is then described as follows: the first line contains an integer $N$, representing the length of the arrays, the second line contains $N$ natural numbers representing the array $A$, and the third line contains $N$ natural numbers representing the array $B$.

# Output data
For each request, print `YES` if Santa Claus can save the holidays and `NO` if not.

# Constraints
* $1 \leq T \leq 10$
* $1 \leq N \leq 2 \cdot 10^5$
* $1 \leq A_i, B_i \leq 2^{30} - 1$

## Subtask 1 (15 points)
* $N \leq 4$
* $A_i, B_i \leq 15$

## Subtask 2 (29 points)
* $N \leq 500$
* $A_i, B_i \leq 511$

## Subtask 3 (36 points)
* $N \leq 10^5$
* $A_i, B_i \leq 2^{17} - 1$

## Subtask 4 (20 points)
* Without additional constraints.

# Example
`stdin`
```
2
3
1 6 12
5 0 15
4
2 7 7 8
1 2 8 15
```
`stdout`
```
YES
NO
```
Explanations
---
In the first request, the following operations can be performed:
* $K = 0, R = 0$, $B$ becomes $[4, 1, 14]$.
* $K = 1, R = 0$, $B$ becomes $[6, 1, 12]$, which is a permutation of $A$.

---
~[amoeba.png|align=right]

Tired of evolutionary theories, quantum physics laws, and the multiplication table, the amoeba brothers (three in number: Boss, Weak, and Tiny) decided to play a classic card game: War in Three.

The rules of the game are simple: each of the $3$ players has $N$ cards numbered with values from $1$ to $3 \times N$. All $3 \times N$ cards are distinct, and the game consists of $N$ rounds. In one round, each player chooses one card to play. The card with the highest value brings $A$ points to the winner, while the second-highest card brings $B$ points (it is guaranteed that $A \geq B$).

Annoyed by the arrogant attitude of their older brother, Weak and Tiny decided to team up. Their only goal in this game is to minimize their brother's (Boss's) score, so it doesn't matter how much they each get independently. Unfortunately, they don't really know how to read the numbers written on their cards. Thus, their only strategy is to play the first card from their hand and pray to the god Amibus to win.

Knowing each player's cards, as well as the order in which the brother Boss plays his hands, your goal is to select an order for the other $2$ brothers such that you minimize the score of the first brother. If you succeed, the god Amibus will reward you with 100 points.

# Input data
The input file `amiba.in` will contain on the first line a natural number $T$ (the number of tests), followed by $T$ tests. Each test will be described by $4$ lines:
* The first line will contain $3$ natural numbers: $N$, $A$, and $B$ with their meanings from the statement.
* The second line will contain $N$ distinct natural numbers from the interval $[1, 3 \times N]$ representing the cards of the first player (Boss). He will play the cards exactly in the given order.
* The third line will contain $N$ distinct natural numbers from the interval $[1, 3 \times N]$ representing the cards of the second player (Weak).
* The fourth line will contain $N$ distinct natural numbers from the interval $[1, 3 \times N]$ representing the cards of the third player (Tiny).

# Output data
The output file `amiba.out` will contain the answers for each of the $T$ tests, represented by $2$ lines:
* The first line will contain $N$ natural numbers representing the cards of the second player (Weak) in the order he will play them.
* The second line will contain $N$ natural numbers representing the cards of the third player (Tiny) in the order he will play them.

If there are multiple solutions that minimize the score of the first player (Boss), you can display any of them.

# Constraints and clarifications
* $T \leq 500$.
* The sum of the values of $N \leq 1\ 001\ 000$.
* $A, B$ are natural numbers with $0 \leq B \leq A \leq 1\ 000\ 000\ 000$.
* Tests worth $15$ points will only have $A=1$ and $B=0$.
* Tests worth $15$ points will only have $A=1$ and $B=1$.
* Tests worth $40$ points will have $T \leq 100$, the sum of the values of $N \leq 10\ 000$ and $N \leq 1\ 000$.
* Tests worth $60$ points will contain the sum of the values of $N \leq 101\ 000$.

# Example
`amiba.in`
```
2
6 10 8
1 10 17 14 7 11
8 2 15 12 4 16
13 5 6 3 9 18
6 10 4
1 10 17 14 7 11
8 2 15 12 4 16
13 5 6 3 9 18
```

`amiba.out`
```
4 12 2 16 8 15
6 5 3 18 9 13
4 12 2 16 8 15
6 13 18 3 9 5
```

Explanations
---
$T=2$, we have two tests.
The first two lines in the output file represent the answer for the first test, and the next two lines represent the answer for the second test.
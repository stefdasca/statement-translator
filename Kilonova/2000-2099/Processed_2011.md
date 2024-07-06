Albina Livia wants to open a flower hotel for other bees. The hotel will consist of $N$ flowers arranged in a line, each flower representing a room for a bee. While preparing for the hotel opening, Albina Livia decided it would be a good idea to organize a test weekend where she'd invite her friends to spend a night in some of the hotel rooms.

Albina Livia has $K$ flower colors available to design the hotel. The problem is that she hasn't decided yet on the best floral design and how to distribute her bee friends in the rooms. The only information she has is that her friends are very competitive, so if two of them have the same flower color and can see each other (no other bee is lodged between them), the two will start debating about which one looks better in that color and will go home dissatisfied. Therefore, she wants to avoid this situation at all costs.

To solve her dilemma, Albina Livia decided to draw on a sheet of paper all the ways in which she can choose the flower colors and distribute her friends in the rooms. However, being a very practical and busy bee, she asks you to help her calculate how many such ways there are. Note that Albina Livia has a variable number of friends, so you will need to consider all possibilities.

# Task

Given $N$ and $K$, the number of rooms and the number of flower colors Albina has at her disposal, find the number of possible ways modulo $1 \ 000 \ 000 \ 007$.

# Input data

The first line contains two natural numbers, $N$ and $K$, separated by a space.
# Output data

Print a single natural number, representing the result modulo $1 \ 000 \ 000 \ 007$.

# Constraints and clarifications

* $1 \leq N \leq 1 \ 000 \ 000$
* $1 \leq K \leq 1 \ 000 \ 000 \ 000$

| # | Points | Constraints |
| - | ------- | ---------- |
| 1 | 13 | $1 \leq N, K \leq 7$ |
| 2 | 21 | $1 \leq N, K \leq 400$ |
| 3 | 28 | $1 \leq N, K \leq 1 \ 000$ |
| 4 | 38 | No additional constraints |

# Example

`stdin`
```
2 2
```

`stdout`
```
14
```

## Explanation

~[albine.png]
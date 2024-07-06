> — Ionele, why do you waste your life with computer games!
> — It's alright, Mom, I still have three lives left!

In the Great Battle to save all the good in the world, $H$ heroes fight against a gang of $M$ monsters. The fighters stand in a circle in a certain order. After the $i$-th hero in the circle, there are $m_i$ monsters (respectively $m_1 + m_2 + \dots + m_H = M$).

Starting with the first hero, each fighter attacks with their sword. A hero can hit any monster, and a monster can hit any hero. If a monster gets hit $K$ times, it dies. The heroes are invincible.

# Task

The heroes fight for glory and want to be hit as little as possible. What is the minimum number of hits the heroes will receive until they defeat all the monsters?

# Input data

The first input line contains the numbers $H$ and $K$, separated by space.

The second line contains $H$ numbers separated by space, $m_1$, $m_2$, ..., $m_H$.

# Output data

The first line will contain a single value representing the minimum number of hits the heroes will receive.

# Constraints and clarifications

* $1 \leq H \leq 3 \ 000$
* $1 \leq M \leq 1 \ 000 \ 000 \ 000$
* $1 \leq K \leq 1 \ 000$
* $0 \leq m_i \leq M$ for $1 \leq i \leq H$
* It is guaranteed that the answer will not exceed $10^{18}$. 

| # | Points | Constraints          |
| - | ------- | ------------------- |
| 0 | 0      | Examples             |
| 1 | 7      | $H \leq 10$, $M \leq 4$, $K \leq 4$|
| 2 | 11     | $H \leq 20$, $M \leq 10$, $K \leq 30$|
| 3 | 15     | $M \leq 150 \ 000$    |
| 4 | 17     | $M \leq 5 \ 000 \ 000$   |
| 5 | 19     | $M \leq 30 \ 000 \ 000$    |
| 6 | 31     | No additional constraints    |

# Example 1

`stdin`
```
3 1
0 3 3
```

`stdout`
```
3
```

## Explanation

There are $H=3$ heroes and $M=6$ monsters, each with $K=1$ life points. The initial order is `HHMMMHMMM` (where `H` is a hero and `M` is a monster). The first two heroes kill the first two monsters. The third monster attacks. The third hero kills the fourth monster. The last two monsters attack. The circle now is `HHMHMM`. In the second round, each hero hits a monster and no hero gets hit.

# Example 2

`stdin`
```
3 2
0 3 3
```

`stdout`
```
10
```
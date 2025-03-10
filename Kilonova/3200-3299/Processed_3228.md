
# Task

Because they were bored one day, Ross and Rachel were sitting at the Central Perk café playing a card game called *XOR Cards*. *XOR Cards* is played with a deck of $2^N$ cards, on which natural numbers from $0$ to $2^N-1$ are written. In turns, Ross and Rachel each take a card from the deck, which they can choose as they wish, and place it in front of them, face up. Ross always takes the first card. In the end, one of them is considered to be in a *winning position* if they have a card $K$ in front of them on which is written the XOR of all $2^{N-1}$ cards that they have in front of them, including $K$.

If exactly one of them is in a *winning position*, they win the game. Otherwise, it's a draw. To make the game more interesting, Ross's first card is chosen by the committee. Considering that both players play optimally, we want to know the winner of the game. 

# Input data

The first line contains $T$, the number of scenarios to analyze. The next $T$ lines contain pairs of the form $N$, $C$, indicating the size of the deck in the $i$-th scenario and the card chosen by the committee for Ross in that scenario.

# Output data

The output file will have $T$ lines. On the $i$-th line, print the result of the $i$-th scenario: `Victory` if Ross would win, `Defeat` if Rachel would win, and `Draw` otherwise.

# Constraints and clarifications

* $1 \leq T \leq 200\, 000$;
* $2 \leq N \leq 24$;
* $0 \leq C \leq 2^N-1$;
* For tests worth $10$ points, $T \leq 10$ and $N \leq 4$ for each scenario;
* For other tests worth $30$ points, $T \leq 1\, 000$;
* For other tests worth the remaining $60$ points, there are no additional restrictions;
* By optimal play, we mean if one of the players can force a victory, they will force it; if not, but they can still force a draw, they will force the draw.

# Example

`stdin`
```
1
2 3
```

`stdout`
```
Defeat
```

## Explanation

Rachel's first move will be to take the card $0$. Then, whether she remains with card $1$ or $2$ in addition, the XOR of her cards will be $0 \oplus 1 = 1$ or $0 \oplus 2 = 2$. In both cases, Rachel is in a winning position, and Ross will have $3$ and $2$ ($3 \oplus 2 = 1$) or $3$ and $1$ ($3 \oplus 1 = 2$), and he is not in a winning position in either case, so Rachel wins.

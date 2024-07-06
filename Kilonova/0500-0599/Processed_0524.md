# Pitmutare

Pitmutare is a card game for two players, each having a full deck of `N` cards numbered from `1` to `N`. The two players shuffle their decks and one by one place a card on the table. The player with the higher card wins a point. In case of a tie, no one gets the point. The game ends when the two decks are exhausted.

For certain positions from `1` to `N`, the card of the first player is known, and for the remaining positions, the card of the second player is known.

# Task

Given the number `N` of cards, a value `S`, and the known cards for the two players, determine for how many configurations of the unknown cards the first player will get exactly `S` points.

# Input data

The file `pitmutare.in` contains:
- The first line contains the numbers `N` and `S` separated by a space.
- The second line contains, in order, the cards of the first player. This line contains `N` values between `0` and `N`. The values of `0` are at the positions of the unknown cards, the other numbers represent the known cards.
- The third line contains, in the same manner, the cards of the second player.

# Output data

The file `pitmutare.out` must contain a single number representing the answer to the task modulo $10^9 + 7$.

# Constraints and clarifications

* `0 \leq S < N \leq 300`
* For tests worth `10` points `N \leq 8`
* For tests worth `20` points `N \leq 18`
* For tests worth `40` points `N \leq 30`
* For tests worth `60` points `N \leq 80`
* For tests worth `20` points, the known values for the two players are distinct

# Example

`pitmutare.in`
```
4 2
4 2 0 0
0 0 4 2
```
`pitmutare.out`
```
2
```

Explanations
---
The configurations in which the first player wins `2` points are:

```
4 2 1 3
1 3 4 2
```

```
4 2 3 1
3 1 4 2
```


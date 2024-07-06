~[lupusor.png]

Mielu from the kitchen is about to leave permanently from the company where he works. Comrade Lupusor from Personnel offers him one last chance: to beat him in a card game. Mielu accepts and Lupusor presents the rules of the game as follows. On the table, there are `N` playing cards numbered from `1` to `N`. Each card `i`, where `1 \leq i \leq N`, has two positive integers $a_i$ and $b_i$ written on it. All numbers written on the cards are distinct pairwise. In the first move of the game, Mielu chooses some of the cards and removes them from the game. He can choose not to remove any card, but removing all the cards is not allowed. In the second move, Lupusor chooses two cards from those remaining in the game, with initial indices `i` and `j`. Lupusor is allowed to choose the same card twice (i.e., `i = j`). If $a_i > b_j$ then Lupusor wins the game, otherwise, Mielu wins. Lupusor is particularly cunning, so he will always choose the values `i` and `j` on the second move such that he wins if possible.

# Task
Mielu is now in a tight spot: to keep his position, he will need to answer two tough questions given `N` and the values $a_1, ... , a_N$ and $b_1, ... , b_N$:
1. What is the minimum number of cards Mielu can remove on the first move so that Lupusor loses the game? If this is not possible, then the answer is $-1$.
2. In how many ways can Mielu remove cards on the first move so that Lupusor loses the game? The answer is required modulo $10^9 + 7$. 
$\underline{\text{Note, in this case, it is not necessary to remove a minimum number of cards!}}$

A number `C ∈ {1, 2}` is given. If `C = 1` then Mielu will only have to answer question `1`, otherwise only question `2`.

**Even more seriously!** `M` times the comrade director comes and changes the values written on one of the `N` cards. Specifically, at the `i`-th modification, for `1 \leq i \leq M`, the director changes the values $a_{id_i}$ and $b_{id_i}$ written on the card $id_i$ to $c_i$ and, respectively, $d_i$. After each modification, Mielu will have to answer again the question indicated by the number `C`. It is guaranteed that after each modification the values written on the cards remain pairwise distinct.

# Input data
The first line of the input file `lupusor.in` contains `C`. The second line contains `N`. The third line contains the numbers $a_1, ... , a_N$, separated by spaces. The fourth line contains the numbers $b_1, ... , b_N$, separated by spaces. The fifth line contains `M`. The next `M` lines describe the modifications ordered by the director: line `i` contains positive integers $id_i, c_i, d_i$, separated by spaces, where `1 \leq i \leq M`.

# Output data
In the output file `lupusor.out`, there will be `M + 1` lines. Each line will contain a single integer, representing the answer to the first, or respectively, the second task, depending on the value of `C`. The first line will represent the answer before the modifications, the second line the answer after the first modification, and so on, line `i` will represent the answer after the first `i - 1` modifications.

# Constraints and clarifications
* `1 \leq N \leq 100 000`
* `0 \leq M \leq 100 000`
* $1 \leq a_i, b_i \leq 2N + 2M$, for any `1 \leq i \leq N`.
* $1 \leq c_i, d_i \leq 2N + 2M$, for any `1 \leq i \leq M`.
* $1 \leq id_i \leq N$, for any `1 \leq i \leq M`.
* Each number `1 \leq k \leq 2N + 2M` appears exactly in one of the arrays `a, b, c`, or `d`.

## Subtask 1 (5 points)
* `C = 1` and `N, M \leq 10`
## Subtask 2 (6 points)
* `C = 1` and `N, M \leq 100`
## Subtask 3 (6 points)
* `C = 1` and `N, M \leq 400`
## Subtask 4 (10 points)
* `C = 1` and `N, M \leq 2 000`
## Subtask 5 (15 points)
* `C = 1` and `N, M \leq 50 000`
## Subtask 6 (7 points)
* `C = 1`
## Subtask 7 (5 points)
* `C = 2` and `N, M \leq 10`
## Subtask 8 (7 points)
* `C = 2` and `N, M \leq 100`
## Subtask 9 (7 points)
* `C = 2` and `N, M \leq 400`
## Subtask 10 (13 points)
* `C = 2` and `N, M \leq 2 000`
## Subtask 11 (13 points)
* `C = 2` and `N, M \leq 50 000`
## Subtask 12 (6 points)
* `C = 2`

# Examples

`lupusor.in`

```
1
3
1 7 6
5 10 8
2
2 9 3
3 2 4
```

`lupusor.out`

```
1
2
1
```

`lupusor.in`

```
2
3
1 7 6
5 10 8
2
2 9 3
3 2 4
```

`lupusor.out`

```
4
2
3
```

`lupusor.in`

```
1
1
1
2
1
1 4 3
```

`lupusor.out`

```
0
-1
```

`lupusor.in`

```
2
1
1
2
1
1 4 3
```

`lupusor.out`

```
1
0
```

Explanations
---

In the first example, card `1` initially has the numbers $a_1 = 1$ and $b_1 = 5$ written on it, which we will write simply as `(1, 5)`, card `2` has the numbers `(7, 10)`, and card `3` has the numbers `(6, 8)`. We have `C = 1`, so only question `1` is answered. Noting that if Mielu does not remove any card, then Lupusor would win by choosing `i = 2` and `j = 1` because $a_2 = 7 > 5 = b_1$. However, if Mielu chooses to remove card `1`, then only cards `2` and `3` remain in the game, with values `(7, 10)` and `(6, 8)`. In this case, Lupusor cannot choose `i` and `j` among the remaining cards such that $a_i > b_j$, so Mielu wins.

After the first modification, card `1` has the numbers `(1, 5)`, card `2` the numbers `(9, 3)`, and card `3` the numbers `(6, 8)`. This time, it is necessary to remove two cards: either cards `1` and `2` or cards `2` and `3`.

After the second modification, card `1` has the numbers `(1, 5)`, card `2` the numbers `(9, 3)`, and card `3` the numbers `(2, 4)`. This time, it is sufficient to remove only card `2`.

The second example is identical to the first, except that question `2` is answered (because `C = 2`). Before modifications, there are `4` ways to remove a part of the cards so that Mielu wins:
1. Remove only card `1`;
2. Remove cards `1` and `2`;
3. Remove cards `2` and `3`;
4. Remove cards `1` and `3`.

Noting that removing all cards is forbidden by the game rules.

After the first modification, there are `2` ways to remove a part of the cards so that Mielu wins:
1. Remove cards `1` and `2`;
2. Remove cards `2` and `3`.

After the second modification, there are `3` ways to remove a part of the cards so that Mielu wins:
1. Remove only card `2`;
2. Remove cards `1` and `2`;
3. Remove cards `2` and `3`.

Noting that only the first of these `3` ways removes a minimum number of cards, but we are interested in the total number of ways, regardless of whether they remove a minimum number of cards or not.
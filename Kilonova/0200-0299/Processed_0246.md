# Tennis Ball Purchase Problem

Little MP loves watching tennis tournaments with his family and friends. He has recently watched the *Australian Open 2022 Finals* on TV and noticed that each tennis ball used by the players must have an integer weight from `0` to `w - 1`, inclusive. Moreover, there may be several different models of balls with each weight. For weight `i`, there exist $v_i$ different models with this weight. We use the convention that if $v_i = 0$, then no ball with weight `i` was used in the tennis tournament. *We consider that any two balls with the same weight and model are identical*.

Little MP goes to InfO(1)Sports, one of his favorite sports shops in his hometown, and enthusiastically finds out that there is an infinite supply for every single tennis ball model he saw on TV last month. In other words, for each weight `i`, there are infinitely many balls for each of the $v_i$ models with that weight.

Little MP wants to buy `n` tennis balls, but he has a constraint on this purchase. Suppose he buys the balls with weights $w_1, ..., w_n$ and models $m_1, ..., m_n$, respectively. He then requires that:

$$(w_1 + ... + w_n) \mod w \leq x.$$

Furthermore, the sports shop has a very strange way of determining the prices of the balls. The price of the sequence of the `n` balls mentioned above is given by $count^k$, where `count` is the number of balls from the sequence with weight *at most* `y`.

Little MP is now curious about something: if we consider all the possible sequences of `n` balls that satisfy Little MP’s requirements, what is the sum of their costs? (A sequence may contain multiple identical balls; the order ***matters*** within such a sequence. For example, if `(w, m)` denotes a ball with weight `w` and model `m`, then the sequence `(1, 2), (2, 1)` is different from the sequence `(2, 1), (1, 2)`. Thus, two sequences are considered identical if and only if they contain identical balls in all positions.)

# Task
The first line of the input contains the integers `n, w, k, x`, and `y`. The second line of the input contains the integers $v_0, v_1, ..., v_{w-1}$, representing the number of different models of tennis balls with each weight, as described above.

# Input Data
The first line of the input contains the integers `n, w, k, x`, and `y`. The second line of the input contains the integers $v_0, v_1, ..., v_{w - 1}$, representing the number of different models of tennis balls with each weight.

# Output Data
The only line of the output must contain just one number: the sum of the costs of all the possible sequences of `n` balls that satisfy Little MP’s requirements modulo $10^9 + 7$.

# Constraints and Clarifications
* $1 \leq n \leq 10^9$
* `1 \leq w \leq 700`
* $0 \leq v_0, v_1, ..., v_{w - 1} \leq 10^9$
* `1 \leq k \leq 2`
* `0 \leq x, y < w`

## Subtask 1 (7 points)
* $n \leq 10^6$
* `x = w - 1`
* `y = w - 1`

## Subtask 2 (2 points)
* `x = w - 1`
* `y = w - 1`

## Subtask 3 (10 points)
* $v_0 = v_1 = ... = v_{w - 1} = 0$

## Subtask 4 (15 points)
* `n \leq 50`
* `w \leq 50`

## Subtask 5 (4 points)
* `n \leq 2500`
* `w \leq 50`
* `y = w - 1`

## Subtask 6 (5 points)
* `y = w - 1`
* $v_0 = v_1 = ... = v_{w - 1}$

## Subtask 7 (11 points)
* `n \leq 2500`
* `w \leq 50`
* `k = 1`

## Subtask 8 (7 points)
* `w \leq 50`
* `k = 1`

## Subtask 9 (12 points)
* `n \leq 2500`
* `w \leq 50`
* `k = 2`

## Subtask 10 (7 points)
* `w \leq 50`
* `k = 2`

## Subtask 11 (9 points)
* `k = 1`

## Subtask 12 (11 points)
* `k = 2`

# Examples

`stdin`
```
7 3 2 1 1
0 0 0
```

`stdout`
```
0
```

`stdin`
```
1000000 4 1 2 1
0 0 0 0
```

`stdout`
```
0
```

`stdin`
```
1 2 1 1 1
2 2
```

`stdout`
```
4
```

`stdin`
```
1 2 2 1 1
2 2
```

`stdout`
```
4
```

`stdin`
```
2 2 1 1 1
2 2
```

`stdout`
```
32
```

`stdin`
```
1 3 1 1 1
1 1 1
```

`stdout`
```
2
```

`stdin`
```
3 2 1 1 1
25 37
```

`stdout`
```
714984
```

`stdin`
```
6 5 2 3 2
1 2 6 70 1
```

`stdout`
```
227678571
```

`stdin`
```
6 5 1 2 3
1 6 70 1 4
```

`stdout`
```
398503624
```

`stdin`
```
500 4 1 2 3
10 20 30 40
```

`stdout`
```
651382141
```

# Explanation

We denote a ball with weight `w` and model `m` with `(w, m)`.

In the first two examples, there are no balls at all. Thus, there are no sequences of balls that can be bought, and the sum of their costs is `0`.

In the third and fourth examples, the balls are `(0, 1),(0, 2),(1, 1),(1, 2)`. Little MP could buy `(0, 1)`, or `(0, 2)`, or `(1, 1)`, or `(1, 2)`. Each of these sequences has a cost equal to `1` in both examples (since $1^1 = 1^2 = 1$). Thus, the total cost is `4`.

In the fifth example, we have the same possible balls, and Little MP can buy any pair of balls. Thus, Little MP can buy `4 × 4 = 16` sequences of balls. The cost of a pair of balls is the number of balls whose weight is at most `1` (i.e. all `n = 2` of them) to the power of `k = 1`, so the cost is `2`. Therefore, the sum of costs is `32`.

In the next example, there are three possible balls, `(0, 1),(1, 1),(2, 1)`. Little MP can buy one ball whose weight is at most `1` modulo `3`, so he can buy either `(0, 1)` or `(1, 1)`. Both of these sequences have a cost of `1`, so the total cost is `2`.
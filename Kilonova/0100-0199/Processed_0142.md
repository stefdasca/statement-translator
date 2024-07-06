**Task**

Known for many important things, such as the city's subway and the Nespus festival, the city of Jluc also hosts another tourist attraction, albeit less known than the previously mentioned ones – *Piezișă*.

At first glance, Piezișă is just a street, with several shops along it. More precisely, it has `n` shops positioned along it, numbered from `0` to `n - 1`. However, Piezișă is more than it seems: it is a place where memories are made. Shop `i` has an associated number $v_i$, which represents the quality of the memories made in that shop.

Hearing about this street, Alex wants to visit a continuous interval of shops this evening. He has `q` plans for such intervals, the `i`-th being in the form $[l_i, r_i]$. To save time, he wants to travel along Piezișă with his new *electric scooter*. However, Alex is superstitious, and he is convinced that if the `xor` sum of the values $v_i$ from a visited interval is not `0`, it will bring him bad luck. Therefore, for each plan, he wants to find the length of the minimum-length interval that contains the shops from the plan, and has the `xor` sum `0`.

Formally, given an array of `n` integer values, and `q` intervals of the form $[l_i, r_i]$, you need to calculate, for each such interval, the length of the minimum-length interval `[x, y]`, with the property that $x \leq l_i \leq r_i \leq y$ and for which $v_x \; xor \; v_{x+1} \; xor \; ... \; xor \; v_y = 0$.

## Input data

The first line contains a single natural number, representing the value of `n`. The second line contains `n` integers, representing the values $v_0, v_1, ..., v_{n-1}$. The third line contains a single natural number, representing the value of `q`. The following `q` lines contain the corresponding plan values. Line `i + 3` contains `2` integers, representing $l_i$ and $r_i$.

## Output data

Print `q` lines. On line `i`, print the answer to the `i`-th plan.

## Constraints and clarifications

* The `xor` operation represents the exclusive or operation on bits. In C/C++, this operator is `^`.
* If, for a plan, there is no segment with the `xor` sum equal to `0`, the answer is `-1`.
* $1 \leq n \leq 500000$
* $1 \leq q \leq 500000$
* $0 \leq v_i < 2^{30}$, for any $0 \leq i < n$
* $0 \leq l_i \leq r_i < n$, for any $0 \leq i < q$

### Subtask 1 (10 points)

* $1 \leq n, q \leq 500$

### Subtask 2 (15 points)

* $1 \leq n, q \leq 3000$

### Subtask 3 (5 points)

* $v_i < 4$, for any `0 \leq i < n`

### Subtask 4 (40 points)

* $1 \leq n \leq 100000$

### Subtask 5 (30 points)

* No additional restrictions

## Example 1

`stdin`
```
6
2 0 3 3 2 2
4
5 5
1 1
0 1
2 2
```

`stdout`
```
2
1
5
2
```

### Explanation

The first plan wants to visit the shop at position $5$, which has the value $2$. We can see that the subarray $[4, 5]$ (which contains the values $2, 2$) has the `xor` sum `0`, so it is the smallest subarray with `xor` `0` that contains $[5, 5]$. Therefore, the answer will be $2$.

The second plan contains only the shop at position $1$, which has the value `0`. The optimal segment for this plan is $[1, 1]$.

The third plan contains the shops $0$ and $1$, which have the values $2, 0$. The optimal segment for this plan is $[0, 4]$.

The fourth plan contains only the shop at position `2`, which has the value `3`. The optimal segment for this plan is `[2, 3]`.

## Example 2

`stdin`
```
10
5 7 3 6 1 2 5 2 5 4
3
7 9
5 8
1 5
```

`stdout`
```
8
4
-1
```

### Explanation

For the first plan, one of the optimal segments is $[2, 9]$, with a length of $8$.

For the second plan, one of the optimal segments is $[5, 8]$, with a length of $4$.

For the third plan, no valid subarray exists, so $\text{−1}$ is printed.
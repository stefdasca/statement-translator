Certainly! Here's the translated problem statement:

---

We all know that popcorn is a true culinary delicacy. In your preparations for this year's batch (and for the after parties), you have ordered **`N` types of microwave popcorn**. Each type has `3` associated values:
* `A[i]` = The time (in seconds) when any kernel of that type "pops";
* `B[i]` = The time (in seconds) when any kernel of that type "burns";
* `C[i]` = The quantity (in kernels) of that type.

You also have **`M` single-use popcorn bags** of very large (practically infinite) capacity and a microwave oven. Since, of course, nobody likes uncooked or burnt popcorn, you want to conveniently partition them into the `M` bags and then place them one by one into the microwave, setting an appropriate cooking time `prep[i]`, so that after the `M` batches you get **as many edible popcorn kernels as possible**.

Formally, a kernel of type `i` placed in bag `j`, cooked at time `prep[j]` (in seconds) is edible if and only if `A[i] \leq prep[j] < B[i]`.

Given the `N` types of popcorn and the number of available bags, you need to find a convenient partition and the optimal cooking times for each bag, so that in the end you get the maximum number of edible popcorn kernels, which you will print in the output file. Too easy!

# Input data
The input file `popcorn.in` contains on the first line the natural numbers `N` and `M`, separated by a space, with the meaning given in the problem statement. The next `N` lines contain the values `A[i], B[i], C[i]` corresponding to each type of popcorn.

# Output data
The file `popcorn.out` will contain a single natural number representing the maximum number of edible popcorn kernels that can be obtained.

# Constraints and clarifications
* `1 \leq M \leq N \leq 200000`
* `1 \leq A[i] < B[i] \leq 200000`
* The total number of popcorn kernels does not exceed $10^9$
* Some bags can be empty!
* `X = max{N, B[1], B[2], \ldots, B[N]}`
* For `10` points: `X \leq 550, M \leq 100`
* For another `10` points: `X \leq 3000, M \leq 50`
* For another `10` points: `M \leq X \leq 3000`
* For another `10` points: `X \leq 50000, M = 3`
* For another `20` points: `X \leq 50000, M \leq 20`
* For another `15` points: `X \leq 200000, M \leq 50`
* For another `15` points: `M \leq X \leq 50000`
* For the remaining `10` points: the original constraints

# Examples
`popcorn.in`
```
5 2
2 4 3
1 5 6
4 8 10
7 8 2
10 11 2
```
`popcorn.out`
```
21
```

We have `5` types of popcorn and `2` available bags.
One possible solution is:

- Bag `1` will contain types `1` and `2` and will be cooked at time `3`.
- Bag `2` will contain types `3, 4, 5` and will be cooked at time `7`.

All types of popcorn will be cooked successfully, except type `5`, which will remain unpopped.

Explanation
---
`popcorn.in`
```
3 3
1 2 2
2 3 3
1 3 5
```
`popcorn.out`
```
10
```

Explanation
---

We can choose the bags as follows:
- Bag `1` will contain types `1, 3` and will be cooked at time `1`.
- Bag `2` will contain type `2` and will be cooked at time `2`.
- Bag `3` will be empty.

---
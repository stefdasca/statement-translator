
Sile the Great Buyer (SMC) has gone to the market! He knows that the market consists of `N` stalls, each stall selling an infinite number of products. Additionally, SMC knows the initial price $A_i$ of the product at stall `i` and the ratio $B_i$ by which this price increases with each purchase of a product. In other words, if the first product bought from stall `i` costs $A_i$, the second will cost $A_i+B_i$, the third will cost $A_i+2 \cdot B_i$, and so on.

# Task

SMC wants to buy `K` products such that the sum of the prices of the purchased products is minimized. Since SMC does not know arithmetic, you need to help him by writing a program!

# Input data

The first line of the file `tarabe.in` contains two natural numbers `N` and `K`, representing the number of stalls and the number of products SMC wants to buy, separated by a space. The following `N` lines each contain two natural numbers $B_i$ and $A_i$ representing the ratio and the initial cost of a product at stall `i`.

# Output data

The first and only line of the file `tarabe.out` must contain a single number, which is the minimum sum of prices that SMC can achieve if he buys **exactly** `K` products.

# Constraints and clarifications
* `1 \leq N \leq 200 \ 000`;
* `1 \leq K \leq 1 \ 000 \ 000 \ 000`;
* $1 \leq A_i, B_i \leq 1 \ 000$;
* For `20%` of the tests `N, K \leq 1 \ 000`;
* For `60%` of the tests `N, K \leq 200 \ 000`;
* **Attention!** SMC guarantees that for the result, data types of `64` bits with sign can be used.

# Example

`tarabe.in`

```
4 7
9 3
10 2
5 2
4 10
```

`tarabe.out`

```
48
```

Explanation
---

In order, the products bought will be: from stall `3` with the cost `2`, from stall `2` with the cost `2`, from stall `1` with the cost `3`, from stall `3` with the cost `2+5`, from stall `4` with the cost `10`, from stall `3` with the cost `2+5+5`, and from stall `2` with the cost `2+10`.

There is no other variant that ensures a lower sum of prices.
```

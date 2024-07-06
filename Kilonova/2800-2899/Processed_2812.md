Andrei is greedy. After eating the main courses, he wants to prepare **three cakes**, of which he will eat just one at random.

A cake will be made up of various types of chocolate. We define the **weight** of such a cake as the sum of the weights of the chocolate types used, meaning a cake made up of $20$ grams of white chocolate and $30$ grams of dark chocolate will have a weight of $50$ grams.

Andrei has $N$ types of chocolate available, arranged in a line on a shelf in his pantry, each with a certain order number.
* For the first cake, he will use all chocolate types from the first to a certain order number $A$, chosen by him;
* For the second cake, he will use all chocolate types from order number $A + 1$ to a certain order number $B$, chosen by him;
* For the third cake, he will use all chocolate types from order number $B + 1$ to the last type.

Since the cake he will eat will be chosen at random, Andrei wants to ensure that he will be satisfied choosing any of the three cakes, so he proposes to minimize the difference between the weight of the "heaviest" cake and the weight of the "lightest" cake.

In other words, noting the weights of the three cakes as `T1`, `T2`, `T3`, Andrei wants the following expression, called the recipe error, to be as small as possible:
```c++
max(T1, T2, T3) - min(T1, T2, T3)
```

# Task

Given the $N$ types of chocolate and their weights, find **the smallest** possible recipe error, helping Andrei choose the two positions/order numbers $A$ and $B$.

# Input data

The first line of the input file `desert.in` will contain the number $N$.

The second line will contain the weights of the $N$ types of chocolate on the shelf.

# Output data

The first line of the output file `desert.out` will contain the minimum recipe error.

# Constraints and clarifications

* $3 \le N \le 2 \cdot 10^5$
* $1 \le$ weight of any type of chocolate $\le 10^4$
* $10$ points are awarded by default.

| # | Points |      Constraints      |
|:-:|:-------:|:--------------------:|
| 1 |    20   |   $3 \le N \le 500$  |
| 2 |    20   |  $3 \le N \le 10^4$  |
| 3 |    50   | Without additional constraints |

# Example

`desert.in`
```
10
8 16 11 1 5 20 14 20 7 5
```

`desert.out`
```
7
```

## Explanation

We can choose $A = 4$ and $B = 7$, and the cakes will look as follows:

~[desert.png|align=left|width=75%]

Thus, the first cake will contain the types from $1$ to $4$, having a weight of $8 + 16 + 11 + 1 = 36$.
The second cake will contain the types from $5$ to $7$, having a weight of $5 + 20 + 14 = 39$.
The third cake will contain the types from 8 to 10, having a weight of $20 + 7 + 5 = 32$.
In this case, the recipe error is $\max(36, 39, 32) - \min(36, 39, 32) = 39 - 32 = 7$. It can be demonstrated that this answer is optimal.
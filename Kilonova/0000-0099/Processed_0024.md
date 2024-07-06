# Translation

You have recently opened a Japanese-themed restaurant, but things are not going great. Sometimes the customers have to wait a long time for their ordered food, and now you think you understand why this happens.

The restaurant does not have tables, but a single very long bar equipped with a conveyor belt that transports food portions from the kitchen to the customer. The bar has `500,000,000` seats numbered in increasing order, with seat `1` being the closest to the kitchen. Sometimes clients place new orders. An order placed at the second `T` by the client sitting at seat number `P` will arrive instantly at the kitchen. The food preparation will take `D` seconds, and then the food will be placed on the belt and will take exactly `P` seconds to reach the customer. During this time, the food will pass in front of seats `1, 2, ... P - 1`. If for some reason the customer doesn't pick up the food from the belt, it will continue to move. In that case, the relevant customer is expected to pick up the food when it reaches their seat at the second `T + D + P`.

So far, the restaurant serves only one type of food: ramen. Thus, the orders placed by customers tend to be easily interchangeable, and they are very open to taking advantage of this fact.

The following is known:

* A customer can have zero or more pending orders.
* A customer with zero pending orders is completely inactive.
* The number of pending orders of a customer who places an order at the second `T` will increase by one exactly at the second `T`.
* A customer with at least one pending order will pick up the first ramen portion that passes in front of them, regardless of whether it was intended for them or not. If they do this at moment `T`, their number of pending orders will decrease by one exactly at moment `T`.

For example, let's analyze the following situation with two orders:

The preparation time of ramen is `D = 2` seconds. This value is a constant and applies identically to every order.
At the second `T1 = 10`, the person on seat number `P1 = 8` (let's call them A) orders a portion of ramen. At the second `T1 + D = 12`, their portion is placed on the belt.

At the second `T2 = 16`, the person on seat number `P2 = 6` (let's call them B) orders a portion of ramen. At the second `T2 + D = 18`, their portion is placed on the belt.

At the second `18` the portion intended for customer `A` passes in front of seat `6`, and customer `B`, being themselves waiting for an order, will take it and eat it. They will eat it at the second `18` and will then ignore their own order when it passes by.

At the second `26` the portion intended for customer `B` will reach customer `A`, who will take it and eat it. They will eat it at the second `26`.

It can be observed that generally, despite the delays created, each customer will consume exactly as many portions as they ordered.

# Task

To evaluate the impact of this habit on the waiting times, you have obtained data about all the orders placed on the current day. Your goal is to find out for each order the following value: if that order is the `NR`-th made by the respective customer, what is the second at which the customer in question will eat for the `NR`-th time?

# Input data

The input file `ramen.in` will contain the number of orders `N`, and the time to prepare a portion of ramen `D` on the first line. The next `N` lines will contain a pair of numbers each: `T[i]`, the second at which the `i`-th order is placed, and `P[i]`, the seat number from which the `i`-th order was placed. It is guaranteed that the order times are distinct and increasing in the order they are read.

# Output data

The output file `ramen.out` will contain `N` lines, each containing a single natural value: the `i`-th value will represent the answer to the `i`-th order in the reading order.

# Constraints and clarifications

1. `1 \leq N \leq 100 000`
2. `0 \leq D, T[i] \leq 500 000 000`, for any `1 \leq i \leq N`
3. `1 \leq P[i] \leq 500 000 000`, for any `1 \leq i \leq N`
4. It is guaranteed that `T[i] < T[i+1]`, for any `1 \leq i \leq N`
5. For tests worth a total of `22` points, it is additionally guaranteed that `N \leq 2000` and `D, T[i], P[i] \leq 5000`
6. For other tests worth a total of `25` points, it is additionally guaranteed that `N \leq 2000`.

# Examples

`ramen.in`
```
2 2
10 8
16 6
```

`ramen.out`
```
26
18
```

`ramen.in`
```
3 2
5 4
6 4
7 3
```

`ramen.out`
```
12
13
10
```

`ramen.in`
```
3 0
0 6
3 3
4 5
```

`ramen.out`
```
10
3
8
```

# Explanations

The first test is the example described in the statement.

For the second test:
Observe that in this example the customer on seat number `4` places two orders. The respective answer for the first order is the second the customer eats for the first time, and the respective answer for the second order is the second the customer eats for the second time.

For the third test:
Observe that in this example the customer on seat number `3` places an order at the second `3`. At that exact moment, a portion of ramen appears in front of them, and they consume it immediately.
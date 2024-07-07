
After a productive day of cleaning, Henry and Hetty went out to a sushi restaurant in the city. This restaurant has `N` tables connected by `N-1` double-sided conveyor belts, so any two tables are directly or indirectly connected through conveyor belts. For each table `i`, `1 \leq i \leq N`, we know both the number $K_i$ of tables it is directly connected to, and the ordered list of its neighboring tables: $V_{i,1}, V_{i,2} \ldots V_{i,K_i}$.

The conveyor belts transport dishes to customers. They follow a unique route defined by the following rule: for any table `i`, a dish at table `i` that just came from table $V_{i,j}$ will go from table `i` to table:

* $V_{i,j+1}$, if $1 \leq j < K_i$
* $V_{i,1}$, if $j = K_i$

Additionally, if a new dish is sent from table `1` to table $V_{1,1}$, we know that it will reach table `i` for the first time coming from table $V_{i,1}$, for any `i`, `1 \leq i \leq N`.

# Task

Henry and Hetty entered the restaurant at time `0`. They know that during their visit, `M` dishes will be placed on the conveyor belts. For each of the `M` dishes, they know the triplet `(x, y, t)`, meaning that at time `t`, the dish will be placed on the belt at table `x` to go towards table $V_{x,y}$. They also know that it takes one unit of time for a dish to travel between two neighboring tables. The two will sit at a table and take all the dishes that pass by that table. Henry and Hetty wonder: for each table `i`, what is the minimum time after which they collect all `M` dishes that will be placed on the belt?

# Input data

The first line of the input file `sushi.in` will contain two natural numbers `N` and `M`, representing the number of tables and the number of dishes in the restaurant. On the next `N` lines will be the descriptions of the neighbor lists for each table. Thus, on line `i+1`, there will be the natural number $K_i$, followed by $K_i$ natural numbers: $V_{i,1}, V_{i,2} \ldots V_{i,K_i}$, as described previously. On each of the next `M` lines will be a triplet of natural numbers `(x, y, t)`, meaning that at time `t`, a dish will be placed on the belt at table `x` to go towards table $V_{x,y}$.

# Output data

The first line of the output file `sushi.out` will contain `N` natural numbers, where the `i`-th number represents the time required to collect all the dishes from the belt if Henry and Hetty sit at the table with index `i`.

# Constraints and clarifications

* `1 \leq N \leq 100 000`
* `1 \leq M \leq 100 000`
* For each triplet `(x, y, t)` we have `1 \leq x \leq N`, $1 \leq y \leq K_x$, and `0 \leq t \leq 100 000`

# Example

`sushi.in`
```
5 1
3 2 3 4
1 1
2 1 5
1 1
1 3
3 1 0
```
`sushi.out`
```
1 4 0 2 7
```

Explanations
---

We have `N = 5` tables and `M = 1` dish.
Table `1` is neighboring with `3` tables: `(2, 3, 4)`
Table `2` is neighboring with `1` table: `(1)`
Table `3` is neighboring with `2` tables: `(1, 5)`
Table `4` is neighboring with `1` table: `(1)`
Table `5` is neighboring with `1` table: `(3)`

The only dish will be placed at time `0` at table `3` to go towards the first table in table `3`'s neighbor list: table `1`.
The dish will follow this route: `3, 1, 4, 1, 2, 1, 3, 5, 3` ...
It can be picked up from:
- table `1` at time `1`
- table `2` at time `4`
- table `3` at time `0`
- table `4` at time `2`
- table `5` at time `7`

`sushi.in`
```
3 2
2 2 3
1 1
1 1
2 1 0
3 1 1
```
`sushi.out`
```
2 3 2
```

Explanations
---

We have `N = 3` tables and `M = 2` dishes.
Table `1` is neighboring with `2` tables: `(2, 3)`
Table `2` is neighboring with `1` table: `(1)`
Table `3` is neighboring with `1` table: `(1)`

A dish is placed at time `0` at table `2`, heading towards the first table in table `2`'s neighbor list: table `1`. It can be picked up from:
- table `1` at time `1`
- table `2` at time `0`
- table `3` at time `2`

The other dish is placed at time `1` at table `3`, heading towards the first table in table `3`'s neighbor list: table `1`. It can be picked up from:
- table `1` at time `2`
- table `2` at time `3`
- table `3` at time `1`

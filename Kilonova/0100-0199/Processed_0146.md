In a museum, there is a linear corridor consisting of `N` rooms, numbered from `1` to `N`. In room `1 \leq i \leq N`, there is an infinite reserve of gold ingots of the same type with value $v_i$ and weight $g_i$. In the first room, `K` thieves enter, each carrying a backpack with capacity `G`, initially empty. When a thief is in room `i`, they can take as many ingots as they want from the current room and add them to their backpack, provided that the total weight of the ingots in the backpack does not exceed `G`. Once an ingot is stolen, it will remain in the thief's backpack until they exit the museum.

The thieves act as a group, so they will tour the museum in `N` steps, as follows: on step `1 \leq i \leq N`, all thieves advance from room `i` to room `i + 1`, where room `N + 1` is considered the exterior of the museum. It is observed that after the first `i` steps, all thieves will be in room `i + 1`. The museum management has installed alarms at the doors between any two consecutive rooms. More precisely, alarm `1 \leq i \leq N` is installed between rooms `i` and `i + 1` and is characterized by a value $x_i$. It is triggered if and only if at the time when the thieves pass through the door between rooms `i` and `i + 1`, there are at least $x_i + 1$ thieves whose backpacks have the same total weight at that moment, because in this case a routine control would be performed, and the thieves would be caught (this happens even if the thieves haven't stolen anything until that point). Of course, alarm `N` is installed between room `N` and the exterior of the museum.

Once outside the museum, the thieves calculate the total haul as the sum of the values `v` corresponding to the ingots in the `K` backpacks. There are `T` scenarios, and for each, the maximum possible haul in the given conditions is required, or `−1` if whatever they do, the thieves would be caught.

# Input data
The first line contains a single natural number `T`, representing the number of scenarios. The descriptions of the `T` scenarios follow. The description of a scenario is as follows: the first line contains three natural numbers `N, K, G`, separated by spaces; the following `N` lines each contain three natural numbers, where on line `1 \leq i \leq N` the numbers $v_i, g_i, x_i$ are given, separated by spaces.

# Output data
Print `T` lines, representing, in the given order, the answers for the `T` given scenarios.

# Constraints and clarifications
* `1 \leq T \leq 900`
* `1 \leq N \leq 300`
* `1 \leq K \leq 50`
* `1 \leq G \leq 300`
* $1 \leq v_i \leq 300$, for any `1 \leq i \leq N`.
* $1 \leq g_i \leq 300$, for any `1 \leq i \leq N`.
* $1 \leq x_i \leq 50$, for any `1 \leq i \leq N`.
* $1 \leq S_N \leq 900$, where $S_N$ denotes the sum of the values `N` corresponding to the `T` scenarios.

## Subtask 1 (11 points)
* `N \leq 4, K \leq 3, G \leq 7`, $S_N \leq 12, v_i \leq 20, 2 \leq g_i \leq 7, x_i \leq 3`, for any `1 \leq i \leq N`.

## Subtask 2 (18 points)
* There exists `1 \leq j \leq N` such that $x_i = K$ for any `1 \leq i \leq N, i \ne j`.

## Subtask 3 (40 points)
* `N \leq 40, G \leq 40`, $S_N \leq 120, v_i \leq 40, g_i \leq 40`, for any `1 \leq i \leq N`.

## Subtask 4 (31 points)
* No additional constraints.

# Examples

`stdin`

```
3
2 1 3
10 2 1
9 1 2
2 2 3
10 2 1
9 1 2
2 3 3
10 2 1
9 1 2
```

`stdout`

```
27
46
-1
```

Explanations
---

There are `T = 3` scenarios.

### First scenario
We have `N = 2` rooms and `K = 1` thief equipped with a backpack of capacity `G = 3`. In room `1` there is an infinite reserve of gold ingots with value `10` and weight `2`, and in room `2` there is an infinite reserve of gold ingots with value `9` and weight `1`. The alarm between room `1` and room `2` has $x_1 = 1$, and the alarm between room `2` and the exit has $x_2 = 2$. Under the given conditions, the alarms will not sound regardless of what the thief chooses to do, so they can achieve a maximum haul of `27 = 9 + 9 + 9` by stealing three ingots from room `2`.

### Second scenario
This scenario is identical to the first, except we have `K = 2` thieves, each with a backpack of capacity `3`. If both thieves take `3` ingots from room `2`, they would have a total haul of `54 = 6 × 9`. Unfortunately, if they did this, they would be caught by the alarm between rooms `1` and `2`. **It is observed that they would be caught by this alarm even if they choose not to steal anything from any room!** The maximum haul is actually obtained, for example, if the first thief chooses to steal one ingot from each room (total `19 = 10 + 9`), and the second thief chooses to steal three ingots from room `2` (total `27 = 9 + 9 + 9`). In total `46 = 19 + 27`.

### Third scenario
This scenario is identical to the first two, except we have `K = 3` thieves. In this case, the three thieves will not be able to pass room `1` without triggering the alarm, so the answer is `−1`.
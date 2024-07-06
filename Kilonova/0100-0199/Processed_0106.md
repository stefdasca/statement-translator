It is well-known that the Dragon is a car enthusiast. Yesterday, he reached a very peculiar intersection (if we can call it that) as shown in the figure below …

~[masina.jpg]

At this intersection, `N` cars (numbered from `1` to `N`) arrived. The Dragon is in car `X`. At that moment, he was racing against car `Y` (`X` different from `Y`). The `3` roads are very narrow, so only one car can fit, making overtaking impossible. However, due to the configuration of the roads, cars can change positions at the exit.

For example, for `N = 3`, there are `5` possible orderings of the `3` cars:
1. `1 2 3`: car `1` enters the middle road, comes out as `1`, car `2` enters and comes out as `2`, car `3` enters and comes out as `3`
2. `1 3 2`: car `1` enters and comes out as `1`, car `2` enters, car `3` enters, car `3` comes out, car `2` comes out
3. `2 1 3`: car `1` enters, car `2` enters, car `2` comes out, car `1` comes out, car `3` enters, car `3` comes out
4. `2 3 1`: car `1` enters, car `2` enters, car `2` comes out, car `3` enters, car `3` comes out, car `1` comes out
5. `3 2 1`: car `1` enters, car `2` enters, car `3` enters, car `3` comes out, car `2` comes out, car `1` comes out

Any of the `M` (in this case `N = 3`, `M = 5`) possible configurations have equal chances of occurring.

The Dragon wants to know the chances (in percentages) that he will end up ahead of the car he was racing against.

# Task
Help the Dragon determine the chances of winning, that is, of finishing ahead of car `Y`.

# Input data
The first line of the file `masina.in` contains `3` natural numbers `N`, `X` and `Y`, separated by a space, representing the number of cars, the Dragon's car, and the competitor's car, respectively.

# Output data
The file `masina.out` will contain on its only line a single real number truncated to exactly `2` decimal places, which represents the chances (in percentages) that the Dragon will end up ahead of the competitor.

# Constraints and clarifications
* `1 < N < 101`
* `0 < X,Y < N+1`
* for `50%` of the tests `X=1`
* truncating the real number `60.5673` to two decimal places results in `60.56`
* truncating the real number `60.5628` to two decimal places results in `60.56`
* truncating the real number `60.5655` to two decimal places results in `60.56`

# Example

`masina.in`
```
3 1 3
```

`masina.out`
```
60.00
```

Explanation
---

Out of the `5` total configurations, in `3` of them car `1` finishes ahead of car `3`, so the chances are `60%`.
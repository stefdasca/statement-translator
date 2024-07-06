Renowned for their admiration for cocoa beans, the Aztecs decided to store them in the capital of the empire. The Aztec Empire consists of `N` cities (numbered from `0` to `N - 1`), connected by `N - 1` roads, so that one can travel from any city to another by traversing one or more roads.

A city can be called a capital only if, after destroying all the roads adjacent to this city, any connected set (for which however we choose `2` cities, we can travel from the first to the second via roads) has at most $ \frac{N}{2} $ cities.

The chief architect of the Aztecs is thinking of changing the road structure of the empire. Thus, he can perform the following operation (possibly multiple times): destroy a road and build a new one, keeping the empire connected.
The architect does not yet know in which city it is safest to store the beans, but he would like to find out for each city from `0` to `N - 1` the minimum number of operations that need to be performed so that it can be called a capital. (The Aztecs can change their capital, as long as their beans are safe.)

# Input data
The first line will contain `T`, the number of scenarios. Then follow `T` groups of lines, each describing a scenario to be solved. On the first line of a scenario is `N` with the meaning from the statement. On the next `N - 1` lines follow two numbers `x` and `y` separated by spaces, meaning there is a road between `x` and `y`.

# Output data
`T` lines will be printed, each consisting of `N` numbers separated by spaces, for each `i` from `0` to `N - 1` the minimum number of operations necessary for the city `i` to be called a capital.

# Constraints and clarifications
* `1 \leq N \leq 300 000`
* $0 \leq X_i, Y_i \leq N - 1$ for `0 \leq i \leq N - 2` and $X_i \neq Y_i$.
* Let $S_N$ be the sum of N's for all scenarios. $1 \leq S_N \leq 300\ 000$.
* `1 \leq T \leq 300 000`.
* It can be observed that for a particular road configuration, multiple cities can be the capital at the same time.

## Subtask 1 (7 points)
* $1 \leq S_N \leq 10$
## Subtask 2 (14 points)
* $1 \leq S_N \leq 50$
## Subtask 3 (17 points)
* $1 \leq S_N \leq 200$
## Subtask 4 (21 points)
* $1 \leq S_N \leq 2 \ 000$
## Subtask 5 (18 points)
* $1 \leq S_N \leq 40\ 000$
## Subtask 6 (23 points)
* No additional constraints.

# Example

`stdin`

```
2
3
0 2
0 1
7
1 0
1 2
2 3
3 4
5 1
1 6
```

`stdout`

```
0 1 1
1 0 1 2 2 1 1
```

Explanations
---

For the first example:
* The city `0` can be called a capital without any modifications.
* For the city `1`, the road `(0, 2)` is destroyed and the road `(1, 2)` is built.
* For the city `2`, the road `(0, 1)` is destroyed and the road `(1, 2)` is built.
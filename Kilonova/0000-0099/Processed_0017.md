Marian is in the galaxy OJI-2020 and it is the year 11235. In this galaxy, there are `N` different planets and `M` bidirectional transport channels of the type `(x, y, t)` which allow you to travel from planet `x` to planet `y` (or vice versa) in `t` seconds. But Marian is a true engineer and, because he finds this transport method very inefficient, he developed a device that allows teleportation from a planet `x` to any other planet `y` in `P` seconds under the condition that you could reach from planet `x` to planet `y` using at most `L` transport channels. This device is currently just a prototype, so he cannot use it more than `K` times. Marian is on planet `1` and asks you to tell him the minimum time required to reach planet `N`.

# Task 
Write a program that calculates the minimum time required to reach planet `N` starting from planet `1`.

# Input data
The first line of the file `ateleport.in` will contain `5` values `N, M, P, L, K`, separated by a single space, with the meanings from the statement. Each of the next `M` lines will contain `3` values $X_i, Y_i, T_i$ which describe a transport channel.

# Output data
The output file `ateleport.out` will contain a single value on the first line which represents the minimum time required to reach planet `N` starting from planet `1`.

# Constraints and clarifications 
* `1 \leq N, M \leq 10\ 000`; 
* `0 \leq L, K \leq 10`;
* `1 \leq T_i, P \leq 100\ 000`;
* `1 \leq X_i, Y_i \leq N`;
* between any two planets there is at most one channel; 
* for tests worth `30` points it is guaranteed that `K = 0` and all communication channels have $T_i = 1$; 
* for OTHER tests worth `20` points it is guaranteed that `K = 0`; 
* for OTHER tests worth `20` points it is guaranteed that `N \leq 300`; 
* it is guaranteed that for all tests there exists a solution; 
* `10` points are awarded automatically.

# Examples

`ateleport.in`

```
6 7 3 2 1 
1 2 2 
1 3 5 
2 3 4 
2 4 23 
3 4 6 
5 4 7 
5 6 9
```

`ateleport.out`

```
14
```

`ateleport.in`

```
6 7 3 2 0 
1 2 2 
1 3 5 
2 3 4 
2 4 23 
3 4 6
5 4 7 
5 6 9
```

`ateleport.out`

```
27
```

Explanations
---

For the first test:
The device can be used at most once. To reach planet `6` in minimum time, we will traverse channel `1 → 2`, then teleport to planet `5`, from where we will traverse channel `5 → 6`. The final cost is `2 + 3` (teleportation) `+ 9 = 14`

~[ateleport.png]

For the second test:
The device cannot be used at all. To reach planet `6` from planet `1` in minimum time, we will traverse the channels in the order `1→3→4→5→6` and the time obtained is `5+6+7+9=27` seconds.
```markdown
Alex wants to dry his clothes on the balcony. He washed `K` t-shirts and one sock. Alex's drying rack has `N` levels, and each level has `M` spots where only one piece of clothing can be hung. Alex dries the clothes in a specific way: he starts by placing the sock on level `A`, spot `B`, and then brings the laundry basket with the `K` t-shirts and places them one by one, always choosing a free spot as far away as possible from where he placed the sock. The metric he finds most appropriate when it comes to drying clothes is the Manhattan distance, so the distance from level `r1`, spot `c1` to level `r2`, spot `c2` is given by the expression `|r1 – r2| + |c1 - c2|`.

# Task
Find the distance between the position where the last t-shirt was hung and the position where the sock is drying.

# Input data
The first line of the input file `rufe.in` will contain `5` integers `N, M, A, B,` and `K`, with the significance given in the statement, separated by a space.

# Output data
The output file `rufe.out` will contain a single line that will print the requested value.

# Constraints and clarifications
* $1 \leq N, M \leq 10^9$
* `1 \leq A \leq N`
* `1 \leq B \leq M`
* `1 \leq K \leq N * M – 1`
* For tests worth `13` points, it is guaranteed that $N, M \leq 10^3$.
* For other tests worth `12` points, it is guaranteed that $N \leq 10^6$.
* For other tests worth `12` points, it is guaranteed that $M \leq 10^6$.
* For other tests worth `18` points, it is guaranteed that $K \leq 10^6$.
* For other tests worth `7` points, it is guaranteed that `A = B = 1`.

# Examples

`rufe.in`
```
5 6 3 3 4
```

`rufe.out`
```
4
```

`rufe.in`
```
3476 53410 438 9217 1000000
```

`rufe.out`
```
45818
```

`rufe.in`
```
1000000000 1000000000 1 1 7
```

`rufe.out`
```
1999999995
```

`rufe.in`
```
654321 123456 5454 1212 10000000000
```

`rufe.out`
```
628395
```

Explanations
---

For the first test:
The drying rack has `5` levels with `6` spots per level. The sock is placed on level `3`, spot `3`. The first `2` t-shirts will be hung at a distance of `5` in the corners of the drying rack. The next `2` t-shirts can only be placed at a distance of `4`.

For the last test:
In this case, Alex is drying $10^{10}$ t-shirts. Pay attention when reading such a large value from the file.
```
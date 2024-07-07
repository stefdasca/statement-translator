
The Archipelago of Zopopan consists of `n` triangular islands numbered from `1` to `n`. Each island is located using the Cartesian coordinates of its vertices.

The administration wants to purchase helicopters to facilitate transportation between the islands. A helicopter will be able to ensure a route between two islands at the minimum distance obtained horizontally or vertically (parallel to the coordinate axes). Additionally, due to the tank capacity, such a route cannot exceed a value `k` — a natural number. The helicopters can travel the routes in both directions.

The investment must meet the following conditions:
1. The number of helicopters purchased must be minimal.
2. The number of pairs of islands between which transportation can be achieved using one or more helicopters must be maximal.
3. The sum of the lengths of all routes must be minimal.

# Task
Write a program that, for given `n`, `k`, and the known coordinates of the island vertices, determines:
1. the minimum number of helicopters that will be purchased by the administration;
2. the number of unordered pairs of islands between which transportation can be achieved by helicopters directly or indirectly;
3. the sum of the distances traveled by all the purchased helicopters (the distance traveled by a helicopter is considered the distance between the islands it ensures transportation between).

# Input data
The input file `elicoptere.in` contains on the first line a value `v` which can be `1`, `2`, or `3`, depending on the task that will be solved, on the second line, the natural numbers `n` and `k` separated by a space, as described above, and on the next `n` lines are six natural numbers `x1, y1, x2, y2, x3`, and `y3` separated by space representing the coordinates of the three vertices of the islands in (abscissa, ordinate) format.

# Output data
If the value of `v` is `1` then the output file `elicoptere.out` will contain on the first line only the minimum number of helicopters that will be purchased by the administration.
If the value of `v` is `2` then the output file `elicoptere.out` will contain on the first line only the maximum number of pairs of islands between which transport by helicopters can be achieved.
If the value of `v` is `3` then the output file `elicoptere.out` will contain on the first line the minimum sum of the lengths of the routes traveled by helicopters.

# Constraints and clarifications
* `1 \ \leq n \ \leq 100`;
* `1 \ \leq k \ \leq 1000`;
* the coordinates of the island vertices are natural numbers $0 \ \leq x_i , y_i \ \leq 10^6$;
* any two islands do not have common points;
* for task `2`, if you can travel from island `A` to island `B` then it is evident that you can travel from `B` to `A`, so the pair consisting of `A` and `B` is counted only once;
* The distance between two islands can also be a real number. For task `3`, the result is required with an accuracy of `0.001`, i.e., the result noted with `R` is considered correct if, compared to the commission result `C`, it meets the condition `|R-C|<0.001`.
* To calculate and display a real number `x` with as much precision as possible, we recommend using the `double` type.
* For correctly solving task `1`, `40%` of the score is awarded;
* For correctly solving task `2`, `20%` of the score is awarded;
* For correctly solving task `3`, `40%` of the score is awarded.

# Examples

`elicoptere.in`
```
1
6 11
100 20 100 30 105 30
20 20 30 30 20 30
200 20 200 30 205 30
100 40 100 50 105 40
10 40 5 40 10 50
10 20 5 30 10 30
```

`elicoptere.out`
```
3
```

`elicoptere.in`
```
2
6 11
100 20 100 30 105 30
20 20 30 30 20 30
200 20 200 30 205 30
100 40 100 50 105 40
10 40 5 40 10 50
10 20 5 30 10 30
```

`elicoptere.out`
```
4
```

`elicoptere.in`
```
3
6 11
100 20 100 30 105 30
20 20 30 30 20 30
200 20 200 30 205 30
100 40 100 50 105 40
10 40 5 40 10 50
10 20 5 30 10 30
```

`elicoptere.out`
```
30
```

Explanations
---

For the first test:
The data corresponds to the previous figures:
`v = 1`, so **ONLY** the first task will be solved.
Pairs of islands with direct helicopter transport: `(1,4) (2,6), (6,5)` thus we obtain `3` helicopters.

For the second test:
The data corresponds to the previous figures:
`v = 2`, so **ONLY** the second task will be solved.
Pairs of islands with direct helicopter transport: `(1,4) (2,6), (6,5)` thus we obtain `3` helicopters.
Island `3` remains isolated, thus we have two groups of islands. The first group contains islands `1` and `4`, and the second group contains islands `2, 5, 6`. From the first group, the pair `(1,4)` is counted, and from the second group, pairs of islands `(2,5), (2,6)` and `(5,6)` are counted. In total `4` pairs of islands between which transport by helicopter can be achieved either directly or indirectly.

For the last test:
The data corresponds to the previous figures:
`v = 3`, so **ONLY** the third task will be solved.
Pairs of islands with direct helicopter transport: `(1,4) (2,6), (6,5)` thus we obtain `3` helicopters.
Island `3` remains isolated, thus we have two groups of islands. The first group contains islands `1` and `4`, and the second group contains islands `2, 5, 6`.
The helicopters ensure direct transport between islands:
`1` and `4` with a vertical distance equal to `10`;
`2` and `6` with a horizontal distance equal to `10`;
`5` and `6` with a vertical distance equal to `10`;
In total, the transport routes have a distance of `30`.


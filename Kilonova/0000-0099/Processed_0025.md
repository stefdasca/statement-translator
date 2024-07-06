```markdown
To attract tourists, the town hall of a city decided to build an enormous water park with `n` pools. The park will have a covered area and will be surrounded by an open space for outdoor activities.

The enclosed area will be covered by a single building in the shape of a polygon, and the pools will be designed at the vertices of the polygon and can communicate with each other through `m` access paths that do not intersect. The access paths between two pools can be of type `1`: a water-filled canal inside the building, or of type `2`: an alley outside the building.

In the adjacent example, the covered part of the park is delimited by the dotted line. We have `5` pools and `6` access paths: `(1,2), (2,5), (1,4), (1,3), (3,4), (3,5)`, of which `2` are canals (type `1`): `(1,3)` and `(1,4)`, respectively `4` are alleys (type `2`): `(1,2), (2,5), (3,4) and (3,5)`.

Another project that keeps the same access paths but differs in their types is to build `4` canals: `(1,2), (3,4), (3,5), (2,5)` and `2` alleys: `(1,3), (1,4)`.

In total, we can build `8` distinct projects with these access paths. Two projects are considered distinct if there is at least one access path that has different types in the two projects.
\
~[aquapark.png|width=27em]

# Task
Knowing the access paths between pools, determine one of the following requirements:
1. a way to construct the access paths, specifying the type of each;
2. the number of distinct projects.

# Input data
The input file `aquapark.in` contains on the first line three numbers separated by a space `c n m` representing in this order the type of task, the number of pools, and the number of access paths. The next m lines contain two numbers `x` and `y`, representing an access path between pool `x` and pool `y`.

# Output data
The output file `aquapark.out` will contain the following information depending on the value of `c`:
- if `c=1`: on m lines, it will print three numbers separated by a space `x y t`, meaning that between pool `x` and pool `y` there is an access path of type `t` (`1`-canal, `2`-alley). Each edge read from the input file must appear exactly once in the output file, regardless of the order of reading.
- if `c=2`: it will print a single number representing the number of distinct projects modulo `666013`.

# Constraints and clarifications
* `1 \ \leq \ n \ \leq \ 70\ 000`
* `1 \ \leq \ m \ \leq \ 100\ 000`
* Between two pools, there is at most one access path
* There is no access path from a pool to itself
* It is ensured that for the test data, there is at least one solution
* If there are multiple solutions, any of them can be displayed.
* For tests worth `16` points, `n, m \ \leq \ 15`
* For other tests worth `49` points, `n \ \leq \ 1000, m \ \leq \ 1500`
* The maximum score for the problem is `100` points, of which `10` points are granted.

# Example

`aquapark.in`
```
1 5 6
1 2
2 5
1 4
3 1
4 3
5 3
```

`aquapark.out`
```
1 2 1
1 3 1
1 4 1
2 5 2
3 4 1
3 5 2
```

`aquapark.in`
```
2 5 6
1 2
2 5
1 4
3 1
4 3
5 3
```

`aquapark.out`
```
8
```

Explanations
---

For the first test:
`c=1`, a way to construct the access paths is requested:
We have access paths of type `1` (canals) between pools `(1,2), (1,3), (1,4)` and `(3,4)`. We have access paths of type `2` (alley) between pools `(2,5)` and `(3,5)`.
See the drawing above.

For the second test:
We have `8` distinct ways to construct the access paths for the water park:
| Solution | paths of type 1         | paths of type 2         |
|----------|-------------------------|-------------------------|
| 1        | (1,2) (1,3) (1,4) (3,4) | (2,5) (3,5)             |
| 2        | (1,3) (1,4) (3,4)       | (1,2) (2,5) (3,5)       |
| 3        | (1,2) (1,3) (1,4)       | (2,5) (3,5) (3,4)       |
| 4        | (1,3) (1,4)             | (1,2) (2,5) (3,5) (3,4) |
| 5        | (2,5) (3,5)             | (1,2) (1,3) (1,4) (3,4) |
| 6        | (1,2) (2,5) (3,5)       | (1,3) (1,4) (3,4)       |
| 7        | (2,5) (3,5) (3,4)       | (1,2) (1,3) (1,4)       |
| 8        | (1,2) (2,5) (3,5) (3,4) | (1,3) (1,4)             |
```

Fish *Nemo* needs your help! In his archipelago, some ambitious fishermen have appeared who want to exploit the area. Nemo's archipelago can be represented as a matrix with $N$ rows and $M$ columns. It consists of islands surrounded by water, where an island represents an area of adjacent cells in rows or columns that do not contain water cells inside and cannot be expanded. Besides islands, one of the cells represents Nemo's shelter, which **will not** be located on an island (for obvious reasons).

In the archipelago, there are cells controlled by fishermen (these will not cover islands or Nemo's shelter). Each day, fishermen will extend their nets by one unit in a certain direction (row or column), but in **both** directions (left and right, or up and down), as long as they do not go outside the boundaries of the archipelago. They will have a preferred direction determined from the first day, and it will remain constant throughout all days. Also, being honest men, they will follow the following rules:

1. A fisherman cannot extend over land or over another fisherman's net.
2. If after a certain day a fisherman can no longer extend in a certain direction, he will continue to extend in the remaining direction.
3. If two fishermen reach the same cell on the same day, the one on the row with the smaller index gets priority, and in case of equal rows, the leftmost one.

# Task

*Nemo* is asking which is the first day from which he will no longer be able to reach the shelter from his starting point, knowing that he cannot swim on land, pass through fishermen's nets, or go out of the archipelago's boundaries. He can move from a cell only to adjacent cells in rows or columns.

# Input data

The first line of the `nemo.in` file will contain two numbers $N$ and $M$ representing the dimensions of the archipelago. Then $N$ lines will follow, each with $M$ characters describing the archipelago on the first day:

* Character `.` represents a water cell
* Character `N` represents Nemo's position
* Character `A` represents Nemo's shelter
* Character `#` represents a land area
* Character `L` represents a fisherman who will extend his net only along the row (left and right each day as long as he does not go outside the archipelago)
* Character `C` represents a fisherman who will extend his net only along the column (up and down each day as long as he does not go outside the archipelago)

# Output data

Write in the `nemo.out` file a single number, representing the first day starting from which *Nemo* will not be able to reach the shelter. If such a day does not exist, print the value $\-1$.

# Constraints and clarifications

* $2 \leq N \leq 1000$ and $2 \leq M \leq 1000$
* It is possible that after a certain day a net may cover Nemo's shelter, causing him to no longer be able to reach the shelter.
* It is possible that after a certain day a net may cover Nemo's starting point, causing him to no longer be able to reach the shelter.
* The tests are grouped, unlike how they were during the competition.

|#| Points | Constraints |
|-|--------|-------------|
|1|15|There will be no islands and there will be a single fisherman in the entire archipelago|
|2|35|$N \leq 200$ and $M \leq 200$|
|3|50|No additional constraints|

# Example 1

`nemo.in`
```
10 10
........L.
....C.....
.N........
..A...L...
..........
..........
..........
...#......
..###.....
.#####....
```

`nemo.out`
```
-1
```

## Explanation
This is how the archipelago will look on the third day, with the extended nets of the fishermen also marked with `C` and `L`:
```
....C.LLLL
....C.....
.N..C.....
..A.CLLLL.
..........
..........
..........
...#......
..###.....
.#####....
```
The fisherman on the second row extended with priority and separates Nemo's shelter from the rest of the archipelago.

# Example 2

`nemo.in`
```
10 10
.N........
..........
..........
......L...
....L.....
..........
...#.....A
..###..LC.
.#####....
#######...
```

`nemo.out`
```
4
```

## Explanation
The archipelago on the 4th day:
```
.N........
..........
..........
...LLLLLLL
.LLLLLLLC.
........C.
...#....CA
..###LLLC.
.#####..C.
#######.C.
```
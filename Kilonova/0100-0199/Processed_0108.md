A newspaper has its editorial office on the floor of a building. This floor, in the shape of a square, is made up only of rooms of the same size and square shape. For a floor with 4×4 rooms we have the configuration:

~[ziduri1.png]

Some of the walls of the rooms are missing. **The director** and **the chief editor** each have their offices in separate rooms. **The director** has his office in the room on line 1 and column 1, and **the chief editor** in the room on the last line and last column. Moving between two neighboring rooms can only be done if they do not have a dividing wall. To increase the speed of movement between the offices of **the director** and **the chief editor**, the decision was made to remove some walls. A study conducted by the administrative department shows that moving between two rooms without a wall costs one monetary unit, and moving between two rooms that had a wall which was demolished costs p monetary units.

# Task
Determine the minimum cost of moving from the **director's** room to the **chief editor's** room. Among all the minimum-cost routes, determine the minimum number of walls that need to be demolished in such a route.

# Input data
The input file `ziduri.in` contains on the first line `n` (the number of rooms on a line, respectively column) and `p`, the cost of moving from one room to another between which the dividing wall was demolished; the two numbers are separated by a space. On the next `n` lines there are `n` natural numbers from the set `{0,1,…,15}` separated by a space. These natural numbers transformed into base `2` (on `4` bits) give us information about the existence of walls around the room (`1` for wall and `0` otherwise). For example, if such a number has the representation `abcd` in base `2`, then `a` is for the west wall, `b` for the north wall, `c` for the east wall, and `d` for the south wall.

# Output data
The output file `ziduri.out` will contain on the first line the minimum cost of moving from **director** to **chief editor**, and on the second line the minimum number of walls demolished.

# Constraints and clarifications
* `1 < n < 101`
* `0 < p < 101`
* Partial scores are not awarded.

# Example

`ziduri.in`
```
4 3
9 1 1 0
12 5 5 1
1 5 5 4
4 6 12 0
```

`ziduri.out`
```
8
1
```

Explanation
---

The configuration of the editorial offices (the walls are marked with thick lines)
~[ziduri2.png]
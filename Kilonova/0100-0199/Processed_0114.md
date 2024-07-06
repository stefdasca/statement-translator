Renowned architect Prăbușilă wants to build one of the most interesting towers on the planet. This tower will have floors of various widths, between `1` and `100`, integer numbers.

Prăbușilă has already decided the size of each floor of the tower, but not how to arrange them horizontally. He first wants to know how many variants there are.  
~[turnuri.png]  
The floors can be placed at integer coordinates and such a tower must not collapse.
* The condition for a tower to be stable is that at each floor the perpendicular dropped from the center of gravity of the group of upper floors must fall strictly within that floor (it cannot be on the edges or outside - for example, towers `2` and `3` are unstable).
* The center of gravity of a floor is in the middle of that floor.
* The center of gravity of a group of floors has the `x` coordinate (horizontal) as the average of the `x` coordinates of the centers of gravity of the component floors. (The floors have equal masses, regardless of how wide they are).

In example `1`, the top floor has the `x` coordinate of the center of gravity `2`, and the group of the `2` top floors has its center of gravity at coordinate `x=1.75` (the arithmetic mean between `2` and `1.5`)

It is observed in figure `1` that although the perpendicular from the center of gravity of floor `2` falls outside floor `1`, the tower is still stable because the perpendicular from the center of gravity of the group formed by floors `2-8` falls strictly within floor `1`.

# Task
Determine how many stable towers exist.

# Input data
The input file `turnuri.in` contains a single line with a list of natural numbers separated by a space, numbers representing the widths of the tower's floors, starting with the topmost. The list ends with a `0`.

# Output data
The output file `turnuri.out` contains the number of towers.

# Constraints and clarifications:
- the maximum number of towers will not exceed `2\ 000\ 000\ 000`
- the maximum number of floors of a tower is `200`
- the maximum width of a floor is `100`

# Example:

`turnuri.in`
```
1 3 4 1 0
```

`turnuri.out`
```
6
```

The `6` variants are:
~[turnuri2.png]
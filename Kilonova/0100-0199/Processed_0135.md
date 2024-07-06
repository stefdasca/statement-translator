The Hedgehog Gălușcă is an ordinary hedgehog by day. At night, however, he is the mysterious hero of the city of Hedgytown—a unique city, since it has buildings both above the ground and underground, where gravity is inverted.

The city can be viewed as a line (representing the ground), with a series of rectangular buildings attached above the ground, and a series of rectangular buildings attached below the ground. There are `N` buildings above ground and `M` below ground. The two series start and end at the same positions. Each building is characterized by three values: `L, H`, and `E`. `L` represents the width of the building, `H` represents the height of the building, and `E` represents the effort required to use the elevator in that building.

Initially, Gălușcă was on the left side of the city, at ground level (in front of the first building) and must reach the right side of the city, also at ground level (in front of the last building). To achieve this, he can move along the outlines of the buildings, consuming one unit of effort to move one unit along the outline of a building—or by using the elevators.

Elevator movement is always from the outline of one building *to the outline of the building on the other side of the ground*—in other words, when using the elevator, the hedgehog is not allowed to stop at ground level or to stop inside the building. If the building where the hedgehog is located requires an effort of `E` to use the elevator and the building on the opposite side of the ground requires an effort of `E'`, then the total effort needed to use the elevator is `E + E'`.

Elevator movement is performed vertically. Thus, the elevator will leave Gălușcă at the same horizontal distance from the beginning of the city, but on the roof of the opposite building. The elevator cannot be used where two adjacent buildings meet horizontally—neither if they meet on the side of the ground where the movement starts, nor if they meet on the side of the ground where the movement ends. *Attention, since Gălușcă is a hero, he will never go back—he only moves forward or uses the elevators.*

# Task
Find the minimum number of effort units that the hedgehog Gălușcă needs to reach his destination.

# Input data
The first line of the input file `superhedgy.in` contains `N`, representing the number of buildings above the ground.
The next `N` lines of the input file contain `L, H`, and `E`, representing the data of the buildings above the ground, in the order in which they are positioned in the city, starting with the nearest building to Gălușcă.
The `N + 2` line of the input file contains `M`, representing the number of buildings below the ground.
The next `M` lines of the input file contain `L, H`, and `E`, representing the data of the buildings below the ground, in the order in which they are positioned in the city starting with the nearest building to Gălușcă.

# Output data
The output file `superhedgy.out` will contain a single natural number, representing the minimum number of effort units that Gălușcă needs to reach his destination.

# Constraints and clarifications
* `1 \leq N, M \leq 100\ 000`
* `1 \leq L, H \leq 1\ 000\ 000\ 000`
* `0 \leq E \leq 1\ 000\ 000\ 000`
* The total lengths of the buildings above and below the ground coincide. Let $L_{\text{Total}}$ be this total length.
* For `20` points: $1 \leq L_{\text{Total}} \leq 10$
* For another `20` points: `E = 0` for all buildings in the city, $1 \leq L_{\text{Total}} \leq 100\ 000$
* For another `40` points: $1 \leq L_{\text{Total}} \leq 100\ 000$
* For another `20` points: Without additional constraints

# Examples

`superhedgy.in`

```
3
1 2 5
3 1 1
2 3 1
4
1 4 10
2 3 1
1 2 1
2 1 1
```

`superhedgy.out`

```
13
```

Explanation
---

The city will look like the picture below:
\
~[superhedgy1.png]
A possible path for the hedgehog will be as follows:
\
~[superhedgy2.png]
\
*Attention!* Elevator movement could not have been performed further to the left or right by `0.5` units.
Emperor Kaktus the wicked has possession of the Magic Barrel and has flooded the Enchanted Forest! The Painter and the three small hedgehogs must now return to the Beaver's Den to take shelter from the water as quickly as possible!

The map of the Enchanted Forest is made up of $L (1 \le L \le 500)$ rows and $C (1 \le C \le 500)$ columns, resembling a matrix. Dry regions are represented by the character `.`, flooded regions by `*` and rocks by `X`. Additionally, the Beaver's Den is represented with `D`, and the Painter, along with the three small hedgehogs, are represented by `S`. The Painter and the three small hedgehogs are always in the same region and do not separate from each other.

Each minute, the Painter and the three small hedgehogs can move to 4 neighboring dry regions (up, down, left, or right). Also, each minute, the flood extends, and all dry regions that share at least one side with a flooded region will be flooded. Neither the water nor the Painter and the three small hedgehogs can pass through rocks. Of course, the Painter and the three small hedgehogs cannot pass through flooded regions, and water cannot flood the Beaver's Den.

**Note**: The Painter and the three small hedgehogs cannot move into a region that is about to be flooded (in the same minute).

# Task
Write a program that, using a map of the Enchanted Forest, will find the shortest time needed for the Painter and the three small hedgehogs to safely reach the Beaver's Den. If $T$ has the value 1, the first requirement will be solved, and if $T$ has the value 2, the second requirement will be solved.
1. For this requirement, it is guaranteed that there are no flooded regions.
2. For this requirement, there will be at least one flooded region.

**Note:** Input data is read from the keyboard, and output data is displayed on the console.

# Input data
The first line of input will contain a number $T$ equal to $1$ or $2$.
The second line of input will contain two natural numbers, $L$ and $C$.
The next $L$ lines contain each $C$ characters (`.`, `*`, `X`, `D`, `S`).

# Output data
Print on the first line the minimum time in which the Painter and the three small hedgehogs can safely reach the Beaver's Den. If there is no path that meets the task's conditions, print the word `KAKTUS` on the first line.

# Constraints and clarifications
- For tests worth 30 points, $T = 1$.
- For other tests worth 40 points, $1 \le L \le 50 \ ; \ 1 \le C \ \le 50$.
- For the remaining 30 points, there are no other constraints.

# Example 1

`stdin`
  ```
1
3 3
D..
...
..S
  ```
  `stdout`
  ```
4
  ```

# Example 2
  `stdin`
  ```
2
3 3
D.*
...
.S.
  ```

  `stdout`
  ```
3
  ```

# Example 3

`stdin`
  ```
2
3 3
D.*
...
..S
  ```
  `stdout`
  ```
KAKTUS
  ```

# Example 4

`stdin`
  ```
2
3 6
D...*.
.X.X..
....S.
  ```

  `stdout`
  ```
6
  ```


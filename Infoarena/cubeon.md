## Task 

The $K$ (with $K \geq 1$) members of the Light Cubing Club want to move to Cube Street. On this street, there are $N$ (with $1 \le N$) adjacent buildings, each with a certain width. The $K$ members will each buy consecutive sequences of buildings (which are pairwise disjoint), demolish them, and build a house on the ground from those buildings. For obvious reasons, members really love cubes and therefore will build each house in the shape of a cube, whose edge length is equal to the total width of the buildings that were demolished to make space for that house. Also, they do not want to live next to those who do not share their love of cubes, so they want each building to be bought by a single member of the club. While the members are not poor, they are not made of money (unlike cubes, of course). So they would like to know the minimum total costs that can be paid to construct the buildings. Notice that the cost to construct a building whose edge length is $x$ units is $x^3$. 

## Input data

The input file `cubeon.in` contains the first line and it will contain the number $T$, the number of tests. Each test will contain two lines. The first line will contain $N$ and $K$. The second line will contain $N$ non-negative integers whose sum will not exceed $1\ 000\ 000$, the widths of the $N$ buildings.

## Output data

The output file `cubeon.out` will contain the answers for each test in order. For each test, obtain the minimum total cost.

## Constraints and clarifications

$1 \leq T \leq 20$

$1 \leq N$

$K \leq 1\ 000\ 000$

## Example

`cubeon.in`

```
1
8 3
1 2 1 3 1 4 3 2
```

`cubeon.out`

```
593
```

Please double-check the grammar to ensure that it adheres to the rules of the English language.
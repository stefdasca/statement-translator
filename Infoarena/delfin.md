## Task

The dolphin is actually a turtle. Naming maintained for legacy reasons. Teognis, recently in high school, started developing paranormal powers. More precisely, he can telepathically control the school's mascot turtle, Percy. Somehow transported into the mystical world of turtles, he now wants to capture the magical turtle treasure. The turtle world can be modeled as a matrix with $N$ rows and $M$ columns, where each cell contains either land or water. Teognis and Percy move according to the following rules:
- It takes both Teognis and Percy one unit of time to move from one cell to an adjacent orthogonal cell (i.e., a neighboring cell in one of the four cardinal directions).
- They are allowed to move simultaneously.
- Percy will permanently stay on water cells.
- Teognis can travel alone only on land cells.
- Teognis can travel on water if he is on Percy's back.
- To climb onto Percy's back, Teognis must move to a water cell where Percy is already present or moves at the same time. Analyze the first example for clarifications in this regard.
- To get off Percy's back, Teognis must step onto a land cell adjacent to the current position. He can climb onto and get off Percy as many times as he wants. The magical turtle treasure is somewhere on land. What is the minimum time required for Teognis to reach the cell with the treasure?

## Input data

The input file `delfin.in` contains:
- The first line contains $N$ and $M$, 2 integers representing the dimensions of the matrix that represents the turtle world.
- The next $N$ lines will each contain $M$ characters, representing the matrix of the turtle world. Each cell in the matrix contains a character, with their meanings as follows:

Character | Meaning
--- | ---
1 | Land
0 | Water
S | Teognis (appears only once)
F | Treasure (appears only once)
D | Percy (appears only once)

## Output data

The output file `delfin.out` will contain a single number, the minimum time to reach the treasure.

## Constraints and clarifications

$1 \leq N, M \leq 1000$

For 15 points it is guaranteed that $N = 1$

For another 35 points it is guaranteed that $1 \leq N, M \leq 50$

The cells initially containing Teognis and the treasure contain land.

The cell initially containing Percy contains water.

It is guaranteed that the treasure is always reachable.

You will receive evaluation results only on the example input files. These will not affect the problem's score, having a score of 0.

## Example

`delfin.in`

```
1 4
S0DF
```

`delfin.out`

```
3
```

`delfin.in`

```
7 5
S1100
0010 
0010
0000
D000
00F
```

`delfin.out`

```
10
```

`delfin.in`

```
13 8
S1111111
00000001
11111101
10000001
10111111
10100000
10111111
10000001
11111101
00000101
11111101
1D000000
1111111F
```

`delfin.out`

```
29
```

## Explanation

In the first example, Percy will move towards Teognis by one cell, and at the same time, Teognis will climb onto his back. Then Percy will move one cell towards the treasure, and Teognis will use another unit of time to get off Percy exactly in the cell with the treasure.

In the second example, Teognis will climb onto Percy at cell $(4, 3)$, and it will take him 5 units of time to do this (Percy, being at distance 3 from this cell, can be present at the meeting point already at time 3). Then they will travel together for another 5 units of time until Teognis gets off directly onto the cell containing the treasure.
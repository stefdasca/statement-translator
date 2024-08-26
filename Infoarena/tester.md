## Task

Paraschiva is a game tester. The last game she is testing has $N$ states and $M$ buttons that define certain actions. Each button changes the game's state from a certain state $x$ to $y$. Paraschiva knows from the game creators that any two buttons $(x, y)$ and $(y, z)$ pressed consecutively produce a special combo (the second button must necessarily affect the state in which the game is left by the first button). Paraschiva has to test all possible combos that can appear in the game. To do this, she proceeds as follows: she starts from any game state and begins pressing buttons to discover the effects of the combos. She can also reset the game at any time, that is, she can restart from any state she wants. Paraschiva gets bored quickly, so she wants to test the game in the most enjoyable way possible: she wants to produce a series of button presses and resets such that every possible combo appears in the sequence exactly once, and the total number of game resets is minimal.

## Input data

The input file `tester.in` contains on the first line two integers, $N$ and $M$. The next $M$ lines each contain two integers: line $i+1$ contains $x$ and $y$ representing the fact that button $i$ changes the game state from $x$ to $y$. 

## Output data

The output file `tester.out` will contain a single line describing the states through which the game passes in Paraschiva's sequence. Any reset is marked with an $R$. To better understand the output file format, study the example and explanation.

## Constraints and clarifications

$1 \leq N \leq 500$

$1 \leq M \leq 5000$

There won't be two buttons with the same effect (i.e., having the same pair $(x, y)$).

Button $(x, y)$ is different from button $(y, x)$.

Any solution that meets the conditions in the statement will get full marks on the respective test.

The undirected graph determined by states as nodes and buttons as edges is connected.

## Example

`tester.in`
```
5 5
1 2
2 3
3 5
5 4
2 4
```

`tester.out`
```
1 2 3 5 4 R 1 2 4
```

`tester.in`
```
4 7
1 2
2 3
3 2
1 4
4 3
3 1
4 3
```

`tester.out`
```
1 4 3 1 4 3 1 4 3 4 R 2 3 1 2 3 4 3 2 3 2
```

## Explanation

For the first example, the buttons pressed are $(1, 2)$ $(2, 3)$ $(3, 5)$ $(5, 4)$ - $(1, 2)$ $(2, 4)$. It can be observed that every possible combo appears in the sequence exactly once ($(1, 2)$ is a button, not a combo so it can appear multiple times). Note, the displayed values are the game states and not the buttons; the buttons are implicitly determined by two consecutive numbers in the sequence.
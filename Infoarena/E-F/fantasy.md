# Fantasy

Many, many years ago in the Great Kingdom of Cluj lived a famous wizard, a dragon, and a knight with an enchanted sword in a balance ready to vanish. The three did not get along at all, but none were strong enough to defeat the other two. Thus, the wizard could at any moment use his magic to kill the knight. The knight, in turn, could at any moment with a strike of his enchanted sword kill the dragon, and the dragon, being completely immune to the wizard's magic, could at any time devour him. None of the three dared to eliminate the one they could defeat because they would then be powerless against the remaining one. For example, if the wizard tried to get rid of the knight, the dragon could get rid of him. One day, however, the wizard, by sheer luck (or perhaps misfortune), managed to teleport himself, the dragon, and the knight into a labyrinth in the form of a tree (an undirected, connected, acyclic graph), where the rooms of the labyrinth are the nodes of the tree, and a connection between two rooms represents an edge of the tree. From that moment on, each second, each of the three characters either moved to an adjacent cell to the one they were in the previous second or stayed in place. If at any point two of the three characters meet, the stronger one instantly kills the other, regardless if they meet in a room or on a connection. Thus:
- The dragon each second moves to the room closest to the wizard to devour him.
- The knight each second moves to the room closest to the dragon to kill him. If the dragon was already dead, he would no longer move because the wizard will catch and defeat him anyway.
- The wizard, observing how the dragon and the knight move, planned the best strategy so that in the end, only he would be alive. Unfortunately, as clever as the wizard was, he didn't understand trees, so he asks you to quickly tell him if he can be the only survivor in the end, so in case otherwise, he can try to teleport out of the labyrinth.

## Task

The input file `$fantasy.in$` contains on the first line the value $T$ representing the number of tests in the file. A test has the following structure: Its first line contains 4 natural numbers $N$, $D$, $C$, $V$ representing the number of rooms in the labyrinth, and the indices of the rooms where the Dragon ($D$), Knight ($C$), and Wizard ($V$) are located. The next $N - 1$ lines will contain two values each, $x$ and $y$, indicating that there is a connection between the rooms with indices $x$ and $y$. These $N - 1$ connections will describe a tree.

## Output data

The output file `$fantasy.out$` must contain on the first and only line "DA" (The quotation marks are just for clarity) if the wizard has a chance to be the only survivor at the end, or "NU" otherwise.

## Constraints and clarifications

$1 \leq T \leq 100$

$1 \leq N \leq 1000$

$1 \leq D, C, V, x, y \leq N$

$D ≠ C$

$D ≠ V$

$C ≠ V$

The Dragon, Knight, and Wizard move simultaneously in the labyrinth

If the 3 meet in the same node at the same second, then all 3 will die

For 30 points tests

$1 \leq N \leq 200$

$1 \leq T \leq 30$

## Example

`fantasy.in`
```
3
4 2 4 3
1 3
2 3
3 4
4 3 4 1
1 2
2 3
3 4
3 1 3 2
1 2
2 3
```
`fantasy.out`
```
DA
NU
NU
```

## Explanation

In the first example, the wizard is trapped between the dragon and the knight but notices that he can move to room 1. Thus, after one second, the dragon and knight meet in room 2 where the knight will defeat the dragon. From this moment, the knight has no chance (because he is left alone with the wizard), and the wizard will certainly be the only one left alive in the end.

In the second example, no matter what the wizard does, he will be caught by the dragon.

In the third example, the wizard is trapped between the two and can either choose to move towards the knight, killing him and remaining alone with the dragon, or stay in place and all 3 will be in the same node and perish.
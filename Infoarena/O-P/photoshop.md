## Task

It has already been two weeks since you joined Adobe's Photoshop team. The acclimatization period is almost over, and the time has come for you to work on your first piece of production code. Initially, you need to develop a new content selection tool that operates as follows: the user indicates a selection rectangle over the content on the canvas, and the rectangle is automatically minimized so that its area is minimal while still covering all the content indicated by the user. To better understand how the tool should work, you have received the following diagram:

Legend:
- blue: content on the canvas
- red: selection rectangle indicated by the user
- green: rectangle after it has been automatically minimized

For testing the tool, the user has only the following actions available:
- Adding a point on the canvas
- Deleting a point from the canvas
- Indicating a selection rectangle

Given all user actions, for each selection action, calculate the rectangle with the minimum area that covers the same content as the given rectangle.

## Input data

The input file `photoshop.in` contains on the first line a number $N$ representing the number of user interactions with Photoshop. The following $N$ lines describe the user's actions as follows:
- $0 \ X \ Y$: adds the point $(X, Y)$ on the canvas
- $1 \ X \ Y$: deletes the point $(X, Y)$ from the canvas
- $2 \ A \ B \ C \ D$: activates the new selection tool on the rectangle that has its top-left corner and bottom-right corner at the points $(A, B)$ and $(C, D)$ respectively

## Output data

The output file `photoshop.out` will contain one line for each type 2 action (activating the selection tool) in the order they appear in the input file. Each line will describe the minimized rectangle by its top-left corner and bottom-right corner in the same format as specified in the input file. If the selection rectangle does not contain any points, then it will display "-1" (without quotes).

## Constraints and clarifications

$2 \leq N \leq 100000$

$0 \leq X, \ Y, \ A, \ B, \ C, \ D \leq 100000$

The coordinates are natural numbers

## Example

`photoshop.in`
```
9 
0 2 2 
0 4 4 
0 5 3 
2 1 5 6 
1 0 6 6 
2 1 5 6 
1 0 3 3 
1 2 2 
2 1 7 6 
```

`photoshop.out`
```
1 4 5 3 
-1 
5 3 5 3 
```


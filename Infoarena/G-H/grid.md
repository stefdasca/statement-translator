## Task

The owl Owly wants to intern at a startup, and the engineers there gave him a problem to solve at the interview. You are given a grid with $3$ rows and $N$ elements in each row. Then you have $K$ operations of the type "move" the widget numbered $W$ from position $(X_1, Y_1)$ to position $(X_2, Y_2)$. With each move, all widgets that were to the right of the initial position in the grid are shifted one unit to the left, and the widgets that are to the right in the new position are shifted one unit to the right. To better visualize the operation of moving a widget, we offer you the following test page. The final configuration of the widgets should be displayed after the $K$ operations.

## Input data

The file `grid.in` will contain on the first line two numbers $N$ and $K$. 

$N$ represents the number of widgets that are initially on each row. 

$K$ represents the number of moves to be executed. 

On the next $K$ lines, there will be four numbers, the first two $(X_1, Y_1)$ represent the position where a widget is, and the next two $(X_2, Y_2)$ represent the position to which that widget will be moved.

## Output data

In the output file `grid.out` the final configuration of the grid will be printed. 

## Constraints

$1 \leq N \leq 10000$ 

$0 \leq K \leq 150000$ 

$0 \leq X_1, X_2 \leq 2$ 

$0 \leq Y_1, Y_2 \leq N \cdot 3$ 

## Example

`grid.in` 
```
4 0 
1 2 3 4 5 6 7 8 9 10 11 12 
```

`grid.out`
```
4 1 2 3 
0 0 12 
1 2 3 4 5 6 7 8 9 10 11 
```
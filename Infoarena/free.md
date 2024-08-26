Free

At the Happy Prison, the director has not had an incident with his inmates for a very long time. Therefore, he decided to release some of them following a game. In the prison, there are $N$ cells. The door of each cell is controlled by a button that switches its state (if it is closed, it opens, and if it is open, it closes). Initially, all doors are closed, and $N$ steps will be performed. At each step $i$, the director will count from $i$ to $i$ and press the button in front of the door he stops at. At the end, he will release the inmates from the cells that remain open.

## Task

Given $N$, the number of cells in the Happy Prison, calculate the number of unhappy inmates who remain in their cells.

## Input data

The input file `free.in` contains $N$, the number of cells in the Happy Prison.

## Output data

The output file `free.out` will contain $X$, the number of inmates who will remain locked.

## Constraints and clarifications

$1 \leq N \leq 10 \, 100$

## Example

`free.in` `free.out` 
`6` `4`

## Explanation

At step $1$, the guard will press the buttons of cells $1, 2, 3, 4, 5, 6$.

At step $2$, the guard will press the buttons of cells $2, 4, 6$.

At step $3$, the guard will press the buttons of cells $3, 6$.

At step $4$, the guard will press the button of cell $4$.

At step $5$, the guard will press the button of cell $5$.

At step $6$, the guard will press the button of cell $6$.

In the end, only the doors of cells $1$ (the button was pressed once) and $4$ (pressed $3$ times) will remain open.
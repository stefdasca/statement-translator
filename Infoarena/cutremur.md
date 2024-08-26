## Earthquake

After having a Guinness in the Valley of the Kings, Georgel moved on to truly serious problems. The problem is as follows: Let there be $N$ balls placed in an infinite grid, each in a distinct cell. Ball $i$ is initially in cell $(x_i, y_i)$. We will move each ball $i$ a distance of $d_i$ cells in one of the directions left, right or down. Find a way to move the balls so that in the end all balls are in distinct cells. Georgel demonstrated that a solution exists for any configuration. Unfortunately, the demonstration is incorrect, so your task is to find a configuration for which there is no solution and make him aware of it.

## Input data

There is no input data!

## Output data

In the output file `cutremur.out` there will be the configuration for which it is not possible to move the balls in a valid way. The first line will contain an integer $N$ representing the number of balls. The next $N$ lines will each contain 3 integers, representing $x_i$, $y_i$ and $d_i$.

## Constraints and clarifications

$1 \leq N \leq 10^4$

$1 \leq x_i, y_i, d_i \leq 10^9$

The coordinates of the balls must be distinct.

A ball located in cell $(x_i, y_i)$ can move to one of the cells $(x_i + d_i, y_i)$, $(x_i - d_i, y_i)$ or $(x_i, y_i - d_i)$.

The constraints for the coordinates of the balls apply only to their initial positions, not to the final ones.

The balls are all moved simultaneously.

## Example

`cutremur.in`

`cutremur.out`

3

1 1 10

11 1 10

1 7 6

## Explanation

The example is just to illustrate the format, it is not a valid answer.
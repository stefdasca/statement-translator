Inspired by the famous Perspico, Miruna is thinking about the following game: you have a matrix with $N$ rows and $M$ columns where each number between $0$ and $N \cdot M - 1$ appears exactly once. A valid move in this game consists of swapping the element $0$ with one of its $4$ neighbors. Miruna wins if she manages to bring the matrix to the following configuration:

* At any position $(x, y)$, except for the position $(N, M)$, the value $(x - 1) \cdot M + y$ must be found;
* At the position $(N, M)$, the value $0$ must be found.

# Task

Given a configuration of the game, help Miruna finish it, and she will reward you with a kiss ;).

# Input data

The first line of the input file `perspico.in` contains $2$ integers $N$ and $M$, having the significance from the statement. The next $N$ lines will contain $M$ natural numbers each, representing the elements of the matrix.

# Output data

In the output file `perspico.out`, multiple natural numbers from the interval $[1, 4]$ will be written, representing the moves made, with the following codification:

* $1$ – If the element $0$ is swapped with the one above it.
* $2$ – If the element $0$ is swapped with the one to its right.
* $3$ – If the element $0$ is swapped with the one below it.
* $4$ – If the element $0$ is swapped with the one to its left. 

# Constraints and clarifications

* $2 \leq N, M \leq 64$
* If there exist multiple solutions, any one of them can be displayed.
* It is guaranteed that there is at least one solution in all the test files.

# Example

`perspico.in`
```
3 3
0 1 3
4 2 6
7 5 8
```

`perspico.out`
```
3
```

## Explanation

The moves made will be in the following directions: `E`, `S`, `S`, `E`. 
After performing them, the matrix will look like this:
```
1 2 3
4 5 6
7 8 0
```
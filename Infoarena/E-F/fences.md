# Fences

You found an android that appears to be designed for building fences. Excellent, as you don’t particularly like people, a new fence wouldn’t hurt, no matter where it is. The android can move in the directions $L =$ left, $R =$ right, $U =$ up, and $D =$ down. With each move executed, it moves one meter in the chosen direction and adds a segment of a fence between its new position and its old position. Unfortunately, the android does not seem to be reprogrammable, all you can do is reorder the instructions already present in its memory. You cannot add or remove new commands. You are now wondering what is the maximum area of a figure that the android can completely enclose. For example, if you find the commands $LRUD$ in the android's memory, you can enclose a square of area $1$ if you give the commands the order $LURD$. If you do not modify the program, it encloses an area of $0$. Generally, it is not necessary for the android to return to its initial position after executing the commands.

## Task

## Input data

The input file `fences.in` will contain on its first line the number of tests $T$. The following $T$ tests, each containing a string of characters from the set $\{'L', 'R', 'U', 'D'\}$.

## Output data

The output file `fences.out` will contain $T$ numbers, the answer for each test.

## Constraints and clarifications

$1 \leq T \leq 100$

$1 \leq$ The length of the command string $\leq 200\,000$

The total number of commands in the same file is at most equal to $2\,000\,000$.

## Example

`fences.in`
```
3 
LLLR 
LLRUD 
LRLDDDUURLRLRUDRL
```
`fences.out`
```
0 
1 
15 
```

~[name.png|some attribute]
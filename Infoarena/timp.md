# Time

We have at our disposal a rather unusual hourglass that is used to measure a certain period of time. This hourglass is unique in that it does not only have two compartments where the sand can collect, but three. The hourglass rests on two of these compartments, while the sand flows equally from the third one into the other two. Initially, all the sand is collected in a single compartment, and with it, we can measure, let's say, $16$ minutes, as in figure $1a)$. To measure $7$ minutes in one of its compartments, we can rotate the hourglass $120$ degrees clockwise or counterclockwise. We consider that a right rotation is performed in the clockwise direction, and a left rotation is performed counterclockwise. For example, by rotating to the right, we get figure $1b)$, where both compartments contain sand to measure $8$ minutes. Rotating to the left, we get $4$ and $12$. Rotating to the right, we get $14$ and $2$, then rotating to the right again, we get $9$ and $7$. Thus, we have obtained $7$ in one compartment, and we can measure this time.

## Task

Write a program that determines a series of rotations to measure a specific time interval.

## Input data

The input file `timp.in` contains two integers $N$ and $K$ separated by a space. $N$ represents the time that can be measured initially, with all the sand in the bottom left (as in the example). $K$ represents the time we want to obtain in one compartment. It does not matter where the sand for measuring the final time is located.

## Output data

The output file `timp.out` should contain on the first line the number of rotations needed to obtain the required amount of sand. On the following lines, it should contain one value each representing the rotations in the order they were performed. For a left rotation, write $0$, and for a right rotation $1$.

## Constraints and clarifications

$2 \leq K$  
$K \leq N$  
$N \leq 200\ 000\ 000$  
the solution is not unique, and the number of rotations does not need to be minimal  
after a rotation, all the sand in the top compartment must flow down  

## Example

`timp.in`  
```
16 7
```

`timp.out`  
```
4
1
0
1
1
```
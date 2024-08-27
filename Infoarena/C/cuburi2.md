## Task

Laura and Robert are playing with blocks. Robert has built $N$ towers in a straight line and knows the height of each one. To move a block from one tower to a neighboring tower costs one unit of time. Now, he is asking Laura $M$ questions like this: "What is the minimum time required to move all the blocks in the interval $x$ $y$ into a single existing tower?" Of course, he is also interested in which destination tower should be chosen in such a case. Laura could easily answer these questions using her female intuition, but she decided to save it for other occasions. Therefore, you will have to answer Robert's questions.

## Input data

The first line of the input file `cuburi2.in` contains the numbers $N$ and $M$. The next line contains $N$ numbers, representing the heights of the towers. The following $M$ lines contain two numbers $x$ $y$, each pair represents a question asked by Robert.

## Output data

The output file `cuburi2.out` will contain $M$ lines, on each line the answer to one of Robert's questions. The order of the answers must match the order in which the questions were asked. The answers will be displayed in the form $P$ $Cost$, where $P$ represents the position of the destination tower for the respective question, and $Cost$ is the minimum time required to move all the blocks to that tower.

## Constraints and clarifications

$1 \leq N \leq 250\,000$

$1 \leq M \leq 250\,000$

The heights of the towers are integers in the range $[0, 1\,000\,000]$

For 20% of the tests $N, M \leq 250$

For 50% of the tests $N, M \leq 5\,000$

40% of the points are awarded if you only determine the correct final position for all questions. However, in this case, you will still need to display a value for the minimum time, even if incorrect, to respect the output data format.

If there are multiple optimal positions for the destination tower, any will be considered correct.

## Example

`cuburi2.in`

```
5 4
1 3 7 2 5
1 5
1 3
3 5
1 2
```

`cuburi2.out`

```
3 17
3 5
4 12
2 1
```

## Explanation

For the first question, the destination tower is at position $3$. The time required to move the remaining blocks to this position is $2*1 + 1*3 + 1*2 + 5*2 = 17$.

For the third question, another possible final position is $3$, which gives the same minimum time $12$.
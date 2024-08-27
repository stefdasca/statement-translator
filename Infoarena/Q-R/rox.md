Rox

Rox's parents recently bought a plot of land that is $N$ meters wide and $M$ meters long, which they divided into 1-meter side squares, called cells. When seeing the land plan, Rox had an idea. She decided to plant her favorite flowers in stages on $U$ of the land parcels. The flower names are uppercase letters of the English alphabet. A parcel is a rectangle included within the land, with sides parallel to those of the land and containing only complete cells. In each stage in which Rox plants flowers, she proceeds as follows: she chooses a parcel for which she notes the indices of the cells from the top left and bottom right, determines the type of flower she wants to plant throughout the parcel, then writes this information on a piece of paper. After doing research online, Rox comes to the conclusion that the following strange phenomenon occurs: if the same type of flower is planted in a cell an even number of times, the seeds of that type simply disappear. When she finishes planting, Rox tells her parents about her endeavor. Enthusiastic, her parents ask several questions such as "How many types of flowers are left planted in the cell on row $L$ and column $C$?".

## Task

Because Rox planted many flowers, she cannot quickly answer her parents' questions, so she asks for your help and will reward your effort with up to 100 points.

## Input data

The first line of the `rox.in` file contains 3 numbers: $N$, $M$, and $U$, separated by a space and having the meaning from the statement. On each of the next $U$ lines there will be: $L1$ $C1$ $L2$ $C2$ $T$, separated by a space and representing the data written by Rox on the paper, corresponding to a planting stage (the coordinates of the top left and bottom right corners of the parcel and $T$, the type of flower). On line $U+2$ there is $Q$, the number of questions asked by Rox's parents. On each of the next $Q$ lines, there are $L$ $C$ (the coordinates of the cell about which Rox's parents want information).

## Output data

The output file `rox.out` will contain $Q$ lines. On each of these $Q$ lines, there will be the answers to the questions from Rox's parents, in the order in which they were asked.

## Constraints and clarifications

$1 \leq N$, $M \leq 1000$  
$1 \leq U \leq 100000$  
$1 \leq Q \leq 100000$  
$L1 \leq L2$  
$C1 \leq C2$  
Initially, no flowers were planted on the land.  
$T$ represents an uppercase letter of the English alphabet.  
The questions can repeat.  
The input data does not require validation.  
For 15% of the tests $U \times Q \leq 3.000.000$  
For 35% of the tests $N$, $M \leq 100$, $U \leq 300$  
For 60% of the tests $N$, $M \leq 800$  

## Example

`rox.in`
```
14 17 6
3 3 8 10 A
5 6 11 14 B
8 2 11 3 W
6 8 12 17 B
8 5 14 8 A
2 13 2 14 Z
4
4 5
7 9
5 10
8 3
```

`rox.out`
```
1
1
2
2
```

## Explanation

In the cell $(4,5)$, flower $A$ is planted and remains there. In the cell $(7,9)$, flower $A$ is planted, then $B$, then $B$ again (in the second planting of flower $B$, the flower $B$ disappears). In the end, only $A$ remains. In the cell $(5,10)$, $A$ and $B$ are planted and remain there. In the cell $(8,3)$, $A$ and $W$ are planted and remain there. In the figure below, the cells corresponding to the questions are marked with ?.

~[example.png|alt=Rox example]
## Task

Venus has an infinitely large white sheet of paper on which they like to draw lines. Today, Venus wonders if they can draw $N$ lines such that the number of intersections between them is exactly $M$. And if so, what is the maximum number of regions (finite and infinite) in which the paper can be divided by the $N$ lines? An example of 5 lines with 8 intersections. The sheet is divided into 14 regions.

## Input data

The input file `intersect.in` will contain:
- The first line will contain the number $T$ representing the number of test cases.
- The following $T$ lines will each contain two numbers $N$ and $M$ representing the number of lines and the number of intersections, respectively.

## Output data

In the output file `intersect.out`, you will print $T$ numbers, each on a new line representing the answer to the $T$ questions: 0 if it is not possible to draw the $N$ lines such that they have exactly $M$ intersections, or otherwise, the maximum number of regions into which the paper can be divided.

## Constraints and clarifications

$1 \leq T \leq 100$  
$1 \leq N \leq 150$  
$0 \leq M \leq N * (N-1) / 2$  
For tests worth 70 points, $N \leq 100$  
Attention: Any 3 drawn lines are not concurrent.  
Attention: Any two lines do not coincide.  

## Example

`intersect.in`  
```
3
5 8
3 0
3 1
```

`intersect.out`  
```
14
4
0
```

## Explanation

The first test is the one from the image. The second test is with all 3 lines parallel. The third test is impossible because any 3 lines cannot be concurrent.
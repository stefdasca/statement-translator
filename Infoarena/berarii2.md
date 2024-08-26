# Berarii2

Berila has decided to move this summer to a new city with many beautiful beaches. Berila studied the city plan and selected $N$ intersections where he could stay, $M$ unidirectional streets between them, and $P$ breweries located at these intersections. After carefully analyzing the map, Berila realized that there are intersections from which he cannot reach any of the selected breweries, which he finds unacceptable. Therefore, he asks you to find the list of intersections from which he cannot reach any brewery.

## Input data

The input file `berarii2.in` contains on the first line the numbers $N , M, P$. 

Each of the next $M$ lines contains $X, Y$, indicating a road from intersection $X$ to intersection $Y$. 

On the last line, there are $P$ numbers, representing the intersections with breweries. 

## Output data

In the output file `berarii2.out` you will print on the first line $Q$, the number of intersections from which one cannot reach any brewery. 

Then, on each of the following $Q$ lines, print an intersection with this property. 

The intersections will be printed in sorted order. 

## Constraints and clarifications

$1 \leq N \leq 1\ 000\ 000$ 

$1 \leq M \leq 1\ 000\ 000$ 

$1 \leq P \leq 1\ 000$ 

$1 \leq X, Y \leq N$ 

## Example

`berarii2.in`
```
5 5 1
1 5
1 3
4 1
1 4
5 4
2
2 3
```

`berarii2.out`
```
2
2
3
```
# Egypt

In ancient Egypt, a pyramid will be built. Many stone blocks have been transported to the specified site and placed along a straight line. The stone blocks have been pre-processed to have three different sizes. The Pharaoh's chief constructor wants to minimize the effort required to build the pyramid, and thus he wants to arrange the stone blocks in increasing order of size.

## Task

Determine the minimum number of swaps of stone blocks that the Pharaoh's slaves will have to perform in order to arrange them in increasing order. Also identify the indices in the initial configuration of the stone blocks that will be swapped!

## Input data

The input file `egipt.in` contains in the first line the natural number $n$, representing the number of stone blocks. In the next $n$ lines, there is a natural number, representing the type of the stone block. Since there are three sizes, the type will be $1$, $2$, or $3$.

## Output data

The output file `egipt.out` will contain in the first line a natural number $m$, representing the number of swaps needed. In each of the following $m$ lines, one swap will be described, necessary to obtain the sequence of stone blocks ordered as follows: each line will contain two natural numbers $i$ $j$, with the significance that the block at position $i$ will be swapped with the block at position $j$.

## Constraints

$1 \leq n \leq 10\,000$

## Example

`egipt.in`
```
5
3
2
1
1
2
```

`egipt.out`
```
3
2 3
1 4
4 5
```
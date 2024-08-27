Roy-Floyd

## Task

Little Floyd lives in a big city with $N$ intersections. Each pair of intersections is connected by a bidirectional road with a given positive length. Little Floyd is a curious boy and would like to know what is the minimum distance someone would have to travel along the existing roads if they wanted to go from intersection $X$ to intersection $Y$. Since he likes intersections very much, he would also like to know, if there are multiple paths between $X$ and $Y$ of the same minimal length, what is the maximum number of streets someone could travel to obtain this minimal distance.

## Input data

The first line of the file `rf.in` contains the number of intersections $N$. The next $N$ lines contain $N$ integers each. The $j$-th number on the $i$-th line represents the length of the road between intersections $i$ and $j$. The given matrix is symmetric. The intersections are numbered with integers from 1 to $N$.

## Output data

In the file `rf.out`, print two matrices of dimensions $N \times N$. Each matrix should be printed on $N$ lines, each containing $N$ integers, separated by a single space (no extra spaces at the beginning or end of the line). The first matrix represents the minimum road lengths between each pair of intersections. The second matrix represents the maximum number of streets that can be traveled to obtain the minimum distance between any pair of nodes. The $j$-th number on the $i$-th line represents, for each of the two matrices, the answer for the pair of intersections $(i, j)$.

## Constraints and clarifications
1 \leq $N$ \leq 256

The length of a road from an intersection to itself will always be 0

1 \leq length of a road \leq 100000

`rf.in`
```
5
0 2 3 4 5
2 0 4 5 1
3 4 0 1 2
4 5 1 0 3
5 1 2 3 0
```

`rf.out`
```
0 2 3 4 3
2 0 3 4 1
3 3 0 1 2
4 4 1 0 3
3 1 2 3 0

0 2 3 4 3
2 0 3 4 1
3 3 0 1 2
4 4 1 0 3
3 1 2 3 0
```
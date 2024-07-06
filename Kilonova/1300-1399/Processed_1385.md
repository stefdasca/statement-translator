~[stele.png|align=right]
The Country of Enchanted Numbers was a wonderful land! Even the stars in the sky were numbered with distinct positive natural numbers! The stars were part of the Numbers Constellation and were arranged in a triangular cluster, by columns and within each column by rows, as shown in the drawing to the right. The stars with numbers $1$, $3$, $7$, $13$, $21$, $31$, $\\dots$, situated on the row marked with a yellow star in the drawing, formed the **center of the star cluster**.
The columns in the cluster were numbered from left to right, starting with number $1$, and the rows within each column were numbered from bottom to top, starting with number $1$ (as in the drawing).
Legend says that, long ago, there lived in the Country of Enchanted Numbers an exceptionally evil and powerful witch. Everything that this witch touched with her magic wand turned into stone. She intended to turn all the children in the land into statues.
At that time, Numerel, a hardworking and brave boy, was studying at school. Everyone loved him! The Good Fairy decided to help Numerel. She promised the brave boy a magic wand, which Numerel could use against the witch. To receive the wand, Numerel collected the powder from the $K$-th star situated in the center of the cluster to give it to the Fairy.
But the adventure continued! The Fairy lived on the star with the number $N$, and Numerel had to find her address, specifically the column number, as well as the row number within the column, where this star was located.
Your adventure begins now!

# Task

Write a program that reads two natural numbers $K$ and $N$ and determines for Numerel:

1. the number of the $K$-th star situated in the center of the cluster;
2. the column and row (within that column) corresponding to the Fairy's address.

# Input data

The input file `stele.in` contains on the first line the two natural numbers, $K$ and $N$, separated by a space.

# Output data

The output file `stele.out` contains:

* on the first line, the natural number determined at point $a)$;
* on the second line, the column and row determined at point $b)$, in this order, separated by a space.

# Constraints and clarifications

* $0 \\lt K \\leq 60 \\ 000$;
* $0 \\lt N \\leq 60 \\ 000$;
* $20\\%$ of the score is awarded for the correct solution of task $1$;
* $80\\%$ of the score is awarded for the correct solution of task $2$.

# Example 1

`stele.in`
```
5 3
```

`stele.out`
```
21
2 2
```

## Explanation

The first $K = 5$ stars in the center of the cluster are numbered: $1$, $3$, $7$, $13$, $21$.
The star with the number $N = 3$ is located in column $2$, row $2$.

# Example 2

`stele.in`
```
2 5
```

`stele.out`
```
3
3 5
```

## Explanation

The first $K = 2$ stars in the center of the cluster are numbered: $1$, $3$.
The star with the number $N = 5$ is located in column $3$, row $5$.
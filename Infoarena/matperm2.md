Matperm2

Gigel has a matrix $V$ with $N$ rows and $M$ columns containing natural numbers, with the property that $V[x][y] = (x - 1) \cdot M + y$ for every $1 \leq x \leq N$ and $1 \leq y \leq M$. Due to boredom (there aren't many classes before the summer holiday), he decided to play with the matrix. Thus, he will take $P$ steps. In each step, he will shuffle the rows according to a given permutation $P1$. Then, he will shuffle the columns according to another permutation $P2$. After that, since the matrix is still not shuffled enough for Gigel's liking, he will take $Q$ pairs of positions $(x1, y1)$, $(x2, y2)$ and swap them, in the order they appear in the input file. Naturally, being impatient, he hasn't finished performing the $P$ operations and relies on you to tell him how the matrix will look after executing the $P$ steps.

## Input data

The first line of the input file `matperm2.in` will contain 3 numbers, $N$, $M$, and $P$ as described in the task. The second line contains the permutation $P1$, according to which the rows will be shuffled, and the third line will contain the permutation $P2$, according to which the columns will be shuffled. The next line contains a single natural number $Q$, and the next $Q$ lines will contain four numbers each $x1$, $y1$, $x2$, $y2$, representing a pair of positions to be swapped.

## Output data

The output file `matperm2.out` will contain $N$ lines. Each line will contain $M$ natural numbers, separated by a space, representing the elements of the matrix.

## Constraints and clarifications

$1 \leq N, M \leq 1\ 000$  
$1 \leq P \leq 2\ 000\ 000\ 000$  
$0 \leq Q \leq 1\ 000$  

The $Q$ operations are executed in each step!

## Example

`matperm2.in`  
```
3 4 1
1 3 2
1 2 4 3
0
1 2 4 3
```

`matperm2.out`  
```
9 10 12 11
1 2 4 3
5 6 8 7
```

## Explanation

Initially, the matrix is:  
1 2 3 4  
5 6 7 8  
9 10 11 12

After applying $P1$, the matrix becomes:  
1 2 3 4  
9 10 11 12  
5 6 7 8

After applying $P2$, the matrix becomes:  
1 2 4 3  
9 10 12 11  
5 6 8 7
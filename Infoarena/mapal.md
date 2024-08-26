## Task

The great engineer $NN$ has been appointed as the chief inspector of dams. On his first day of work, he receives a sector of a dam next to a reservoir that contains damages, and his mission is to devise a repair plan. Additionally, the repair costs must be minimized. The sector of the dam can be represented as a binary matrix of size $N \times N$. He observed that rows $l_1, l_2, \dots, l_k$ and columns $c_1, c_2, \dots, c_l$ are the only ones that have damages. To repair them, he needs to replace some elements in the matrix so that the damaged rows and columns become palindromes. Help $NN$ find the minimum number of replacements and prove that he is a master at dam repairs of all kinds.

## Input data

The first line of the file `mapal.in` will contain $N$, representing the width and length of the dam. The next $N$ lines will each contain $N$ characters, each character belonging to the set $\{0, 1\}$ and representing the element at row $i$ and column $j$ of the matrix that represents the dam. The next line will contain $L$, representing the number of damaged rows. The next line will contain $L$ numbers representing the indices of the damaged rows. The next line will contain $C$, representing the number of damaged columns. The next line will contain $C$ numbers representing the indices of the damaged columns.

## Output data

The single line of the file `mapal.out` will print the minimum number of replacements needed so that the given rows and columns become palindromes.

## Constraints and clarifications

$1 \leq N \leq 1000$ \\
The elements of the matrix belong to the set $\{0, 1\}$ 

## Example

`mapal.in`
```
4 
1011 
0111 
0000 
1010 
3 
1 2 4 
2 
1 4 
```

`mapal.out`
```
4 
```

## Explanation

One of the solutions for which rows $1, 2, 4$ and columns $1, 4$ become palindromes is:

```
1111 
0110 
0000 
1111 
```
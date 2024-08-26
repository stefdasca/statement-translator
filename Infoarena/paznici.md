## Task

After acquiring his plot of land, Vasilica wants to hire guards to take care of his crops. There are a number of points of interest in Vasilica's plot. More specifically, certain plants that Vasilica cares about a lot. The surface can be represented as a matrix of dimensions $N \times M$. Each element of the matrix belongs to the set $\{0, 1\}$. The value $1$ indicates the presence of a point of interest. The guards can be placed on the edge of the plot. They have visibility either along the entire row or the entire column in which they are positioned. The task is to determine the minimum number of guards necessary so that all points of interest are kept under observation. By making a map of the plot, Vasilica labeled the rows with uppercase letters and the columns with lowercase letters of the English alphabet. Additionally, he established an order relation: $A < B < \dots < Z < a < b < \dots < z$. After hiring the guards, Vasilica wrote down the positions where they are located and obtained a string of characters, for example: $BCET \, abd$. Based on these premises, our hero would like to find the first string of characters, in lexicographical order (the order presented above), from which an optimal placement of the guards results.

## Input data

The input file `paznici.in` will contain on the first line $N$ and $M$ representing the number of rows and columns of the matrix, respectively. The following $N$ lines will contain $M$ elements from the set $\{0, 1\}$ representing the elements of the matrix. The elements of the matrix are not separated by space.

## Output data

The output file `paznici.out` will print on the first line the string of characters according to the task.

## Constraints

$1 \leq N \\
1 \leq M \\
N, M \leq 26$

## Example

paznici.in 
```
13 13 
0000000000000
0010001010010
0000000000000
0000000000000
0010101010010
0000000000000
0000000010010
0000000000000
0000000000000
0000000000010
0000000000000
0000000000000
0000000010010
```

paznici.out 
```
BEil
```

## Explanation
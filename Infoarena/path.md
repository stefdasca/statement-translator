## Task

Consider a directed acyclic graph containing $N$ nodes and $M$ arcs. The nodes are identified by distinct letters from the English alphabet (both uppercase and lowercase letters are allowed). A path consists of a sequence of arcs, and these paths are ordered lexicographically (each path corresponds to a string of characters obtained by concatenating the letters corresponding to the nodes, in the order in which they appear in the path; it is considered that all lowercase letters are, lexicographically, before all uppercase letters). Among all the paths in the graph, only the longest ones (the length of a path is given by the number of arcs that form it) are taken into consideration. The task is to determine the $k$-th lexicographical path among these longest paths.

## Input data

The first line of the input file `path.in` contains three integers $N$, $M$ and $k$ separated by a single space. Each of the following $M$ lines contains two English alphabet characters $c_1$ and $c_2$, separated by a single space, indicating that there is an arc that goes from the node identified by $c_1$ to the node identified by $c_2$.

## Output data

The output file `path.out` will contain on a single line a string of characters representing the determined path. The characters of this string will not be separated by spaces.

## Constraints and clarifications

The number of maximum length paths is greater than or equal to $k$  
$2 \leq N \leq 52$  
$1 \leq M \leq \frac{N(N-1)}{2}$  
Between two nodes at most one edge can exist.  
$1 \leq k \leq 2\ 000\ 000\ 000$  

## Example

`path.in`
```
3 3 1
a b
b c
a c
```

`path.out`
```
abc
```
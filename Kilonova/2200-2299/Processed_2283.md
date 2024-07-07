
A string $S$, initially empty, is considered. Four operations are performed on it:
1. insert($k, e$): inserts in $S$ the element e at position $k$;
2. access($k$): returns the element at position $k$;
3. reverse($i, j$) : changes the order of elements in the sequence $S[i \\ \dots \\ j]$;
4. delete($i, j$) : deletes the subarray $S[i \\ \dots \\ j]$.

# Task

You are required to respond to all operations of type $2$ and display the elements of the sequence $S$ after performing all operations.

# Input data

The first line of the input file `secv.in` will contain two natural numbers, the first representing the number of operations in the file, and the second will be $1$ if there is a reverse operation and $0$ if there is not. The next lines will be of four types, corresponding to each operation:
1. $I \\ k \\ e$: insert($k, e$), where $e$ is a natural number within the interval $[0, 10^9]$ and $k$ a natural number within the interval $[1, n+1]$.
2. $A \\ k$: access($k$), where $1 \\leq k \\leq n$.
3. $R \\ i \\ j$: reverse($i, j$), where $1 \\leq i \\leq j \\leq n$.
4. $D \\ i \\ j$: delete($i, j$), where $1 \\leq i \\leq j \\leq n$.
With $n$ we denote the length of the sequence.

# Output data

In the output file `secv.out` the responses to the operations of type $2$ will be printed on a new line in the order they appear in the input file. On the last line, print the sequence $S$ after performing all operations.

# Constraints and clarifications

* The number of insert operations will not exceed $250\ 000$.
* The total number of operations will not exceed $750\ 000$.
* The operation insert($k, e$) will transform the sequence $S$: $s_1 \\ s_2 \\dots s_k \\dots s_n$ into $S'$: $s_1 \\ s_2 \\dots e \\ s_k \\dots s_n$.
* The operation reverse($i, j$) will transform the sequence $S$: $s_1 \\dots s_{i-1} \\ s_i \\ s_{i+1} \\dots s_{j-1} \\ s_j \\ s_{j+1} \\dots s_n$ into $S'$: $s_1 \\dots s_{i-1} \\ s_j \\ s_{j-1} \\dots s_{i+1} \\ s_i \\ s_{j+1} \\dots s_n$.
* The operation delete($i, j$) will transform the sequence $S$: $s_1 \\dots s_{i-1} \\ s_i \\ s_{i+1} \\dots s_{j-1} \\ s_j \\ s_{j+1} \\dots s_n$ into $S'$: $s_1 \\dots s_{i-1} \\ s_{j+1} \\dots s_n$.
* It is guaranteed that operations $2$, $3$, and $4$ will not be performed on an empty sequence.
* For $15\%$ of the tests, the number of insert operations will not exceed $35\ 000$ and the total number of operations $100\ 000$. For these tests, there will be a reverse operation.
* For another $25\%$ of the tests, the reverse operation will not occur.

# Example

`secv.in`
```
13 1
I 1 1
I 2 2
I 3 3
R 2 3
I 4 4
I 3 5
A 4
R 1 3
D 2 3
A 3
I 2 1
R 1 3
D 3 3
```

`secv.out`
```
2
4
2 1 4
```

## Explanation

The sequence $S$ successively becomes: $(1), (1 \\ 2), (1 \\ 2 \\ 3), (1 \\ 3 \\ 2), (1 \\ 3 \\ 2 \\ 4), (1 \\ 3 \\ 5 \\ \underline{2} \\ 4), (5 \\ 3 \\ 1 \\ 2 \\ 4), (5 \\ 2 \\ \underline{4}), (5 \\ 1 \\ 2 \\ 4), (2 \\ 1 \\ 5 \\ 4), (2 \\ 1 \\ 4)$. The underlined numbers are the responses to the operations of type $2$.

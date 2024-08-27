# The Great Noise

Happy that he qualified for ONI, XORin wants to celebrate by making as much noise as possible. Since he's a programmer, he thought of automating the way he makes noise. To make noise, he uses a board with circuits of various intensities. The board can be represented as a matrix with \( N \) rows and \( M \) columns. Each cell in the matrix has an intensity between \(0\) and \(9\) (a cell with intensity \(0\) corresponds to an empty area without any circuit). A circuit starts in one cell of the matrix and ends in another cell, being a sequence of adjacent cells of the same intensity from one end of the circuit to the other, like a path on the matrix between the two cells. Two cells are considered adjacent if they share a common side, so a cell is adjacent to a maximum of four other cells. The board was designed in such a way that short circuits do not occur; thus, the current in a circuit can only flow in one direction (in other words, each cell in a circuit is adjacent to at most two other cells in the same circuit). There are no circuits of the same intensity adjacent to each other. The noise produced by a circuit equals its length, i.e., the number of matrix cells corresponding to the circuit.

Examples of invalid circuits:

```
0 3
111 33
11 0
33 11
0 0
4 0
444 0
4 0
```

Circuits can short circuit. The circuit does not have exactly two ends.

## Task 

1) Find the number of circuits.

2) Determine the maximum noise value that can be obtained by joining two circuits. Two circuits can be joined if a connection can be made from one end of a circuit to the end of the other circuit, only through the empty cells of the matrix (of intensity \(0\)). The connection must have the form of a circuit. The length of the newly created circuit does not add to the noise produced by the two circuits.

3) Display the board containing the connection that joins the two circuits from which the maximum noise is obtained from task 2. If there are multiple options, any board containing the valid connection can be displayed.

## Input data

The first line of the file `mz.in` will contain \( N \) and \( M \), the length and width of the board. The next \( N \) lines will contain \( M \) numbers characterizing the circuit's intensity passing through that cell. If no circuit passes through that cell, the file will contain the character \(0\).

## Output data

The first line of the file `mz.out` will contain the number of circuits.

The second line will contain the maximum length of a circuit that can be obtained by joining two circuits.

The following lines will print the matrix containing the newly formed circuit. Each cell in the connection through which the circuit passes will be marked with the character 'x'.

## Constraints and clarifications

\[1 \leq N, M \leq 1\ 000\] for all tests.

\[1 \leq N * M \leq 2\ 500\] for \(20\%\) of tests.

\[1 \leq N * M \leq 10\ 000\] for \(40\%\) of tests.

It is guaranteed that at least \(2\) circuits can be joined.

Two circuits can be joined only at their ends (the ends of the connection between circuits must be adjacent to one end of each joined circuit).

Two circuits can only be joined through free zones (the connection can only be formed on cells of intensity \(0\)).

If there are multiple solutions to task 3, any of them will be displayed.

For the correct resolution of task 1, \(20\%\) of the score is awarded.

For the correct resolution of tasks 1 and 2, \(50\%\) of the score is awarded.

For the correct resolution of all \(3\) tasks, \(100\%\) of the score is awarded.

## Example

`mz.in`

```
8 6
122100
111100
000000
000011
222221
000011
000000
333000
```

`mz.out`

```
5
11
1221×0
1111×0
000xx0
xxxx11
222221
000011
000000
333000
```

`mz.in`

```
4 20
00000000000010000000
00000000000010000000
00000000000100000000
00000000001000000000
```

`mz.out`

```
3
3
00000000000×10000000
0000000000xx10000000
0000000000×100000000
00000000001000000000
```

`mz.in`

```
8 25
0000000000000000000000000
0000001110001010011000000
0000010001110101100100000
0000001000000100001000000
0000110000000000000100000
2111000011000000000010000
0001000000000010000012000
0001000000000000000000100
```

`mz.out`

```
20
8
00000xxxxxxx0000000000000
0000xx11100×1010011000000
0000×10001110101100100000
000xx01000000100001000000
0xxx110000000000000100000
2111000011000000000010000
0001000000000010000012000
0001000000000000000000100
```
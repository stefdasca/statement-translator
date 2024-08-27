## Task

Bossanip recently bought a motorcycle and decided to ride it against the traffic on the street (do not try this at home). Although very few in number, Bossanip chose a street with $2$ lanes. Moreover, there are $2$ emergency lanes (one on the left side and one on the right side). The $2$ lanes on the road have many potholes which can be considered obstacles that must be avoided (the emergency lanes have no potholes because no one uses them). We can consider the road as a binary matrix of size $N \times 2$ where $0$ represents a free cell and $1$ represents a pothole. If we were to introduce the emergency lanes, the matrix would turn into a matrix of $N \times 4$ where the first and last columns are always $0$. Bossanip's goal is to start from any free position on the first line and reach any free position on the last line. The only restriction he has is that he is not allowed to stay more than $P$ consecutive cells on the emergency lane (otherwise the police will come and Bossanip wants to keep his record clean). Knowing that at any moment in time Bossanip can only move from line $x$ to line $x + 1$ and can change the column by a maximum of $1$ position to the left or right, help the great driver find out how many distinct paths exist that start from a free position in the first line and reach a free position in the last line (considering the emergency lanes as well). Two paths are considered distinct if they differ by at least one position at any moment.

## Input data

The input file `contrasens.in` contains on the first line $2$ natural numbers $N$ and $P$. On the following lines, there is a binary matrix $N \times 2$ representing the given road.

## Output data

The output file `contrasens.out` will contain a single natural number representing the total number of distinct paths modulo $666013$.

## Constraints and clarifications

$1 \leq P \leq N \leq 100000$

For $40 \%$ of the tests $N \leq 500$

## Example

`contrasens.in`
```
5 2
00
01
10
11
00
```

`contrasens.out`
```
13
```

## Explanation

One of the $13$ paths is the following, marked with $X$.
```
000X
001X
01X0
011X
000X
```
The following path is not valid because Bossanip spends $3$ moments in time on the right emergency lane.
```
00X0
001X
010X
011X
00X0
```
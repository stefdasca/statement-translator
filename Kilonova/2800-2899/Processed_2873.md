> It's one thing to sort cards, another to sort wagons!

At the gate of a mill, there are $n$ sacks, labeled from $1$ to $n$, arranged in a line, in a given order. The sack labeled $i$ has a weight of $g_i$.

The miller asks his apprentice to rearrange the sacks in increasing order of labels. Since there is no maneuvering space to swap the sacks directly, the apprentice takes a chair and places it next to position $k$ in the line, picks a sack and puts it on the chair, then takes another sack and moves it to the vacant spot, and so on, or brings the sack from the chair to the vacant spot. He repeats this process until the sacks are in the order required by the miller. The chair does not move. The effort made by the apprentice to move a sack, whether it is placed on the chair or not, is equal to the product of the sack's weight and the distance it was transported. The distance between two adjacent sacks is equal to one unit.

# Task
Determine the position to place the chair and the order of the sack moves, so that the apprentice makes a minimum number of moves and the effort required for the moves is also minimal.

# Input data
The input file `moara.in` contains:
- The first line contains the number of sacks $n$.
- The second line contains the order of the sacks.
- The third line contains the array of sack weights $g_1, g_2, \dots, g_n$.

# Output data
The output is written to the file `moara.out`, which will contain:
- On the first line, `p k e`, where $p$ is the chair position, $k$ is the number of moves, and $e$ is the effort value.
- On each of the following lines, a move of the form `d s`, where $d$ is the destination position and $s$ is the source position. The chair position is denoted by $0$.

# Constraints and clarifications
- $2 \le n \le 5\ 000$
- $1 \le k \le n$
- $1 \le g_i < 256$, for $1 \le i \le n$
- $30\%$ of the score is awarded if the displayed number of moves is correct and an additional $30\%$ if the displayed effort is correct.

# Example
`moara.in`
```
5
2 4 3 5 1
3 5 1 2 4
```
`moara.out`
```
3 5 25
0 2
2 1
1 5
5 4
4 0

# Mission

Zeratul received a very important mission from Tassadar: he must destroy $N$ Terran command centers, numbered from $0$ to $N - 1$, knowing their coordinates $x$ and $y$ in the plane. Initially, Zeratul is teleported to the command center numbered $0$, where he will need to return after completing his mission and destroying all the other command centers. Zeratul can move between two command centers only in a straight line. The Terrans are cautious and have mined the area corresponding to the entire $XOY$ plane. Therefore, he can pass through a point in the plane at most once (with the exception of command center $0$, where he will be picked up at the end of the mission). Zeratul promises you a reward of $100$ points if you can tell him the order in which to destroy the $N$ command centers so that in the end he returns to the command center indexed $0$ and does not pass through the same point more than once.

## Input data

The input file `mission.in` contains on the first line the integer $N$, signifying the number of command centers that Zeratul must destroy. The next $N$ lines contain two integers each, $x_i$ and $y_i$, representing the coordinates of the $N$ command centers.

## Output data

In the output file `mission.out` you will contain on the first line a permutation of length $N$, representing the order in which the $N$ command centers will be destroyed.

## Constraints and clarifications

$3 \leq N \leq 1000$

$-1\ 000\ 000 \leq x_i, y_i \leq 1\ 000\ 000$

If Zeratul passes through a command center, he is obliged to destroy it (because he cannot pass through that center a second time and thus would not complete his mission); this is valid including for command center $0$

After destroying the $N$-th command center in the indicated route, he will return to command center $0$, also in a straight line

Zeratul cannot pass through a point more than once, even if he has destroyed all command centers

If there are multiple solutions, any can be displayed

Any three command centers are non-collinear

## Example

`mission.in`  
`
5  
0 0  
1 1  
2 0  
0 3  
2 3  
`

`mission.out`  
`
0 3 4 1 2  
`

## Explanation

An example of a permutation that does not meet the requirements is $\{0, 4, 3, 2, 1\}$ because Zeratul passes through the point $(1, 1.5)$ twice.

Another example of a permutation that does not meet the requirements is $\{2, 1, 4, 3, 0\}$ because Zeratul initially passes through command center $0$ without destroying it.
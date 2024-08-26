# Permdist

Juju is a happy turtle since he started working at the Center for Foreign Missions Organization. The happiest part of his day is when he meets his boss, Netaşu. They actually have the same job, namely supervising the other employees. The center can be described by $N$ different offices, each having a different mission. A supervision system over these offices can be described as a permutation of $N$ numbers, $T$. We define supervision as a recursive process that starts from a room $x$, visits it, and then recursively moves to room $T[x]$ (taking one second), until it reaches a room that has already been visited. When this happens, the supervision stops. The two employees have each developed a different supervision system, for Juju this is $A$, and for Netaşu this is $B$. Their contract is for $N$ days, on the $i$-th of which they will have to start a supervision from office $i$. Since they are very happy to meet each other, they want to know how many times they will be in the same office at the same time on the $i$-th day.

## Input data

The input file `permdist.in` will contain on the first line $N$, the number of offices.
The second line will contain $N$ numbers that compose the permutation $A$.
The third line will contain $N$ numbers that compose the permutation $B$.

## Output data

The output file `permdist.out` will contain $N$ numbers, the $i$-th being the number of times the two friends will see each other on the $i$-th day.

## Constraints

$1 \leq N \leq 1\,000\,000$

$1 \leq A_i, B_i \leq N$, for any $i$ that satisfies $1 \leq i \leq N$

$A_i \ne A_j$ and $B_i \ne B_j$, for any $i$ and $j$ that satisfy $1 \leq i < j \leq N$

Attention: on the $i$-th day, office number $i$ is considered to be visited only once (so the two friends will see each other in that office at most once). 
In the world of the two friends, days have a sufficiently large number of seconds.

### Subtasks

Subtask They didn't succeed - 4 points (tests 1-4):
$n \leq 500$

Subtask Not that they didn't try - 6 points (tests 5-7):
$n \leq 2\,000$

Subtask He knows it so well because he didn't swim much - 10 points (tests 8-10):
$n \leq 100\,000$. In addition, each day, Juju and Netaşu visit a maximum of 100 offices

Subtask I don't care-- Even if it gets to 2 o'clock we're still looking for it - 16 points (tests 11-13):
$n \leq 100\,000$. In addition, each day, Juju and Netaşu visit all $N$ offices

Subtask Sleep not knowing if you'll wake up with a knife in your back ( ◜‿◝ ) - 37 points (tests 14-19):
$n \leq 100\,000$

Subtask Random things, such as a sorting network sorting any sequence correctly only if it can sort all sequences of 0/1s - 27 points (tests 20-30): No additional constraints

## Example

`permdist.in`

```
7
3 5 2 6 1 7 4
5 3 1 7 2 4 6
```

`permdist.out`

```
2 2 2 1 2 1 1
```

## Explanation

On day 1:

Juju visits in order: 1 3 2 5

Netaşu visits in order: 1 5 2 3

They see each other in the first and third second.
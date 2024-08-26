# Weirdtree

Azusa, the witch of the highlands, has discovered a garden full of weird trees! Thus, together with her friend, Laika, she decided to spend some time there, taking care of the garden. The garden can be seen as a sequence with $N$ trees, where the trees are numbered from $1$ to $N$. Each tree has a certain height which is a natural number. Therefore, Azusa will spend her time according to a schedule containing $Q$ entries, which can be of various types:
1. A tree-cutting phase, characterized by three integers $l$, $r$, and $k$. In this phase, Azusa will spend the next $k$ days cutting trees. Each day she finds the tallest tree whose position is between $l$ and $r$ and decreases its height by $1$. If there are multiple tallest trees, she chooses the leftmost one. If the tallest tree has a height of $0$, nothing happens on that day.
2. A magic phase, characterized by two integers $i$ and $x$. In this phase, Azusa changes the tree at position $i$ to have a height of $x$.
3. An inspection phase, characterized by two integers $l$ and $r$. In this phase, Azusa finds the sum of the heights of the trees whose positions are between $l$ and $r$. (Note that "between" means inclusive; for example, $1, 2, 3, 4, 5$ are "between" $1$ and $5$.)

Azusa is curious about the results of the tree inspection phases and wants to know them without having to go through the entire schedule by herself. Can you help her?

## Task

You need to solve the problem according to the given description.

## Input data

The first line of the input file weirdtree.in will contain $N$, $Q$. The second line contains the sequence of the $N$ initial heights. The next $Q$ lines each contain an entry from the schedule. The three types of schedule entries (cut, magic, inspect) are coded as $1$ $l$ $r$ $k$, $2$ $i$ $x$, and respectively $3$ $l$ $r$.

## Output data

Print the answers for all the inspection phases, each on a new line.

## Constraints and clarifications

$1 \leq N, Q \leq 300\,000$

It is guaranteed that the functions cut, magic, and inspect will be called exactly $Q$ times in total.

$1 \leq i \leq N$

$0 \leq x, k, h[i] \leq 1\,000\,000\,000$

$1 \leq l \leq r \leq N$

For $8$ points: $N \leq 1\,000$, $Q \leq 1\,000$, $k = 1$

For another $8$ points: $N \leq 80\,000$, $Q \leq 80\,000$, $k = 1$

For another $8$ points: $N \leq 1\,000$, $Q \leq 1\,000$, no magic phases.

For another $16$ points: There are no magic phases.

For another $8$ points: $l = 1$, $r = N$

For another $20$ points: $N \leq 80\,000$, $Q \leq 80\,000$

## Examples

```
weirdtree.in
6 10 
1 2 3 1 2 3 
1 1 6 3 
3 1 6 
1 1 3 3 
3 1 6 
1 1 3 1000 
3 1 6 
2 1 1000 
3 1 6 
1 1 3 999 
3 1 5

weirdtree.out
9 
6 
5 
1005 
4
```

## Explanation

In the first phase, after each of the $3$ days of tree-cutting, the tree heights are $1, 2, 2, 1, 2, 3$ ; $1, 2, 2, 1, 2, 2$ ; and $1, 1, 2, 1, 2, 2$. The sum of these values is $9$, which is the answer to the inspection in the second phase.

In the third phase, after each of the $3$ days of tree-cutting, the tree heights are $1, 1, 1, 1, 2, 2$ ; $0, 1, 1, 1, 2, 2$ ; and $0, 0, 1, 1, 2, 2$. The sum of these values is $6$, which is the answer to the inspection in the fourth phase.

In the fifth phase, after each of the $1000$ days of tree-cutting, the tree heights are $0, 0, 0, 1, 2, 2$. This is because a tree with a height of $0$ cannot be cut. The sum of these values is $5$, which is the answer to the inspection in the sixth phase.

In the seventh phase, the first tree is grown to a height of $1000$, resulting in the heights $1000, 0, 0, 1, 2, 2$. The sum of these values is $1005$, which is the answer to the inspection in the eighth phase.

In the ninth phase, each of the $999$ days of tree-cutting reduces the height of the first tree by $1$. This gives the tree heights $1, 0, 0, 1, 2, 2$ at the end of the phase. The sum of the first five values among these is $4$, which is the answer to the inspection in the tenth phase -- the final phase.
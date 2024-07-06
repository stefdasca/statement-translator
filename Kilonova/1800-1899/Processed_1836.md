> — Calm down a bit...

We have a ball that is on the $X$ axis, initially placed at coordinate $0$. There are also $N$ sets of walls on the $X$ axis. Each set is described as a triplet $(dir, len, freq)$, where:

* $dir$ indicates the direction in which the walls are placed, it can be either `L` (left) or `R` (right)
* if $dir=$ `L`, then the walls in the set are placed at positions $\displaystyle -len$, $\displaystyle -2 \cdot len$, $\displaystyle -3 \cdot len$, ..., $\displaystyle -freq \cdot len$
* if $dir=$ `R`, then the walls in the set are placed at positions $\displaystyle len$, $\displaystyle 2 \cdot len$, $\displaystyle 3 \cdot len$, ..., $\displaystyle freq \cdot len$

It is observed that due to the nature of this information, multiple walls may be placed at the same coordinate.

At time $T=0$ the ball starts to move to the right with a constant speed of one unit per second. When the ball hits a wall, the wall is automatically destroyed and the ball changes direction. If there are multiple walls at the same coordinate, only one of them will be destroyed.

# Task

There are $Q$ questions. For each question, an integer $T$ is given. Display the coordinate of the ball after $T$ seconds.

# Input data

The first line of the input will contain the integers $N$ and $Q$, separated by a space.

The next $N$ lines contain three integers separated by spaces, $dir$, $len$, and $freq$, describing how the walls are placed.

The next $Q$ lines contain one integer, $T$, describing a question. 

# Output data

Print $Q$ lines, the $i$-th line containing the answer to the $i$-th question.

# Constraints and clarifications

* $1 \leq N, Q \leq 250\ 000$
* $1 \leq T \leq 10^{12}$
* $dir \in \{`L`, `R`\}$
* $1 \leq len, freq \leq 10^{12}$

| # | Score | Constraints          |
| - | -------- | ------------------- |
| 0 | 0       | Examples |
| 1 | 13      | $N, Q \leq 1 \ 000$|
| 2 | 8       | $Q, T \leq 1 \ 000$|
| 3 | 16      | $1 \leq len \leq 10$|
| 4 | 10      | $T \leq 10^6$|
| 5 | 11      | $len \cdot freq \leq 10^6$|
| 6 | 9       | Let $S$ be the sum of all $freq$ in the input. $S \leq 10^6$|
| 7 | 33      | No additional constraints|

# Example

`stdin`
```
3 12
R 3 2
R 6 1
L 3 2
0
1
2
3
4
5
6
7
17
18
19
200
```

`stdout`
```
0
1
2
3
2
1
0
-1
5
6
5
-152
```
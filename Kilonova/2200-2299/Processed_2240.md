
Emanuel, freshly arrived at Oxford, is eager to get to work and start... picking apples. The position where he is located in the orchard can be identified using the coordinate pair $(x, y)$, initially found at point $(0, 0)$. Due to the arrangement of the trees in the orchard, Emanuel can move horizontally with a maximum speed $V_A$, and vertically with another maximum speed $V_B$.

Starting his workday, Emanuel notes down in his notebook the coordinates and time $T_i$ when he picks apples from each of the $N$ apple trees, in order to justify his harvest to his boss. Because all this time he was trying to prove the Riemann hypothesis, he always notes in his notebook only one of the two coordinates $X_i$ where he is, sometimes the horizontal one, other times the vertical one.

At the end of the day, he realizes the mistake he made and wonders how plausible his route is, to explain to his boss what happened and not be sent to Cambridge to pick pears. To determine the probability of the route, he will assume for each logged coordinate, in turn, that it is horizontal, and then vertical and will count all possible configurations.

# Task
Implement the function
```cpp
int count(int N, int VA, int VB, int *X, int *T)
```
which will return the number of possible configurations modulo $1\, 000\, 000\, 007$. $N$ represents the number of events (harvests), $V_A$ and $V_B$ the maximum speeds in the two directions. $X$ and $T$ are two arrays of $N$ elements, indexed from $0$, that store one of the coordinates $X$ respectively the time $T$ for each event.

# Constraints and clarifications

* $1 \leq N \leq 200\, 000$
* $1 \leq V_{A}, V_{B} \leq 10^9$
* $-10^9 \leq X_i \leq 10^9$
* $1 \leq T_i \leq 10^9$
* The values $T_i$ are given in increasing order
* The statement and points do not correspond to those from the competition

## Subtask 1 (6 points)
* $N \leq 20$
## Subtask 2 (24 points)
* $N \leq 1000$
## Subtask 3 (41 points)
* $N \leq 100\, 000$
## Subtask 4 (29 points)
* $N \leq 200\, 000$

# Example

Given $N = 4, V_A = 3, V_B = 2$ and the events:
$X_0 = 2, T_0 = 1$
$X_1 = 7, T_1 = 3$
$X_2 = 1, T_2 = 4$
$X_3 = 8, T_3 = 5$

There are $2$ possible ways to assign the coordinates:

* $X_1$ and $X_3$ on horizontal (with speed $v_A$), $X_0$ and $X_2$ on vertical (with speed $v_B$). We have the following pairs (position, time)
  On horizontal: $(0, 0), (7, 3), (8, 5)$
  On vertical: $(0, 0), (2, 1), (1, 4)$
* $X_0$, $X_1$, $X_3$ on horizontal, $X_2$ on vertical.
  On horizontal: $(0, 0), (2, 1), (7, 3), (8, 5)$
  On vertical: $(0, 0), (1, 4)$

It would not be possible to have $X_0$ and $X_2$ on horizontal, $X_1$ and $X_3$ on vertical, because it would mean moving vertically from pair $(0, 0)$ to $(7, 3)$; impossible because we would travel $7$ units in $3$ seconds, and the maximum vertical speed is $2$.

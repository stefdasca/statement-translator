
The kids from 402 heard the bell and quickly ran outside to play. Seeing a very tall pole in the middle of the field, they thought of the following game. Initially, they split into girls and boys (in number of `m`, respectively `n`) and positioned themselves as follows:

\\
~[bfs.jpg]
\\
The pole is in a vertical position (tilt `0`). Each player has a certain strength (`B[i]` - the strength of boy `i`, `F[i]` - the strength of girl `i`). The game proceeds as follows: at each step, either the boy closest to the pole, or the girl closest to the pole, will throw the ball towards the pole (the boy to the right, the girl to the left), after which they will exit the game. After any throw, the pole will tilt further in the opposite direction of the thrower by a value equal to their strength. Naturally, the stronger the thrower, the more the pole will tilt. Furthermore, **the pole will not return to its initial tilt after the throw**.

\\
~[bfs2.jpg]
\\
However, to prevent the game from getting unpleasant twists, the pole must never tilt with a value strictly greater than `S` (in either direction), both during the game and at the end of it.

The kids are wondering if they can find a throwing order such that everyone throws the ball while respecting the above constraints (the pole's maximum tilt must remain within safe limits). Nonetheless, the teacher wants to spice things up, so during `Q` moments of time, she will swap two consecutive girls or two consecutive boys. Any change by the teacher remains for the subsequent moments.

# Task
You need to help the kids find out after each swap if there exists a valid throwing order.

# Input data
The file `bfs.in` contains on the first line three numbers: `n, m` and `S` representing the number of boys, the number of girls, and the maximum allowable tilt of the pole. The second line contains `n` natural numbers representing the boys' strengths. The third line contains `m` natural numbers representing the girls' strengths. The fourth line contains `Q` representing the number of swaps performed. The next `Q` lines are of the form `[B|F] x y`, where `[B|F]` represents which group is being swapped, and `x` and `y` represent the positions between which the swap is made.

# Output data
The file `bfs.out` contains `Q` lines, with the `i`th line containing the value `1` if the game can successfully end after the first `i` swaps, and `0` otherwise.

# Constraints and clarifications
* `1 \leq n, m, Q \leq 100 000`
* $1 \leq B[i], F[i], S \leq 10^9$, for any `i`
* For each swap, it is guaranteed that `|x - y| = 1`
* **It is guaranteed that, before making the first swap, the game can successfully end**.
* For tests worth `10` points `n, m \leq 100` and `Q \leq 250`
* For other tests worth `20` points `n, m \leq 2 500` and `Q \leq 6 000`
* For other tests worth `65` points `n, m \leq 100 000` and `Q \leq 35 000`

# Example
`bfs.in`
```
6 3 30000
15000 15000 60000 30000 29805 56555
60000 60000 57187
14
B 2 3
B 2 3
B 2 3
B 2 3
F 2 3
F 2 3
B 2 3
B 2 3
B 3 4
B 3 4
B 2 3
B 2 3
F 2 3
F 2 3
```

`bfs.out`
```
0
1
0
1
0
1
0
1
0
1
0
1
0
1
```

Explanations
---
No explanations needed.

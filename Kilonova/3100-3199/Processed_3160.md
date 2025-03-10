Azusa, the witch of the highlands, discovered a garden full of peculiar trees! So, together with her friend Laika, she decided to spend some time there, taking care of the garden.

The garden can be seen as a sequence with $N$ trees, where trees are numbered from $1$ to $N$. Each tree has a certain height, a natural number. Thus, Azusa will spend her time according to a schedule containing $Q$ entries, which can be of several types:

1. A tree-cutting phase, characterized by three integers $l, r,$ and $k$. In this phase, Azusa will spend the next $k$ days cutting trees. Each day, she finds the tallest tree whose position is between $l$ and $r$ and decreases its height by $1$. In case there are several such trees with the maximum height, she chooses the leftmost one. If the tallest tree has a height of $0$, then nothing happens that day.
2. A magic phase, characterized by two integers $i$ and $x$. In this phase, Azusa modifies the tree at position $i$, so that it has the height $x$.
3. A tree inspection phase, characterized by two integers $l$ and $r$. In this phase, Azusa will find the sum of the heights of the trees positioned between $l$ and $r$.

(Note that the term "between" means including the endpoints; for example, $1, 2, 3, 4, 5$ are "between" $1$ and $5$.)

Azusa is curious about the results of the tree inspection phases and wants to know them without having to go through the entire schedule on her own. Can you help her?

# Interaction Protocol

The contestant must implement the following four functions:

```cpp
void initialise(int N, int Q, int h[]);
void cut(int l, int r, int k);
void magic(int i, int x);
long long int inspect(int l, int r);
```

The `initialise` function is given $N$ (the number of trees), $Q$ (the number of schedule entries), and an array $h$, where $h[i]$ is the height of the $i^{th}$ tree for $1 \leq i \leq N$. This function is called by the commission's source exactly once, before any of the other three functions are called. The functions `cut`, `magic`, and `inspect` represent the tree-cutting, magic, and inspection phases, respectively, and are characterized by their respective parameters. The contestant's implementation of the `inspect` function must return the sum of the heights of the trees with positions between $l$ and $r$.

The contestant does not need to implement the `main` function. It will be implemented in the commission's file `grader.cpp`; you will receive an example [grader.cpp](https://kilonova.ro/assets/problem/3160/attachment/grader.cpp) in the attachments. Our `main` function will read $N, Q$, the sequence of the $N$ initial heights, and the $Q$ entries from the schedule. The three types of schedule entries (`cut(l, r, k)`, `magic(i, x)`, and `inspect(l, r)`) are encoded as $1 \ l \ r \ k$, $2 \ i \ x$, and respectively $3 \ l \ r$. This is the input file format that will be used in the examples below.

Note that the contestant is allowed to use global variables, additional functions, methods, and classes.

# Constraints and Clarifications

* $1 \leq N, Q \leq 300 \ 000$
* It is guaranteed that the functions `cut`, `magic`, and `inspect` will be called exactly $Q$ times in total.
* $1 \leq i \leq N$
* $0 \leq x, k, h[i] \leq 1 \ 000 \ 000 \ 000$
* $1 \leq l \leq r \leq N$

| # | Score | Constraints           |
| - | ------- | ------------------- |
| 1 | 5      | $N \leq 1 \ 000, \ Q \leq 1 \ 000, \ k = 1$|
| 2 | 8      | $N \leq 80 \ 000, \ Q \leq 80 \ 000, \ k = 1$|
| 3 | 8      | $N \leq 1 \ 000, \ Q \leq 1 \ 000$, no magic phases.|
| 4 | 19      | No magic phases.|
| 5 | 10      | $l = 1, \ r = N$|
| 6 | 21      | $N \leq 80 \ 000, \ Q \leq 80 \ 000$|
| 7 | 29      | No additional constraints.|

# Examples

`stdin`
```
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
```

`stdout`
```
9
6
5
1005
4
```

## Explanation

In the first phase, after each of the $3$ days of cutting trees, the tree heights are $1, 2, 2, 1, 2, 3; \ 1, 2, 2, 1, 2, 2$; and $1, 1, 2, 1, 2, 2$. The sum of these values is $9$, which is the answer to the inspection in the second phase.

In the third phase, after each of the $3$ days of tree cutting, the tree heights are $1, 1, 1, 1, 2, 2; \ 0, 1, 1, 1, 2, 2$; and $0, 0, 1, 1, 2, 2$. The sum of these values is $6$, which is the answer to the inspection in the fourth phase.

In the fifth phase, after each of the $1000$ days of tree cutting, the tree heights are $0, 0, 0, 1, 2, 2$. That's because a tree with height $0$ cannot be cut. The sum of these values is $5$, which is the answer to the inspection in the sixth phase.

In the seventh phase, the first tree is grown to a height of $1000$, resulting in heights of $1000, 0, 0, 1, 2, 2$. The sum of these values is $1005$, which is the answer to the inspection in the eighth phase.

In the ninth phase, each of the $999$ days of tree cutting reduces the height of the first tree by $1$. This gives the following tree heights $1, 0, 0, 1, 2, 2$ at the end of the phase. The sum of the first five values among these is $4$, which is the answer to the inspection in the tenth phase — the final phase.
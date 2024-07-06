Loid Forger has received a new mission: to sabotage an important mine near Berlint, Ostania. The mine has the shape of a vertical column divided into $n$ levels, numbered from $1$ (the top level) to $n$ (the bottom level). Each level contains air (coded as $0$), sand (coded as $1$), or stone (coded as $2$).

Loid's mission consists of dynamiting the stone on some levels to cause the mine to collapse and the sand to flow to the lower levels. He has $m$ tasks numbered from $1$ to $m$. These tasks are of two types:

* `1 t p` (dynamite): Loid must dynamite the stone on level $p$ of the mine at second $t$. For any such task, Loid knows that at second $t$, level $p$ contains stone, and it will be replaced by air at second $t+1$, after dynamiting.
* `2 t p` (question): To test his insight, Loid is asked what level $p$ of the mine contains at second $t$: air, sand, or stone?

In general, the content of a level at second $t$ will be the same at second $t+1$, with two exceptions:
* Sand flow: If at second $t$, level $p$ contains sand and level $p+1$ contains air, the sand will flow, and at second $t+1$, level $p$ will contain air, and level $p+1$ will contain sand.
* Dynamiting by Loid: A level containing stone and dynamited at second $t$ will contain air at second $t+1$.

If, at second $t$, each level $i$ from $1$ to $n$ of the mine has the same content as at second $t-1$, we say that the mine is **stable** at second $t$.

# Task

Given $n$, the contents of all mine levels at second $0$, $m$, and the tasks to be carried out, determine the answers to the question-type tasks.

# Input data

The input file `nisip.in` will contain on the first line two natural numbers $n$ and $m$ separated by a space, representing the number of mine levels and the number of tasks, respectively.

The next line will contain $n$ natural numbers separated by spaces, the $i$-th of which represents the content code of level $i$ of the mine ($0$ for air, $1$ for sand, $2$ for stone).

The following $m$ lines contain descriptions of Loid's mission tasks. The $i$-th of these will contain three natural numbers $c_i$, $t_i$ and $p_i$ separated by spaces, representing in chronological order, the tasks given to Loid: $c_i$ represents the task type $i$ ($1$ for dynamite, $2$ for question), $t_i$ represents the second, and $p_i$ represents the mine level.

# Output data

The output file `nisip.out` contains the codes corresponding to the answers to the question-type tasks ($0$ for air, $1$ for sand, $2$ for stone), in the order from the input file, one on each line.

# Constraints and clarifications

* $1 \leq n \leq 1\ 000\ 000$
* $1 \leq m \leq 1\ 000\ 000$
* $1 \leq t_i \leq 1\ 000\ 000\ 000$ and $1 \leq p_i \leq n$ for any $i$, $1 \leq i \leq m$.
* $t_i < t_{i+1}$ for any $i$, $1 \leq i \leq m$.
* Level $n$ always contains stone, and Loid will never have the task to dynamite the stone on level $n$.
* The mine is stable at second $1$.
* **For each task $i$ for which $c_i = 1$, the mine is stable at second $t_i$**.

|# | Score | Constraints|
| - | - | ------------|
|1|21|$n \leq 1\ 000$, $m \leq 1\ 000$, $t_i \leq 3\ 000$, for any $i$, $1 \leq i \leq m$.|
|2|28|$c_1 = 1$, $c_i = 2$, for any $i$,  $2 \leq i \leq m$.|
|3|22|There are at most $1\ 000$ levels containing sand, and at most $1\ 000$ tasks of type $1$.|
|4|29|No additional constraints.|

# Examples

`nisip.in`
```
6 4
0 1 1 2 0 2
1 1 4
2 2 3
2 4 2
2 5 4
```

`nisip.out`
```
1
0
1
```

# Explanations

The contents of the mine levels are:
* `0 1 1 2 0 2` at second 1,
* `0 1 1 0 0 2` at second 2,
* `0 1 0 1 0 2` at second 3,
* `0 0 1 0 1 2` at second 4,
* `0 0 0 1 1 2` at second 5,
* `0 0 0 1 1 2` at second 6, etc.
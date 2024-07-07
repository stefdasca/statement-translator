
Between two banks of a deep valley, a suspension bridge has been built, composed of $N$ wooden planks tied together with lianas. We assume that the planks are numbered from $1$ to $N$, starting from the bank we are on. Over time, some of the wooden planks have deteriorated, while others have even disappeared.

For crossing the bridge, it is known that:

* steps can only be of lengths $1$, $2$, or $3$
* deteriorated planks are unsafe, so on them and from them, only steps of length $1$ are possible
* obviously, one cannot step on a missing plank

# Task

Write a program to determine the number of ways to cross the bridge (more precisely, to reach the other bank), as well as a solution for crossing, if such a solution exists.

# Input data

The input file `pod.in` has the structure:

```
N
k s1 s2 ... sk
h d1 d2 ... dh
```

$N$ represents the total number of planks.

$k \\ s_1 \\ s_2 \\ldots s_k$ represents the number of missing planks and their respective numbers.

$h \\ d_1 \\ d_2 \\ldots d_h$ represents the number of deteriorated planks and their respective numbers.

# Output data

The output file `pod.out` will contain on the first line the value $\text{-}1$ if it is not possible to cross the bridge, respectively the number of possibilities to cross the bridge if it is possible.

If solutions exist, on the second line will be printed such a solution, by indicating, in order, the planks stepped on, in the form:

```
Nr
p1 p2 ... pm
```

$Nr$ represents the total number of possibilities.

$p_1 \\ p_2 \\ldots p_m$ represents the determined solution, by indicating in order the planks stepped on.

# Constraints and clarifications

* $3 \\leq N \\leq 300$
* $0 \\leq k, h \\leq N$
* $\\{ s_1, s_2, \\ldots, s_k \\} \\subseteq \\{ 2, \\ldots N \\}, \\{ d_1, d_2, \\ldots, d_h \\} \\subseteq \\{ 1, 2, \\ldots, N \\}$
* $ \\{ s_1, s_2, \\ldots, s_k \\} \\bigcap \\{ d_1, d_2, \\ldots, d_h \\} = \\varnothing $
* $Nr$ has at most 80 digits

# Example 1

`pod.in`
```
5
0
0
```

`pod.out`
```
24
3
```

# Example 2

`pod.in`
```
10
2 2 7
1 5
```

`pod.out`
```
48
3 6 8
```

# Example 3

`pod.in`
```
6
2 2 4
1 3
```

`pod.out`
```
-1
```

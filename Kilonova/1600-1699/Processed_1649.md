## English Translation of the Competitive Programming Problem

Gigel works in a warehouse and needs to arrange $n$ crates in a single row. The heights of the crates can differ. To manage them more easily, Gigel has decided that he will arrange them in the shape of a mountain, so that all the crates are visible either from the left or from the right, and the "peak" is visible from both sides. Gigel wants to know in how many distinct ways he could arrange the $n$ crates so that all of them are visible. For example, if we have $5$ crates with heights $2$, $1$, $3$, $2$, $4$, then there are $4$ ways to arrange them, as follows:

~[munte.png|width=44em]

Let's note that if in the above example we had two crates of maximum height $4$, Gigel would not be able to arrange the crates in the shape of a mountain, because he wants the peak of the crates mountain to be **unique**, and the heights of the crates on either side of the mountain to form a **strictly increasing sequence**.

# Task

Create a program that determines the number of possible distinct arrangements. Two arrangements are considered distinct if the height sequences of the crates differ by at least one position.

# Input data

The file `munte.in` contains on the first line the natural number $n$ of crates, and on the next $n$ lines, each a natural number representing the height of a crate.

# Output data

The file `munte.out` will contain on the first line a single number, representing the number of distinct arrangements $\\text{mod } 12 \\ 343$.

# Constraints and clarifications

* $3 \\leq n \\leq 64\ 000$
* $1 \\leq$ heights of the crates $\\leq 64\ 000$

# Example 1

`munte.in`
```
5
3
1
3
2
4
```

`munte.out`
```
4
```

# Example 2

`munte.in`
```
4
2
4
4
2
```

`munte.out`
```
0
```

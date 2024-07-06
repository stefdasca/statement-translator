Giugudel has $N$ sheep grazing on a plane. Tired of running after them all day, Giugudel wants to build a pen around them. Unfortunately, S C Împrejur SRL, the only company in town that deals with pens, only accepts building square-shaped pens.

Giugudel is a clever boy, so he will only accept a pen if:
* It contains all the sheep inside or on the edges;
* There is at least one sheep on each side of the pen (otherwise, he would argue with the company representatives that a smaller pen could be built). If a sheep is located at a corner, it is considered to be on both sides that meet at that corner.

Luckily, Giugudel is not very good at computer science, so he will be satisfied with any pen that meets the above conditions. It is not necessary to find the one with the minimum side.

You will need to help Giugudel in $T$ such situations.

# Input data

The input file `tarc.in` will contain $T$, the number of test cases, on the first line. Each test case will contain a natural number $N$, the number of Giugudel's sheep, on the first line. The next $N$ lines will contain 2 integers each, representing the coordinates of the sheep.

# Output data

In the output file `tarc.out`, $4 \times T$ lines will be printed. For each test case, print $4$ lines containing two real numbers each, representing the coordinates of the pen's corners.

# Constraints and clarifications

* $ 1 \leq T \leq 10$
* $ 2 \leq N \leq 100 \ 000$
* The coordinates of the sheep are integers in the interval $[-10^{6}, 10^{6}]$
* The evaluator works with a precision of $0.000005$
* The order of the pen's vertices does not matter.

# Example

`tarc.in`
```
2
2
0 0
1 1
3
0 0
1 1
0 7
```

`tarc.out`
```
0 0
0 1
1 1
1 0
0 0
0 7
3.5 3.5
3.5 3.5
```

## Explanation

It can be observed that the order of the pen's vertices does not matter.
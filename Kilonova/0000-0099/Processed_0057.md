Authorities in a mountainous region intend to establish an emergency plan to react more effectively to frequent natural disasters in the area. For this purpose, they have identified $N$ strategic points of interest and have numbered them distinctly from $1$ to $N$. The strategic points of interest are connected by $M$ access ways, each with a priority based on its importance. Between any two strategic points of interest, there exists at most one access way that can be traversed in both directions and at least one road (comprising one or more access ways) connecting them.

In the event of a disaster, some access ways may be temporarily interrupted, and thus between certain points of interest there is no longer a connection. This can result in multiple groups of points such that between any two points in the same group there is at least one road, and between any two points in different groups there is no road.

The authorities estimate the severity of a disaster as the sum of the priorities of the access ways destroyed by it and wish to determine a scenario of maximum severity, in which the strategic points of interest are divided into $K$ groups.

# Input data
The input file `urgenta.in` has the following format:
$N\\ M\\ K$
$i_1 \\; j_1 \\; p_1 $ – between points $i_1$ and $j_1$ there is an access way of priority $p_1$
$i_2 \\; j_2 \\; p_2 $ – between points $i_2$ and $j_2$ there is an access way of priority $p_2$
...
$i_M \\; j_M \\; p_M $ – between points $i_M$ and $j_M$ there is an access way of priority $p_M$

# Output data
The output file `urgenta.out` will have the following format:
$\text{gravmax}$ – maximum severity
$C$ – number of access ways interrupted by the disaster
$k_1 \\; h_1$ – between points $k_1$ and $h_1$ the access way was interrupted
$k_2 \\; h_2$ – between points $k_2$ and $h_2$ the access way was interrupted
...
$k_C \\; h_C$ – between points $k_C$ and $h_C$ the access way was interrupted

# Constraints and clarifications
* $1 \\leq N \\leq 255$
* $N - 1 \\leq M \\leq 32\ 384$
* $1 \\leq K \\leq N$
* The priorities of the access ways are strictly positive integers less than $256$.
* A group of points can contain between $1$ and $N$ points inclusive.
* If there are multiple solutions, the program will determine only one.

# Example

`urgenta.in`
```
7 11 4
1 2 1
1 3 2
1 7 3
2 4 3
3 4 2
3 5 1
3 6 1
3 7 5
4 5 5
5 6 4
6 7 3
```

`urgenta.out`
```
27
8
1 3
1 7
2 4
3 4
3 7
4 5
5 6
6 7

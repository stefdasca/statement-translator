The mayor of Oradea intends to install $N$ wind turbines with three blades each (the attached image) to produce electricity for the town's residents ecologically, with minimal costs. According to the mayor's plan, the $N$ wind turbines (numbered $1, 2, 3, \dots, N$) will be installed in a straight line, parallel to the road connecting Oradea to Băile Felix, at not necessarily equal distances from each other. The first turbine will be installed at a distance of $D_1$ from Oradea, the second at a distance of $D_2$ from Oradea, $ \dots $, and the $N$th turbine at a distance of $D_N$ from Oradea. The blades of the turbines are positioned in the same plane, parallel to the road. Under the action of the wind, the blades of the turbines rotate around the nacelle (the following images), and the rotation speeds can be different from one turbine to another.

~[image2.png|align=right]

~[image.png|align=left]

The mayor purchased the turbines and hired Engineer Eol's team to construct the foundations and install them. After constructing the foundations, and before installation, Engineer Eol studied the turbines and found that:

- Turbine $1$ has three identical blades of length $L_1$, turbine $2$ has three identical blades of length $L_2$, $ \dots $, turbine $N$ has three identical blades of length $L_N$ and the lengths $L_1$, $L_2$, $ \cdots $, $L_N$ are not all equal, some of the turbines have blades with different lengths from the other turbines.
- The pillars of the $N$ turbines are identical.
- If they install the turbines as planned, there might be turbines that can hit their blades during rotation and thus damage themselves.

In conclusion, Engineer Eol will have to determine the minimum number $M$ of turbines that can be eliminated from the mayor's plan so that any two remaining turbines do not hit their blades during operation (the blades of two turbines hit if they touch even at one point), regardless of their rotation speeds.

# Task

Write a program that reads the natural numbers $N, D_1, D_2, \dots, D_N, L_1, L_2, \dots, L_N$ (with the significance described in the statement) and determines the minimum number $M$ of turbines that can be eliminated from the mayor's plan so that any two adjacent turbines from the remaining ones do not hit their blades during operation.

# Input data 

The input file `eoliene.in` contains on the first line the natural number $N$. The second line contains the $N$ natural numbers $D_1$, $D_2$, $ \dots $, $D_N$ separated by spaces. The third line contains the $N$ natural numbers $L_1, L_2, \dots, L_N$, separated by spaces, with the significance described in the statement.

# Output data

The output file `eoliene.out` will contain on the first line the natural number $M$ determined.

# Constraints and clarifications

* The numbers $N, D_1, D_2, \dots, D_N, L_1, L_2, \dots, L_N$ are non-zero natural numbers.
* $1 \leq N \leq 1 \ 000; 1 \leq D_1, D_2, \dots, D_N \leq 5 \ 000; 1 \leq L_1, L_2, \dots, L_N \leq 2 \ 500$
* The numbers $D_1, D_2, \dots, D_N$ are distinct from each other.
* The length of the pillars is strictly greater than the length of the blades.

# Example 

`eoliene.in`
```
7
27 9 28 37 3 54 50
1 5 5 4 5 2 2
```

`eoliene.out`
```
3
```

## Explanation

There are $N=7$ turbines. In the mayor's plan, they are arranged as follows:

~[tabel.png|align=left]

The blades of the turbine pairs $(2,5), (1,3), (3,4)$ and $(6,7)$ will collide. Thus, a minimum of M=3 turbines will be eliminated (turbines $2$, $3$ and $6$ or $2,3$ and $7$ or $5,3$ and $6$ or $5,3$ and $7$).
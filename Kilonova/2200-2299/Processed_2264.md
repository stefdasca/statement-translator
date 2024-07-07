
# Task

Consider a cube with side length $N$, composed of $N \times N \times N$ cells. A cell $(i,j,k)$, $(0 \leq i,j,k \leq N-1)$ contains a value $C(i,j,k)$ which can be either $0$ or $1$. We want to place two parallelepipeds inside the cube such that each cell $(i,j,k)$ with $C(i,j,k)=1$ is inside at least one parallelepiped. The two parallelepipeds can intersect.

A parallelepiped is defined by $3$ intervals $[a_1,b_1]$, $[a_2,b_2]$, $[a_3,b_3]$ and contains within it all cells $(i,j,k)$ with $a_1 \leq i \leq b_1$, $a_2 \leq j \leq b_2$ and $a_3 \leq k \leq b_3$.

The volume of the parallelepiped is $(b_1-a_1+1) \cdot (b_2-a_2+1) \cdot (b_3-a_3+1)$.

Determine a placement of two parallelepipeds that respects the specified conditions, such that the sum of the volumes of the two parallelepipeds is minimized.

# Input data

The first line of the input file `ppcover.in` contains the number $T$ of tests described below. The first line of each test contains the number $N$, representing the side length of the cube. The next $N^2$ lines contain $N$ characters each (plus a newline character at the end of each line).

The $L$-th such line $(1 \leq L \leq N^2)$ corresponds to the cells $(i,j,k)$ where $i=(L-1)$ div $N$ and $j=(L-1)$ mod $N$. The $k$-th character $(1 \leq k \leq N)$ on the $L$-th line among the $N^2$ corresponds to the value $C(i,j,k-1)$; if the character is $0$ then $C(i,j,k-1)=0$ and if the character is $1$ then $C(i,j,k-1)=1$.

# Output data

In the output file `ppcover.out` you will print one line for each test given in the input file, containing the minimum sum of the volumes of the two parallelepipeds.

# Constraints and clarifications

* $1 \leq T \leq 40$
* $1 \leq N \leq 40$
* It's allowed for the parallelepipeds (one of them or both) to have a volume of $0$.

# Example

`ppcover.in`
```
2
2
11
00
10
01
3
001
100
101
011
000
000
000
011
100
```

`ppcover.out`
```
5
22
```

> There was once, like in fairy tales,
> There was once like never before,
> From great imperial roots,
> A very beautiful tree with $n$ nodes.

# Task

Gigel, a great computer scientist (nicknamed the morning star of Romanian computer science), wants to color the very beautiful tree using $m$ colors, encoded by the natural numbers from $1$ to $m$.

After associating each color $c$ with a weight $w_c$ and each node $u$ with a value $req_u$, Gigel said that a coloring of the tree's nodes is *good* if each node $u$ meets one of the following conditions:

1. Node $u$ has color $1$; or
2. If node $u$ has color $c>1$, then it has exactly $req_u$ neighbors with color $c-1$.

Gigel also defines the *value* of such a coloring as $w_{c_1}+w_{c_2}+\ldots+w_{c_n}$, where $c_u$ represents the color of the node $u$.

Help Gigel find the greatest *value* of a *good* coloring!

# Input data

The first line of the input file `warb.in` will contain two natural numbers $n$ and $m$ — the number of nodes in the tree, respectively the number of colors.  
The second line will contain $m$ natural numbers $w_1,w_2,\ldots,w_m$ — the weights of the $m$ colors.  
The third line will contain $n$ natural numbers $req_1,req_2,\ldots,req_n$ — the values associated with the $n$ nodes.  
The next $n-1$ lines will contain 2 natural numbers $u$ and $v$, indicating that there is an edge in the tree between nodes $u$ and $v$.

# Output data

The first line of the output file `warb.out` will contain a single natural number, the greatest $value$ of a $good$ coloring.

# Constraints and clarifications
* $1 \leq n \leq 10^5$
* $1 \leq m \leq 100$
* $1 \leq w_i \leq 10^4$
* $0 \leq req_i \leq$ the degree of node $i$.
* It is guaranteed that the graph in the input file is a tree (a connected undirected acyclic graph).
* To obtain points for a specific subtask, at least one submitted source must pass all tests for that subtask.

| #  | Points | Constraints                                                                                   |
|----|--------|-----------------------------------------------------------------------------------------------|
| 0  | 0      | Examples                                                                                      |
| 1  | 4      | $n=1$                                                                                         |
| 2  | 4      | $m=1$                                                                                         |
| 3  | 22     | $n,m \le 7$                                                                                   |
| 4  | 10     | $req_i=0$                                                                                     |
| 5  | 8      | $m \leq 10$, the tree is a chain (the degree of all nodes is less than or equal to $2$)     |
| 6  | 7      | the tree is a chain                                                                           |
| 7  | 10     | the tree is a star (there is a node with degree $n-1$)                                       |
| 8  | 19     | $m, \text{the degree of all nodes} \leq 10$                                                  |
| 9  | 6      | $req_i > 0$                                                                                   |
| 10 | 10     | No additional constraints                                                                     |

# Example 1

`warb.in`
```
3 2
1 2
1 1 1
1 2
1 3
```

`warb.out`
```
5
```

## Explanation

For the first example, an optimal coloring is $c=[1,2,2]$:
* Node $1$ has color $1$.
* Node $2$ has color $2$ and exactly one neighbor with color $c_2-1=1$.
* Node $3$ has color $2$ and exactly one neighbor with color $c_3-1=1$.
* The *value* of this coloring is equal to $w_{c_1}+w_{c_2}+w_{c_3}=w_1+w_2+w_2=1+2+2=5$.

# Example 2

`warb.in`
```
5 4
1 2 3 4
2 3 1 1 1
1 2
1 3
2 4
2 5
```

`warb.out`
```
8
```

## Explanation

For the second example, an optimal coloring is $c=[2,1,1,2,2]$:
* Node $1$ has color $2$ and exactly two neighbors with color $c_1-1=1$.
* Node $2$ has color $1$.
* Node $3$ has color $1$.
* Node $4$ has color $2$ and exactly one neighbor with color $c_4-1=1$.
* Node $5$ has color $2$ and exactly one neighbor with color $c_5-1=1$.
* The *value* of this coloring is equal to $w_{c_1}+w_{c_2}+w_{c_3}+w_{c_4}+w_{c_5}=2+1+1+2+2=8$.

# Example 3

`warb.in`
```
7 4
1 9 8 7
2 2 0 0 1 1 1
1 2
1 3
2 4
2 5
3 6
3 7
```

`warb.out`
```
46
```

## Explanation

For the third example, an optimal coloring is $c=[2,1,1,3,2,2,2]$.

# Example 4

`warb.in`
```
6 5
7 9 50 30 80
0 1 0 0 1 0
1 2
2 3
3 4
3 5
5 6
```

`warb.out`
```
380
```

## Explanation

For the fourth example, an optimal coloring is $c=[4,5,5,5,5,4]$.

# Example 5

`warb.in`
```
7 7
458 2960 8526 2565 6679 9621 8814
1 0 0 0 2 1 1
3 4
1 2
1 4
5 7
4 5
4 6
```

`warb.out`
```
49102
```

## Explanation

For the fifth example, an optimal coloring is $c=[7,7,6,6,1,7,2]$.

# Example 6

`warb.in`
```
7 7
3564 9408 8285 6312 7323 3223 4441
0 0 0 1 1 1 2
3 2
5 3
4 1
7 3
4 7
6 7
```

`warb.out`
```
54831
```
## Explanation

For the sixth example, an optimal coloring is $c=[2,2,4,2,5,2,1]$.
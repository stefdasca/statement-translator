## Pq

You are given a sequence of $N$ natural numbers, $A(1)$, $\dots$, $A(N)$. In this sequence, we define a pair of indices $(u,v)$ as being special if all the following three conditions are met:
- $u < v$
- $A(u) = A(v)$
- There is no index $w$ $(u<w<v)$ such that $A(u)=A(v)=A(w)$. 

The cost of a special pair $(u,v)$ is equal to $v-u$. In addition, you are given $Q$ queries of the following type: given $L$ and $R$, determine the maximum cost of a special pair completely included in the interval $[L,R]$ (i.e., having $L \leq u < v \leq R$).

## Task

## Input data

The first line of the input file `pq.in` contains the natural numbers $N$ and $Q$. 
The next line contains the natural numbers $A(1)$, $\dots$, $A(N)$, in order. 
The next $Q$ lines each contain two natural numbers, $L$ and $R$, representing a query.

## Output data

The output file `pq.out` must contain $Q$ lines, one for each query: the maximum cost of a special pair completely included in the interval $[L,R]$. 
If there is no such special pair, print $-1$.

## Constraints

$1 \leq N$,  
$Q \leq 100000$  
$0 \leq A(i) \leq 99999$  
$1 \leq L \leq R \leq N$

## Example

`pq.in`  
```
8 6
1 7 1 3 1 7 3 3
1 2
1 3
1 5
2 8
4 8
7 8
```

`pq.out`  
```
-1
2
2
4
3
1
```

## Explanation

In the interval $[1,2]$ there is no special pair. 
In the interval $[1,3]$ the special pair $(1,3)$ has the maximum cost. 
In the interval $[1,5]$ the special pairs $(1,3)$ and $(3,5)$ have the maximum cost. 
In the interval $[2,8]$ the special pair $(2,6)$ has the maximum cost. 
In the interval $[4,8]$ the special pair $(4,7)$ has the maximum cost. 
In the interval $[7,8]$ the special pair $(7,8)$ has the maximum cost.
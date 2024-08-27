# Minimal Paths

In the year $3000$, humans live on $N$ planets. To facilitate easier travel, humans have built bidirectional galactic connections between certain pairs of planets. These connections are powered by a spatial generator, and it is known how many energy units each connection consumes. Travel between any two planets can occur either through direct connections or by passing through intermediate planets. However, for reasons yet unknown, when traveling consecutively through several connections, the energy consumed equals the product of the energy cost of each connection taken individually. For statistical purposes, the leader of the armed forces wants to know the number of distinct minimal energy consumption paths between planet $1$ and the other planets. Two paths are distinct if they differ by at least one connection.

## Task

Given the number of planets and the connections between them along with their energy costs, you are required to display the number of minimal paths between planet $1$ and the other planets. Each number will be displayed modulo $104659$.

## Input data

The first line of the `dmin.in` file contains the numbers $N$ and $M$ representing the number of planets and the number of connections, respectively. The next $M$ lines describe the connections between planets. Each line $i$ contains three numbers $x_i$, $y_i$, $c_i$ signifying "there is a connection between planets $x_i$ and $y_i$ with an energy cost of $c_i$".

## Output data

The first line of the `dmin.out` file contains $N-1$ numbers representing the number of minimal paths between planet $1$ and the other planets, where number $i$ represents the remainder of the division of the number of minimal paths between planet $1$ and planet $i+1$ by $104659$.

## Constraints and clarifications

$1 \leq N \leq 1500$

$1 \leq M \leq 2500$

The energy cost of a connection is an integer in the interval $[2, 10^9]$

There can be at most one connection between any two planets

## Example

`dmin.in` 
```
8 9 
1 2 2 
1 3 3 
2 4 3 
3 4 2 
4 5 4 
5 6 2 
5 7 3 
6 8 3 
7 8 2 
```

`dmin.out` 
```
1 1 2 2 2 2 4 
```

## Explanation

Between planets $1$ and $2$ there is a single minimal path with a cost of $2$.

Between planets $1$ and $3$ there is a single minimal path with a cost of $3$.

Between planets $1$ and $4$ there are $2$ minimal paths with a cost of $6$.

Between planets $1$ and $5$ there are $2$ minimal paths with a cost of $24$.

Between planets $1$ and $6$ there are $2$ minimal paths with a cost of $48$.

Between planets $1$ and $7$ there are $2$ minimal paths with a cost of $72$.

Between planets $1$ and $8$ there are $4$ minimal paths with a cost of $144$.
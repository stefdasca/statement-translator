## Task

Even fleas have become annoyed by how much Trăncănici talks. Therefore, they have all decided to gather in his room. Trăncănici's room is an $Ox$ axis on which every integer is marked, within the interval $(-\infty, +\infty)$. There are $N$ fleas in total, and each flea $i$ out of the $N$ has an initial position $P[i]$ on this axis. Two fleas $i$ and $j$, having $P[i] < P[j]$, can perform the following operation: 
Flea $i$ jumps over flea $j$, landing at position $P[j] + (P[j] - P[i])$, while flea $j$ stays in place. 
Flea $i$ stays in place, and flea $j$ jumps over flea $i$, landing at the position $P[i] - (P[j] - P[i])$. 
In other words, one of the fleas will jump over the other, maintaining the distance between them. The fleas would like to cover the entire room of Trăncănici through these operations. In other words, the fleas want to have reached every marked point on the $Ox$ axis in the room of Trăncănici at least once. Your mission is to tell the fleas whether this is possible or not. 

## Input data

The input file `purice2.in` contains on the first line the natural number $T$, representing the number of tests. For each test, the first line will contain the natural number $N$, representing the number of fleas. The second line will contain $N$ integers, representing the initial coordinates of the fleas. 

## Output data

The output file `purice2.out` will contain $T$ lines, each line $i$ out of the $T$ containing the answer for the $i$-th test: $1$ if the fleas can entirely cover the $Ox$ axis, $0$ otherwise. 

## Constraints and clarifications

$1 \leq T \leq 100$ 

$3 \leq N \leq 50$ 

$-10^9 \leq P[i] \leq 10^9$ 

For 30% of the tests, $N = 3$ 

## Example

`purice2.in`

```
2
3
1 2 3
3
1 3 5
```

`purice2.out`

```
1
0
```
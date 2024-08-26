## Task

Por Costel and the Firecracker

One evening, Por Costel, the most famous of the pigs, went for a walk. He was calmly walking on the sidewalk when a firecracker exploded next to him. As any pig would, he had the defensive reaction of starting to squeal desperately and run along the sidewalk. Although Por Costel's movement along the sidewalk seems random, upon closer inspection, we observe a certain pattern. Let's consider the street divided into positions indexed from $1$ to $N$. Por Costel is at position $P$ at time $t=0$. If at time $t$, Por Costel is at position $x_t$, at time $t+1$ Por Costel will be at position $(a \cdot x_t + b) \bmod N$. To be prepared for the situation where Por Costel jumps panicked into the middle of the street (God forbid!), his fans implore you to be able to say at any moment where he is. A query signifies the question "What position is Por Costel in at time $q$?" The queries will be as random as Por Costel's movement. You will be given the initial query $q_0$ and the other queries are generated as follows: if we have just answered the question $q_i$, the query $q_{i+1}$ will be $q_{i+1} = (k \cdot q_i + x_{q_i}) \bmod N$ where $x_{q_i}$ is the answer to the query $q_i$.

## Input data

In the input file `pocnitoare.in`, the first line contains $N$, $a$, $b$, $P$ (Por Costel's initial position), $M$ (the number of queries), $q_0$ (the initial query).

## Output data

In the output file `pocnitoare.out`, there will be $M$ lines, with the answer to the $i$-th query on line $i$.

## Constraints

$2 \leq N \leq 10^9$ 

$0 \leq a, b \leq N-1$ 

$1 \leq P \leq N$ 

$1 \leq M \leq 10^6$ 

$1 \leq q_0 \leq 10^9$ 

$k$ represents the remainder of the division of $a$ by $5$. Be careful with the memory limit!

## Example

`pocnitoare.in`

```
17 3 7 1 3 1
```

`pocnitoare.out`

```
1
14
6
```
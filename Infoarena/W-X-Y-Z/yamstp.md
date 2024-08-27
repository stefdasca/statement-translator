# Yamstp

Let $G$ be an undirected complete graph with $N$ nodes. Each node $V$ has an associated value, denoted by $Val[V]$. The cost of the edge between node $V$ and node $W$ is given by the value of the expression $Val[V] \operatorname{xor} Val[W]$, where $\operatorname{xor}$ denotes the bitwise "exclusive or" operation. The task is to calculate the cost of the minimum spanning tree (MST) of $G$.

## Input data

The input file `yamstp.in` will contain on its first line the number of test cases $T$. There will follow $T$ tests, the structure of a test being as follows: the first line contains $N$, the number of nodes of $G$. The next line contains $N$ integers which constitute the array $Val$.

## Output data

The output file `yamstp.out` will contain $T$ lines, each line containing the answer for the respective test.

## Constraints and clarifications

$$1 \leq T \leq 100$$
$$1 \leq N \leq 25 \ 000$$
$$0 \leq Val[i] \leq 2^{20} - 1$$
The sum of the values of $N$ in the same input file will be at most 250 \ 000.

## Example

`yamstp.in`
```
2
4
2 5 3 7
3
1 1 1
```
`yamstp.out`
```
7
0
```

## Explanation

It's known.
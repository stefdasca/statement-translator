## Task

You are given a number $T$ representing the number of tests. On each of the following $T$ lines, there is a sequence consisting only of the values $0$ and $1$. For each sequence $s$ of length $L$, determine its lexicographical order if we consider all sequences of length $L$ formed only from the values $0$ and $1$.

## Input data

The input file `kbiti.in` will contain the number of tests on the first line. The following $T$ lines will contain a sequence formed from the digits $0$ and $1$.

## Output data

In the output file `kbiti.out`, $T$ numbers will be displayed, one on each line. On the $i$-th line of the output file, the lexicographical order number of the sequence on the $i$-th line of the input file will be printed, considering all possible sequences of the same length in lexicographical order.

## Constraints and clarifications

$1 \leq T \leq 100\ 000$

$1 \leq Length\ of\ the\ sequence\ s \leq 32$

## Example

`kbiti.in`
```
4
1
101 
0
111110
```

`kbiti.out`
```
2
6
1
63
```
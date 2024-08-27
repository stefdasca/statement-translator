Hprob

In a store, there are $4$ objects ($A$, $B$, $C$, and $D$) arranged in a certain order. The store is visited sequentially by $N$ customers. Each customer looks at the objects and tries them. After looking at and trying them, they attempt to place them back in the correct order, but - of course - they no longer remember the exact order in which they found them. For each customer, there is a probability $p1$ that they will place all objects circularly permuted to the right by one position relative to the original order. If the initial order of the objects was ($A$, $B$, $C$, and $D$), in the end, it will be ($D$, $A$, $B$, and $C$). For each customer, there is a probability $p2$ that they will arrange the objects in the reverse order of the original. If the initial order of the objects was ($A$, $B$, $C$, and $D$), in the end, it will be ($D$, $C$, $B$, and $A$). For each customer, there is a probability $p3$ that they will arrange the objects by swapping the order of the middle ones. If the initial order of the objects was ($A$, $B$, $C$, and $D$), in the end, it will be ($A$, $C$, $B$, and $D$). For each customer, there is a probability $p4 = 1.0 - p1 - p2 - p3$ that they will place the objects back in the original order.

## Task

Given the number $N$ of customers, calculate the probability that after all of them have tried the objects sequentially, their final order will be identical to the original one.

## Input data

The first line of the input file `hprob.in` will contain the number $T$ of tests, followed by $T$ lines, each containing the number $N$ of customers, followed by $3$ real numbers, $p1$, $p2$, and $p3$ with the meanings described above.

## Output data

The output file `hprob.out` will contain $T$ lines, each containing a real number rounded to $5$ decimal places depending on the $6$-th, representing the required probability.

## Constraints and clarifications

$0 \leq N \leq 1\ 000\ 000\ 000$ 

$1 \leq T \leq 6$ 

$0 \leq p1, p2, p3 \leq 1$ 

$0 \leq p1 + p2 + p3 \leq 1$ 

## Example

`hprob.in` 

```
6
0 0.1 0.2 0.3
1 0.1 0.2 0.3
10 0.1 0.2 0.3
100 0.1 0.2 0.3
1000 0.1 0.2 0.3
1000000000 0.1 0.2 0.3
```

`hprob.out`

```
1.00000
0.40000
0.09719
0.04167
0.04167
0.04167
```
## Task

Pig Costel got a job at a railway company and, as a trustworthy pig, he was tasked with distributing the tickets for the seats in a single train. The train in question has $N$ seats, with $N$ even, and the $N$ seats are arranged in $\frac{N}{2}$ rows, two per row, as follows: $1$ $2$ $3$ $4$ $\dots$ $N-1$ $N$. Passengers have already started ordering tickets. There are $M$ orders and Pig Costel observes that these are of 3 types:
- order for $1$ person (a random seat needs to be reserved)
- order for $2$ persons (2 seats on the same row need to be reserved)
- order for $3$ persons (2 seats on the same row and another seat on an adjacent row need to be reserved). Pig Costel must respond to any order of $x$ persons by displaying $x$ seats that meet the requested conditions and, obviously, have not been previously distributed to anyone else. The trip is very important and it is announced that the train will be almost full. Pig Costel urgently needs your help to avoid losing this job as well!!!

## Input data

The input file `trenul.in` contains on the first line 2 integers separated by a space, $N$ and $M$, with the aforementioned meanings. The next $M$ lines contain a number $x$ from the set $\{1, 2, 3\}$ which designates the number of seats ordered at each step.

## Output data

The output file `trenul.out` must contain $M$ lines. On the line with number $i$, it must contain Pig Costel’s response to the $i$-th order from the input file. If an order $i$ was of type $x$, then the line with index $i$ must contain $x$ numbers separated by a space.

## Constraints and clarifications

$1 \leq N \leq 10^5$ 

$1 \leq M \leq 10^5$

The total number of people served in the $M$ orders $\leq N$

## Example

`trenul.in`
```
6 2
3
2
```

`trenul.out`
```
1 2 4
5 6
```
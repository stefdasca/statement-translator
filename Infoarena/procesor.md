# Processor

You have a processor and $N$ processes that need to be executed on this processor. The runtime of each process is exactly one second, and the processor can execute at most one process at any given moment in time. Starting from time zero, you need to decide which processes will run on the processor and at what moments in time. If a process $i$ starts execution later than time $T_i$ (at a moment in time greater than or equal to $T_i$), a penalty $P_i$ will be applied. You need to calculate the minimum possible total penalty.

## Input data

The input file `procesor.in` will contain on the first line the natural number $N$, having the significance from the statement. Then follow $N$ lines, on the $i+1$ line there are, separated by a single space, two values $T_i$ and $P_i$.

## Output data

The output file `procesor.out` will contain a single value, the minimum possible total penalty.

## Constraints and clarifications

$1 \leq N \leq 100\,000$

$1 \leq T_i \leq 1\,000\,000$

$1 \leq P_i \leq 1\,000\,000\,000$

## Example

`procesor.in` 
```
3
1 10
1 5
4 4
```

`procesor.out` 
```
5
```

## Explanation

One possible solution is as follows: at time $0$, the first process starts execution. Then at time $1$, the third process starts execution. At time $2$, the second process starts execution, for which a penalty of $5$ is applied.
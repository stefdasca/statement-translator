# Proc2

We have a computer with $N$ processors. There are $M$ tasks that need to be executed, each having a start time $S_i$ and a processing duration $D_i$. Tasks must be executed in chronological order and each task must be executed on the processor with the smallest available index at time $S_i$.

## Task

You need to calculate which processor will execute each task.

## Input data

The input file `proc2.in` contains on the first line the values $N$ and $M$. The next $M$ lines contain two numbers $S_i$ and $D_i$ separated by spaces, as described.

## Output data

The output file `proc2.out` must contain $M$ lines. On line $i$, it must contain the index of the processor that executes task $i$.

## Constraints and clarifications

$1 \leq N \leq 1\,000\,000$

$1 \leq M \leq 100\,000$

For any $i$ between $1$ and $M$, $1 \leq S_i \leq 2\,000\,000\,000$

$1 \leq S_i + D_i \leq 2\,000\,000\,000$

For any $i$ between $1$ and $M-1$, $S_i < S_{i+1}$

It is guaranteed that each task can be executed.

The processor that executes task $i$ is busy during the time intervals $[S_i, S_i + D_i)$

## Example

`proc2.in`
```
3 3
1 2
2 3
3 3
```

`proc2.out`
```
1
2
1
```

## Explanation

At time $1$, processors $1, 2, 3$ are available. Therefore, task $1$ will be executed by processor $1$. At time $2$, processors $2, 3$ are available. Therefore, task $2$ will be executed by processor $2$. At time $3$, processors $1, 3$ are available. Therefore, task $3$ will be executed by processor $1$.
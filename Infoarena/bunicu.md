Grandfather

Grandfather thought of surprising grandmother with a binary string of length $N$. Thus, the $N$ grandchildren gathered and each created a binary string of length $N$. When they went to ask grandfather if the strings were good, grandfather smiled and after $3$ seconds he said: "NOOOOO!!!". The conclusion was that the $N$ grandchildren must find a different $N+1$-th binary string of length $N$. Help the grandchildren find such a string (they are also kind souls).

## Input data

The input file `bunicu.in` will contain on the first line a natural number $T$, the number of tests. The next lines will contain the $T$ sets of tests: each set starts with a line containing $N$. The next $N$ lines will be the $N$ binary strings of length $N$.

## Output data

The output file `bunicu.out` will contain $T$ lines. The line $i$ will print the $N+1$-th binary string of length $N$ for the $i$-th set.

## Constraints and clarifications

$1 \leq T \leq 5$ 

$1 \leq N \leq 1000$ 

Be careful of the memory limit! Try to solve the problem with $O(n^2)$ time and $O(1)$ memory.

## Example

`bunicu.in`

```
1
3
000
010
110
```

`bunicu.out`

```
100
```
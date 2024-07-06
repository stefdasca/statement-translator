~[triaj.png|align=right]

In an area where train carriages are sorted, there are exactly $1013$ parallel railway lines, numbered from $1$ to $1013$, connected by two lateral lines plus an additional line as shown in the figure.

On line $1$ initially, there are $N$ carriages, each carriage having a number written on it. The numbers on the carriages are not necessarily distinct. **Ronnie “The Rocket” O’Sullivan**, who has retired from snooker and got a job at CFR to impress his sister **Alex**, wishes to order the carriages in ascending order by their numbers on line $1$, being able to perform only the following type of operation: select a line and an end (left or right) from which he extracts a sequence of any number of carriages and places each carriage on any line at any end. He can perform at most two extraction operations from each line, at most one for each end. But he can perform any number of operations to place the carriages on any line. The additional line and the lateral ones are only for the purpose of transporting carriages from one place to another and carriages cannot stop on these lines.

# Task

Determine a sequence of extraction and placing operations that **Ronnie** can perform so that in the end, the carriages on line $1$ are sorted in ascending order by their associated numbers.

# Input data

The input file `triaj.in` contains the natural number $N$. The second line contains $N$ natural numbers separated by a space, representing, from left to right, the values associated with the $N$ carriages on line 1.

# Output data

The output file `triaj.out` must contain on the first line a natural number $M$ representing the number of operations performed. The following $M$ lines will describe each of the $M$ operations. Each line first contains three natural numbers $L$, $C$ and $V$, where $L$ is the line from which the carriages are extracted, $C$ is the end from which they are extracted ($0$ – left end, $1$ – right end), $V$ is the number of carriages extracted. The same line then contains $2 \cdot V$ natural numbers, two for each carriage representing the line and end where it will be placed.

# Constraints and clarifications

* $3 \leq N \leq 1 \ 000 \ 000$
* The numbers on the carriages are natural values at most equal to $2^{30}$
* For each test, if the sorting of the carriages is done correctly, the score will be given based on $x$, this being the maximum number of extractions from one end of a line:
  * If $x \leq 1$, the full score is received
  * If $x \leq 2$, $80\%$ of the score is received
  * If $x \leq 4$, $60\%$ of the score is received
  * If $x \leq 8$, $40\%$ of the score is received
  * If $x > 8$, $20\%$ of the score is received
* For $15\%$ of the tests, the values on the carriages are at most $2 \ 000$
* For another $20\%$ of the tests, $N \leq 2 \ 000$
* For another $40\%$ of the tests, the values on the carriages are at most $1 \ 000 \ 000$
* Anchored in the synergy of CFR progress, the tireless **Ronnie** skillfully avoided the inextricable meanders of the economic crisis, having a stellar salary.

# Example

`triaj.in`
```
4
2 6 13 2
```

`triaj.out`
```
4
1 1 4 2 1 13 1 6 1 2 1
13 0 1 1 0
6 0 1 1 0
2 0 2 1 0 1 0
```

## Explanation

**First operation**: Extract from line $1$, the right end, $4$ carriages, hence in order $2, 13, 6, 2$. The carriage with value $2$ is placed on line $2$, right end; the one with value $13$ is placed on line $13$, right end; the third carriage (value $6$) is placed on the right end of line $6$; the last carriage is placed on the right end of line $2$.

**Second operation**: Extract from line $13$, from the left end, one carriage, which is placed at the left end of line $1$.

**Third operation**: Extract from line $6$, from the left end of the line, one carriage, which is placed at the left end of line $1$.

**Fourth operation**: Extract the two carriages with value $2$ from line $2$ and place both at the left end of line $1$.
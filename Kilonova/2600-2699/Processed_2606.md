**English Translation:**

The Romanian Institute of Psychology has received much more state funding after recent legislative changes. A renowned scientist wants to conduct a study on how people make decisions within a social group they are not part of. He randomly chose $N$ people and involved them in a test that proceeds as follows:
- There are $N$ seats in a row.
- There are $N$ people numbered from $1$ to $N$.
- The $N$ people come one after another to occupy the seats according to the following *rules*:
  - the first person sits in the middle of the row;
  - the second person (if there is one) chooses the seat furthest from $1$;
  - the third person (if there is one) chooses the seat furthest from $1$ and $2$;
  - each following person will choose the longest interval of unoccupied seats, and within such an interval they will choose a seat so that the minimum distance to any occupied seat is maximized.

# Task
Determine the number of ways $N$ people can be seated according to the rules stated.

# Input data
The input file `studiu.in` contains on the first line the natural number $N$.

# Output data
The output file `studiu.out` will contain on the first line the number of ways the $N$ people can be seated. Because this value can be very large, the result should be displayed modulo $1\ 000\ 000\ 007$.

# Constraints and clarifications
- $1 \leq N \leq 100\ 000\ 000$
- Two sequences of $N$ people $A$ and $B$ are considered different if at some position $i$ the numbers associated with the respective people differ in the two sequences ($A_i \neq B_i$).

|#| Score | Constraints                                     |
|-|-------|------------------------------------------------|
|1| 13    | $1 \leq N \leq 100\ 000$ and $N$ is odd         |
|2| 13    | $1 \leq N \leq 100\ 000$ and $N$ is even        |
|3| 18    | $100\ 001 \leq N \leq 10\ 000\ 000$ and $N$ is odd |
|4| 18    | $100\ 001 \leq N \leq 10\ 000\ 000$ and $N$ is even |
|5| 38    | No additional constraints                       |

# Example 1
`studiu.in`
```
3
```
`studiu.out`
```
2
```
## Explanation
$N = 3$: $|2|1|3|$, $|3|1|2|$

# Example 2
`studiu.in`
```
5
```
`studiu.out`
```
4
```

## Explanation
$N = 5$: $|2|4|1|5|3|$, $|2|5|1|4|3|$, $|3|4|1|5|2|$, $|3|5|1|4|2|$
NREcou

Wanting to invent something new, Mate invented the "echo" numbers. A natural number $A$ is called an echo-number if there exists a natural number $B$ with the property that the number $A$ can be obtained by concatenating the number $B$ a certain number of times (at least two times). For example, the number $313313$ is an echo-number, but $31313$ is not an echo-number.

## Task

Mate proposed to find out how many echo-numbers are among the natural numbers that have exactly $N$ digits. Since this number can be very large, only the remainder of the result when divided by $10^9+17$ will be displayed.

## Input data

The input file nrecou.in contains, on the first line, the number $N$.

## Output data

In the output file nrecou.out, the first line will contain the required value.

## Constraints and clarifications

for 20% of the tests $1 \leq N \leq 6$

for another 20% of the tests $N \leq 12$

for another 30% of the tests $N \leq 10^4$

for another 30% of the tests $N \leq 10^6$

## Example

```
nrecou.in

3
```

```
nrecou.out

9
```

## Explanation

The three-digit echo-numbers are $111$, $222$, $333$, $444$, $555$, $666$, $777$, $888$, $999$.
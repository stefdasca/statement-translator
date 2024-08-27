## Task

Two numbers $N$ and $P$ are given. Consider a string of length $N$ (indexed from position $1$ to $N$), filled with $0$s. The money boss knows that he has chosen $P$ distinct positions where he changed $0$ to $1$. His question is whether the newly formed string is periodic or not (a string is called periodic if it can be obtained by repeatedly concatenating one of its prefixes, with a length strictly smaller than the length of the string; For example, "101010" is periodic because it has the period "10", but "10011" is not periodic). If it is periodic, the length of its smallest period will be displayed, otherwise $-1$ will be displayed.

## Input data

The input file `perioada01.in` will contain on the first line 2 numbers $N$ and $P$. The next line will contain $P$ numbers, representing the distinct positions where the changes have been made (from $0$ to $1$).

## Output data

The output file `perioada01.out` will contain a single number: $-1$ if the string is not periodic and $minLength$ if the string is periodic (where $minLength$ represents the length of the smallest period).

## Constraints and clarifications

$2 \leq N \leq 1\ 000\ 000\ 000$  
$1 \leq P \leq \leq 1\ 000\ 000$  

For 20% of the tests, $N \leq 100\ 000$  
For another 20% of the tests, $N \leq 10\ 000\ 000$ and $P \leq 100$  
For another 20% of the tests, $P \leq 100\ 000$  
Positions are given in ascending order  
$P \leq N$

## Example

`perioada01.in`  
```
999999999 3  
1 333333334 666666667
```

`perioada01.out`  
```
333333333
```
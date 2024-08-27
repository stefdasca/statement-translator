## Matching

Since summer has arrived and you have less and less desire to code, we have prepared a sadistic problem for you, and moreover, we accept barbaric solutions!!! You are given two character strings $A$ and $B$. You are asked to find the first occurrence of $B$ in the string $A$. Note: the string $B$ can contain, besides the lowercase letters of the English alphabet, the character '*'. This can be replaced with any subarray of characters (even with the empty one).

## Input data

The input file `potrivire.in` will contain two integers $N$ and $M$, representing the length of string $A$ and respectively $B$. The next two lines will contain the two strings $A$ and $B$.

## Output data

The output file `potrivire.out` will contain two integers, $left$ and $right$, representing the starting and ending positions of the subarray of string $A$ that matches the string $B$. If there are multiple solutions, you are requested to print the one with the smallest $left$, and in case of equality, the one with the smallest $right$.

## Constraints and clarifications

$1 \leq N$

$M \leq 10\ 000$

the number of '*' characters is less than or equal to $30$

character strings are indexed starting with position $1$

in case there is no solution, print $-1$

## Example

`potrivire.in`
```
8 5
zxabedgh
ab*gh
```

`potrivire.out`
```
3 8
```


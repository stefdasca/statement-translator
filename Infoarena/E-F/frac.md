Frac

Patratel is very passionate about fractions. One day, he thinks of writing on a piece of paper, in ascending order, all the irreducible fractions with the denominator $N$. Realizing in time that there are an infinite number of such fractions, he does not bother anymore and wants to find only the $P$-th fraction in the sequence he had in mind.

## Task

Determine the numerator of the $P$-th fraction in the sequence constructed according to the above rules.

## Input data
The first line of the file `frac.in` contains two integers $N$ and $P$, separated by a space, with the meaning described in the statement.

## Output data
The first line of the file `frac.out` contains a natural number that represents the numerator of the $P$-th fraction in the sequence of irreducible fractions with the denominator $N$.

## Constraints and clarifications
$1 \leq N \leq 12\,000\,000\,000$ (12 billion)

$1 \leq P \leq 10^{14}$

It is guaranteed that the result will not exceed $2^{61}$

## Example

`frac.in` 
```
12 5
``` 

`frac.out` 
```
13
```

## Explanation

The fractions of the sequence are: $1/12$, $5/12$, $7/12$, $11/12$, $13/12$, $17/12$, $\dots$

The 5th fraction in this sequence is $13/12$ and has the numerator $13$.
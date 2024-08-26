## Task

You arrive at the algorithm laboratory. Nobody says anything. The lab assistant has his feet on the table, sunglasses on his eyes, and looks melancholically out the window. It's clear he came from the club and is trying to create a lab assignment on the spot. Finally, he says: You are given a sequence of $N$ brackets. In how many ways can you choose two disjoint and non-empty subarrays, $A$ and $B$, with $A$ to the left of $B$, such that the string obtained by concatenating the string $A$ with $B$ forms a valid parenthesization? A valid parenthesization is defined as follows:

- The empty string is valid.
- If the string $A$ is valid, then the string $(A)$ is also valid.
- If the strings $A$ and $B$ are valid, then the string $A$ concatenated with $B$ is valid.

## Input data

The input file `brackets2.in` contains on the first line the number $T$ of tests. The next $T$ lines contain one sequence of brackets each.

## Output data

The output file `brackets2.out` contains $T$ lines, each containing a number equal to the answer to the question in the statement for the corresponding sequence.

## Constraints and clarifications

$1 \leq T \leq 25$

$1 \leq N \leq 1\,500$

For at least 18 tests, $1 \leq N \leq 100$

A subarray of a string is a subsequence of consecutive elements of that string.

## Example

`brackets2.in`

```
1
(())
```

`brackets2.out`

```
7
```
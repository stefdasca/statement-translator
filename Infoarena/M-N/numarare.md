# Counting

Miruna has an array of $N$ numbers. She calls a subarray $S$ of length $2*K$ interesting if $S[i] + S[j] = S[i+1] + S[j-1] = \dots = S[i+K-1] + S[j-K+1]$ (we consider the subarray $S$ to be located between indices $i$ and $j$, $i \leq j$). Miruna wants to know how many interesting subarrays her array contains.

## Task

## Input data

The input file `numarare.in` contains:
- The first line contains a single natural number $N$ representing the length of the array.
- The second line contains the elements of the array, separated by space.

## Output data

In the output file `numarare.out` you will print the number of interesting subarrays.

## Constraints

$ 1 \leq N \leq 100\ 000 $

$ -100\ 000 \leq S[i] \leq 100\ 000 $

## Example

`numarare.in`

```
4
1 2 3 4
```

`numarare.out`

```
4
```

## Explanation

The 4 subarrays are: $1 2$, $2 3$, $3 4$, $1 2 3 4$
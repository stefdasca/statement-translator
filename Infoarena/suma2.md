## Task

The math teacher gave Gigel a sequence of $N$ integers, from the interval $[-10000, 10000]$, and asked him to find a subsequence of it, such that no two elements of it are on consecutive positions in the initial sequence and the sum of the subsequence is maximum. Write a program that solves Gigel's problem.

## Input data

The first line of the file `suma2.in` contains the number $N$ of elements of the sequence. The next line contains $N$ integer values (the elements of the sequence), separated by spaces.

## Output data

In the file `suma2.out` you will print the maximum sum of a subsequence of the given sequence that has the above-mentioned property.

## Constraints and clarifications

$1 \leq N \leq 200\ 000$ 

The subsequence may contain no elements.

## Example

`suma2.in`
```
7
3 7 5 -1 6 6 2
```

`suma2.out`
```
16
```

## Explanation

The subsequence with the sum $16$ contains the elements at positions: $1, 3, 5, 7$.
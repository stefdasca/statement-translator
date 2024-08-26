Invsc

Gigel had just learned at school the algorithm for calculating the longest increasing subsequence of an array of natural numbers. He liked it so much that he spent several days applying this algorithm to multiple arrays of numbers (distinct from each other). For this, he used an auxiliary array $v$ with the significance $v_i$ = the length of the longest increasing subsequence in the initial array that ends at position $i$ (obviously, the result was represented by the maximum from this array). Wanting to get a good grade for his effort, $e$ wanted to show his computer science teacher all his calculations. However, just before Gigel left home, his sister Georgiana took all the papers with the arrays on which he had applied the newly learned algorithm and tore them into pieces. Thus, Gigel was left with only the papers with the auxiliary arrays he had used.

## Task

Not having time to reassemble all the papers, Gigel needs your help to reconstruct the initial arrays.

## Input data
The first line of the input file invsc.in will contain the non-zero natural number $N$ representing the length of an array on which Gigel applied the newly learned algorithm. The next $N$ lines contain the auxiliary array $v$ calculated by Gigel.

## Output data
The output file invsc.out will contain the initial array from which Gigel started, that is, $N$ non-zero natural numbers, each with a maximum of 8 digits, each number on a separate line.

## Constraints and clarifications

$N \leq 200\\ 000$

It is guaranteed that for each test there will be at least one solution.

If there are multiple solutions, any of them can be printed.

## Example

`invsc.in`

```
5
1
2
2
2
3
```

`invsc.out`

```
5
10
7
6
12
```
# Munte7

A sequence of $N$ natural numbers is given, which must be transformed into a "mountain" form. A sequence has a mountain form if there exists $1 \leq i \leq n$ such that:
- for any $j$, $1 \leq j < i$, $v[j] \leq v[j + 1]$
- for any $k$, $i \leq k < n$, $v[k] \geq v[k + 1]$

In other words, a sequence has a mountain form if it is increasing up to a position $i$ and then decreasing until the end.

## Task

Calculate the minimum number of elements that need to be modified for the sequence to have a mountain form.

## Input data

The input file `munte7.in` contains on the first line the number $N$ = the number of elements in the sequence. The second line will contain the $N$ numbers of the sequence.

## Output data

The output file `munte7.out` will contain on the first line the number of modifications required to give the sequence a mountain form.

## Constraints

$2 \leq N \leq 200000$

The elements of the sequence are integers with an absolute value $\leq 10^9$

For 40% of the tests $N \leq 2000$

For the remaining 60%, $N \leq 200000$

## Example

`munte7.in`
```
7
-1 2 3 -1 3 2 1
```

`munte7.out`
```
1
```

## Explanation

If we change the element at position 4 to 3, then the sequence becomes $-1 2 3 3 3 2 1$ and it has a mountain form.

`munte7.in`
```
9
1 5 4 7 6 8 3 5 2
```

`munte7.out`
```
3
```

We change the element at position 3 to 6, the element at position 5 to 7, and the element at position 7 to 6. The sequence becomes $1 5 6 7 7 8 6 5 2$, so it is a "mountain" with a peak at position 6.
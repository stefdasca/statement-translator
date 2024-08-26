## Task

Johnie has a binary array of $N$ elements. He can extract a certain subarray from the array, thus remaining with a smaller array. Then, he can insert the extracted subarray at any position in the resultant array. The task is to determine the maximum length of a subarray filled with $1$s that Johnie can obtain if he performs a single operation.

## Input data

The input file `maxsecv.in` contains:

- The first line contains $N$, the size of the array. 
- The next line contains $N$ numbers, $0$s and $1$s, representing the elements of the array.

## Output data

The output file `maxsecv.out` must contain a single number, representing the required value.

## Constraints and clarifications

$1 \leq N \leq 1\ 000\ 000$

## Example

`maxsecv.in`
```
6
1 1 0 1 1 1
```

`maxsecv.out`
```
5
```

`maxsecv.in`
```
13
0 1 1 1 0 1 1 1 1 0 1 1 0
```

`maxsecv.out`
```
7
```

## Explanation

In the first example, Johnie can move the subarray formed by the last $3$ elements of the array to the beginning, obtaining a subarray formed by $5$ of $1$s. In the second example, Johnie can select the sequence of $4$ of $1$s from the middle of the array and move it next to the sequence of $3$ of $1$s at the beginning.
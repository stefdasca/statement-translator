# Minimum

Consider an array of $n$ integers. The problem focuses on subarrays. Note that the elements of a subarray have consecutive indices in the considered array.

## Task

Determine the subarray with the minimum sum that has the smallest length. If there are multiple such subarrays, eliminate the one that has the smallest starting index. Eliminate this subarray from the array, then determine another subarray of minimum length among those with the minimum sum among the remaining elements in the array. Continue this process until the array becomes empty.

## Input data

The first line of the file `minim.in` contains the natural number $n$, representing the size of the array. The following $n$ lines each contain an integer.

## Output data

The output file `minim.out` will contain $k$ triplets, where $k$ is the number of detected subarrays. A triplet on the $i$-th line of the file consists of the numbers $s$, $p$, $u$, where $s$ represents the sum of the $i$-th subarray, $p$ represents the index of the first element of the subarray, and $u$ is the index of the last element of the subarray. Indices $p$ and $u$ are indices of the respective elements in the original array. The three numbers will be separated by a space.

## Constraints and clarifications

$5 \leq n \leq 1000$

$-10000 \leq nr[i] \leq 10000$ $(i = 1, 2, \dots, n)$

## Example

`minim.in`

```
10
6
-8
-2
-4
-6
20
-10
-3
12
-19
```

`minim.out`

```
-20 2 5
-19 10 10
-10 7 7
-6 5 5
-4 4 4
-3 8 8
-2 3 3
6 1 1
12 9 9
20 6 6
```
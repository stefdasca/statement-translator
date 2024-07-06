## Given text translated to English:

A sequence of `N` integers denoted by `A` is given. A *subarray* of the sequence `A` is a sequence $A_i A_{i+1} A_{i+2} \ldots A_j$ with `1 \\leq i \\leq j \\leq N`, and the length of this subarray is equal to `j - i + 1`. An *operation* consists of selecting a subarray from the sequence and deleting it. In an operation, **the length of the selected subarray must be a power of `2`**. Throughout all operations performed on the sequence, **the lengths of the deleted subarrays must be distinct**.

For each subarray in the sequence, we consider the sum of its elements. We define the *cost* of a sequence as the maximum of these sums if the sequence contains at least one positive number; otherwise, the cost of the sequence is `0`.

We can apply a succession of operations (possibly none) to the sequence `A`. As a result of these operations, certain elements of the sequence will be deleted, thus obtaining a set of sequences $M=\\{A, A'_{1}, A'_{2}, A'_{3}, ...\\}$.

## Task
Determine the maximum possible cost that can be obtained from a sequence in the set `M`.

## Input data
The first line of the input file `recyclebin.in` contains an integer `N`.
The second line contains `N` integers, separated by a space, representing the values of the sequence `A`.

## Output data
Print the value of the maximum cost on the first line of the output file `recyclebin.out`.

## Constraints and clarifications
* `1 \\leq N \\leq 1000`
* $-10^6 \\leq A_i \\leq 10^6$ for `1 \\leq i \\leq N`
* For tests worth `10` points `1 \\leq N \\leq 30`
* For other tests worth `15` points it is guaranteed that there is a solution with at most one operation performed
* For other tests worth `20` points it is guaranteed that there is a solution with at most two operations performed
* `10` points are awarded by default.

## Example

`recyclebin.in`
```
14
13 -19 13 -5 -12 11 20 4 -10 1 -7 19 -19 3
```
`recyclebin.out`
```
76
```

Explanation
---

The initial sequence is:
`[13 -19 13 -5 -12 11 20 4 -10 1 -7 19 -19 3]`

From position `8` delete `4` elements, the resulting sequence is
`[13 -19 13 -5 -12 11 20 19 -19 3]`

From position `4` delete `2` elements, the resulting sequence is
`[13 -19 13 11 20 19 -19 3]`

From position `2` delete one element, the resulting sequence is
`[13 13 11 20 19 -19 3]`

The subarray with the maximum sum in the final sequence is
`[13 13 11 20 19]`

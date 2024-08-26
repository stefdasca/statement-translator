## Task

You are given an array with $N$ numbers which contains exactly once all numbers from $1$ to $N$ (a permutation of the set $1, 2, \dots, N$). We want to sort the given array in two steps.

In step 1, the array is divided into subarrays such that each element of the initial array belongs to exactly one subarray.

The elements within the same subarray must maintain the same relative order as in the initial array.

In step 2, from the existing subarrays at a given moment, two are chosen, one is placed at the end of the other, then the two chosen arrays are eliminated and the resulting one is placed instead.

For each such operation performed in the second step, the cost is $1$.

Determine the total minimum cost required to sort the given array in ascending order in the manner described above.

## Input data

The first line of the file `sortare2.in` contains a natural number $N$, representing the size of the permutation.

The second line contains the elements of the permutation separated by single spaces.

## Output data

The first line of the file `sortare2.out` contains a number that represents the required minimum cost.

## Constraints

$1 \leq N \leq 100000$

## Example

`sortare2.in` `sortare2.out`
``` 
4 
4 1 3 2 
2 
``` 

## Explanation

In the case of the first example, we can form

3 subarrays: $(4)$, $(1, 2)$, $(3)$.

We can place the subarray $(4)$ at the end of the subarray $(3)$ and remain with the subarrays: $(1, 2)$, $(3, 4)$.

Then, placing the array $(3, 4)$ at the end of the array $(1, 2)$, we obtain the sorted permutation.
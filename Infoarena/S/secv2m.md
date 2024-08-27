## Task

Ingrid has another problem to solve with sequences. She has two arrays of integers of length $N$ and respectively $M$. She wants to find two subarrays of length $L$, one from the first array and the other from the second array, $A_{i1}$ , $A_{i2}$ , $\dots$ , $A_{iL}$ and $B_{j1}$ , $B_{j2}$ , $\dots$ , $B_{jL}$ such that $\max(A_{i1} + B_{j1}, A_{i2} + B_{j2}, \dots, A_{iL} + B_{jL})$ is as small as possible.

## Input data

The input file `secv2m.in` will contain on the first line the numbers $N$, $M$ and $L$. The second line contains $N$ integers representing the first array, and the third line contains $M$ integers representing the second array.

## Output data

In the output file `secv2m.out` you will print on the first line the minimum required value. The second line will contain the starting position of the first subarray and the starting position of the second subarray separated by a space. If there are multiple solutions, choose the one where the first subarray has the smallest starting position. If there are still multiple solutions in this case, choose the solution where the second subarray has the smallest starting position.

## Constraints and clarifications

$1 \leq L \leq N$ 

$M \leq 2000$ 

All numbers in the input file are between $0$ and $10^8$

## Example

`secv2m.in` 
```
5 7 3 
4 3 4 2 2 
3 1 3 2 5 3 2
```

`secv2m.out`
```
5 
1 2
```

## Explanation

The chosen subarrays are: 

`4 3 4 2 2` and `3 1 3 2 5 3 2` 

(Note, subarrays are required, not subsequences).
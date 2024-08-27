## Task

Given an array $A = (a_1, a_2, \dots, a_N)$ consisting of $N$ integers, as well as $M$ pairs of numbers $(x, y)$. For each pair of indices $(x, y) \ (1 \leq x \leq y \leq N)$, you need to determine the subarray with the maximum sum within the subarray $a_x, a_{x+1}, \dots, a_y$.

## Input data

The input file `sequencequery.in` will contain two integers $N$ and $M$ on the first line. The next line will contain $N$ integers separated by a space. These will represent the numbers $a_1, a_2, \dots, a_N$. The following $M$ lines will each contain a pair of two numbers separated by a space. These will indicate the pairs of indices for which the maximum subarray sums need to be determined.

## Output data

The output file `sequencequery.out` will contain $M$ lines. Each of these lines will contain an integer representing the sum of the elements in the optimal subarray according to the criteria stated in the problem.

## Constraints and clarifications

$1 \leq N, M \leq 100\ 000$  
$-100\ 000 \leq a_i \leq 100\ 000$  
The chosen subarrays must contain at least one element. 

## Example

`sequencequery.in`  
```
8 3  
-1 2 3 -2 4 -3 8 -3  
1 5  
4 8  
6 6  
```

`sequencequery.out`  
```
6  
7  
8  
```

## Explanation

The selected subarrays for each query are highlighted:

`[-1 2 3 -2 4] -3 8 -3`  
`-1 2 3 [-2 4 -3 8 -3]`  
`-1 2 3 -2 4 [-3] 8 -3`
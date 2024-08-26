# Split2

Given an array $V$ with $N$ natural numbers, we want to partition it into $M$ subarrays of even length. The cost of a subarray is equal to the maximum of the sum of the elements in the first half and the sum of the elements in the second half of the subarray. The total cost of a partitioning is equal to the maximum cost of any subarray. Compute the minimum total cost that can be obtained by partitioning the array $V$.

## Input data

The input file `split2.in` contains on the first line $T$, the number of tests. Next, each test contains 2 lines. The first line contains $N$ and $M$. The second line contains the $N$ numbers of the array $V$.

## Output data

The output file `split2.out` will contain on separate lines the required result for each of the $T$ tests.

## Constraints and clarifications

$1 \leq T \leq 50$ 

$1 \leq M \leq N \leq 1000$ 

$1 \leq V[i] \leq 10000$ 

$N$ is even.

It is guaranteed that there exists a partition into $M$ intervals

## Example

`split2.in`

```
1
10 3
1 2 4 2 4 5 2 2 1 3
```

`split2.out`

```
6
```

## Explanation

1 2 4 2 | 4 5 | 2 2 1 3 

First subarray 1 2 4 2 has cost 6. 

Second subarray 4 5 has cost 5. 

Third subarray 2 2 1 3 has cost 4.
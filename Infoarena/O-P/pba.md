# Problem A

Antonio wanted this problem to be called Problem A, so this problem is indeed called Problem A. A natural number $N$ and a sequence of $N$ natural numbers are given. The entire sequence is to be divided into exactly 3 subarrays so that the product of the maximums of the 3 subarrays is maximized. This maximum product modulo $1,000,000,007$ should be displayed.

## Input data

The input file `pba.in` contains on the first line the natural number $N$. The second line will contain $N$ natural numbers, representing the elements of the sequence.

## Output data

The output file `pba.out` will contain a single natural number, representing the maximum product obtained by multiplying the maximums from the 3 chosen subarrays, modulo $1,000,000,007$.

## Constraints

$3 \leq N$

$N \leq 50\ 000$

The elements of the sequence are natural numbers with values between $1$ and $10^9$.

## Example

`pba.in`
```
5
9 9 9 9 9
```

`pba.out`
```
729
```

## Explanation

No matter how we divide the entire sequence into 3 subarrays, the product of the maximum values from each subarray will always be $729$.
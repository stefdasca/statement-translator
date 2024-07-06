*After long searches, Ruffi found the manuscript of truth, on which the ancient secrets of the FFT were written. Using these secrets, he composed the following problem:*

We denote by `++` the concatenation of two arrays (e.g., `[1, 2, 3] ++ [4, 5, 6] = [1, 2, 3, 4, 5, 6]`).

We define the function `inc` as follows:
$inc([a_0, \dots, a_{n-1}], k, s) = [(a_0+k) \% s, \dots, (a_{n-1}+k) \% s]$, where `a%b` denotes the remainder of the division of `a` by `b`.

We define recursively the family of arrays `FFT` as follows:
`FFT(0, s) = [0]`
`FFT(k+1, s) = inc(FFT(k, s), 0, s) ++ inc(FFT(k, s), 1, s) ++ \dots ++ inc(FFT(k, s), s-1, s)`

For example:
`FFT(1, 3) = [0, 1, 2]`,
`FFT(2, 3) = [0, 1, 2, 1, 2, 0, 2, 0, 1]`,
`FFT(3, 3) = [0, 1, 2, 1, 2, 0, 2, 0, 1, 1, 2, 0, 2, 0, 1, 0, 1, 2, 2, 0, 1, 0, 1, 2, 1, 2, 0]`

# Task
Given an array `v` of length `N`, a non-zero natural number `s`, find the first position where `v` appears as a subarray in $FFT(10^{10^{10^{100}}}+ 1, s)$ and display the remainder of this position divided by $10^9+7$, or specify that it does not appear in the array.

# Input data
The input file `pscfft.in` contains the non-zero natural number `T` which represents the number of tests on the first line. The `T` tests follow, each with the following format:
The first line of a test contains a non-zero natural number `N`, and a non-zero natural number `s`. The next line contains `N` natural numbers between `0` and `s-1`, representing the values of `v`.

# Output data
In the output file `pscfft.out` for each test, print on one line either the remainder divided by $10^9+7$ of the start position of the first appearance of the array `v` as a subarray in the array $FFT(10^{10^{10^{100}}}+ 1, s)$, or `-1` if it does not exist.

# Constraints and clarifications
* `1 \leq s \leq 1 000 000 000`
* `1 \leq N \leq 500 000`
* `1 \leq T \leq 500 000`
* The sum of the `N`'s for all tests in one file does not exceed `500 000`.
* For `10%` of the score, `T \leq 20`, `N \leq 100` and `s \leq 3`
* For another `10%` of the score, `T \leq 20`, `s \leq 4` and the response, if it exists, does not exceed `500 000`
* For another `10%` of the score, `s \leq 4`
* For another `30%` of the score, `s \leq 5`
* For another `30%` of the score, `s \leq N`
* It is guaranteed that if for a test there exists a `K` such that the array `v` appears in the array `FFT(K, s)`, then this array `v` will also appear in the array $FFT(10^{10^{10^{100}}}+ 1, s)$

# Examples
`pscfft.in`
```
5
4 2
1 0 1 1
5 3
2 0 1 2 1
20 6
2 4 5 0 1 2 3 5 0 1 2 3 4 0 1 2 3 4 5 1
2 10000000
5 5
5 5
4 3 2 1 0
```

`pscfft.out`
```
11
134
83
273492549
-1
```

There are `T=5` tests

In the first test, the first `16` numbers from $FFT(10^{10^{10^{100}}}+ 1, s)$ are 0 1 1 0 1 0 0 1 1 0 0 **1 0 1 1** 0

The last test has no solution.
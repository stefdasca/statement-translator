# Radix Sort Algorithm used for sorting an array consisting of natural numbers involves following these steps:
- the elements of the array are sorted by the last digit, and in case of a tie by the initial position in the sequence;
- the elements of the array are sorted by the penultimate digit, and in case of a tie by the position from the previous step;
- this operation is repeated until the most significant digit (of maximum order) in the writing of the numbers in the sequence.

For example, for the sequence $525, 417, 381, 291, 455$, the algorithm involves performing the following steps:
- sort by the last digit and obtain: $381, 291, 525, 455, 417$;
- sort by the penultimate digit and obtain: $417, 525, 455, 381, 291$;
- sort by the first digit and obtain: $291, 381, 417, 455, 525$.

If in the initial sequence the elements have associated indices $1, 2, 3, 4, 5$, and after each step of the sorting algorithm these indices are written in the order corresponding to the elements associated in the initial sequence, then the order of indices after each step will be:
- $3, 4, 1, 5, 2$;
- $2, 1, 5, 3, 4$;
- $4, 3, 2, 5, 1$.

We observe that the values of these sequences represent the initial indices of the array we want to sort. Thus, at each step, they form a permutation of the numbers from $1$ to $N$.
\\
Similarly, the sequence can be sorted in any base $B$ if we transform the numbers into base $B$ and then apply the same procedure. For example, if the sequence we want to sort is $6, 8, 5$ and we want to call Radix Sort in base 2, the numbers will be transformed into $110_{(6)}$, $1000_{(8)}$ and $101_{(5)}$. Then we will obtain the following sequences for each bit:
- sort by the last bit: $110, 1000, 101$;
- sort by the penultimate bit: $1000, 101, 110$;
- sort by the third bit from the end: $1000, 101, 110$;
- sort by the most significant bit: $101, 110, 1000$.

Therefore, the permutations obtained are, in order:
- $1, 2, 3$;
- $2, 3, 1$;
- $2, 3, 1$;
- $3, 1, 2$.

# Task
Pia the cat has an initial sequence of length $N$ on which she has applied the Radix Sort algorithm in base $B$. Unfortunately, her sister Mitzu played with Pia's sequence and it got lost, but Pia still has the permutations obtained at each step following the algorithm's call. Help Pia discover a possible initial sequence.

# Input data
The first line of the input file contains the number $T$, representing the number of tests in the problem. The first line of each test will contain 3 natural numbers: $N$ - representing the number of elements in the sequence, $B$ - representing the base used in calling the Radix Sort algorithm, and $K$ - representing the number of steps of the algorithm. The following $K$ lines contain $N$ natural numbers each, representing the permutation of the initial indices of the elements in the sequence after each step of the algorithm.

# Output data
The output file will contain $T$ lines, with line $i$ containing the answer for the $i$-th test. If the test admits a solution, it will contain $N$ natural numbers representing the elements of the initial sequence (written in base 10), so that applying the Radix Sort algorithm in the base given in the test to this sequence, the permutations of the indices of the sequence elements after each step of the algorithm match those given in the input file. If instead, the test does not admit a solution, line $i$ will contain $−1$.

# Constraints and clarifications
- $1 \leq N, T \leq 10^{6}$.
- $2 \leq B \leq 10^{9}$.
- $1 \leq K \leq 64$.
- The total number of elements read in input from all permutations does not exceed $10^6$ (the sum of $N * K$ from each test is $\leq 10^6$).
- For any test that admits a solution, there exists a solution that contains elements between $0$ and $10^{18}$ inclusive. **Any correct solution containing elements within this range is acceptable.**

|# | Score | Constraints|
| - | - | ------------|
|1|6|$N = 4$, $1 \leq T, maxval \leq 30$, for each of the $T$ tests. $maxval$ in this case suggests that for any test that admits a solution, there exists a solution that contains only values up to $30$|
|2|6|$N \leq B$, for each of the $T$ tests|
|3|11|$K = 1$, for each of the $T$ tests|
|4|13|$K = 2$, for each of the $T$ tests|
|5|17|$B = 2$, for each of the $T$ tests|
|6|19|$B = 10$, for each of the $T$ tests|
|7|28|Initial constraints|

# Example
`xidartros.in`
```
3
5 10 3
3 4 1 5 2
2 1 5 3 4
4 3 2 5 1
3 2 4
1 2 3
2 3 1
2 3 1
3 1 2
3 2 1
3 2 1
```
`xidartros.out`
```
525 417 381 291 455
6 8 5
-1
```

# Explanation
For the first 2 tests, see the explanations in the problem statement. For the 3rd test, there is no sequence that, sorted with Radix Sort in base 2, is sorted in a single instance and obtains the permutation $3, 2, 1$.
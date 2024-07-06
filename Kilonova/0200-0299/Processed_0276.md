Sufle is a character with pointy ears, passionate about algorithms. He has a deep aversion to Aisimok, who always challenges him to solve problems using all sorts of formulas. Sufle has named these problems Emsiteanap. Today, Aisimok has thrown a new challenge at young Sufle:

For any two natural numbers, the following operation is defined:
- consider the representations in base `2` for the two numbers;
- choose a position in the binary representation of the first number;
- swap the digit at that position in the first number with the digit at exactly the same position in the second number.
(Notice how Aisimok, obsessed with mathematics, did not use the term bit, just to irritate Sufle.)

For an arbitrary sequence of natural numbers, the above operation can be applied any number of times and on any two numbers. The final goal is for the sum of the squares of the numbers in the sequence to reach the minimum possible value. We call this minimum value the **cost of the sequence**.

To become even more disagreeable, Aisimok asks Sufle to calculate this cost for multiple subarrays of a given sequence. The cost of a subarray is equal to the cost of the sequence defined by that subarray.

# Task
For a known sequence and several given subarrays, calculate the minimum sum of squares of the numbers in the subarray after applying the described operation, as many times as considered necessary and on any numbers in the subarray.

# Input data
The file `sufle.in` contains in the first line the natural numbers `N` and `Q`, representing the number of terms in the sequence and the number of queries respectively. The second line contains `N` natural numbers, the terms of the sequence. The following `Q` lines describe the queries. Each of these lines contains two natural numbers `L` and `R`, the boundaries of the subarray corresponding to a query.

# Output data
The file `sufle.out` will contain `Q` lines. On each of these lines, a number will be printed, representing the answer to the corresponding query from the input file.

# Constraints and clarifications
* `1 \leq N \leq 100 000`
* `1 \leq Q \leq 100 000`
* `1 \leq L \leq R \leq N`
* For all queries, the operations will be considered to be applied on the initial sequence, without taking into account changes resulting from previous queries.
* All terms in the sequence are natural numbers less than or equal to `1 000 000`.

# Example
`sufle.in`
```
6 2
8 10 5 6 0 5
2 5
1 1
```
`sufle.out`
```
125
64
```

Explanation
---

The response is requested for two queries:

For the first query, the numbers in the subarray are `10, 5, 6` and `0` which have the binary representations `1010, 101, 110, 0`.
We will number the positions starting with `1`, which corresponds to the least significant bit.
Perform the operation for the second and fourth numbers at position `1`. Obtain the numbers `1010,100,110,1`.
Perform the operation for the first and last number at position `2`. Obtain the numbers `1000,100,110,11`.
The numbers in base ten are `8,4,6,3`. The sum of the squares `125` is minimal. A smaller sum cannot be obtained.

In the second query, the sequence contains only the number `8`, so the operation can never be applied. The sum of the squares is reduced to a single number, the square of `8` which is `64`.
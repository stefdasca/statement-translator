Certainly! Here is the translated text in English, preserving the required format:

---

Considering $K$ a natural number, we will call a permutation of size $K$ an arrangement in any order of elements from the set $\\{1, 2, ..., K\\}$. Ana finds written on a sheet of paper, a sequence of natural numbers $v = (v_1, v_2, v_3, ..., v_N)$.

Starting from this sequence, Ana calls a *subarray* of $v$, a subsequence of numbers that appear in consecutive positions in the initial sequence. For example, the sequence $5, 7, 8, 9, 1, 6$ contains the subarray $8, 9, 1$, the subarray $7, 8, 9, 1, 6$, but does not contain the subarray $8, 9, 6$.

Ana comes up with the idea to check if the sequence of numbers can be divided into subarrays that represent permutations of different sizes.

For example, if Ana finds the sequence $v = (2, 1, 4, 1, 3, 2)$, then she can divide it into two subarrays of permutations as follows: the subarray $v_1, v_2$ and the subarray $v_3, v_4, v_5, v_6$.
If Ana finds the sequence $v = (1, 2, 2, 3)$ then she will not be able to obtain a division into subarrays of permutations.

# Task

Create a program that reads a sequence of $N$ natural numbers and solves the following task:
* Determine a division of this sequence into subarrays of permutations. If there are multiple solutions, display the minimum lexicographic solution.
If the sequence can be divided into subarrays of permutations, for each number in the sequence, in the order $v_1, ..., v_N$, display the number of the permutation it belongs to. The numbering of the permutations will start consecutively from number $1$.

# Input data

The input file `perm.in` contains on the first line the natural number $N$, and on the second line, a sequence of $N$ natural numbers separated by a space.

# Output data

The output file `perm.out` contains on the first line the message `NU` if the sequence cannot be divided into subarrays of permutations. If the division can be performed, then on the first line it will contain the number of obtained permutation subarrays, and on the second line a sequence of numbers representing the determined minimum lexicographic division. The numbers on the second line will be separated by a space.

# Constraints and clarifications

* $1 \\leq N \\leq 100 \\ 000$
* $1 \\leq v_i \\leq 20 \\ 000$
* For two sequences of $N$ numbers $a_1, a_2, ..., a_N$ and $b_1, b_2, ..., b_N$ we say that sequence $a$ is lexicographically smaller than sequence $b$, if there exists an index $j$, with $1 \\leq j \\lt N$, such that $a_1 = b_1, a_2 = b_2, ..., a_j = b_j$ and $a_{j + 1} < b_{j + 1}$.

# Example 1

`perm.in`
```
10
2 1 3 4 1 1 2 3 4 5
```

`perm.out`
```
3
1 1 1 1 2 3 3 3 3 3
```

## Explanation

The first subarray that represents a permutation consists of the first $4$ elements, the second from the element in position $5$, and the third from the last $5$ elements.

# Example 2

`perm.in`
```
4
1 2 2 3
```

`perm.out`
```
NU
```

## Explanation

The sequence cannot be divided into subarrays made of permutations.

---


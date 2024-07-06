Gustavo, after realizing that he possesses the ability to foresee the future, decided it was time to move to the next level and harness his extrasensory capabilities. To gain prestige and become more renowned among professional magicians, he chose to debut at the National Informatics Olympiad by predicting the input data for certain problems proposed in the contest.

Gustavo's first client, Alfredo, would like to discover the content of an input file for a contest problem in a novel way, where the elements of an array `p` of `N` integers are written. To make things more interesting, Gustavo charges a fee of `C(i,j)` coins to reveal the sum of the numbers in array `p` with indices in the interval `[i,j]`, specifically $p_i+p_{i+1}+\ldots+p_j$.

# Task
Given the value of `N` and all the values of `C(i,j)` with `1 \leq i \leq j \leq N`, determine the minimum total cost that Alfredo must pay to discover all the elements of the array `p`.

# Input data
The file `oracol.in` contains on the first line the natural number `N`. The next `N` lines contain the fees charged by Gustavo as follows: on line `i+1` there are `N-i+1` natural numbers separated by a space, representing in order the costs `C(i,i), C(i,i+1), ..., C(i,N)`.

# Output data
The file `oracol.out` must contain a single number that represents the minimum total cost that Alfredo must pay to discover the array `p`.

# Constraints and clarifications
* `1 \leq N \leq 1000`;
* for any `1 \leq i \leq j \leq N` it is guaranteed that `0 \leq C(i,j) \leq 1\,000\,000`;
* for tests worth `48` points `1 \leq N \leq 250`.

# Example

`oracol.in`

```
3
4 5 1
6 3
2
```

`oracol.out`

```
6
```

Explanation
---
The minimum total cost is `6` and it is obtained as follows:
With a cost of value `C(1,3)=1` we can find the sum $p_1+p_2+p_3$.
With a cost of value `C(3,3)=2` we can find the value of $p_3$.
With a cost of value `C(2,3)=3` we can find the sum $p_2+p_3$.
From these, we can exactly determine all the elements of the array `p`.
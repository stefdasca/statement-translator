# Trapezoid

Consider two arbitrarily chosen horizontal lines. A trapezoid $T_i$ has two vertices located on the upper line and two located on the lower line (see figure below). We will denote $a_i$, $b_i$, $c_i$, $d_i$ as the top-left, top-right, bottom-left, and bottom-right vertices of the trapezoid $T_i$. A set of trapezoids is called independent if none of its members intersect.

## Task

Given $N$ trapezoids, find the cardinality of the largest independent subset. Additionally, you need to find the number of independent subsets of maximum cardinality, modulo 30013.

## Input data

The first line contains $N$, the number of given trapezoids. Each of the following $N$ lines will contain 4 numbers: $a_i$, $b_i$, $c_i$, $d_i$. No two trapezoids will intersect at a single point.

## Output data

The only line of the output file will contain two numbers separated by space: the cardinality of the largest independent subset, then the number of independent subsets of maximum cardinality modulo 30013.

## Constraints and clarifications

1 $\leq N \leq$ 100000

1 $\leq a_i$, $b_i$, $c_i$, $d_i \leq$ 1000000000

For correct answers to the first task, you will receive 40% of the test score.

For 40% of the tests, $N \leq$ 5000

## Example

`trapezoid.in`

```plaintext
7
1 3 1 9
4 7 2 8
11 15 4 12
10 12 15 19
16 23 16 22
20 22 13 25
30 31 30 31
```

`trapezoid.out`

```plaintext
3 8
```

## Explanation

Note, the image above is not an accurate representation of the input data. The top and bottom edges are moved for visibility.
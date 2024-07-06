```markdown
# Problem Statement

Zăhărel has become the mayor of his city, and the first measure he will take is to develop tourism. In the city, there are $N$ tourist attractions connected by $M$ one-way streets. To attract as many tourists as possible to his city, there must be a possibility to form a tourist route as follows: you start from a tourist attraction, travel each street exactly once and return to the starting point, visiting each tourist attraction at least once. (Ideally, a route should be constructed in such a way that visits each tourist attraction only once, not each street, but this problem is too hard).

# Task

Write a program for Zăhărel to determine the minimum number of additional streets that need to be built in the city so that there is a possibility to form a tourist route.

# Input data

The input file `turism.in` contains the natural numbers $N$ and $M$ on the first line. The next $M$ lines contain pairs of integers $a \\ b$ separated by spaces, meaning that there is a one-way street from the tourist attraction $a$ to the tourist attraction $b$.

# Output data

The output file `turism.out` will contain a single integer $K$ on the first line, representing the minimum number of additional streets that need to be built in the city so that there is a possibility to form a tourist route. The next $K$ lines contain pairs of integers $a \\ b$ separated by spaces, meaning that a one-way street will be built from the tourist attraction $a$ to the tourist attraction $b$.

# Constraints and clarifications

* $1 \\leq N \\leq 30 \\ 000$;
* $0 \\leq M \\leq 100 \\ 000$;
* The tourist attractions are numbered with integers from $1$ to $N$;
* There may be multiple one-way streets between two attractions;
* For a test, $30\\%$ of the score will be awarded if the correct number $K$ of additional streets is determined,
  $70\\%$ of the score if a set of $K$ streets that meet the problem’s requirements is also determined, and $100\\%$
  of the score if the set of $K$ edges is minimal from a lexicographical point of view.
* A set of streets $S1 = (a_1, b_1)\\ (a_2, b_2) \\ldots (a_K, b_K)$ is smaller from a lexicographical point of view than another
  set of streets $S2 = (c_1, d_1)\\ (c_2, d_2) \\ldots (c_K, d_K)$ if there is a position $1 \\leq p \\leq K$ such that $a_p < c_p$ or $a_p = c_p$ and $b_p < d_p$, and $(a_i, b_i) = (c_i, d_i)$ for $1 \\leq i < p$.

# Example 

`turism.in`
```
6 7
1 2
1 3
2 3
3 5
4 5
4 6
6 5
```

`turism.out`
```
4
3 1
5 1
5 4
5 4
```

## Explanation
~[imag.png]

A valid tourist route is:
(1, 2) (2, 3) **(3, 1)** (1, 3) (3, 5) **(5, 4)** (4, 6) (6, 5) **(5, 4)** (4, 5) **(5, 1)**
```
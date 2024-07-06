```markdown
A sequence of $N$ natural numbers is considered. We call ***rectangle-sequence*** any continuous subarray of the sequence (formed from elements in consecutive positions) that contains at least two elements. Each ***rectangle-sequence*** is *characterized* by a rectangle with side lengths equal to the largest two elements within it.

# Task

Calculate the remainder of the sum of the areas of rectangles that characterize all ***rectangle-sequences*** in the sequence when divided by $10^9+7$.

# Input data

The first line contains the non-zero natural number $N$, representing the number of elements in the sequence, and the second line contains, separated by spaces, the $N$ elements. Since the input data volume is very large, we recommend, if you are using the **iostream** library from the C++ standard, to add the following instructions at the beginning of the **main** function:

```cpp
std::iosbase::sync_with_stdio(false);
std::cin.tie(0);
```

# Output data

The output contains the determined number, modulo $10^9+7$.

# Constraints and clarifications

* $1 \leq N \leq 1\ 000\ 000$
* $1 \leq \text{any element in the sequence} \leq 1\ 000\ 000\ 000$

|#|Points|Constraints|
|-|-|--------|
|1|13|$1 \leq N \leq 2\ 000$|
|2|23|$1 \leq N \leq 100\ 000$ and there are at most $100$ distinct numbers in the sequence.|
|3|27|$1 \leq N \leq 200\ 000$|
|4|37|No additional constraints|

# Example

`stdin`
```
3
2 3 1
```

`stdout`
```
15
```

## Explanation

There are $3$ rectangle-sequences: $(2, 3)$; $(2, 3, 1)$; $(3, 1)$. The areas of the three rectangles that characterize them are: $6, 6, 3$.
```
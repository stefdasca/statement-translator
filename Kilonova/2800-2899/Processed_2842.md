> Comment, in a minimum of 50 words, on the text below, highlighting the relationship between the poetic idea and the artistic means used.

Given is a permutation \( p_1, \dots, p_N \) of the set \( \{1, 2, \dots, N \} \). An element \( p_j \) is called _critical_ for the element \( p_i \) if \( j > i \) and the element \( p_j \) appears in all increasing subsequences of maximum length which start with the element \( p_i \).

# Task

For each \( 1 \leq i \leq N \), find how many elements \( p_j \) are critical for the element \( p_i \).

# Input data

The first line of the input will contain a single integer \( N \). The second line of the input will contain the \( N \) elements of the permutation.

# Output data

The first line of the output will contain \( N \) natural numbers, each representing the number of critical elements for each position \( i \ (1 \leq i \leq N )\).

# Constraints and clarifications

* \( 1 \leq N \leq 1 \ 000 \ 000 \)

| # | Points | Constraints          |
| - | ------- | ------------------- |
| 1 | 4      | \(1 \leq N \leq 80\) |
| 2 | 11      | \(1 \leq N \leq 750\)     |
| 3 | 19      | \(1 \leq N \leq 2 \ 000\)     |
| 4 | 33      | \(1 \leq N \leq 100 \ 000\)     |
| 5 | 33     | No additional restrictions      |

# Example

`stdin`
```
5
3 5 1 2 4
```

`stdout`
```
0 0 2 1 0
```

## Explanation

* For the element \(3\), the maximum length increasing subsequences are \((3, 5)\) respectively \((3, 4)\). We observe that no element (other than \(3\)) appears in all of them.
* For the element \(5\), the unique maximum length subsequence is \((5)\). No element (other than \(5\)) appears in the sequence.
* For the element \(1\), the unique maximum length subsequence is \((1, 2, 4)\). In this sequence (apart from \(1\)), the elements \(2\) and \(4\) appear.
* For the element \(2\), the unique maximum length subsequence is \((2, 4)\). In this sequence (apart from \(2\)), the element \(4\) appears.
* For the element \(4\), the unique maximum length subsequence is \((4)\). No element (other than \(4\)) appears in the sequence.
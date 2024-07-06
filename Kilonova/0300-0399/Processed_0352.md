Gigel learned in school about the longest strictly increasing subsequence. Being very curious by nature, he wondered how many such longest strictly increasing subsequences exist in a sequence $S$.

# Task
Given the sequence $S$, consisting of positive natural numbers, determine the number of longest strictly increasing subsequences in it.

# Input data
The program reads from the keyboard the natural number $N$ contained in the first line. The second line contains $N$ positive natural numbers separated by a space, representing the elements of the sequence $S$.

# Output data
The program will print the number of longest strictly increasing subsequences in the sequence $S$. Because this number can be very large, it must be printed modulo $1\ 000\ 000\ 007$.

# Constraints and clarifications
* $1 \leq N \leq 100\ 000$
* Each element in the sequence is $\leq 2\ 000\ 000\ 000$.
* For 20 points, $1 \leq N \leq 100$.
* For an additional 20 points, $1 \leq N \leq 5\ 000$.
* A subsequence is formed of one or more elements in order from the given sequence, not necessarily on consecutive positions.
* The distinction between two subsequences is made by the positions of the elements, not their values.
* The elements of the sequence are indexed from 1.

# Example
`stdin`
```
10
2 3 4 1 2 3 5 9 1 9
```

`stdout`
```
4
```

# Explanation
There are 4 longest strictly increasing subsequences. These are $\{2, 3, 4, 5, 9\}$, $\{1, 2, 3, 5, 9\}$, $\{2, 3, 4, 5, 9\}$, and $\{1, 2, 3, 5, 9\}$. The first two subsequences have $9$ from position $8$, and the last two subsequences have $9$ from position $10$.
$4\ mod\ 1\ 000\ 000\ 007 = 4$.
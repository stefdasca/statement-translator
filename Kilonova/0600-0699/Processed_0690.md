Suppose we have an array $A$ of $N$ integers, indexed from 1 to $N$, and two positions $i$ and $j$ such that $1 \leq i < j \leq N$.
We call the array $A$ almost sorted if, when $a_i$ swaps its value with $a_j$, the array $A$ becomes strictly increasing.

# Task

Given the number $N$ and the elements of the array $A$, determine if the given array is almost sorted.

# Input data

The first line contains the number $T$, representing the number of tests.
The following $2 * T$ lines contain the $T$ tests, formatted as: the first line contains a natural number $N$, and the second line contains $N$ integers, the elements of the array $A$. The numbers on the same line are separated by a space.

# Output data

Print $T$ lines, the answers to the $T$ queries. Each line will contain a single word, "DA" or "NU", representing the answer to the question "Is the array $A$ almost sorted?".

# Constraints and clarifications

* $1 \leq N \leq 100\ 000$;
* $1 \leq $ The sum of all numbers $N \leq 5\ 000\ 000$;
* $1 \leq T \leq 100\ 000$;
* The numbers are distinct from each other;
* $1 \leq a_i \leq 1\ 000\ 000\ 000, \ i \in \{1, 2, ..., n\}$.

|#|Points|Constraints|
|-|-|--------|
|1|20|$T \leq 5$ and $N \leq 100$|
|2|20|$T \leq 50$ and $N \leq 1000$|
|3|60| No additional constraints |

# Note

Due to the very large input data, the following instructions should be used at the beginning of the program:
```c++
ios_base::sync_with_stdio(false);
cin.tie(nullptr);
cout.tie(nullptr);
```

# Example

`stdin`
```
2
5
1 7 5 3 9
4
1 2 3 4
```

`stdout`
```
DA
NU
```

## Explanation

For the first test, if we swap the element at position 2 with the element at position 4, the array $A$ becomes:
$1\ 3\ 5\ 7\ 9$, which is a sorted array.
In the second test, the array is already sorted. Thus, it is not almost sorted.
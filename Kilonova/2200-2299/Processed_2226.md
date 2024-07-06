# Gauss and Seidel, bored with their daily activities, have started a new game. Given a string of $N$ characters and a number $K$, find a subarray $[i, j]$ of this string (i.e., a subset of elements located in consecutive positions) of minimum length $K$, such that the number of occurrences of the subarray $[i, j]$ in the given string plus $j - i + 1$ is maximized.

# Task

Given a string of $N$ characters and a natural number $K$, find a subarray within positions $[i, j]$ that maximizes the number of occurrences of this subarray in the string plus its length, i.e., $j - i + 1$.

# Input data

The input file `jocs.in` contains in the first line a natural number $T$ representing the number of test cases. A test is described by two lines. The first line contains the numbers $N$ and $K$ with the above meanings. The second line contains $N$ characters representing the given string.

# Output data

The output file `jocs.out` will contain $2 \cdot T$ lines, representing the answers for the $T$ tests. An answer is written on two lines: the first line will contain the number of occurrences of the found subarray plus its length, and on the second line, the numbers $i$ and $j$ representing the endpoints of the subarray.

# Constraints and clarifications

* $1 \leq N \leq 100\ 000$
* $1 \leq K \leq N$
* $1 \leq T \leq 5$
* for a response to be considered correct, the displayed subarray must appear in the initial string at least $2$ times
* it is guaranteed that for each given $K$ there is a solution
* in case there are multiple correct answers, you can display any of them

# Example 1

`jocs.in`
```
2
18 1
atasarapavamefgefg
18 2
atasarapavamefgefg
```

`jocs.out`
```
7
1 1
5
13 15
```

## Explanation

For the first case, the letter `a` appears $6$ times in the string, so the answer is $6 + 1 = 7$. For the second case, the string `efg` appears $2$ times, so the answer is $2 + 3 = 5$.
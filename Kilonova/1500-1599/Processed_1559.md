Zedd has discovered the beauty of applications in cryptography. Thus, he has activated his hacking skills and encountered the following problem: given a string composed only of lowercase English alphabet letters, Zedd needs to find sequences that he can form without any letter appearing too many times.

# Task

Given Zedd's text, it is necessary to determine:
1. The number of distinct sequences in which each letter may appear at most $k$ times. Two sequences are considered distinct if they differ either by the starting position or by the ending position.
2. The longest sequence that contains only distinct letters. If there are multiple sequences of maximum length composed of distinct letters, the first one in lexicographic (alphabetical) order is chosen.

# Input data

The input file `criptografie.in` contains:
- The first line contains the task $C$ (which can be $1$ or $2$).
- The second line contains the natural number $k$, as mentioned above, and a natural number $n$, separated by a space.
- The third line contains a text composed of $n$ lowercase English alphabet letters (not separated by spaces).

# Output data

The output file `criptografie.out` will contain on the first line:
- If $C=1$, a natural number representing the answer to task 1.
- If $C=2$, the string representing the answer to task 2.

# Constraints and clarifications

* A sequence is composed of a succession of letters on consecutive positions in an array;
* $0 < n \leq 10^5$;
* $0 < k \leq n$;
* For tests worth 67 points, $C = 1$, and for 33 points, $C = 2$;
* For tests worth 17 points, it is guaranteed that $C = 1$, $k = 1$ and $n \leq 100$;
* For tests worth another 17 points, it is guaranteed that $C = 1$ and $n \leq 1 \ 000$;
* For task 2, it is guaranteed that the value of $k$ is $1$.

# Example 1

`criptografie.in`
```
1
1 4
abac
```

`criptografie.out`
```
8
```

## Explanation

For the given text, the variants that could be obtained according to the task are: `a`, `ab`, `b`, `ba`, `bac`, `a`, `ac`, `c`. In total, the number of sequences with distinct characters ($k = 1$) that can be formed is $8$.

# Example 2

`criptografie.in`
```
2
1 6
abacba
```

`criptografie.out`
```
acb
```

## Explanation

The maximum length of a sequence of distinct elements is $3$. There are three such sequences. The first one in alphabetical order is `acb`.
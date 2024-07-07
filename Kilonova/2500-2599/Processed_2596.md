
A pair of strings $S$ and $T$, consisting only of the letters 'A', 'B', and 'C', is **matchable** if the strings can become equal after a transformation consisting of a sequence of $0$ or more operations. An **operation** consists of inserting or deleting one of the subarrays: 'AAA', 'BBB', 'CCC', 'ABC', or 'BAC' from one of the strings. Both insertion and deletion can be performed at any position. As a result of an operation, the resulting string may become empty.

# Task

For a given sequence of pairs of strings, determine for each pair whether it is matchable.

# Input data

The input file `segalt.in` will contain on the first line the number $Q$ of pairs. For each pair, the two strings are specified on different lines.

# Output data

The output file `segalt.out` will contain $Q$ lines. The $i$-th line will contain the message `YES` if the $i$-th pair in the input file is matchable, and the message `NO` otherwise.

# Constraints and clarifications

* $1 \leq Q \leq 10 \ 000$
* $1 \leq$ the maximum length of a string (denoted by $N_{max}$) $\leq 175 \ 000$
* The sum of the lengths of the strings from all pairs (denoted by $S$) is at most $350 \ 000$

|#|Score|Constraints|
|-|-|-|
|1|15|$S \leq 3 \ 000$ and if the pair is matchable, there exists a transformation with at most **one operation**|
|2|23|$S > 3 \ 000$ and if the pair is matchable, there exists a transformation with at most **one operation**|
|3|22|$N_{max} \leq 8, S \leq 800$ and if the pair is matchable, there exists a transformation with at most **two operations**|
|4|40|No additional constraints|

# Example

`segalt.in`
```
2
ABC
CCC
AABBACCBCCBC
CCCCCCCCC
```

`segalt.out`
```
YES
NO
```

## Explanation

For the first pair, the subarray `ABC` from the first string can be deleted, then the subarray `CCC` is inserted.  
For the second pair, it can be shown that there is no transformation after which the strings become equal.
```

I've double-checked and fixed potential grammar and syntax errors according to the rules of the English language.

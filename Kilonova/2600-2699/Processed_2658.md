Archaeologists have discovered, among other relics of a vanished civilization, an unusual representation of numbers they have named DREI. In the DREI representation, signs appear that have been equated by archaeologists with lowercase letters from the English alphabet. A DREI representation is a string of distinct letters that either consists of a single letter or satisfies the following two conditions:
   1. The maximum letter appears at one of the ends;
   2. The string obtained by removing the maximum letter is a DREI representation.
   
The first twelve representations, corresponding to the numbers $1$, $2$, $3$, $4$, $5$, $6$, $7$, $8$, $9$, $10$, $11$, $12$ are `a`, `ab`, `b`, `ba`, `bac`, `bc`, `abc`, `ac`, `c`, `ca`, `cab`, `cb`.

Let us denote with $\\text{max}(x)$ the largest letter in the DREI representation $x$.

To compare two DREI representations denoted $x$ and $y$, we apply, in order, the following rules:
   1. If $\\text{max}(x) > \\text{max}(y)$, then $x > y$.
   2. A representation consisting of a single letter is greater than any other representation that has the same maximum letter at the right end and is smaller than any other representation that has the same maximum letter at the left end.
   3. If both representations $x$ and $y$ have the same maximum letter positioned at the right end, then the maximum letter is removed from both representations, and the resulting representations (let's denote them $x_{dr}$ and $y_{dr}$) are compared. If $x_{dr} < y_{dr}$, then $x > y$, and if $x_{dr} > y_{dr}$, then $x < y$.
   4. If both representations $x$ and $y$ have the same maximum letter positioned at the left end, then the maximum letter is removed from both, and the resulting representations (let's denote them $x_{st}$ and $y_{st}$) are compared. If $x_{st} < y_{st}$, then $x < y$, and if $x_{st} > y_{st}$, then $x > y$.

For example:
   * `edabc` $<$ `edc` (first applying rule 4, then comparing `dabc` with `dc`; again applying rule 4 and comparing `abc` with `c`, then applying rule 2);
   * `ab` $<$ `b` $<$ `ba`, according to rule 2;
   * `abe` $<$ `caf`, according to rule 1;
   * `bac` $<$ `cba`, according to rule 2;
   * `bac` $<$ `abc` (first applying rule 3, then comparing `ba` with `ab`, applying rule 2).

# Task

Write a program that determines the answers for $Q$ queries of the following 4 types:

| Query Type |                             Response                                                   | 
|------------|-----------------------------------------------------------------------------------------|
|    $1 \\ x$       | print `1` if the string $x$ is a DREI representation, otherwise `0` |
|    $2 \\ x \\ y$     | compare the DREI representations $x$ and $y$ and print `-1` if $x < y$, `0` if $x = y$, and `1` if $x > y$   |
|    $3 \\ N$       | print the $N$-th DREI representation                                         |
|    $4 \\ x$       | print the ordinal number of the DREI representation $x$                                 |

# Input data

The input file `drei.in` contains on the first line the natural number $Q$ representing the number of queries.

The next $Q$ lines contain the $Q$ queries, one query per line, in the format described above.

# Output data

The output file `drei.out` will contain $Q$ lines. The $i$-th line will contain the response for the $i$-th query from the input file.

# Constraints and clarifications

* $1 \\leq Q \\leq 10^5$
* $1 \\leq N \\leq 10^{12}$
* The strings appearing in the queries have a length at most equal to $26$.
* The DREI representations are numbered in ascending order starting from $1$.

|#| Points |        Restrictions                                    | 
|-|---------|--------------------------------------------------------|
|1|   10    | All queries are of type 1                             |
|2|   13    | All queries are of type 2                             |
|3|   20    | All queries are of type 3                             |
|4|   20    | All queries are of type 4                             |
|5|   12    | The strings in the queries or those obtained as a result of type 3 queries contain at most the first $10$ letters of the alphabet and $Q < 10 \ 000$.|
|6|   25    | No additional restrictions                            |
 

# Example

`drei.in`
```
6
1 acb
1 abcd
1 xabby
2 bac abc
3 12
4 cb
```

`drei.out`
```
0
1
0
-1
cb
12
```

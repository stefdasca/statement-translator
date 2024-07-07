
# Task

The two teams named Runtime Terror meet in a match between their robots, which will decide which is the best team with the name Runtime Terror!

To decide victory, the members of the two teams decide to test their robots in an unusual manner, having them sum numbers! Now you need to help the members of team 22105 Runtime Terror win the fight, but you have to do it quickly!

In other words, given a sequence $v$ of $n$ values and $q$ queries. For each query, you will need to find the sum of the following values, depending on the type:

* $1 \\ L \\ R$ -- find the sum of the AND results for all unordered pairs of numbers in that subarray. In other words, find $\\sum_{i=L}^{R} \\sum_{j=i+1}^{R} v_i \\& v_j$.
* $2 \\ L \\ R$ -- find the sum of the XOR results for all unordered pairs of numbers in that subarray. In other words, find $\\sum_{i=L}^{R} \\sum_{j=i+1}^{R} v_i \\oplus v_j$.
* $3 \\ L \\ R$ -- find the sum of the OR results for all unordered pairs of numbers in that subarray. In other words, find $\\sum_{i=L}^{R} \\sum_{j=i+1}^{R} v_i | v_j$.

Help your favorite team win the round so they can show the world that they are the best Runtime Terror team!

# Input data

The first line will contain $n$, the length of the sequence. The next line will contain the $n$ values of the array $v$.

The third line contains $q$, the number of queries. Each of the next $q$ lines contains three values $t \\ L \\ R$, where $t$ represents the type of the query, $L$ and $R$ being the ends of the subarray.

# Output data

Print $q$ lines, representing the answer for each query.

# Constraints and clarifications

* $1 \\leq n, q \\leq 5 \\cdot 10^5$;
* $0 \\leq v_i < 2^{20}$;
* $1 \\leq t \\leq 3$;
* $1 \\leq L < R \\leq n$;

|#|Score|Constraints|
|-|-|--------|
|0|0|Example|
|1|14|$1 \\leq n, q \\leq 100$|
|2|12|$1 \\leq n, q \\leq 1000$|
|3|16|$0 \\leq v_i \\leq 1$|
|4|21|$0 \\leq v_i \\leq 15$|
|5|37|No additional constraints|

# Example

`stdin`
```
9
8 1 9 4 7 9 4 9 3
14
1 7 8
2 1 4
1 5 6
3 1 7
2 2 8
3 2 3
2 3 6
3 5 7
1 1 9
2 1 9
3 1 9
1 2 5
2 2 9
1 4 6
```

`stdout`
```
0
48
1
210
166
9
57
35
77
278
355
7
216
5
```

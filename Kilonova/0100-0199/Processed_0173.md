```markdown
All finite sequences of positive natural numbers are considered and ordered as follows:
`[1]; [1,1]; [2]; [1,1,1]; [1,2]; [2,1]; [3]; [1,1,1,1]; [1,1,2]; [1,2,1]; [1,3]; ...`

The ordering is based on the following rule: if we have two sequences with different sums of elements, the sequence with the smaller sum appears earlier. If we have two sequences with equal sums, we compare the sequences term by term until we find a different term. The sequence with the smaller term appears earlier. In other words, the first criterion for ordering is the sum of the elements, and in case of a tie, the second criterion is lexicographic order.

Each sequence is associated with a position (a positive natural number) and vice versa, each position is associated with a sequence.

For example:
- The sequence `[1,1,2]` is associated with position `9`.
- Position `14` is associated with the sequence `[3,1]`.

# Task
Answer a number of queries of the following type:
1. Given a sequence of positive natural numbers, determine the position associated with the sequence.
2. Given a natural number representing a position associated with a sequence, determine the corresponding sequence.

# Input data
The input file `order.in` contains on the first line a natural number `Q` representing the number of queries.
The following `Q` lines contain the queries.
If the query is of type `1`, the line will contain the number `1`, followed by a natural number `N` representing the number of terms in the sequence, followed by `N` positive natural numbers separated by a space representing the terms of the sequence.
If the query is of type `2`, the line will contain the number `2`, followed by a positive natural number `P` representing the position of the requested sequence.

# Output data
The output file `order.out` will contain `Q` lines. Each line describes the answer to the corresponding query from the input file.
If the query is of type `1`, the corresponding line will display a single number `P` representing the position of the sequence described in the query.
If the query is of type `2`, the corresponding line will contain a natural number `N` representing the number of terms of the requested sequence, followed by `N` positive natural numbers representing the terms of the sequence. The numbers on these lines must be separated by a space.

# Constraints and clarifications
* $1 \leq P \leq 10^{15}$ (more precisely, it is ensured that for both types of queries, the position associated with the considered sequence does not exceed $10^{15}$)
* $1 \leq Q \leq 10^5$
* For `40` points, the tests will only contain queries of type `1`
* For `40` points, the tests will only contain queries of type `2`
* For `20` points, the tests will contain queries of both types

# Example:

`order.in`
```
2
1 3 1 1 2
2 14
```

`order.out`
```
9
2 3 1
```

Explanation
---

The input file contains two queries. The first is of type `1` and requests the determination of the position of the sequence `[1,1,2]` which has the length `3`. This sequence is at position `9` according to the order described in the statement. The second query requests the determination of the sequence at position `14`. This sequence is the sequence `[3,1]` with a length of `2`.
```
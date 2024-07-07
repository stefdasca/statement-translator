
At a competition, $N$ contestants participated. Each of them received a competition number so that no two contestants have the same number. The competition numbers belong to the set $\\{ 1,2, \\ldots ,N \\}$.

Unfortunately, the final ranking was lost, and the committee can only remember a few relationships between some participants (such as "the participant with number $3$ finished before the one with number $5$").

# Task

The head of the committee needs a final ranking and asks you to help determine the first lexicographic ranking that respects the relationships the committee remembers.

# Input data

Input file: `compet.in`

Line $1$: $N \\ M$, two non-zero natural numbers, representing the number of contestants and the number of relationships the committee remembers, respectively;

Lines $2 \\ldots M+1$: $i \\ j$, on each of these $M$ lines there are two non-zero natural numbers $i$ and $j$, meaning: the contestant with competition number $i$ was ranked before the contestant with competition number $j$.

# Output data

Output file: `compet.out`

Line $1$ contain: $nr_1 \\ nr_2 \\ldots \\ nr_N$, this line will contain the ranking as a sequence of non-zero natural numbers, separated by a space, representing the competition numbers of the contestants, in order from first to last.

# Constraints and clarifications

* $1 < N \leq 1 \ 000;$
* $1 < M \leq 10 \ 000;$
* The correctness of the input data is guaranteed, and there is always a solution.

# Example 1

`compet.in`
```
3 1
1 2
```

`compet.out`
```
1 2 3
```

# Example 2

`compet.in`
```
4 2
2 1
3 4
```

`compet.out`
```
2 1 3 4
```

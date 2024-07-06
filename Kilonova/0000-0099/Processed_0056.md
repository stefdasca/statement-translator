Here is the translated competitive programming problem statement in English, including corrections for grammar and syntax:

# Task

A dragon with $n$ heads travels from story to story, where in traditional tales it meets a Prince Charming who reduces its heads by several, while in modern stories it saves humanity by devouring killer insects that emerged through genetic mutations. One evening, the dragon plans a succession of stories to bring to life. It knows $p$ stories numbered from $1$ to $p$, the duration of each, and the number of heads it loses in each story. It also knows a set of $k$ pairs of stories, indicating that the second story in the pair cannot be told after the first story in the pair.

# Input data

The input file `zmeu.in` contains on the first line the numbers $n, p$, and $k$ separated by a space. Each of the next $p$ lines contains a pair of numbers $d_i$ and $c_i$ (separated by a space) representing the duration and the number of heads lost for each story. The last $k$ lines each contain a pair of numbers $p_i$ and $p_j$ (separated by a space) indicating that story $p_j$ cannot be told after story $p_i$.

# Output data

The output file `zmeu.out` contains a single line with a natural number representing the (minimum) duration of the story sequence or the value $-1$ if such a sequence does not exist.

# Constraints and clarifications

* $2 \leq N \leq 500$
* $1 \leq P \leq 200$
* $1 \leq k \leq 30 \ 000$
* The values representing the durations and the number of heads are natural numbers (the durations being strictly positive), not exceeding the value $10$.

# Example

`zmeu.in`
```
10 4 2
2 6
4 0
1 3
3 3
3 2
4 3
```

`zmeu.out`
```
9
```

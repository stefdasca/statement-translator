
# Task

Andreea received an assignment from her mathematics teacher to complete a table, knowing a sequence $A$ consisting of $N$ integers. The table is a square matrix of size $N \cdot N$. Each cell of the matrix of the form $\{i,j\}$ will have the value: gcd$(A_i,A_j)$.

Andreea completed the table and went to bed. Unfortunately, her younger brother Răzvan noticed the table and the sequence on the desk, and out of boredom, he threw the sequence in the trash and rearranged the values in the table in a random order.

When she woke up, Andreea was shocked to see her modified table. She would have started to recreate it, but she could not find the sequence with the values given by the teacher.

As she is in a time crisis and there is a possibility that there could be multiple valid sequences, she asks you to find a sequence that can construct all the numbers in the table.

The order of the numbers in the new table doesn't matter, so we can rearrange them as we like.

# Input data

On the first line of the input file `matrix.in` will contain a single natural number $N$, with the significance from the statement.
On the second line will contain the $N \cdot N$ natural numbers, these being the values from the matrix shuffled by Răzvan.

# Output data

On the first line of the output file `matrix.out` will contain the sequence found by you.

# Constraints and clarifications

* $1 \leq N \leq 500$;
* The values in the matrix shuffled by Bob are non-zero natural numbers $\leq 10^9$.
* If there are multiple possible solutions, you are allowed to print any of them.

# Example 1

`matrix.in`
```
4
14 1 11 14 10 14 2 1 1 2 2 14 2 1 1 1 
```

`matrix.out`
```
10 11 14 14 
```

# Example 2

`matrix.in`
```
1
6
```

`matrix.out`
```
6
```

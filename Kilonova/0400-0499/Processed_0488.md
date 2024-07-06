```markdown
# Task
Luka is bored again during chemistry class while the teacher explains Avogadro's law.

Thus, Luka drew a table with $3$ rows and $N$ columns. Then he wrote the numbers from $1$ to $N$ on the first row in an arbitrary order, each number appearing exactly once. 
On the other two rows, he wrote numbers between $1$ and $N$ again, but he did not care about how many times a number appeared.
Luka can now delete any number of columns from the table. After doing this, he will sort the numbers in each row in ascending order.

Write a program that determines the smallest number of columns that need to be deleted so that all three rows are identical after sorting.
# Input data
The first input line will contain the natural number $N$, the number of columns in the table.
The next three lines contain $N$ natural numbers each, separated by single spaces. The numbers will be between $1$ and $N$, and there will be no duplicates on the first row.
# Output data
Print on the first line the minimum number of columns that need to be deleted.
# Constraints and clarifications
- $ 1 \ \le N \ \le 10^5 $
- For tests worth 40 points, $N \le 100 $.
- For other tests worth 30 points, $N \le 10.000$.
- For the remaining 30 points, there are no additional constraints.
# Example 1
  `stdin`
  ```
7
5 4 3 2 1 6 7
5 5 1 1 3 4 7
3 7 1 4 5 6 2
  ```

  `stdout`
  ```
 4
  ```
  # Example 2

  `stdin`
  ```
 9
1 3 5 9 8 6 2 4 7
2 1 5 6 4 9 3 4 7
3 5 1 9 8 6 2 8 7
  ```
  `stdout`
  ```
 2
  ```

```
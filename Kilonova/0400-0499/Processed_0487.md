```markdown
# Task
Ana lives in a small, but cheerful village. There is a row of cherry trees along the main street. Ana has numbered the trees with consecutive integers starting from $1$. After many studies, Ana observed that the number of the tree influences the quantity of cherries that grow on it.

For a cherry tree, the groups of consecutive digits of its number are considered. For each group of digits, the digit is multiplied by the square of the group's length. The sum of the results obtained for all the groups indicates the total number of cherries that grow on the tree.

For example, in the tree number $77 744 007$, the groups are: $777$, $44$, $00$, and $7$. The quantity of cherries will be: $7 \times 3^2 + 4 \times 2^2 + 0 \times 2^2 + 7 \times 1^2 = 86$.
The time has come to pick the cherries, and the villagers have agreed to collect all the cherries from the trees numbered from $A$ to $B$. Write a program that will calculate the quantity of cherries collected.

# Input data
The first line contains two natural numbers, $A$ and $B$, the first and last tree from which the villagers will pick cherries.

# Output data
Print a single integer, the number of cherries picked by the villagers.

# Constraints and clarifications
- $ 0 \le A \le B \le 10^{15} $
- For tests worth 10 points, $A, B \le 100$.
- For other tests worth 10 points, $A, B \le 1000$.
- For other tests worth 25 points, $A, B \le 10^7$.
- For other tests worth 25 points, $A, B \le 10^9$.
- For the remaining 30 points, there are no other constraints.

# Example 1
  `stdin`
  ```
  1 9
  ```

  `stdout`
  ```
  45
  ```

# Example 2

`stdin`
  ```
  100 111
  ```

  `stdout`
  ```
  68
  ```

# Example 3

  `stdin`
  ```
  7774407 7774407
  ```

  `stdout`
  ```
  86
  ```
```
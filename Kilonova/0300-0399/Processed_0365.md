Everyone knows that Mirel has $2\cdot N$ perfume bottles arranged on a shelf with $2\cdot N$ positions, numbered from $1$ to $2\cdot N$. He has $N$ perfume bottles bought from the countryside and another $N$ perfume bottles bought from France. The bottles bought from the countryside are labeled $r_1$, $r_2$, $r_3$, ..., $r_N$, while the bottles bought from France are labeled $f_1$, $f_2$, $f_3$, ..., $f_N$. Each bottle is associated with the value it was purchased for.

Initially, Mirel has the bottles bought from the countryside placed on the first $N$ positions, sorted in ascending order by value, and the bottles bought from France placed on the next $N$ positions, also sorted in ascending order by value. Thus, the $2\cdot N$ perfume bottles are arranged in the following way: $[r_1, r_2, r_3, \ldots, r_N, f_1, f_2, f_3, \ldots, f_N]$. Specifically, bottle $r_i$ is on position $i$, and bottle $f_i$ is on position $N+i$, for $i$ in the interval $[1, N]$.

His best friend, Marian, thought of surprising him by rearranging the perfume bottles in the following order: $[r_1, f_1, r_2, f_2, r_3, f_3, \ldots, r_N, f_N]$. Since Marian has two hands, he can only perform the following type of operation: take two bottles from the shelf (from two different positions) and swap them.

# Task
Given the number $N$ and $2 \cdot N$ values representing the value of each perfume bottle, help Marian perform the necessary operations to rearrange the perfume bottles in the specified order in the statement.

# Input data
The input file `aranjare.in` contains on the first line the number $N$, and on the next line $2\cdot N$ natural numbers, separated by a space. The first $N$ numbers represent the values of the bottles bought from the countryside, and the next $N$ numbers represent the values of the bottles bought from France. Both the first $N$ and the last $N$ numbers are sorted in ascending order by value.

# Output data
The output file `aranjare.out` will contain multiple lines. Each line will contain two different numbers $x$ and $y$ from the interval $[1, 2\cdot N]$, indicating that Marian needs to swap the bottle on position $x$ with the bottle on position $y$.

# Constraints and clarifications
- $2 \leq N \leq 100\ 000$
- If there are multiple solutions, any of them can be displayed.
- The solution does not necessarily need to perform the minimum number of operations.
- For $15\%$ of the tests, it is guaranteed that $N \leq 13$.
- For another $25\%$ of the tests, it is guaranteed that $N \leq 300$.
- For another $30\%$ of the tests, it is guaranteed that $N \leq 1\ 000$.

# Example
`aranjare.in`
```
3
1 3 5 2 3 5
```
`aranjare.out`
```
2 4
3 5
3 4
```

## Explanation
In the explanation below, each bottle has the label name followed by its value in parentheses.
The initial sequence is: $[r_1(1), r_2(3), r_3(5), f_1(2), f_2(3), f_3(5)]$.
After the first move, it becomes: $[r_1(1), f_1(2), r_3(5), r_2(3), f_2(3), f_3(5)]$.
After the second move, it becomes: $[r_1(1), f_1(2), f_2(3), r_2(3), r_3(5), f_3(5)]$.
After the last move, it becomes: $[r_1(1), f_1(2), r_2(3), f_2(3), r_3(5), f_3(5)]$.
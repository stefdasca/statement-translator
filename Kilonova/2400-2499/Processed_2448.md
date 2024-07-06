For an array of $N$ integer numbers, one can determine a central position such that the sum of the numbers on the left of the position is as close as possible to the sum of those on the right. If the number at the central position is odd, then $1$ is added to the smaller sum.

Operations can be performed on the terms of the array in the form: $P\ V$. The term from the array at position $P$ will be replaced with the number $V$.

On the initial array, $T$ operations described above are successively performed. After each operation, the central position is recalculated.

# Task

Calculate the position for the $T$ derived arrays.

# Input data

The following data will be read from the input file `centrat.in`:
* The first line contains a natural number $N$, representing the length of the array;
* The second line contains the initial array consisting of $N$ natural numbers;
* The third line contains a natural number $T$, representing the number of operations performed;
* The next $T$ lines contain two numbers $P_i$ and $V_i$, which indicate changing the number at position $P_i$ to $V_i$.

# Output data

The output file `centrat.out` will contain $T$ numbers, one on each line, representing the central positions of the $T$ modified arrays.

# Constraints and clarifications

* $1 \leq N, T \leq 100\ 000 $;
* $1 \leq P_i \leq N$, $\forall\ 1 \leq i \leq T$;
* $1 \leq V_i \leq 1\ 000\ 000 $, $\forall\ 1 \leq i \leq T$;
* For $30\%$ of the tests, $N \leq 100$, or $N \leq 2\ 000$ and $T \leq 10\ 000$.
* If there are multiple possible central positions, display the smallest one.

# Example

`centrat.in`
```
5
4 1 3 9 1
2
4 2
1 10
```

`centrat.out`
```
2
2
```

## Explanation
The array obtained after the first operation is `4 1 3 2 1`, and after the second operation, the array obtained is `10 1 3 2 1`.

For the first array, the minimum difference is $1$, obtained at position $2$. The sum on the left of the position is $4$, while the sum on the right is $3+2+1=6$. Since the left sum is smaller and $1$ is an odd number, it becomes $4+1=5$.
# Input data

The first line contains a natural number $n$.

# Output data

Print the answer to the problem, which can be $0$ or $1$.

# Constraints and clarifications

* It is guaranteed that there are no two tests with the same $n$.
* There is no correlation between input and output :)
* $0 \leq n < 4096$

|#|Score|Constraints                    |
|-|-----|-------------------------------|
|0| 0   | Examples                      |
|1| 20  | $0 \le n < 4$                 |
|2| 20  | $4 \le n < 16$                |
|3| 30  | $16 \le n < 64$               |
|4| 30  | $64 \le n < 4096$             |

* **Pay attention to how the tests are grouped!**

# Example 1

`stdin`
```
1
```

`stdout`
```
1
```

# Example 2

`stdin`
```
64
```

`stdout`
```
0
```
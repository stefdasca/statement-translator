Sure, here is the translated competitive programming problem statement in English:

---

The people of southern Sweden are known for eating a lot of falafel. The price of falafel is very volatile, and the best way to analyze the current state of the economy is to go to the same falafel place every day and calculate the sum of all the prices on their menu.

A falafel place has $N$ different dishes on the menu. The $i$-th dish has the price $p_i$.

Each day, one of the following events occurs:

* `INFLATION x`: An integer $x$ is added to all prices on the menu.
* `SET x y`: Each dish with the price $x$ changes its price to $y$.

Process the events of the $Q$ days and display the sum of all prices at the end of each day.

# Input data

The first line contains an integer $N$, the number of dishes.

The second line contains $N$ integers $p_1$, $p_2$, ..., $p_N$.

The third line contains an integer $Q$, the number of days.

The next $Q$ lines each contain a string $s$ followed by one or two integers.

If $s$ is `INFLATION`, then it will be followed by an integer $x$ meaning that $x$ is added to all prices on the menu.

If $s$ is `SET`, then it will be followed by two integers, $x$ and $y$, meaning that all dishes that had the price $x$ will now have the price $y$.

# Output data

Print $Q$ lines, the sum of all prices $p_i$ at the end of each day.

# Constraints and clarifications

* $1 \leq N \leq 3 \cdot 10^5$
* $1 \leq p_i \leq 10^6$ for each $i$ with $1 \leq i \leq N$
* $1 \leq Q \leq 10^5$
* $1 \leq x, y \leq 10^6$ for any day

**Note:** The answer might not fit in a 32-bit datatype, so be careful if you are using `C++`.

Your solution will be tested on several groups of tests, each group having its own number of points. Each group of tests may contain multiple tests. To obtain the score for a group of tests, the solution must pass all the tests in that group.

| # | Score  | Constraints                |
| - | ------ | -------------------------- |
| 1 | 14     | $N = 1$                    |
| 2 | 28     | $N, Q, p_i, x, y \leq 100$ |
| 3 | 19     | Only `INFLATION` events    |
| 4 | 23     | Only `SET` events          |
| 5 | 16     | No additional constraints  |

# Example 1

`stdin`
```
5
2 1 1 2 5
6
INFLATION 1
SET 3 2
SET 5 2
INFLATION 4
SET 6 1
SET 10 1
```

`stdout`
```
16
14
14
34
14
5
```

## Explanation

~[inflation-sample-2.png]

This image corresponds to the first two days from example $1$. Notice that the sum of the prices at the end of the first day is $16$, therefore, the first value printed by your program should be $16$.

# Example 2

`stdin`
```
3
1 4 1
5
SET 1 1
SET 3 4
INFLATION 2
SET 3 1
SET 6 4
```

`stdout`
```
6
6
12
8
6
```

---
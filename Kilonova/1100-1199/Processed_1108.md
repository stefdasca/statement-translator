Alexa bought $n$ balls of different colors for her cat. Each day $i$ of the following $t$ days, the cat will choose $q_i$ pairs of adjacent balls to play with and will swap the positions of the balls in each pair. Alex knows the colors of the balls that were swapped, but not the order in which the swaps happened. Therefore, he asks you to find the order of the balls for each day.

The colors are encoded by natural numbers from $1$ to $n$. Initially, the balls are sorted in ascending order by the color index. The answer for each day will be given in the form of a code stored in an **unsigned long long** variable and obtained from the following formula: ($\sum_{i=0}^{n-1} 23^{n-1-i} \ \cdot \ v_i$) modulo $2^{64}$, where $v_i$ means the color of the ball at position $i$.

# Interaction Protocol

The contestant will implement the `init` function, with the following signature:

```cpp
void init (int n, int nrTestCase);
```

Through this function, you will receive the number $n$ and the number of the current test.

Also, the contestant will implement the `makeSwaps` function, with the following signature.

```cpp
unsigned long long makeSwaps (int q, int a[], int b[]);
```

The parameters of this function have the following meaning:

* $q$ is the number of pairs of balls that are swapped
* $a$ and $b$ are two arrays of $q$ elements that describe the pairs of **colors** that need to be swapped. Pair $i$ (with $i$ from $0$ to $q - 1$) is ($a[i]$, $b[i]$). It is guaranteed that $a[i] \neq b[i]$. The order of the two numbers within the pair is random. These pairs are given in an order not necessarily identical to the one in which the swaps were carried out by the cat.

The function will return the result requested in the problem. **The contestant should not implement the `main` function**.

# Constraints and clarifications

* The `init` function will be called only once at the start of the program.
* Note that the number $t$ is not given as a parameter in the `init` function. It remains unknown to the contestants' program. However, it is found in the input file.
* The `makeSwaps` function will be called $t$ times, and during a call of this function, any (unordered) pair of colors appears at most once.
* The scoring will be done separately, the tests being independent of each other.
* The first test ($nrTestCase = 1$) has the property that the pairs are given in the order in which the swaps were made. This test is worth $7$ points.
* The next $2$ tests have the following constraints: $2 \leq n \leq 20\ 000$ and $t = 1$. These tests are worth $12$ points each.
* The next $3$ tests have the following constraints: $2 \leq n, t, q_i \leq 50$. These tests are worth $11$ points each.
* The next $4$ tests have the following constraints: $2 \leq n, t, q_i \leq 20\ 000$. These tests are worth $9$ points each.
* $\sum_{i = 1}^{t} q_i \leq 1\ 000\ 000$ for all tests.

# Example 1

`balls.in`
```
4 2 -1
2
1 2
1 3
4
4 3
2 4
3 2
1 4
```

`balls.out`
```
25948
50302
```

## Explanation

$N = 4$

$t = 2$

$nrTestCase = -1$ (this test is not among those used for evaluation)

For the first day:

$[1, 2, 3, 4] \rightarrow [2, 1, 3, 4] \rightarrow [2, 3, 1, 4]$

Note that the sequence $[1, 2, 3, 4] \rightarrow [3, 1, 2, 4] \rightarrow [3, 2, 4, 1]$ is incorrect because elements $1$ and $3$ are not adjacent when they are swapped.

$25948 = 23^2 \cdot 3 + 23^1 \cdot 1 + 23^0 \cdot 4$

For the second day:

$[2, 3, 1, 4] \rightarrow [2, 3, 4, 1] \rightarrow [2, 4, 3, 1] \rightarrow [4, 2, 3, 1] \rightarrow [4, 3, 2, 1]$

$50302 = 23^3 \cdot 4 + 23^2 \cdot 3 + 23^1 \cdot 2 + 23^0 \cdot 1$

***During the competition, the time limit was increased to 1.5s. Now we have changed it back to 1s to encourage finding more efficient solutions.***

# Statement
The Fantastic Man finds a permutation $p_1, p_2, ..., p_n$ of degree $n$. He can modify any element of the permutation, but at a cost. Thus, he chooses $p_i$ and $d$, such that $1 \leq i \leq n$ and $d$ divides $p_i$, and $p_i$ will be modified to $d$, with the cost $p_i \oplus d$. Everyone knows that he doesn't like disorder. He wants to find the minimum cost to obtain a sorted array in non-decreasing order, not necessarily strictly, after all modifications. However, he is not the type to implement Slope-Trick at Marytone and decides to ask for your help.

# Task
Given $n$ and the permutation $p$, help the Fantastic Man.

# Input data
The input file `divixori.in` contains on the first line a natural number $n$. The second line contains $n$ natural numbers, $p_1, p_2, ..., p_n$, representing the elements of the permutation $p$.

# Output data
The output file `divixori.out` contains a natural number representing the minimum cost to obtain a sorted array in non-decreasing order, not necessarily strictly, after all modifications.

# Constraints and clarifications
* $1 \leq n \leq 10^6$
* $1 \leq p_i \leq n, 1 \leq i \leq n$
* [Definition of the $ \oplus $ operation](https://en.wikipedia.org/wiki/XOR_gate)
* **Attention!** The task is to implement the function `solve()`. The submitted code will not contain the `main()` function — this will be replaced by the `solve()` function. Here is an example of a valid program:
```cpp
long long solve(int n, int p[]) {
    return 0;
}
```
* For tests worth $10p$ we have $1 \leq n \leq 10$
* For tests worth $20p$ we have $1 \leq n \leq 10^3$
* For tests worth $30p$ we have $1 \leq n \leq 10^5$
* For tests worth $20p$ we have $1 \leq n \leq 5 \times 10^5$
* For tests worth $20p$ we have $1 \leq n \leq 10^6$

# Example 1
`divixori.in`
```
6
1 4 2 3 6 5
```
`divixori.out`
```
10
```

# Example 2
`divixori.in`
```
6
6 5 4 3 2 1
```
`divixori.out`
```
21
```

## Explanations
For the first example, we can modify $p_5$ from $6$ to $3$ and $p_2$ from $4$ to $1$, the total cost being $6 \oplus 3 + 4 \oplus 1 = 10$.
For the second example, the only way is to modify all elements to $1$, the total cost being $21$.

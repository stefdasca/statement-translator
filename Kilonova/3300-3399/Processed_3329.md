Certainly! Below is the translated problem statement in English, with the specified formatting and terminology preserved:

---

Consider $N$ friends $F_0, \dots , F_{N-1}$ and $N$ types of ramen $R_0, \dots , R_{N-1}$ at the ramen restaurant. Each friend $F_i$ has a certain affinity $A_{ij}$ for type $j$ of ramen — the higher the affinity, the more $F_i$ likes the ramen $R_j$. Each friend's affinities are distinct — that is, $A_{ij} \neq A_{ij'}$ for $j \neq j'$. Naturally, it is possible that $A_{ij} < 0$.

Suppose the friends visit the ramen restaurant multiple times. During each visit, two friends cannot eat the same type of ramen (the ingredients would be insufficient). Assume that the friends take their ramen in the order $F_{\pi_0}, \ldots, F_{\pi_{N - 1}}$, for a certain permutation $\pi_0, \ldots, \pi_{N - 1}$ of $0, \dots , N - 1$. Then, friend $F_{\pi_0}$ will take their favorite ramen (i.e., the one for which they have the highest affinity), friend $F_{\pi_1}$ will take their favorite ramen _except for the one taken by_ $F_{\pi_0}$, and so on. In other words, $F_{\pi_i}$ will take their favorite ramen among those not taken by $F_{\pi_0} , \dots , F_{\pi_{i - 1}}$.

The _goodness_ of a permutation $\pi$ is the sum of the friends' affinities for the types of ramen they take. In other words, if friend $i$ takes ramen of type $\sigma_i$, then the goodness of $\pi$ is $\sum_{i = 0}^{N - 1} A_{i, \sigma(i)}$.

Your goal is to find a permutation $\pi$ with maximum goodness. You can achieve this by experimenting with different orders in which the friends take their ramen (i.e., different visits to the restaurant). The aim is to find an optimal permutation without requiring too many visits to the restaurant.

# Interaction Protocol

You must implement the following function:

```cpp
std::vector<int> find_order(int N);
```

Here, $N$ is the number of friends. The function should return a permutation $\pi$ of the numbers $0, \dots , N-1$ with maximum goodness. To implement it, you may repeatedly call the following function up to a maximum of $750$ times:

```cpp
std::vector<std::pair<int, int>> query(const std::vector<int>& order);
```

The function takes as input a permutation $\pi$ of the numbers $0, \dots , N - 1$ (identified by the parameter `order`) and returns a list of pairs $(\sigma(i), A_{i, \sigma(i)})$, where $\sigma(i)$ is the type of ramen taken by friend $i$ if the friends take their ramen in the order given by $\pi$.

# Constraints and Clarifications

* $1 \leq N \leq 75$
* $| A_{ij} |\leq 2\ 000\ 000$
* The scientific committee's solution requires at most $cN^k$ queries for certain constants $c, k \geq 1$. To avoid overloading the testing infrastructure, you may call `query` at most $750$ times, which generously reflects the practical performance of the model solution.

| # | Score | Constraints          |
| - | ------- | ------------------- |
| 1 | 5      | $N = 5$ |
| 2 | 15      | $N = 15$      |
| 3 | 20      | $N = 30$      |
| 4 | 20      | $N = 45$     |
| 5 | 20      | $N = 60$      |
| 6 | 20      | $N = 75$      |

# Example

| Your Program  | Commission's Program         |
|----------------------|----------------------------|
|                      | Calls `find_order(2)`.    |
| `query({0, 1})`      | `{{0, 9}, {1, 0}}`        |
| `query({1, 0})`      | `{{1, 5}, {0, 5}}`        |
| `find_order(2)` returns `{1, 0}` | |

## Explanation

In this example, there are $N = 2$ friends with the following affinities $A_{ij}$ for $N = 2$ types of ramen:

$$
\begin{pmatrix}
9 & 5 \\
5 & 0
\end{pmatrix}
$$

The interaction starts with the commission calling your function: `find_order(2)`. Your function then queries the two possible permutations: $\{0, 1\}$ and $\{1, 0\}$. The first yields a goodness of $0 + 9 = 9$, while the second yields a goodness of $5+5 = 10$. Then the function returns the better of the two, which is $\{1, 0\}$. The returned permutation has the maximum possible goodness, as per the requirements.
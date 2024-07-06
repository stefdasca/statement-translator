```markdown
Kaguya has just managed to schedule a new shopping session with Kei, Miyuki's sister. *Just with Kei this time, without the Fujiwara sisters... I will find out everything about Miyuki!* Understandably, Kaguya does not want to meet anyone else. And, of course, Kaguya is upset when she finds out that Chika Fujiwara plans her own shopping session on the same day and in the same mall.

The mall consists of `N` stores numbered from `1` to `N`, connected by `N - 1` alleys so that it is possible to get from any store to any other by walking along one or more alleys. Kaguya and Kei plan to spend their day starting from store `S` and walking to store `F`, visiting every store on the shortest path that connects them (including stores `S` and `F`). We denote this path by $D_{S,F}$. Generally, we denote by $D_{x,y}$ the minimal set of stores that must be visited to get from store `x` to store `y` by crossing the mall's alleys.

Kaguya has found out `Q` possible plans of Chika. Similarly to Kaguya's plan, plan `i` involves Chika starting from store $X_i$ and walking to store $Y_i$, visiting all the stores on the shortest path between them.

Kaguya quickly concludes that the only way to divert Chika from her path is to build a new alley between two stores `t` and `u` in the mall. Thus, we denote by $D^{t,u}_{x,y}$ the minimal set of stores that must be visited to get from store `x` to store `y` by crossing the mall's alleys, possibly (but not necessarily) also using the newly built alley `(t, u)`.

For each plan, Kaguya wonders in how many ways a new alley `(t, u)` can be added to the mall, such that `t < u` and no shortest path $D^{t,u}_{X_i,Y_i}$ has any stores in common with the path $D_{S,F}$. Kaguya's questions are purely hypothetical and do not lead to the addition of any alleys in the mall after finding the answer.

# Task
To solve the problem, you need to implement the function:

```cpp
void solve(int N, int Q, int S, int F, std::vector<int> A, std::vector<int> B, std::vector<int> X, std::vector<int> Y, std::vector<long long> &sol);
```

The parameters `N, Q, S` and `F` have the significance described in the statement. The parameters `A` and `B` are two arrays indexed from `0`, each with `N - 1` elements, representing the alleys in the mall; position `i` represents the existence of an alley between stores `A[i]` and `B[i]`. The parameters `X` and `Y` are two arrays indexed from `0`, each with `Q` elements, containing Chika's plans; position `i` represents the plan of traveling from store `X[i]` to store `Y[i]`. The parameter `sol` represents an array of `Q` elements; you need to populate, at each position `i` from `0` to `Q - 1`, the answer to Kaguya's question regarding the `i`-th plan.
The function will be called only once per test.

## Local Interactor
To help you test your code, we provide a [local interactor](grader.cpp). From the console, the local interactor will read, in order, four numbers `N, Q, S` and `F`, then `N - 1` pairs of numbers $A_i$ and $B_i$, then `Q` pairs of numbers $X_i$ and $Y_i$. The interactor will call the `solve` function with the read data. On the console, the interactor will then display the `Q` elements from the array `sol`, one per line.

# Constraints
* `1 \leq N, Q \leq 100 000`
* `1 \leq S, F \leq N`
* $1 \leq X_i, Y_i \leq N$ for any `i`, `0 \leq i < Q`
* $ \sum_{i=0}^{Q - 1} dist(X_i, Y_i) \leq 1 000 000$, where `dist(a, b)` represents the minimum number of alleys that must be crossed to get from store `a` to store `b` before adding the additional alley.
* The alley `(u, t)` that is added can already exist in the mall; in this case, there will be two alleys between stores `u` and `t`.

## Subtask 1 (5 points)
* `N, Q \leq 100`
## Subtask 2 (5 points)
* `N, Q \leq 500`
## Subtask 3 (10 points)
* `N, Q \leq 5 000`, $D_{S,F}$ and $D_{X_i,Y_i}$ have at least one store in common, `\forall i, 0 \leq i < Q`.
## Subtask 4 (20 points)
* `N, Q \leq 5 000`
## Subtask 5 (15 points)
* `N \leq 10 000, Q \leq 100 000`, $D_{S,F}$ and $D_{X_i,Y_i}$ have at least one store in common, `\forall i, 0 \leq i < Q`.
## Subtask 6 (30 points)
* `N \leq 10 000, Q \leq 100 000`
## Subtask 7 (5 points)
* $D_{S,F}$ and $D_{X_i,Y_i}$ have at least one store in common, `\forall i, 0 \leq i < Q`.
## Subtask 8 (10 points)
* No additional constraints

# Examples

`stdin`

```
6 4 1 2
1 2
2 3
1 4
4 5
5 6
3 5
6 5
6 1
6 4
```

`stdout`

```
3
15
0
14
```

Explanations
---

We have `N = 6` stores and `Q = 3` possible plans. Kaguya and Kei's path starts from store `S = 1` and reaches store `F = 2` by crossing exactly one alley.

For the first plan, the alleys `(3, 5), (4, 5), (5, 6)` satisfy the condition from the statement.

For the second plan, any added alley satisfies the condition from the statement.

For the third plan, no alley satisfies the condition from the statement since store `1` is on the path between stores `S = 1` and `F = 2`.

For the fourth plan, all alleys except one satisfy the condition from the statement. If the alley `(6, 1)` is added, there would be two minimum-length paths: `6 - 1 - 4` and `6 - 5 - 4`. The first one has a store in common, store `1`, with the path between `S = 1` and `F = 2`, making this alley not satisfy the condition from the statement.
```
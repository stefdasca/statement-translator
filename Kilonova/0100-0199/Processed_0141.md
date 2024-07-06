The new district in Bugure is causing a great stir throughout the country. It consists of `N` houses that can be bought, and the $i$-th house is located at the coordinates $(X_i, Y_i)$. We denote $dist(i, j) = |X_i - X_j| + |Y_i - Y_j|$ and $d(i) = min_{j \neq i}(dist(i, j))$.

Being childhood friends and inseparable, Àles, RANDy, and Țeba also want to keep up with the times and decide to purchase houses, one for each of them. They care a lot about their relationship and each wants to have a say in choosing the houses, so they agree on the following:

* `À < R < Ț`
* `dist(À, R) = dist(R, Ț) = dist(À, Ț)`
* `d(À) = d(R) = d(Ț) = dist(À, R)`

where we denote with the initial of each name the house number each one buys.

Upon a detailed analysis, Țeba, the brain of the group, notices that they have many possible choices and wonders: "In how many ways can we choose the houses so that the above requirements are met?"

# Input data
The first line contains the natural number `N`. The next `N` lines contain two numbers $X_i, Y_i$, representing the coordinates of the houses.

# Output data
The first line contains a single number `S` representing the answer to Țeba's question.

# Constraints and clarifications
* `1 \leq N \leq 250000`
* $0 \leq X_i, Y_i \leq 10^9$ for any `1 \leq i \leq N`
* There will be no two houses at the same coordinates.

## Subtask 1 (7 points)
* `N \leq 100`

## Subtask 2 (14 points)
* `N \leq 2000`

## Subtask 3 (28 points)
* $X_i, Y_i \leq 2000$ for any `1 \leq i \leq N`

## Subtask 4 (51 points)
* Without additional constraints

# Examples

`stdin`

```
5
1 1
3 1
2 2
2 6
4 4
```

`stdout`

```
1 
```

Explanations
---

The only triplet that meets the requirements is: `(1, 2, 3)`. The triplet `(3, 4, 5)` satisfies `dist(3, 4) = dist(4, 5) = dist(3, 5)` but `d(3) = 2, d(5) = 4` and `d(4) = 4`.
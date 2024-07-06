```markdown
An *AA tree* is a binary search tree with a special structure. Each node is assigned **a value** and **a level**. Values satisfy the usual properties of binary search trees:

1. The value of each left child (and the nodes in the subtree of the left child) is less than or equal to that of its parent.
2. The value of each right child (and the nodes in the subtree of the right child) is greater than or equal to the value of its parent.

Levels follow these rules:

1. The level of each leaf node is $1$.
2. The level of each left child is exactly one less than that of its parent.
3. The level of each right child is equal to or one less than that of its parent.
4. The level of each right grandchild is strictly less than that of its grandparent.
5. Each node with a level strictly greater than one has exactly two children.

Below are five examples of *AA trees*, having $3$, $5$, $5$, $11$, and $11$ nodes. For clarity, right children at the same level as their parents are colored red.

~[aatree1.png|width=60em]

# Task

Given two numbers $N$ and $L$, how many ways are there to arrange the values $1$, $2$, ..., $N$ into an *AA tree* so that it has exactly $L$ levels?

# Input data

The single line of the input data will contain the integers $N$ and $L$ separated by a space.

# Output data

Print the number of arrangements modulo $10^9 + 7$.

# Constraints and clarifications

* The problem statement has been slightly modified due to an error in the definition of binary search trees in the original problem statement.
* $1 \leq L \leq 9$
* $1 \leq N \leq 10\ 000$

| # | Points | Constraints          |
| - | ------- | ------------------- |
| 0 | 0       | Examples |
| 1 | 19      | $L \leq 4$|
| 2 | 34      | $5 \leq L \leq 7$      |
| 3 | 47      | No additional constraints    |

# Example 1

`stdin`
```
5 2
```

`stdout`
```
2
```

## Explanation

The two possible arrangements are shown in images $2$ and $3$ above.

# Example 2

`stdin`
```
442 6
```

`stdout`
```
896944318
```

# Example 3

`stdin`
```
7133 9
```

`stdout`
```
980381648
```
```
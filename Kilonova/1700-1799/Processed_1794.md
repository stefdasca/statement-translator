```markdown
Tudor is a boy passionate about the forest, so every weekend he goes for a walk on Pietricica. This forest can be represented as a matrix of $N$ rows and $M$ columns where a space with a tree is marked with $1$. The position of Tudor in the matrix is known, which is $(X, Y)$. He asks himself the following question: "How many trees are within a radius of $R$ from the position I am in?". The distance from Tudor to a tree is calculated using the Manhattan distance (the distance from $(x_1, y_1)$ to $(x_2, y_2)$ is $|x_1 - x_2| + |y_1 - y_2|$).

# Task

Can you help Tudor answer his question?

# Input data

The first line will contain the numbers $N$, $M$, $X$, $Y$, $R$. The next $N$ rows will contain $M$ elements representing the forest in which Tudor is.

# Output data

Print a single number that represents the answer to the question.

# Constraints and clarifications

* $1 \leq N, M \leq 100$

# Example

`stdin`
```
2 3 1 1 2
1 1 0
1 1 1
```

`stdout`
```
4
```

## Explanation

The distance from Tudor to a tree is calculated using the Manhattan distance (the distance from $(x_1, y_1)$ to $(x_2, y_2)$ is $|x_1 - x_2| + |y_1 - y_2|$).
```
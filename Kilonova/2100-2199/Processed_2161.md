```markdown
# Task

Given the start and end times of $N$ movies, what is the maximum number of movies we can fully watch, knowing that we can only watch one movie at a time?

# Input data

The first line contains $N$.  
The following $N$ lines contain $2$ values $a b$, meaning that the movie starts at hour $a$ and ends at hour $b$.

# Output data

Print the maximum number of movies.

# Constraints and clarifications

* $1 \leq N \leq 2*10^5$
* $1 \leq a < b \leq 10^9$
* We can start another movie exactly when we finish the one we are currently watching.

# Example 1

`stdin`
```
3
3 5
4 9
5 8
```

`stdout`
```
2
```

## Explanation

We can watch the first and the third.
```
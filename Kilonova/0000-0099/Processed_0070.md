```markdown
# Task

Miguel is a spectator at a horse race and, somehow, found a list of the top speeds of all the horses. There are $N$ horses, each competing exactly once. Horses compete in pairs, the fastest one being the winner. A horse $A$ with speed $X$ will compete with a horse $B$ with speed $Y$ such that horse $B$ has not competed before and $max(X,Y)-min(X,Y)$ is minimized. There will not be 2 horses that satisfy this condition for any horse $A$.

Miguel wants to bet on all the winning horses.

# Input data

A natural number $N$ (the number of horses), followed by $N$ natural numbers (the speeds of each horse)

# Output data

Print, in ascending order, the indices of the winning horses.

# Constraints and clarifications
* $2 \leq N \leq 1000000$
* $N$ is even
* $1 \leq X \leq 100000000$
* The values of X are distinct

# Example

`stdin`
```
8
524 823 408 626 605 435 487 831 
```

`stdout`
```
1 4 6 8 
```

# Explanation

The pairs are $(408, 435)$, $(487, 524)$, $(605, 626)$, $(823, 831)$, the winners having indices $1, 4, 6, 8$
```

We call a list a sequence of natural numbers. We have several lists arranged in order, one below the other. We say that two lists $L_1$ and $L_2$ are neighbors if $L_1$ is immediately above $L_2$, or if $L_2$ is immediately above $L_1$. Any two neighboring lists $L_1$ and $L_2$ can be unified if they have at least one common element. By unification, the new list will include all elements from $L_1$ along with all elements from $L_2$. Lists $L_1$ and $L_2$ will disappear and in their place, the new list will appear.

# Task

Determine the minimum number of lists that result after applying a sufficient number of unifications so that there are no longer two neighboring lists that can be unified.

# Input data

The file `liste.in` contains on the first line a natural number $L$ representing the number of lists. Each of the next $L$ lines describes, in order, one list and has the structure: $K$, $A_1$, $A_2$, $\dots$, $A_K$. The first element denoted $K$ represents the number of elements in the list. It is followed by $K$ natural numbers representing the elements of the list. The numbers on the same line are separated by a space.

# Output data

The file `liste.out` contains a single natural number representing the required value.

# Constraints and clarifications

* $1 \leq L \leq 100\ 000$
* each initial list has at most $10$ elements;
* the values of the list elements are natural numbers $\leq 120$

# Example 1

`liste.in`
```
4
2 0 1
1 0
3 1 3 3
1 2
```

`liste.out`
```
2
```

## Explanation

We have four lists. We can unify the first and second list, which will be replaced by a single list. Then we can unify the resulting list from the first step with the list that was initially the third. Thus, we obtain two lists that can no longer be unified.

# Example 2

`liste.in`
```
7
3 1 11 111 
3 2 22 112
3 2 11 113
3 1 22 6
3 5 55 9
3 7 77 9
3 8 88 6
```

`liste.out`
```
3
```

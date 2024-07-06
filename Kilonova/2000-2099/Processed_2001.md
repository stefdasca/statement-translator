```markdown
# Task

You are given an empty stack, the number $T$ and $T$ operations as follows:
* $1 \ x$: add $x$ to the top of the stack;
* $2$: remove the last element from the stack;
* $3$: display the last element of the stack;
* $4$: display `YES` if the stack is empty, and `NO` otherwise.

# Input data

The first line contains the number $T$, and the next $T$ lines contain the operations.

# Output data

For each query of type $3$ or $4$, print the response on separate lines.

# Constraints and clarifications

* $1 \leq T \leq 10^5 $
* It is guaranteed that operations of type $2$ and $3$ will not be applied on an empty stack.
* For operations of type $1$, $1 \leq x \leq 10^7 $.

# Example

`stdin`
```
8
1 3
1 5
3
2
3
4
2
4
```

`stdout`
```
5
3
NO
YES
```

## Explanation

The stack after each operation:
1) $[3]$
2) $[3, 5]$
3) $[3, 5]$
4) $[3]$
5) $[3]$
6) $[3]$
7) $[]$
8) $[]$
```
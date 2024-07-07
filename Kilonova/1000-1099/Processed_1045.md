Given a sequence $V$ with $N$ non-zero natural values, stored at consecutive positions starting from position $1$. Let $S$ denote the following sequence of code applied to it:

```cpp
maxim = 0;
rep = 0;
for (i = 1; i \leq N; i++)
    if (V[i] > maxim)
        maxim = V[i];
    else
        if (V[i] == maxim)
            rep++;
```

Consider the operation of removing the element from $V$ at a given position $P$. As a result of the removal operation, the elements at positions $P + 1, P + 2, \ldots, N$ move to a position $1$ less, and $N$ decreases by $1$.

Given multiple removal operations (**independent of each other, meaning each is applied to the initial sequence, not after the previous operation**), determine the value of the variable `rep` if we apply the sequence $S$ to the sequence obtained after each removal operation.

# Input data

The file `maxime.in` contains on the first line a natural number $N$. The second line contains $N$ non-zero natural numbers, separated by a space. The next line contains a number $M$ representing the number of removal operations. The following line contains $M$ numbers, ranging between $1$ and $N$, representing the position in the sequence of the element where the current removal operation is performed. The numbers on this line are separated by a space.

# Output data

The file `maxime.out` contains on the first line $M$ numbers, separated by a space, representing the value of the variable `rep` obtained by applying the sequence $S$ after each removal operation.

# Constraints and clarifications

* $2 \leq N \leq 100\, 000$
* $1 \leq V_i \leq 100\, 000$
* $1 \leq M \leq 100\, 000$
* $1 \leq \text{removal position} \leq N$

# Example

`maxime.in`
```
6
3 1 3 8 1 8
3
2 5 6
```

`maxime.out`
```
2 2 1
```

## Explanation

Applying the first removal operation, the sequence becomes: $N = 5$ and $V = 3, 3, 8, 1, 8$, the value of `rep` becomes $2$.
Applying the second removal operation, the sequence becomes: $N = 5$ and $V = 3, 1, 3, 8, 8$, the value of `rep` becomes $2$.
Applying the third removal operation, the sequence becomes: $N = 5$ and $V = 3, 1, 3, 8, 1$, the value of `rep` becomes $1$.
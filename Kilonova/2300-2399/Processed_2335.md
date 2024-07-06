```markdown
After noon in Iezăreni, the $N$ members of the national informatics team will participate in a special game of paintball. Each contestant will receive a weapon and a single paintball. 
First, the contestants are numbered from $1$ to $N$. Having a single paintball, each contestant decides beforehand whom they will shoot. A contestant who has been shot with a paintball is declared "dead" and can no longer shoot.
Contestants shoot successively, in any order they wish.

# Task

Determine the minimum and maximum number of "deads".

# Input data

The input file `paintball.in` contains on the first line the natural number $N$ representing the number of contestants. The second line contains $N$ natural numbers separated by spaces; the $i$-th number on the line represents the number of the contestant whom contestant $i$ will shoot.

# Output data

The output file `paintball.out` will contain a single line containing two natural numbers separated by a space $nr_{min} \ nr_{max}$ representing the minimum and maximum number of "deads".

# Constraints and clarifications

* $1 \leq N \leq 1 \ 000 \ 000$;
* A contestant can shoot themselves.

# Example

`paintball.in`
```
8
2 3 2 2 6 7 8 5
```

`paintball.out`
``` 
3 5
```

## Explanation

If, for example, the order in which the contestants shoot is $1, 4, 3, 5, 7$, the minimum number of deads will be $2, 6, 8$.
If the order is $2, 1, 4, 7, 6, 5$, the maximum number of deads will be $3, 2, 8, 7, 6$.
```
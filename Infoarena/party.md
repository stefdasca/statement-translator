## Task

George wants to organize his coming-of-age party, and he wants the party to be unforgettable. The food, drinks, location, and sound system are already taken care of, and now the only problem left is inviting friends. He and his best friend Lucian have different preferences and to avoid arguments, they have set up a list of requirements that must all be met so that the party goes smoothly! For convenience, George's friends will be identified by integers from $1$ to $N$ and the requirements will be of types $0$, $1$, $2$, or $3$. A requirement of the type $x$ $y$ $0$ means that either $x$ or $y$ must attend the party; $x$ $y$ $1$ means that if $x$ attends, there is no restriction for $y$, but if $x$ does not attend then $y$ also does not attend; $x$ $y$ $2$ has the same meaning as requirement $1$ but symmetrically, and requirement $x$ $y$ $3$ means that at least one of $x$ and $y$ should not attend the party. Write a program to help the two determine which people will be invited to the party; it is guaranteed that it will always be possible to organize a party!

## Input data

The first line contains the numbers $N$ and $M$, which represent the number of friends and the number of requirements to be fulfilled. On the next $M$ lines, there will be requirements of the form $x$ $y$ $z$ where $1 \leq x,y \leq N$ and $0 \leq z \leq 3$.

## Output data

The first line contains a number $Nr$ representing the number of guests at the party, and on the next $Nr$ lines, one guest per line.

## Constraints and clarifications

$1 \leq N \leq 100$

$1 \leq M \leq 1\ 000$

## Examples

`party.in`
```
4 4
1 4 3
2 3 3
1 2 1
2 4 1
```

`party.out`
```
2
1
3
```

`party.in`
```
3 7
3 2 1
3 1 1
2 1 1
2 3 1
2 3 3
1 2 3
3 1 2
```

`party.out`
```
2
2
3
```

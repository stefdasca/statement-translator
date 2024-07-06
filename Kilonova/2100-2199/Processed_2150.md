# Task

In the city of Tecuci, there are $N$ buildings situated in a line, each with a certain height. Due to the high risk of lightning storms in that area, the mayor of the city has decided that the heights of the $N$ buildings must be modified so that any building is at least $K$ units taller than the one to its left (if such a building exists).
We define an operation on a building as either adding or subtracting one unit from its height. Because the city's budget is limited, the mayor wants to modify the buildings to the desired form with a minimum number of operations. Because you want to be made an honorary citizen of the city, you must help the mayor.

# Input data

The first line of the file `ktown.in` contains $N$ and $K$, the number of buildings in Tecuci, and the minimum difference between any building and the one to its left, respectively. The next line contains $N$ integers, the $i$-th of these integers representing the height of the $i$-th building.

# Output data

The first (and only) line of the file `ktown.out` must contain the minimum number of operations required to modify the heights of the buildings so that they meet the required properties.

# Constraints and clarifications

* $1 \leq N \leq 3\ 000$
* $1 \leq K \leq 1\ 000\ 000$
* $-2\ 200\ 000\ 000 \leq$ height of a building $\leq 2\ 200\ 000\ 000$
* For $60\%$ of the tests $N \leq 300$
* The value of $K$ was determined by researchers from the National University of Tecuci, after extensive debates

# Example

`ktown.in`
```
5 1
5 4 3 2 1
```

`ktown.out`
```
12
```

## Explanation

We will bring building $1$ to height $1$ (at a cost of $4$), building $2$ to height $2$ (at a cost of $2$), building $3$ to height $3$ (at a cost of $0$), building $4$ to height $4$ (at a cost of $2$), and building $5$ to height $5$ (at a cost of $4$).
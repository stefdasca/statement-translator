Here is the translated text:

The trade of flooring installer has become easier since laminated flooring appeared. It comes in square tiles of $1 \\ \\text{m} ^ 2$ and its installation is quite easy. Gigel is convinced that he is skilled enough to perform this operation in his own home. He has the house plan and has bought a certain amount, representing $X \\ \\text{m} ^ 2$, of laminated flooring. The house plan is described by a two-dimensional array of size $N \\times M$, each element of the array representing exactly $1 \\ \\text{m} ^ 2$. The walls are represented by the character `P` and the room surfaces by the character `S` (space). In the plan of the following figure, a house is described with $5$ rooms having respectively, areas of $10, 2, 1, 3, 5 \\ \\text{m} ^ 2$.
~[parchet.png|align=center]
Gigel is not sure if the flooring he bought is enough. For this reason, he initially decided to lay the flooring starting with the largest room, then the next one, in descending order of area, and so on, until the remaining flooring is no longer enough to cover the area of the next room. He will not leave a larger room unfloored to floor a smaller one.
Gigel is also considering the possibility of completely covering a maximum number of rooms using the entire amount of flooring.

# Task

Given $N$, $M$, $X$ and the house plan, determine:
1. the number $C$ of rooms that Gigel managed to cover and the number $R$ of $\\text{m} ^ 2$ of remaining flooring, proceeding as he initially decided.
2. the number of possibilities to floor a maximum number of rooms using the entire amount of flooring.

# Input data

The input file `parchet.in` contains on the first line a natural number $p$ representing the requirement to be solved ($1$ or $2$). The second line of the input file contains the natural numbers $N$ and $M$ separated by a space. The third line contains the natural number $X$. The next $N$ lines contain $M$ characters `P` or `S` describing the house plan.

# Output data

If the value of $p$ is $1$, then the output file `parchet.out` contains on the first line two natural numbers $C$ and $R$ separated by a space, representing respectively the number of rooms covered with flooring and the amount of remaining flooring, expressed in $\\text{m} ^ 2$.
If the value of $p$ is $2$, then on the first line of the output file it will be written the number of possibilities to floor a maximum number of rooms using the entire amount of flooring, or the value $0$ if this is not possible.

# Constraints and clarifications

* $2 \\leq N, M \\leq 250$
* In the house, there are at most $20$ rooms and the house has walls towards the exterior.
* The area of a room does not exceed $(N - 2) \\cdot (M - 2) \\ \\text{m} ^ 2$.
* For a correct solution to requirement $1$, $50\\%$ of the score is awarded, and for a correct solution to requirement $2$, $50\\%$ of the score is awarded.

# Example 1

`parchet.in`
```
1
7 9
19
PPPPPPPPP
PSSSPSPSP
PSSSPSPPP
PSSPPPPSP
PSPPSSPSP
PSPSSSPSP
PPPPPPPPP
```

`parchet.out`
```
3 1
```

## Explanation

Only requirement $1$ will be solved.
The house has $5$ rooms with areas of $10, 2, 1, 3, 5 \\ \\text{m} ^ 2$. Three rooms can be completely floored using $18 \\ \\text{m} ^ 2 = 10 + 5 + 3$. $1 \\ \\text{m} ^ 2$ of flooring remains unused.

# Example 2

`parchet.in`
```
2
7 9
19
PPPPPPPPP
PSSSPSPSP
PSSSPSPPP
PSSPPPPSP
PSPPSSPSP
PSPSSSPSP
PPPPPPPPP
```

`parchet.out`
```
1
```

## Explanation

Only requirement $2$ will be solved.
If the rooms with areas $10, 1, 3, 5$ are selected, the entire flooring area will be used. There is only one possibility to select a maximum number of rooms.
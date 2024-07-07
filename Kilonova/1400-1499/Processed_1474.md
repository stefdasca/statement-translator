
Farmer Quinto has an orchard full of fruit trees. The orchard has $N$ rows, numbered from $1$ to $N$, with $M$ fruit trees in each row, numbered from $1$ to $M$. Quinto's orchard is special, so for some trees, the amount of fruit (expressed in kg) that can be harvested is known, while for others it can be determined based on a formula. Quinto aims to harvest $C$ kg of fruit from the trees in his orchard.

He uses a modern machine for picking fruit. The machine can be used on any of the orchard's rows, but it can only gather fruit from a consecutive sequence of trees, starting with the first tree on that row, without the possibility of partially picking fruit from a tree.

Concerned about the beauty of his orchard, Quinto thought of additional restrictions for harvesting the quantity $C$ of fruit. Thus, he wants to gather the fruit from trees on a maximum of $R$ different rows, so that $N - R$ rows remain complete.

Also, he wants to prioritize picking trees that have as small an amount of fruit as possible, so that the most productive trees remain in the orchard. Quinto realized that it is difficult to pick exactly $C$ kg of fruit, so he is also content with a larger quantity that meets the other conditions he has imposed.

# Task

Determine the smallest possible value $X$ so that it is possible to gather, under the above conditions, a quantity of at least $C$ kg of fruit and any tree from which fruit is picked contains at most $X$ kg of fruit.

# Input data

The first line of the file `livada.in` contains 4 natural numbers $N, M, C, R$ with the meaning from the statement. The second line of the input file contains 5 natural numbers $x, y, z, w, u$, separated by a space. If we denote $A[i][j]$ as the amount of fruit (expressed in kg) from the $j$-th tree on row $i$, then:

The third line of the input file contains $M$ values $A[1][i]$, $1 \leq i \leq M$, separated by a space.

The fourth line of the input file contains $N-1$ values $A[i][1]$, $2 \leq i \leq N$, separated by a space. The other values $A[i][j]$, $2 \leq i \leq N$, $2 \leq j \leq M$, are calculated according to the formula:

$$
A[i][j] = ( x \cdot A[i-1][j] + y \cdot A[i][j-1] + z \cdot A[i-1][j-1] + w ) \% u
$$

# Output data

The output file `livada.out` will contain a single value written on the first line, which represents the smallest value of the amount of fruit (expressed in kg) from a picked tree, so that all the problem's restrictions are respected.

# Constraints and clarifications

* $1 \leq R \leq N \leq 100$
* $1 \leq M \leq 25\ 000$
* $0 \leq x, y, z, w, u \leq 10^9$
* $0 \leq A[i][j] \leq 10^9$
* Attention to the determination of each value $A[i][j]$ because the formula contains products that can yield values larger than $2^{32}-1$
* $1 \leq C \leq 10^{18}$
* It is guaranteed that the problem has a solution for all tests
* For $30$% of tests, it is guaranteed that $1 \leq M \leq 100$ and $1 \leq A[i][j] \leq 100$
* For $70$% of tests, it is guaranteed that $1 \leq M \leq 4\ 000$

# Example

`livada.in`
```
5 6 18 4
3 6 5 2 7
4 1 3 5 1 2
5 2 6 3
```

`livada.out`
```
4
```

# Explanation

There are $5$ rows with $6$ trees in each row. The adjacent figure shows the matrix obtained by the specified formulas.

We aim to collect at least $18$ kg of fruit from a maximum of $4$ rows out of the $5$.

$$
\colorbox{#808080}{4 1 3} 5 1 2 \\
5 6 3 1 1 5 \\
\colorbox{#808080}{2 1} 5 1 2 6 \\
6 2 6 3 3 6 \\
\colorbox{#808080}{3 0 2 4 1} 6 \\
$$
In the adjacent figure, a possible solution is presented where the maximum amount collected from a tree is $4$ kg.

It is not possible to collect $18$ kg of fruit from a maximum of $4$ rows while only picking trees with a fruit amount of $3$ kg (in this case, at most $8$ kg can be collected).

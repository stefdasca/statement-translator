## Task

After numerous palindrome problems composed by $Dani$, his team members told him to refresh his ideas because everyone got bored of them. $Dani$ agreed, but he didn't give up on his more general passion for symmetry. This time, he was inspired by the history of the ancient $Hansha$ empire, whose development he found very interesting. Initially, the $Hansha$ empire consisted of a single city, and this city had a number as its name: the number $1$. Then, each century, for $K$ centuries, the empire developed as follows: Its number of cities doubled, and if its cities were numbered up to now from $1$ to $N$, the new cities would take the values $N + 1$, $N + 2$\dots $2 * N$ as names. Furthermore, these $N$ new cities would have the exact same road structure as the initial cities. Specifically, there would be a road between city $N + i$ and city $N + j$, where $1 \leq i, j \leq N$ if and only if there was already a road between cities $i$ and $j$. Thus, it could be said that at this stage of development, the empire "mirrored", forming two identical copies. To connect these copies, a single new road will be built connecting a duplicated city to its counterpart. Specifically, for a unique $1 \leq x \leq N$, a road will be added between nodes $x$ and $N + x$. This $x$ can vary from one development phase to another. $Dani$ has several possible scenarios of the $Hansha$ empire's development in front of him. A scenario is defined by a number $K$, which represents the number of development phases and the description of the $K$ values $x$, the numbers of the cities that will be connected with their duplicate in each of the $K$ phases of development. For each scenario, $Dani$ asks what is the minimum number of roads that need to be traversed to get from city $A$ to city $B$ after all the development stages in that scenario have been completed.

## Input data

The input file hansha.in will contain on its first line the value $T$, representing the number of scenarios to be analyzed. Then follow the $T$ scenarios, the format of a scenario being as follows: The first line contains the value $K$, representing the number of development phases in that scenario. A line with $K$ values follows, representing the number of the city that will be connected with its duplicate at each development phase. The third line will contain two values $A$ and $B$, representing the numbers of the cities whose distance interests $Dani$.

## Output data

The output file hansha.out will contain $T$ values, the $i$-th of these representing the answer to $Dani$'s question in scenario number $i$.

## Constraints and clarifications

$1 \leq T \leq 1.000$

$1 \leq K \leq 30$

For $40$ points

$1 \leq K \leq 10$

## Example

```
hansha.in
3
4
1 2 3 4
1 16
4
1 2 4 7
2 13
5
1 2 4 6 10
3 30
```

```
hansha.out
6
7
11
```
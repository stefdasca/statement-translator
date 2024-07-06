# Task

Fetițele din grupa mare de la grădiniță culeg flori și vor să împletească coronițe pentru festivitatea de premiere. În grădină sunt mai multe tipuri de flori. Fiecare dintre cele $n$ fetițe culege un buchet având același număr de flori, însă nu neapărat de același tip. Pentru a împleti coronițele fetițele se împart în grupe. O fetiță se poate atașa unui grup numai dacă are cel puțin o floare de același tip cu cel puțin o altă fetiță din grupul respectiv.

# Task
Given a natural number $n$ representing the number of girls and a natural number $k$ representing the number of flowers in a bouquet, determine the groups that are formed.

# Input data
The input file `flori.in` contains on the first line, separated by a space, the natural numbers $n$ and $k$, representing the number of girls and respectively the number of flowers in each bouquet. Each of the next $n$ lines contains, for each girl, $k$ values separated by a space representing the types of flowers picked.

# Output data
The output file `flori.out` will contain on each line a group formed by the ordinal numbers of the girls separated by a space, in ascending order, as in the example.

# Constraints and clarifications
- $1 \leq n \leq 150$
- $1 \leq k \leq 100$
- The type of a flower is an integer from the interval $[0, 100]$.
- In a group, the ordinal numbers of the girls must be given in strictly ascending order.
- In the output file, the groups will be displayed in ascending order of the ordinal number of the first girl in the group.

# Example
`flori.in`
```
5 4
1 2 3 4
5 6 9 6
1 1 1 1
2 4 4 3
7 7 7 7
```
`flori.out`
```
1 3 4
2
5
```
## Explanation
Girls $1$ and $3$ both picked flowers of type $1$, and girls $1$ and $4$ both picked flowers of types $2$, $3$, and $4$, so all three girls ($1$, $3$, $4$) will be in the same group. Girls $2$ and $5$ will each form a separate group because they did not pick flowers of the same type as any other girl.
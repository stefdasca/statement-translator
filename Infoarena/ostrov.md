## Task

Ostrov

Recently, a new island in Russia called Ostrov was discovered. Initially, this island has no city or street built. Due to its extraordinary geographical properties, many Russian investors want to invest in this island to build magical flat water factories to continue the beautiful habits of those from Staropramen. Thus, there are $Q$ operations as follows:
- $0 \rightarrow$ city $N + 1$ is built
- $1 \ X \ nr \ m$ and in the following $m$ lines, there are 3 numbers each $x, y, s$ representing a bidirectional street between cities $x$ and $y$ with cost $s$, $x$ and $y$ belonging to the $nr$ cities built united with city $X$ -> the owner of city $X$ builds another $nr$ cities (cities from $N+1$ to $N+nr$) which are connected (city $X$ with the $nr$ new cities) through the $m$ bidirectional streets mentioned above. After this operation, $N = N + nr$
- $2 \ x \ y \ s \rightarrow$ because it is not possible to reach from city $x$ to city $y$, the investors owning these two cities collaborate and build a bidirectional street between cities $x$ and $y$ with cost $s$
- $3 \ x \ y \ s \rightarrow$ the cost of the street between cities $x$ and $y$ becomes $s$. It is guaranteed that the street between $x$ and $y$ was previously built
- $4 \ x \ y \rightarrow$ display the minimum cost of a route from city $x$ to city $y$, or $-1$ if it is not possible to reach from city $x$ to city $y$

## Input data

The input file `ostrov.in` contains on the first line the number $Q$, followed by the $Q$ operations in the form described above.

## Output data

In the output file `ostrov.out`, you must print the answer for each operation of type $4$ on a separate line.

## Constraints and clarifications

$$
\begin{align*}
\text{at the end } N &\leq 100000 \\
\text{at the end the number of streets} &\leq 300000 \\
nr &\leq 10 \\
s &\leq 1000 \\
the number of operations of type 3 &\leq 10000 \\
the number of operations of type 4 &\leq 300000 \\
ATTENTION! \text{ It is recommended to parse the input file. You can use the code on this site}
\end{align*}
$$

## Example

`ostrov.in`
```
11
0
1 1 3 4
1 2 3 2 4 5
1 3 1 3 4
2 4 1 4
0
2 3 5
4 1 2
3 4 2
6 2 6 8
3 6 7
1 4 5 7
0
4 9
2 3 2
4 1 4
5 7
3 11
-1
10
```

`ostrov.out`
```
0
1
1
2
3
4
-1
```
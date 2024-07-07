
An undirected complete graph with $N$ vertices labeled from $1$ to $N$ is considered. We associate with each vertex $i$ an initial value $v_i$. The values in the vertices transform starting from an initial moment $T_0=0$ every second according to the following rule: the value at a vertex $k$ at second $T+1$ is equal to the sum of the values in all other vertices at second $T$.

# Task
Knowing $N$ – the number of vertices of the graph as well as the initial values in the vertices of the graph, answer $Q$ questions given as pairs of the form $(t, p)$ with the significance: "If after $t$ seconds the values in the vertices are considered sorted in ascending order, what is the value on position $p$?" Since these values can be very large, they will be calculated modulo $40\ 099$.

# Input data

The input file `complet.in` contains on the first line two non-zero natural numbers separated by a space: $N$ and $Q$. The second line contains $N$ non-zero natural numbers separated by a space, representing the values initially in the vertices of the graph. The third line contains exactly $9$ non-zero natural numbers separated by a space $x \\ y \\ z \\ t_1 \\ t_2 \\ t_3 \\ p_1 \\ p_2 \\ p_3$ with the help of which the $Q$ questions will be constructed. The first three questions are given by the pairs $(t_1, p_1)$, $(t_2, p_2)$, $(t_3, p_3)$. The question $i$ (with $i=4..Q$) will be generated with the relations:
* $t_i = 1 + (t_{i-3} \cdot x + t_{i-2} \cdot y + t_{i-1} \cdot z)\ %\ 10^{15}$
* $p_i = 1 + (p_{i-3} \cdot x + p_{i-2} \cdot y + p_{i-1} \cdot z)\ %\ N$
* $x, y, z$ are non-zero natural numbers fixed with at most $3$ digits

# Output data

The output file `complet.out` will contain $Q$ lines, each containing a single number representing the answer to the corresponding question from the input file, modulo $40\ 099$.

# Constraints and clarifications
* $2 \leq N \leq 100\ 000$
* The initial values in nodes are non-zero natural numbers and less than or equal to $30\ 000$
* $1 \leq p_i \leq n$ for each question
* $0 \leq t_i \leq 10^{15}$ for each question
* $3 \leq Q \leq 10^6$

# Example

`complet.in`
```
4 4
1 4 2 3
1 1 1 1 1 1 1 1 1
```

`complet.out`
```
6
6
6
204
```

## Explanation

The questions will be:
$1 \ 1$
$1 \ 1$
$1 \ 1$
$4 \ 4$
In the second $1$ the values are: $9 \ 6 \ 8 \ 7$
After sorting, on the first position is $6$.
In the second $4$ the values are: $201$, $204$, $202$, $203$
After sorting, on the fourth position is $204$.

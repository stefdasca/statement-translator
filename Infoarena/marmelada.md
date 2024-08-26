##  Marmelada

The mayor of the Marmelada county needs to entirely rebuild the road network. In the county, there are $N$ cities numbered with natural numbers from $1$ to $N$. Additionally, $M$ roads need to be constructed, where a road directly connects two cities and can be traveled in both directions. The mayor now has to decide what length each road should have. The construction company has offered to build $M$ roads with lengths of $C_1$, $C_2$, $\dots$, $C_M$, and the mayor is free to decide the length of each road (in other words, a bijection must be created between the set of lengths and the set of roads). The mayor has two favorite cities, $S$ and $D$, and wishes for the shortest possible path to exist between these two cities after the roads are built. A path is a succession of roads such that any two consecutive roads share a common city. Help the city mayor determine the length of each road connecting two cities.

##  Input data

The input file `marmelada.in` contains on the first line four natural numbers separated by a space, $N$, $M$, $S$, and $D$, with the significance given in the statement. Then follow $M$ lines, each containing two numbers separated by a single space $a$ and $b$ indicating that a road must be built between cities $a$ and $b$. On line $M+2$ of the file, there are $M$ natural numbers $C_1$, $C_2$, $\dots$, $C_M$, with the significance given in the statement.

##  Output data

In the output file `marmelada.out`, $M$ natural numbers between $1$ and $M$ (each number on a new line) will be displayed. If the $i$-th number in the file is $j$, it means that the road with index $i$ (the roads are numbered from $1$ to $M$ in the order they appear in the input file) has been assigned the length $C_j$. If there are multiple solutions, any of them can be displayed.

##  Constraints and clarifications

$1 \leq N$, 

$M \leq 100\ 000$

The lengths of the roads are natural numbers in the range $[1, 10\ 000]$

The roads are numbered from $1$ to $M$ in the order they appear in the input file 

There will always be at least one path between $S$ and $D$ 

There can be multiple roads between two cities, and there can be roads that connect a city with itself 

##  Example

`marmelada.in` 

```
4 4 1 4
1 2
2 4
1 3
3 4
1 2 3 4
```

`marmelada.out`

```
1
2
3
4
```

##  Explanation

The road $1-2$ has length $1$ and the road $2-4$ has length $2$, so there is a path of length $3$ between cities $1$ and $4$. Another possible solution would be `3 4 1 2`. There is no other allocation of the road lengths that results in a shorter path between $1$ and $4$.
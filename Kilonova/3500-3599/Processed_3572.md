# Task

The railway network of a country has the shape of a tree. The nodes are the cities of the country, and the edges represent pairs of cities between which there is a railway line. Each edge has a given length in kilometers.

Node $1$ is the capital of the country. At some point, trains simultaneously depart from two given cities heading towards the capital, following the shortest path (the unique elementary path in the tree between the starting node and node $1$). Each train has a speed expressed in kilometers per hour, and the trains have different speeds. The trains will pass through stations without stopping. 

It is a problem if the two trains end up intersecting at some moment on one of the edges, with the slower train being overtaken by the faster train. In this case, a supplementary railway line should be constructed between the ends of that edge. We want to identify these cases. Note that if the routes of two trains intersect exactly at a city, there is no need to build anything additional (stations have multiple spare lines). Given the structure of the tree, we must answer several queries of the type described above. If for a query a supplementary railway line should be constructed, we must also indicate the edge where the train paths intersect.

# Input data

The file `trenuri.in` contains on the first line the number of cities in the country, denoted by $n$. The next $n-1$ lines each contain an edge described by $3$ values: its endpoints (numbers from $1$ to $n$) and its length in kilometers (a positive natural number). The following line contains the value $m$, representing the number of queries. Each of the following $m$ lines describes a query with 4 values: $T_1$, $V_1$, $T_2$, $V_2$, respectively: the city from which the first train departs, the speed of the first train, the city from which the second train departs, the speed of the second train.

# Output data

The file `trenuri.out` will contain $m$ lines, one for each query, in the order they appear in the input file. If the trains corresponding to a query do not intersect strictly on an edge, the corresponding line will contain only the value $0$. If the trains intersect strictly on an edge, the respective line will contain $1$ and the nodes that describe the edge on which they intersect, *in increasing order*.

# Constraints and clarifications

* $1 \leq n \leq 100\ 000$;
* $1 \leq m \leq 100\ 000$;
* For $30\%$ of the tests, $1 \leq n \leq 1\ 000$ and $1 \leq m \leq 1\ 000$;
* The lengths of the edges and the speeds of the trains are positive natural numbers $\leq 10\ 000$;
* For any query:
  * $T_1 \neq T_2$;
  * $V_1 \neq V_2$.
* The queries are independent;
* For $51$ points $n \leq 1\ 000$ and $m \leq 1\ 000$;
* For $23$ of these points, the tree is a "line".

# Example

`trenuri.in`
```
6
1 2 6
2 3 2
2 4 2
2 5 5
4 6 40
3
3 2 4 1
3 2 5 4
4 1 5 4
```

`trenuri.out`
```
0
1 1 2
0
```

## Explanation

Trains $3$ and $4$ will not meet. For example, train $1$ after one hour is in city $2$, while train $4$ is then halfway between cities $4$ and $2$. Moreover, train $4$ is slower than $3$.
Trains $3$ and $5$ meet on edge $(2, 1)$. Train $5$ overtakes train $3$ at some point strictly on this edge.
Trains $4$ and $5$ do not meet (train $4$ arrives in city $2$ after $2$ hours, while train $5$ has already passed by city $2$ by that time, heading toward $1$ and with a greater speed).

~[retea.png|width=20rem]
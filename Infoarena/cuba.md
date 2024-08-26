## Task

The great businessman and artist, Sorin Pastrama, wants to spend his spring vacation in Cuba. The country looks like a tree with $N$ nodes, each edge having a length (these are bidirectional). In each node, there are gas stations (where you can refuel) and, also, on each edge, there is an electric car that can carry a fuel tanker with the purpose of helping Mr. Pastrama to cross the edge safely. The cost of renting such an electric car to carry $x$ units of fuel is $x^2$. To plan his journey, Pastrama will ask for your help and requests you to answer $Q$ queries of the form: $X$ $Y$ $C$ $\to$ what is the minimum cost that Pastrama has to pay the company that rents those electric cars if he wants to travel from node $X$ to node $Y$, having a Mercedes with a tank capacity of $C$ units of fuel? (certain edges will have a length greater than $C$, so on these edges, an electric car of a certain capacity will be rented)

## Input data

The input file `cuba.in` contains on the first line the natural numbers $N$ and $Q$, with the meanings from the statement. On the next $N-1$ lines, there are two natural numbers $T_i$ and $L_i$ representing the parent of node $i$ and the length of the respective edge ($2 \leq i \leq N$). The root of the tree is node $1$. On the next $Q$ lines, there are 3 numbers $X$ $Y$ $C$, with the meanings from the statement.

## Output data

The output file `cuba.out` contains $Q$ lines, each line containing the answer to a query, in the order they appear in the input file.

## Constraints and clarifications

$1 \leq N, Q \leq 10^5$ 

$1 \leq L_i, C \leq 10^5$ 

$1 \leq X, Y \leq N$ 

To traverse a distance of length $x$, $x$ units of fuel are required. No matter how much Pastrama would like to spend as much time as possible with the Cuban driver of the electric car, he wants to keep his money so he can travel to other foreign countries as well.

## Example

`cuba.in`

```
5 3
1 4
1 5
2 1
2 3
5 3
4 2
3 2 4
5 3 1
```

`cuba.out`

```
13
0
```

## Explanation

First query: The tank with a capacity of $4$ is enough for the edges $5 \to 2$ and $2 \to 1$, but it is not enough for the edge $1 \to 5$. For this edge, one more unit of fuel is needed. Therefore, the cost is $1^2 = 1$.

Second query: For the edges $2 \to 1$ and $1 \to 5$, $2$ and $3$ additional units of fuel are required, respectively. Therefore, the cost is $2^2 + 3^2 = 13$.

Third query: The tank with a capacity of $3$ is enough for each edge on the path from node $4$ to node $5$. Therefore, the cost is $0$.
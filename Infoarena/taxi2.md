## Task

We are in the year $2050$, and the Drumul Taberei metro has been recently inaugurated. Taxi companies believe that the lives of Bucharest's residents have become too good, so they decided to punish them by increasing the costs of a taxi ride. Specifically, a customer ordering a taxi by phone now has to pay for the distance the taxi travels from its initial location to the customer's address. Furthermore, if at any point there are $M$ phone orders that need to be fulfilled and $M$ available taxis, the dispatch will pair the taxis with the orders such that the total distance traveled by the $M$ taxis to the respective addresses is maximized. We want to study the costs of such a pairing, based on the initial positions of the taxis and customers. In the meantime, Bucharest has become an undirected tree with $N$ nodes and positive edge distances (a tragic transformation, but it has not necessarily worsened the traffic). Each of the $M$ taxis can be located in any of the $N$ nodes. The same is true for each of the $M$ customers. A node can host an unlimited number of taxis and/or customers. Thus, there are a total of $N^{2M}$ different configurations of taxi/customer positions. If a taxi located at node $X$ is paired with an order from node $Y$, the cost of its journey will be equal to the distance between nodes $X$ and $Y$. Our question is the following: If $S$ is the sum of the maximum cost pairings for all the $N^{2M}$ possible configurations, what is the value of $S$ modulo $10^9 + 7$?

## Input data

The input file `taxi2.in` will contain on its first line the numbers $N$ and $M$, representing the number of nodes of Bucharest, respectively the number of taxis and the number of customers. The next $N - 1$ lines will contain a triplet $a \ b \ dist$ indicating that there is an undirected edge between nodes $a$ and $b$ with distance $dist$.

## Output data

The output file `taxi2.out` will contain the value $S$ modulo $10^9 + 7$.

## Constraints and clarifications

$1 \leq N, M \leq 1,000$

For $70\%$ of the score, $1 \leq N, M \leq 100$

For each edge of the tree, $1 \leq dist \leq 10,000$

## Example

`taxi2.in` 

```
2 1
1 2 5
```

`taxi2.out` 

```
10
```
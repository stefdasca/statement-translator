## Task

Aurora Flash is connected to a network of $N$ computers and $M$ bidirectional connections. Each connection between two computers $x$, $y$ has an associated cost which represents the time required for the information to travel through that connection. Computer $1$ is Aurora's computer and computer $N$ is the server. Aurora is tired of so much lag (she cannot play Starcraft $2$ peacefully) so she has bought $K$ accelerators. An accelerator can be installed on a certain connection to halve the cost of that connection. If $k$ accelerators are installed on a connection, the cost of the connection decreases by $2^k$ times. Aurora wants to install the $K$ accelerators to minimize the time required for her computer to communicate with the server. Information exchange between two computers happens on the minimum cost path that connects the two computers. The cost of a path is equal to the sum of the costs of the connections on that path. Help Aurora Flash to play Starcraft $2$.

## Input data

The input file `retea.in` will contain on the first line the numbers $N$, $M$, and $K$ representing the number of computers in the network, the number of connections between the $N$ computers and, respectively, the number of accelerators bought by Aurora. The next $M$ lines will each contain $3$ natural numbers $x$, $y$, and $c$ representing that there is a bidirectional connection of cost $c$ between computers $x$ and $y$.

## Output data

In the output file `retea.out` you will print a single number $C$ with exactly $4$ decimal places, representing the minimum cost of a path between computers $1$ and $N$ after installing the $K$ accelerators.

## Constraints and clarifications

$1 \leq N \leq 1\,000$

$1 \leq M \leq 100\,000$

$1 \leq K \leq 10$

The cost of any connection will not exceed $1\,000\,000$

## Example

`retea.in`
```
5 5 2
1 2 1
2 3 9
3 5 1
1 4 5
4 5 5
```

`retea.out`
```
4.2500
```

## Explanation

Aurora installs both accelerators on the connection of cost $9$ which results in a path of cost $4.25$. If she had placed one accelerator on each of the connections of cost $5$, the minimum path would have been equal to $5$.
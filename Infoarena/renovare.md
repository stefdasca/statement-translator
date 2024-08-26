# Renovation

The population of the city of Galati has grown significantly in recent years, and its infrastructure struggles to keep up with the large number of residents. The city is supplied with water by a pumping station located a few kilometers away, which pumps water through a network of pipes. The pipes are interconnected by reservoirs, such that a pipe connects 2 reservoirs, and 2 distinct pipes communicate with each other if they have an end in the same reservoir. Each pipe is characterized by 4 numbers: $a$, $b$, $c$, $cst$, with the following meaning: through that pipe, $c$ liters of water can be pumped from reservoir $a$ to reservoir $b$. If we pay $nr*cst$ lei for renovating the pipe, then we will be able to pump $c+nr$ liters of water through it. It is known that reservoir number $1$ is the pumping station and reservoir number $n$ is the reservoir from which water goes to the houses in the city. Your mission is to find out the minimum cost that needs to be paid for the pumping station to send $x$ liters of water to the city.

## Input data

The first line of the `renovare.in` file will contain 3 numbers $n$ $m$ $x$ representing the number of reservoirs, the number of pipes, and the number of liters that need to be pumped through the network, respectively. On the following $m$ lines, there will be 4 numbers each, representing the characteristics of each pipe, with the numbers having the meaning described in the statement.

## Output data

The `renovare.out` file will contain a single number, the minimum cost that needs to be paid for the network to be able to transport $x$ liters of water from reservoir $1$ to reservoir $n$.

## Constraints and clarifications

$1 \leq n \leq 200$

$1 \leq m \leq 2000$

$1 \leq x \leq 200000$

Water cannot be stored in a reservoir, the amount of water entering the reservoir must be equal to the amount of water exiting it.

The initial capacity of the pipes is less than or equal to $100$

The renovation cost of the pipes is less than or equal to $1000$

It is guaranteed that the result will be less than $2 \* 10^9$

## Example

`renovare.in`
```
6 7 11
1 2 3 2
1 3 2 3
1 4 1 2
4 5 1 3
2 3 6 2
3 6 5 2
5 6 1 10
```

`renovare.out`
```
22
```

## Explanation

We increase the capacity of the pipe connecting reservoirs $1$ $2$ by $3$ units, the capacity of the pipe connecting reservoirs $1$ $3$ by $2$ units, and the capacity of the pipe connecting reservoirs $3$ $6$ by $5$ units. Thus, the total cost is: $2*3 + 3*2 + 5*2 = 22$
Ivan needs to get to Cluj-Napoca to participate in the National Informatics Team preparations. For this, he has chosen the train as his mode of transport. He has been given a sum for transport by the Ministry of Education, Research and Innovation, which he must not exceed. Ivan doesn't like to wait, so he would like the maximum waiting time between two trains to be as small as possible.

# Task

Given Ivan's budget and the list of all trains running, along with the cost of a ticket, the departure time, and the arrival time of the train, find the cheapest way to get from city $1$ to city $N$.

# Input data

The first line of the `trenuri.in` file contains $3$ integers, $N$ (number of cities), $M$ (number of trains), and $B$ (Ivan's budget). The following $M$ lines contain the descriptions of the trains. On line $i + 1$, there are integers $a, b, c, p, s$ (separated by a single space), indicating that there is a train that departs from city $a$ at time $p$, arrives at $b$ at time $s$, and the cost of a ticket for this train is $c$.

# Output data

The `trenuri.out` file will contain on the first line $2$ integers, $T$ and $C$, representing the minimum wait time and the cost of the tickets. In the case of multiple solutions with the same $T$, the solution with the minimum $C$ will be displayed.

# Constraints and clarifications

* \(2 \leq N \leq 15\ 000\)
* \(2 \leq M \leq 200\ 000\)
* \(0 \leq c \leq 10\ 000\)
* \(0 \leq B \leq 2\ 000\ 000\ 000\)
* For any train, \(p < s\)
* Waiting time at the initial station is not counted; Ivan can come from home at any time he wishes
* A train departing at time $p$ can be taken only if Ivan arrives at the departure station at a time $s \leq p$; wait time is $p - s$
* There is a solution for all tests
* Ivan recommends you parse the input file; this way, you will have more time to help him

# Example 1

`trenuri.in`
```
5 6 20
1 2 4 2 8
2 4 5 9 11
1 3 5 1 5
3 4 1 2 6
4 5 13 12 14
4 5 10 15 20
```

`trenuri.out`
```
4 19
```

## Explanation

Ivan first takes the train from city $1$ to city $2$. From city $2$, he takes the train to city $4$, waiting one time unit. After that, he takes the train to city $5$ at time $15$, waiting $4$ time units. The maximum wait time is $4$ time units, and the total cost is $19$.
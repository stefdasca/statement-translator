A newly elected mayor wants to prove to his electorate that voting for him was the right choice. To this end, he has decided to repave the streets between $N$ important buildings in the city, numbered from $1$ to $N$. Between any two of these buildings, there is a single street with two-way traffic. The building numbered $1$ is the town hall.

The mayor asks his advisors to determine all routes on which the streets can be repaved among the $N$ buildings, knowing that there are $H$ "preferred" streets that must be repaved mandatory. It is known that any two preferred streets do not share a common endpoint. The routes that will be repaved must start from the town hall, visit each of the other $N-1$ buildings exactly once, and then return to the town hall.

# Task

Determine the number of distinct routes, respecting the above requirements.

# Input data

The first line of the input file `asfalt.in` contains two natural numbers separated by a space, representing the number of buildings ($N$), and the number of the mayor's preferred streets ($H$).

# Output data

The first line of the output file `asfalt.out` will contain a single integer, representing the number of possible distinct routes.

# Constraints and clarifications

* $3 \leq N \leq 1 \ 000$
* $0 \leq H \leq \frac{N}{2}$
* If a route differs from another only by the direction in which the road is traversed, starting from the town hall and returning there, it is considered identical to the first. For example, route $1 - 2 - 3 - 4 - 1$ is identical to route $1 - 4 - 3 - 2 - 1$.

# Example

`asfalt.in`
```
4 1
```

`asfalt.out`
```
2

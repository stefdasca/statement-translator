Three Ubuntzei have decided to spend May 1st at the seaside, together with their friends, which is why they planned a trip from their city Cluj-Napoca to Vama Veche, where the sand awaits them.

In the land of Ubuntzei, there are $N$ localities, numbered from $1$ to $N$, connected by $M$ bidirectional roads of different lengths. The departure locality of the Ubuntzei, the city of Cluj-Napoca, is numbered $1$, and the destination locality, Vama Veche, is numbered $N$. Between any two localities, there is at most one road. Each road connects two distinct localities and it is possible to travel between any two localities using only roads.

The friends of the Ubuntzei live in $K$ distinct localities, different from Cluj-Napoca and Vama Veche. To avoid traveling alone, the three Ubuntzei want to pass through the $K$ localities where their friends live, and then, together with them, continue their trip to the sea.

Eager to reach their destination quickly, the Ubuntzei decided to plan a route of minimum length that passes through all $K$ localities.

# Task
Write a program to determine, for the Ubuntzei, the minimum length $L$ of a route from Cluj-Napoca to Vama Veche that passes through all $K$ localities.

# Input data
The first line of the input file `ubuntzei.in` contains two natural numbers $N\ M$, separated by a space, with the meaning from the statement. The second line of the file contains $K + 1$ distinct natural numbers: $K\ C_1\ C_2\ ...\ C_K$, separated by spaces, $K$ having the meaning from the statement, and $C_1, C_2, ..., C_K$ representing the $K$ localities where the friends live. Each of the next $M$ lines contains three natural numbers $x\ y\ z$, separated by spaces, representing a road that connects the locality $x$ with the locality $y$ and has length $z$.

# Output data
The output file `ubuntzei.out` will contain the natural number $L$ representing the sought minimum length.

# Constraints and clarifications
* $1 \leq N \leq 2\ 000$
* $1 \leq M \leq 10\ 000$
* $0 \leq K \leq \min\\{15, N - 2\\}$
* $2 \leq C_1, C_2, ..., C_K \leq N - 1$
* The route may pass through any locality multiple times.
* The cost of an edge will be between $1$ and $10^5$.
* For the first $20\%$ of tests $K = 0$.
* For the first $50\%$ of tests $K \leq 10$.
* For the first $70\%$ of tests $N \leq 200$.

# Example

`ubuntzei.in`
```
4 5 
1 2
1 2 1
1 3 1
2 3 1
2 4 4
3 4 2
```

`ubuntzei.out`
```
4
```

Explanations
---

There is only one route of minimum length from locality $1$ to locality $4$ which passes through locality $2$, namely: $[1,2,3,4]$. The length $L$ of this route is $4$.
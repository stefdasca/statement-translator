~[fermier.png|align=right|width=30%]

Dorel has acquired a farm with $n$ plantations and a transport vehicle with a capacity $c$ for transporting fertilizers to all the plantations. The fertilizers are stored in a warehouse, in a sufficient quantity for the intended purpose. The plantations and the warehouse are arranged in a circle. There are roads only between plantation $i$ and plantation $i+1$ ($1 \leq i \leq n-1$), as well as between the warehouse and plantation $1$ and the warehouse and plantation $n$, as shown in the figure. A plantation $i$ can be reached from the warehouse by passing through plantations $1, 2, \dots, i-1$ or through plantations $n, n-1, \dots, i+1$, the choice being made based on the shortest route. These distances and the amount of fertilizers required for each plantation are known. At each loading, Dorel takes exactly the amount $c$ from the warehouse.

Dorel wants to organize his work at the farm well and consume as little fuel as possible by **choosing the shortest paths to travel**. The plantations must be supplied **necessarily** in the following order: first plantation $1$, then plantation $2$, plantation $3$, $\dots$, plantation $n$. Moreover, he has decided to load a new amount of fertilizer only after using up the entire previous amount loaded. Thus, the fertilizer transportation to the plantations starts from plantation $1$. After transporting the entire necessary amount for this plantation, he moves on to plantation $2$, and so on in order to $3, 4$ etc., until the last plantation is serviced. If after transporting the fertilizers needed for plantation $i$ there are still fertilizers left in the vehicle, these should be used for other plantations, chosen in the imposed order (starting with plantation $i+1$, then $i+2$ etc.), until the entire transported amount is exhausted. Thus, if from plantation $i$ he has to get to plantation $i+1$, he will choose the shortest path between the direct route from plantation $i$ to $i+1$ and the route passing through plantations $i-1$, $i-2$, $\dots$, $1$, warehouse, $n, n-1, $\dots$, i+1. In the end, the vehicle must return to the warehouse, empty or with the remaining quantity after supplying the fertilizers to plantation $n$.

# Task

Help Dorel calculate the distance traveled to transport fertilizers to all $n$ plantations, according to the requirements.

# Input data

The input file `fermier.in` contains the natural numbers $n$ and $c$ on the first line, separated by a space. The second line contains the natural numbers $d_0, d_1, d_2, \dots, d_{n-1}, d_n$ separated two by two by a space, where $d_0$ is the distance between the first plantation and the warehouse, $d_i$ is the distance between plantation $i$ and plantation $i+1$, and $d_n$ is the distance between plantation $n$ and the warehouse. The third line contains the natural numbers $q_1, q_2, \dots, q_{n-1}, q_n$ separated two by two by a space, where $q_i$ represents the amount of fertilizer needed for plantation $i$.

# Output data

The output file `fermier.out` will contain a natural number on the first line according to the requirements.

# Constraints and clarifications

* $1 \leq n \leq 100$;
* $1 \leq n \leq 2$, for tests worth $20$ points;
* $1 \leq d_i, c, q_i \leq 1 \ 000$;
* $10$ points are awarded by default.

# Example

`fermier.in`
```
3 6
1 10 2 3
13 2 7
```

`fermier.out`
```
22
```

## Explanation

At plantation $1$, an amount equal to $13$ must be transported, the maximum amount that the vehicle can transport being $6$. Plantation $1$ is reached by the shortest direct route from the warehouse. Thus, he will travel first with the amount $6$, return to the warehouse, reload the vehicle, take $6$, return, load and leave only $1$ (that's all that's needed). For this, a distance of $1+1+1+1+1=5$ was traveled. Now, an amount equal to $5$ remains in the vehicle. Now, he must go to plantation $2$ by the shortest route.

On the direct route, the distance is $10$, while on the reverse route passing through the warehouse, the distance is $6$ ($1+3+2$). He will choose the route with a distance of $6$. He leaves $2$ (that's required for plantation $2$), $3$ remain for plantation $3$. From plantation $2$, he reaches plantation $3$ directly at a distance equal to $2$ or inversely, passing through the warehouse at a distance of $14$ ($10+1+3$). He chooses the route with a distance of $2$. He leaves the remaining fertilizers and goes again to the warehouse, reloads, and leaves $4$ at plantation $3$. For this, he travels an additional distance of $3+3$.

At the end, the vehicle must return to the warehouse, so an additional route with a distance of $3$. In total: $5+6+2+6+3=22$
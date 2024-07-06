On the number line, we consider a highway with an unlimited number of lanes. At the point corresponding to kilometer $0$ (the origin of the number line), there is a radar. This radar detects $N$ cars traveling at constant speeds. For each car $i$, the time $t_i$ at which it is detected by the radar, expressed in hours, and its speed $v_i$, expressed in km/h, are known.

# Task

Answer $Q$ queries of the form: given $t$, which is the closest car to the radar at time $t$ among those detected until then (including those detected exactly at time $t$)? If there are multiple cars detected up to time $t$ for which the distance to the radar is minimal, you can display any of them.

# Input Data

The first line contains the numbers $N$ and $Q$, the number of cars, and the number of queries, respectively. The next $N$ lines contain two numbers each, $t_i$ and $v_i$, with the mentioned significance (for any $i = 1 \dots N$). The last line contains $Q$ integers, corresponding to the $Q$ queries (each query reads a number corresponding to $t$ with the mentioned significance).

# Output Data

Print a single line containing $Q$ numbers separated by a space, corresponding to the answers to the queries. For each query $t$, print the index of the closest car to the radar at time $t$ among those detected up to time $t$ (the cars are indexed starting from $1$ in the order they were read). If no car has been detected until time $t$, print $-1$ for that query.

# Constraints and clarifications

* $1 \leq N \leq 100\ 000$
* $1 \leq Q \leq 300\ 000$
* $-1\ 000\ 000\ 000 \leq v_i , t_i \leq 1\ 000\ 000\ 000$, $v_i \neq 0$ for any $i = 1 \dots N$
* $-1\ 000\ 000\ 000 \leq t \leq 1\ 000\ 000\ 000$ for any query
* For tests worth $32$ points, $1 \leq N \leq 1\ 000$ and $1 \leq Q \leq 3\ 000$.

# Example

`stdin`
```
3 3
2 1
4 2
-2 -1
1 3 4
```

`stdout`
```
3 1 2
```

## Explanation

At time $t = 1$, only the third car had already been detected.  
At time $t = 3$, the radar had already detected cars $1$ and $3$. Among them, the closest to the radar at time $t = 3$ is car $1$, located at a distance of $1$.  
At time $t = 4$, the radar had already detected all the cars. Among these, the closest is car $2$, located at a distance of $0$ from the radar.

# Task

Tim Goodman and Detective Pikachu are investigating the source of the mysterious gas $R$ that makes the pokemon in Ryme City go wild. After a long interrogation session with an uncooperative Mr. Mime, they managed to gather some valuable information.

Under Ryme City, there is a network consisting of $N$ control points numbered from $0$ to $N-1$, connected by $N-1$ bidirectional tunnels, so there is a unique path between any two control points $X_i$ and $Y_i$. Mr. Mime took the shortest path and remembers the minimum concentration $Z_i$ of the gas $R$ encountered at the control points on that path.

The last piece of information given by Mr. Mime is that very likely, all but two of the control points have exactly two adjacent tunnels.

To continue the investigation, Tim and Detective Pikachu need to find a possible form of the tunnel network based on the information provided by Mr. Mime.

# Input data

The input file `detective.in` contains on the first line $N$ and $M$, representing the number of control points and the number of pieces of information about the network, respectively. On line $2 + i$  $(0 \leq i \leq M-1)$ we have the triplets $X_i \\ Y_i \\ Z_i$ representing the information provided by Mr. Mime.

# Output data

The output file `detective.out` will contain $N-1$ pairs $(x, y)$, representing two control points connected by a tunnel.

# Constraints and clarifications

* $1 \leq N, M \leq 250\ 000$;
* For tests worth $40$ points, $1 \leq N \leq 1\ 000$, $0 \leq M \leq 2\ 000$;
* For other tests worth $10$ points, $1 \leq N \leq 500$, $0 \leq M \leq 250\ 000$, for any $0 \leq a,b \leq N-1$, there exists a path $i$ taken by Mr. Mime such that $X_i=a$ and $Y_i=b$;

# Example

`detective.in`
```
5 10
3 0 0
3 4 0
3 1 0
3 2 0
0 4 0
0 1 0
0 2 0
4 1 1
4 2 1
1 2 1
```

`detective.out`
```
3 0
0 4
4 1
1 2
```

## Explanation

A possible network of tunnels and control points is represented in the following image:

~[graph4.png]

The following network representation is, however, incorrect because the minimum concentration of gas $R$ observed by Mr. Mime on the path from $4$ to $2$ is $1$, but the network would indicate that this concentration is $2$, $2$ being the minimum of the concentrations on the path ($4$ and $2$).

~[graph5.png]

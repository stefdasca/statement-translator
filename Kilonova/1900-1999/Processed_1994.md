
# Task

In the warehouse of a construction company, there are $N$ stone blocks, either white or black. They are arranged in order $1, 2, \dots , N$ from the entrance into the warehouse to the inside. 

The stone blocks need to be transported to a construction site in the order in which they are stored, and for this, a truck will need to be rented from a transport company. This company owns $Q$ types of trucks. A truck of type $i$ can carry a maximum of $K_i$ stone blocks at a time and for one trip a fee $T_i$ is charged. 

The transport company believes that, in order to keep their clientele, they must impose certain standards, no matter how absurd they may be. Therefore, the condition is that all stone blocks placed in the truck for a trip must be of the same color. Consequently, to transport all the blocks to the site, the construction company will choose a truck of a certain type, and the truck will make one or more trips.

To minimize the total amount paid, the construction company has the option to change the color of any stone block (from white to black or from black to white). For each block $i$ the amount $S_i$ that must be paid to change its color is known.

For each of the $Q$ types of trucks owned by the transport company, determine the minimum amount that the construction company will pay to transport all the $N$ stone blocks to the site.

# Input data

The input file `trans.in` contains on the first line the integer number $N$, representing the number of stone blocks in the warehouse. Each of the following $N$ lines contains information about one stone block. On the $i$-th of these $N$ lines, there are two integers separated by a space: $C_i \\ S_i$, representing the color of the $i$-th block ($C_i$ is $0$ for white and $1$ for black) and the amount to be paid to change its color (if necessary). On the next line contains the natural number $Q$, representing the number of types of trucks owned by the transport company. Each of the following $Q$ lines contains information about one type of truck. On the $i$-th of these $Q$ lines, two natural numbers separated by a space $K_i \\ T_i$ are written, representing the maximum number of blocks that can be carried simultaneously by a truck of type $i$ and the fee to be paid for each trip made.

# Output data

The output file `trans.out` will contain $Q$ lines. On the $i$-th of these lines will be printed the minimum total amount paid by the construction company to transport all $N$ stone blocks, in case they rent a truck of type $i$.

# Constraints and clarifications

* $1 \leq N \leq 16 \ 000$
* $1 \leq S_i \leq 10 \ 000$
* $1 \leq Q \leq 100$
* $1 \leq K_i \leq N$
* $1 \leq T_i \leq 100 \ 000$
* At least $40\\%$ of the tests will have $Q \leq 10$ and $K_i \leq \min(N, 100)$

# Example

`trans.in`
```
4
0 2
1 3
0 10
1 2
3
4 1000
4 1
2 5
```

`trans.out`
```
1005
5
14
```

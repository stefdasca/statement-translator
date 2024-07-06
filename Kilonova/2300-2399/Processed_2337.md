$N$ computers, numbered from $1$ to $N$, are interconnected in a network. Computer $1$ possesses some information that it wants to transmit to all other computers (this type of information transmission is known as broadcast). For this, the program running on computer $1$ must establish an intelligent transmission strategy so that the information reaches all other computers as quickly as possible. Any two computers can communicate with each other, and the transmission duration of information from any computer $i$ to any computer $j$ is known (the transmission duration from $i$ to $j$ can be different from the transmission duration from $j$ to $i$). Once computer $i$ has received the information, it can further transmit it to other computers. At any given moment, a computer can only transmit information to one other computer. Therefore, if computer $i$ wants to transmit information to computers $j$ and $k$, it must first transmit the information to computer $j$, and after it is received (after a duration of time equal to the transmission duration from $i$ to $j$), it can then be transmitted to computer $k$. Obviously, transmissions between two different pairs of computers can be performed in parallel. The time after which the information reaches all computers is the largest moment in time at which a computer receives the information (considering that the transmission process starts at moment $0$).

# Task

Determine the minimum duration (corresponding to an intelligent broadcast strategy) after which the information reaches all computers.

# Input Data

The input file `bcast.in` contains on the first line the natural number $T$, representing the number of test data sets. Next, the descriptions of the $T$ sets follow. The first line of each test set contains the natural number $N$, representing the number of computers. The next $N$ lines each contain $N$ integers, separated by a space. The $j$-th number on the $i$-th of these lines contains the transmission duration of information from computer $i$ to computer $j$. The transmission duration from a computer to itself will always be equal to $0$.

# Output Data

In the output file `bcast.out`, you will print $T$ lines, one for each set of test data. On the $i$-th line will be a natural number $T_{min}$ representing the minimum duration after which the information can reach all computers for the $i$-th test set from the input file.

# Constraints and clarifications

* $1 \leq T \leq 10$;
* $1 \leq N \leq 12$;
* $0 \leq $ Transmission duration of information from a computer $i$ to a computer $j \leq 10\ 000$

# Example

`bcast.in`
```
2
4
0 4 2 1
4 0 16 13
7 8 0 9
10 11 3 0
2
0 0
10 0
```

`bcast.out`
```
5
0
```

## Explanation

In the case of the first test set, at moment $0$, computer $1$ starts transmitting information to computer $4$ (the transmission lasts until moment $1$). At moment $1$, computer $1$ starts transmitting information to computer $2$ (the transmission lasts until moment $5$), and computer $4$ starts transmitting information to computer $3$ (the transmission lasts until moment $4$). The moments in time at which the $4$ computers receive the information are: $0$, $5$, $4$, and $1$. 

In the case of the second test set, at moment $0$ computer $1$ starts transmitting information to computer $2$, and the transmission ends also at moment $0$.
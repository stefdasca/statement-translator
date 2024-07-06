## The Longest Tunnel

The longest tunnel of the Moldova highway has a length of $L$ (expressed in meters) and is one-way. Vehicles traveling through the tunnel move at a constant speed. The tunnel is under constant video surveillance. If incidents are detected, according to emergency protocol, the following events occur:

* Entry into the tunnel is stopped;
* Vehicles inside the tunnel are located by detecting the position $x$ relative to the entrance to the tunnel as well as the speed of movement $v$;
* Overtaking another vehicle is prohibited.

During the protocol period, groups of vehicles (stauband) are formed in the tunnel. The speed of movement of each group of cars is adjusted to the speed of the first car in the group. The reference location (position) of the vehicle that joins a stauband will become the location of the first vehicle in the stauband. It is assumed that both vehicles and formed staubands have point representations.

# Task

1) The number of staubands formed until all vehicles exit the tunnel in the event of protocol activation;
2) The maximum number of vehicles in a group (stauband).

# Input data

The input file `tunel.in` contains on the first line the nonzero natural numbers $N$ and $L$ with meanings as described above. On the next $N$ lines are found $N$ pairs of nonzero natural numbers $x \\ v$, representing the position relative to the tunnel entrance, and the speed of vehicle $i$ ($1 \\leq i \\leq N$).

# Output data

The output file `tunel.out` will contain two natural values, one on each line, representing the number of formed staubands and the maximum number of vehicles in a stauband.

# Constraints and clarifications

* $2 < N \\leq 50 \\ 000$;
* $1 < L \\leq 50 \\ 000$;
* $0 < x < L$, $x$ – natural number;
* $0 < v < 100$, $v$ – natural number;
* A stauband contains at least one vehicle;
* Position (location) is expressed in meters and the speed of movement in meters/second;
* The initial locations of the vehicles in the tunnel are distinct two by two;
* A stauband is considered to have exited the tunnel when its coordinate $x$ is greater than $L$;

# Example 1

`tunel.in`
```
5 13
10 2
8 4
1 3
4 1
2 2
```

`tunel.out`
```
2
3
```

## Explanation

After one second of travel, vehicles $m_1 (x = 1, v = 3)$ and $m_2 (x = 2, v = 2)$ form a stauband that will move at speed $v = 2$, and vehicles $m_4 (x = 8, v = 4)$ and $m_5 (x = 10, v = 2)$ form a stauband that will move at speed $v = 2$. After another second, stauband $m_1$, $m_2$, and $m_3$ is formed and moving at speed $v = 1$.

~[tunel.png]
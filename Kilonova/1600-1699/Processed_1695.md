The robot **Curiosity's** adventure on Mars continues. The robot moves along an Ox coordinate axis. The starting point of the expedition has the coordinate $x = 0$, and the point where the study is completed has the coordinate $X_f$. The robot travels at a constant speed and covers one unit of road in one unit of time.

Researchers have established $N$ zones that make it possible to receive data transmitted by the robot to the satellite. Each zone is defined by a pair $X_i$, $L_i$ ($X_i$ – the starting coordinate of zone $i$, $L_i$ – the length of the zone). The zones do not interfere (do not have common points). The data is transmitted in fixed-size packets, and the transmission duration of a packet is $D$.

During a zone, the robot can transmit one or more data packets. After completing the transmission of a packet, the robot can continue transmitting another packet, if possible (partial packet transmission is not accepted), or it can interrupt the transmission. After interruption, the robot can resume transmission only after consuming at least $T$ units of time.

# Task

Determine the maximum number of data packets that the robot can transmit to the satellite.

# Input data

The file `curiosity2.in` contains on the first line four natural numbers $X_f$, $D$, $T$, $N$ with the meaning given in the statement. The following $N$ lines describe the zones: $X_i$, $L_i$, natural numbers, where $X_i$ represents the starting coordinate of zone $i$, and $L_i$ represents the length of the zone.

# Output data

The file `curiosity2.out` contains on a single line a single natural number representing the maximum number of data packets that the robot can transmit.

# Constraints and clarifications

* $1 \leq N \leq 100\ 000$;
* $1 \leq D \leq 10^6$;
* $1 \leq T \leq 10^9$;
* $0 < L_i, X_f \leq 10^9$;
* $0 \leq X_i \leq X_f$;
* Transmissions can only be carried out in the specified zones;
* The transmission of a packet starts and ends at integer coordinates;
* The robot can start transmitting a packet only if the previous transmission has been completed;
* When it reaches the coordinate $X_f$, the robot must complete the transmissions;
* The zones are given in ascending order of distance from the origin.

# Example

`curiosity2.in`
```
16 2 3 3
2 5
8 4
14 3
```

`curiosity2.out`
```
4
```

## Explanation

~[curiosity2.png]
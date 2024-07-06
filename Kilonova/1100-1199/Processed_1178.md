# Task

On a conveyor belt that performs a back-and-forth movement, there are $n$ initially empty boxes. A fixed device suspended above the belt releases a candy from time to time, placing it in the box that is exactly below it at that moment. The belt moves constantly so that every second, a different box is exactly below the device (the box next to the one that was previously below it). If $n=4$, then initially box number $1$ is below the device, in the next second the belt will have moved so that box $2$ is below the device. In seconds $3$, $4$, $5$, $6$, $7$, $8$, etc., boxes $3$, $4$, $3$, $2$, $1$, $2$, etc. will successively be below the device.

The total length of the belt is $2 \cdot n-1$ times the length of a box so that during the movement, there will always be a box below the device that releases the candies. The figure below shows the first $8$ seconds of operation of the assembly consisting of the conveyor belt with $4$ boxes and device $D$. It is known that in the first second of operation, the device releases a candy into box number $1$.

~[cutii.png|align=right]

# Task

Given the number of boxes $n$, the time duration $t$ between two successive candy releases, and the total number of candies $b$ released by the device, determine the number of boxes that remain empty and the maximum number of candies in a single box at the end of the process.

For example, if $n=6$, $t=4$, and $b=10$, then since in seconds $1$, $5$, $9$, $13$, $17$, $21$, $25$, $29$, $33$, $37$ the device releases a candy into boxes $1$, $5$, $3$, $3$, $5$, $1$, $5$, $3$, $3$, and respectively $5$, it means that $3$ boxes remain empty (boxes $2$, $4$, and $6$) and the maximum number of candies in a box is $4$.

# Input data

The file `cutii.in` contains on one line, separated by a space between them, the numbers $n$, $t$, $b$, representing the total number of boxes, the number of seconds after which the device releases another candy, and the total number of candies released.

# Output data

The file `cutii.out` contains on one line, with a space between them, the numbers $c$ and $m$, representing the number of boxes that remain empty at the end of the process, and the maximum number of candies in a box at the end of the process.

# Constraints and clarifications

* $1 < n < 1\ 000$;
* $0 < t < 10^6$;
* $0 < b < 10^9$;

# Example 1

`cutii.in`
```
4 17 5
```

`cutii.out`
```
0 2
```


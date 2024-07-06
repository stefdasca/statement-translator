# Task

Determine the maximum sum of data values transmitted by a subset of the $N$ sensors, such that the data transmission of these sensors respects all the specified constraints.

# Input data

The input file `senzori.in` contains on the first line the natural number $N$, representing the number of sensors. Each of the following $N$ lines contains 4 integers separated by space: $T_{1,i} \\ T_{2,i} \\ d_i \\ v_i$; the $i$-th of these lines corresponds to the sensor with number $i$.

# Output data

In the output file `senzori.out`, you will print the maximum sum of the data values transmitted by a subset of sensors that can send their data to the central station while respecting all the specified constraints in the statement.

# Constraints and clarifications

* $1 \\leq N \\leq 2 \ 000$
* $0 \\leq T_{1,i} < T_{2,i} \\leq 2 \ 000$
* $1 \\leq d_i \\leq T_{2,i} - T_{1,i}$
* $1 \\leq v_i \\leq 10 \ 000$

# Example

Input file `senzori.in`
```
4
0 5 3 6
1 4 3 7
2 8 3 5
6 8 2 5
```

Output file `senzori.out`
```
16
```

## Explanation

The sensors that will send data to the central station are: $1$, $3$, and $4$. Sensor $1$ will send data in the interval $[0,3)$, sensor $3$ will send data in the interval $[3,6)$, and sensor $4$ in the interval $[6,8)$. The total value of data sent is $6+5+5=16$.
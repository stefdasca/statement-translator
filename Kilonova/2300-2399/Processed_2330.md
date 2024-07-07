Your country is at war, and you are the head of the country's defense council. You recently received a worrying message: $N$ enemy ships have invaded the country's marine space. Each of the $N$ ships is moving in a straight line (more precisely along the Ox axis) at a constant speed. 
A satellite has provided you with a map that marks the positions of the ships at time $0$ (distance from the origin expressed in meters). You have observed that at time $0$, all the ships are at integer coordinate points.
You have the option to bombard the enemy ships using a special system. The system allows the detonation of bombs, but it is only possible to detonate all bombs at exactly the same time. When a bomb is detonated, it will destroy all ships located at a distance $\leq R$ meters (the bomb's range).

# Task

Your mission is to detonate a minimum number of bombs so that all ships are destroyed. Additionally, you want to detonate that minimum number of bombs in the shortest possible time.

# Input data

The input file `bombe.in` contains the first line which contains a natural number $N$, representing the number of ships, followed by a real number $R$, representing the range of the bombs. The next $N$ lines describe the $N$ ships, one ship per line. Each line that describes a ship will contain two numbers separated by a space $x \\ v$, where $x$ represents a natural number indicating the position of the ship at time $0$, and $v$ is a real number indicating the speed (in $\\frac{m}{s}$) at which the ship is moving. If the speed is positive, the ship moves along the Ox axis, and if the speed is negative, the ship moves in the opposite direction of the Ox axis.

# Output data

The output file `bombe.out` will contain a single line with two numbers separated by a space $nr_{min} \\ t_{min}$, where $nr_{min}$ represents the minimum number of bombs needed to destroy all the ships, and $t_{min}$ is the minimum time (expressed in seconds) at which the $nr_{min}$ bombs can be detonated to destroy all the ships. The time will be displayed with $3$ decimal places.

# Constraints and clarifications

* $1 \\leq N \\leq 300$
* $0 < R \\leq 5$
* $x \\leq 1 \\ 000 \\ 000$, for any $1 \\leq i \\leq N$
* $|v| \\leq 100$, for any $1 \\leq i \\leq N$
* It is possible that at some point two ships may be in the same position, but there will never be $3$ ships in the same position.
* The minimum displayed time is considered correct if it differs by at most $0.01$ from the correct minimum time.

# Example

`bombe.in`
```
6 0.25
2 0.5
3 -1
5 -1
5 0.333
8 0.5
10 -0.2
```

`bombe.out`
```
4 0.333

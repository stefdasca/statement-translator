# The Curiosity Robot’s Mission

The **Curiosity** robot's mission is to send images and information to the satellite placed in Mars' orbit. The robot’s exploration area is along the Ox coordinate axis. The robot is equipped with a solar battery with a maximum energy capacity $C$ and consumes one energy unit for each unit of distance traveled. The starting point of the robot's journey (with respect to the origin $x$ = $0$) is $X_s$, and the endpoint where the study is completed has the coordinate $X_f$.

Additionally, researchers have identified $N$ points that allow the robot to recharge its batteries, numbered from $1$ to $N$. Depending on the intensity of the received sunlight, reflected in the battery charging duration, the recharging points are of three types: type $1$ – minimum intensity/long charging time, type $2$ – medium intensity/medium charging time, type $3$ – maximum intensity/short charging time. Each recharging point $i$ is described by the pair $t_i$, $x_i$, meaning the type of recharging, and its position on the axis respectively. At any recharging point, the robot can decide whether to recharge the battery with energy units, not exceeding the maximum capacity. The robot can move both left and right on the axis.

To shorten the distance to the endpoint, it is desired to determine an optimal strategy for recharging stops so that the total amount of energy recharged at type $1$ points is minimized. If there are multiple stopping strategies for which the total amount of energy recharged at type $1$ points is minimal, then the strategy for which the total amount of energy recharged at type $2$ points is minimal will be chosen.

# Task

Given $X_s$, $X_f$, $C$, as well as the description of the $N$ recharging points, determine a movement strategy between coordinates $X_s$ and $X_f$, optimal in terms of the time necessary for recharging the batteries.

# Input data

The file `curiosity.in` contains on the first line four natural numbers $X_s$, $X_f$, $C$, $N$ with the significance from the statement. The next $N$ lines describe the recharging points: $t_i$, $x_i$, where $t_i$ represents the type of recharging of point $i$, and $x_i$ is its position on the axis.

# Output data

The file `curiosity.out` contains on a single line two natural numbers separated by a space, representing the total minimum amount of energy recharged at type $1$ points, and respectively the total minimum amount of energy recharged at type $2$ points. If there is no solution, the value $-1$ will be printed.

# Constraints and clarifications

* $1 \leq N \leq 100 \ 000$
* $1 \leq C \leq 1 \ 000$
* $1 \leq t_i \leq 3$
* $-10^6 \leq x_i \leq 10^6$
* $-10^6 \leq X_s < X_f \leq 10^6$. These may coincide with the coordinates of the recharging points;
* The recharging points are distinct. The coordinates of the points are integer type;
* The recharging points are given in increasing order
* Note, when leaving point Xs the robot is fully charged to the maximum capacity $C$.

# Example

`curiosity.in`
```
1 11 5 4
3 -1
1 3
2 7
3 10
```

`curiosity.out`
```
1 3
```

## Explanation

~[curiosity.png]

On the axis, there are $n = 4$ recharging points. The robot starts from point $x_s$ = $1$ and needs to reach point $x_f$ = $11$. Initially, the robot's battery is fully charged to the maximum capacity $C = 5$ units. The robot stops at point $x$ = $3$. For the journey from $x$ = $1$ to $x$ = $3$, it consumed $2$ units of energy. It recharges the battery with $1$ unit (type $1$). The battery now has a capacity of $4$ units, enough to reach point $x$ = $7$ where it recharges the battery with $3$ units (type $2$). At point $x$ = $10$, it recharges the battery with $1$ unit (type $3$).
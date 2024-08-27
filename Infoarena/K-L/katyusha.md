## Task

" Katyusha rocket launchers are a type of reactive artillery initially built and used by the Soviet Union starting from World War II. Compared to other artillery pieces, these multiple rocket launchers can quickly saturate a target with a large amount of explosives, but have reduced accuracy and require a longer reload time. " You have before you a battlefield, represented by the Cartesian plane. There are $N$ enemy vehicles, represented by points, which move in a straight line and at a constant speed. For each vehicle, the following are known: the position at the initial moment $(T=0)$, the position after one unit of time, and its cost. You have at your disposal a Katyusha battery and $M$ firing options represented by circles on the Cartesian plane, which we will simply call targets. For a firing option, the time can be chosen (greater or equal to $0$, not necessarily an integer) at which it will be executed, and all vehicles at that moment inside the target will be destroyed, causing damage to the enemy equal to the sum of the costs of the destroyed vehicles. For each firing option, calculate, if it were chosen, the maximum possible sum of the costs of the destroyed vehicles.

## Input data

The first line of the file `katyusha.in` will contain two natural numbers $N$ and $M$, as mentioned in the statement. Each of the next $N$ lines will contain, in order, the following: two real numbers $x_0$, $y_0$ (initial position of a vehicle), two real numbers $x_1$, $y_1$ (the position after one unit of time of the vehicle), an integer $v$ (cost of the vehicle). Each of the next $M$ lines will contain three real numbers: $x$, $y$, $r$, representing a target (center $(x, y)$ and radius $r$).

## Output data

On each of the first $M$ lines of the file `katyusha.out`, print the maximum possible sum of the costs of the destroyed vehicles for each firing option, respectively.

## Constraints and clarifications

$1 \leq N * M \leq 300000$

$-10^9 \leq x_0, y_0, x_1, y_1, x, y, r \leq 10^9$

$1 \leq v \leq 3000$

For 45% of tests

$1 \leq N, M \leq 200$

## Example

`katyusha.in`  
```
3 2
0.0 0.0 3.0 3.0 7
3.0 1.5 3.0 1.5 2
0.0 5.0 1.0 5.0 10
2.0 2.0 2.0
3.0 1.0 1.4143
```

`katyusha.out`  
```
9
9
```

## Explanation

The first shot can be executed at moment $0.5$. The second shot can be executed at moment $0.662981$. In both cases, vehicles 1 and 2 are destroyed, leading to a total damage value of $9$.
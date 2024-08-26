Ben

At a gas station, $N$ cars arrive in one day to refuel. For each car, the arrival time and departure time from the gas station are known, with the time interval between arrival and departure being exclusively used for refueling. A gas pump can be used to refuel only one car at a time (it can refuel multiple cars but not simultaneously). Refueling a car starts exactly at the moment it arrives at the gas station and ends exactly at the moment it departs, using the same pump for the entire duration of its stay at the gas station.

## Task

Knowing the arrival and departure information of the $N$ clients, find $K$, representing the minimum number of gas pumps needed to serve all clients. Also, determine the number of distinct ways to serve the clients using exactly $K$ gas pumps.

## Input data

In the file `ben.in` the first line contains a number $N$ representing the number of clients. The following $N$ lines each contain two numbers, $A$ and $B$ ($A < B$), separated by a space representing the arrival time and departure time of a client, respectively.

## Output data

The output file `ben.out` will contain a single line with two integers $K$ and $S$, representing the minimum number of gas pumps and the number of ways to serve the clients using exactly $K$ gas pumps. The number $S$ will be displayed modulo $32173$.

## Constraints and clarifications

$0 \leq N \leq 30000$, 
but for $70 \%$ of the tests $N \leq 300$.

Arrival and departure times will be integers in the range $[1, 30000]$.

There will be no car that arrives at the departure time of another car.

If the first number in the output file is correct, you will receive $6$ points for that test, and if both numbers are correct, you will receive $10$ points.

No points will be awarded if only the second number is correct.

Two ways of serving the clients are considered different if there is at least one client who was not served at the same pump in the two ways.

Clients do not like to wait, so you must ensure that there is at least one free pump at the arrival of each client at the gas station.

Attention! The number will be displayed modulo $32173$.

## Examples

`ben.in`
```
4
1 4
5 7
8 10
2 7
```

`ben.out`
```
2 4
```

## Explanation

The minimum number of gas pumps is $2$. The $4$ ways of serving the clients are: $1, 1, 1, 2$ (first way) $1, 1, 2, 2$ (second way) $2, 2, 1, 1$ (third) $2, 2, 2, 1$ (fourth)

Each number represents the index of the pump where each client was refueled, maintaining their order from the input file.
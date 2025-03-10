
# Task

Andrei has just acquired his new blue electric car and now wants to enjoy a ride. He has planned a very long route but realized that he might not be able to complete it entirely because the charging stations might not be frequent enough. The chosen route is linear, without self-intersections.

For each station, the distance from the starting point is known.

It is also known that Andrei starts with the battery fully charged, and at any station, he can charge as much as needed (obviously, without exceeding the battery capacity). For simplicity, we will consider the battery capacity expressed in the number of distance units that can be traveled. If the battery runs out before reaching a station, the car will not be able to reach the station, but if it runs out exactly upon reaching a station, it can be charged there.

Determine the maximum distance that Andrei can travel. Also, we need to determine the minimum number of stops to achieve this maximum distance.

# Input data

The file `electric.in` contains on the first line a natural number $C$ representing the battery capacity. On the second line is a value $n$ representing the number of charging stations along Andrei's route. On the third line are $n$ natural numbers, separated by spaces, representing the distance of each station from Andrei's starting location.

# Output data

The file `electric.out` contains two values, separated by space, representing respectively the maximum distance traveled by Andrei and the minimum number of stops to travel that maximum distance.

# Constraints and clarifications

* $1 \leq C \leq 1 \ 000 \ 000 \ 000$;
* $1 \leq n \leq 100 \ 000$;
* The distances to the stations are nonzero natural numbers, at most equal to $1 \ 000 \ 000 \ 000$.

# Example

`electric.in`
```
3
4
4 2 7 11
```

`electric.out`
```
10 3
```

## Explanation

Andrei has a battery with a capacity of $3$. He can reach the station located at distance $2$ with capacity $1$ remaining in the battery; there, he can charge the battery and consume another $2$ to reach the station at distance $4$, arriving with $1$ in the battery. There he recharges and reaches the station at a distance of $7$ with the battery at $0$. From there, he can travel $3$ more units but will not reach the station at distance $11$ to be able to charge again.

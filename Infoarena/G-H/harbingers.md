# Harbingers

A long time ago, on the territory of Moldova, there were $N$ medieval cities, uniquely numbered with integers between $1$ and $N$. The city numbered $1$ was the Citadel and was considered the capital of the land. Between these cities, there existed $N-1$ bidirectional paths, each path having a known length, expressed in kilometers. The paths were constructed such that there is a unique road between any two cities, without passing through the same city twice (the graph of paths was a tree). When a city was attacked, the urgent message had to be sent as quickly as possible to the capital. The message was carried by messengers, with one messenger in each city. Each messenger was characterized by the time required to start the journey and his constant speed after departure. The message from a city was always transported on the shortest route to the capital. Initially, the messenger from the attacked city would take the message. In each city he traversed, a messenger had $2$ options: either continue to the next city on the way to the capital or leave the message to the messenger in the city. The messenger who received the message would apply the same procedure as above. Along the way, a message could be carried by any number of messengers before reaching the capital. Determine the minimum time needed to send a message to the capital from each city.

## Input data

The input file `harbingers.in` contains a natural number $N$, the number of cities in the land of Moldova. Each of the next $N-1$ lines contains $3$ integers $u$ $v$ $d$, separated by a space, describing a path of length $d$ between the cities numbered with $u$ and $v$. Then follows another $N-1$ pairs of integers, one pair per line. The $a_i$-th pair, $S_i$ $V_i$, describes the characteristics of the messenger from the city $(i+1)$: $S_i$ is the number of minutes required by the messenger to prepare for the journey, and $V_i$ is the number of minutes required by the messenger to travel one kilometer. There is no messenger in the capital.

## Output data

The output file `harbingers.out` must contain exactly $N-1$ integers. The $i$-th number represents the minimum time, in minutes, required to send a message from city $(i+1)$ to the capital.

## Constraints and clarifications

$$1 \leq N \leq 100\ 000$$
$$0 \leq S_i \leq 10^9$$
$$1 \leq V_i \leq 10^9$$
The length of any path will not exceed $10\ 000$
For $20\%$ of the tests, $$N \leq 2\ 500$$
For $50\%$ of the tests, each city will neighbor at most $2$ other cities (the graph of paths will be a line graph)

## Example

`harbingers.in`
```
5
1 2 20
2 3 12
2 4 1
4 5 3
26 9
1 10
500 2
2 30
```

`harbingers.out`
```
206
321
542
328
```

## Explanation

The paths and their lengths are presented in the image on the left. The time required for preparing the journey and the speed of the messengers are written in brackets. The minimum time to send a message from city $5$ to the capital is obtained as follows. The messenger from city $5$ takes the message and leaves the city after $2$ minutes. He travels a distance of $4$ kilometers in $120$ minutes before reaching city $2$. There he leaves the message to the city's messenger. This one needs $26$ minutes to prepare for the journey and will travel for $180$ minutes before reaching the capital. The total time is therefore $2 + 120 + 26 + 180 = 328$.
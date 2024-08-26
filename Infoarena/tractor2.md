## Task

In the city of Târgu Mureș, there is a lesser-known amusement park. The main attraction is the XTreme Tractor - a high-speed tractor, the only one remaining from its series of high-speed tractors. The park staff desires to manage the visitors who board it as efficiently as possible. Before boarding, people line up at one of the two queues at the entrance: the first queue is intended only for individuals, while the second queue is intended only for groups of $2$, $3$, or $4$. Individuals in a group cannot separate and will ride the tractor together. People in the first queue and groups in the second queue line up at various times, but within the same queue, there will be only distinct entry times. Throughout the day, $N$ people will enter the first queue, and $M$ groups will enter the second queue. Additionally, besides the entry time in the corresponding queue, the boarding duration is known for each person and each group. For economic reasons, the park management wants exactly $4$ visitors to ride the tractor at each trip. A person or a group from a queue can board the tractor only if all people or groups in front of them from that queue have boarded. Visitors from the same queue or different queues can be coupled to ride together. After selecting the $4$ visitors for the current trip, the boarding duration for the current trip will be the maximum of the boarding durations for the chosen visitors (i.e., individuals and groups). Also, the duration of a tractor ride is $P$ seconds. Because there is only one tractor, the next $4$ visitors who want to board must wait for the current trip to finish. For example, consider the current trip with: a person arriving at time $15$ with a boarding duration of $6$, a person arriving at time $18$ with a boarding duration of $4$, and a group of $2$ people arriving at time $20$ with a boarding duration of $5$. The trip duration is $10$. If the tractor is free at time $20$, the $4$ people will board with duration $max(6, 4, 5) = 6$, meaning at time $26$, and the trip will last $10$, meaning it will end at time $36$. Help the management find the minimum time in which all individual persons and groups from both queues can ride the tractor.

## Input data

The input file `tractor2.in` contains on the first line the integers $N$, $M$, and $P$, with the meanings: $N$ - the number of individuals entering the first queue; $M$ - the number of groups entering the second queue; $P$ - the duration of a tractor ride. On the next $N+M$ lines, there are three integers $t$ $d$ $c$. If $d$ is $1$, then it is a person who at time $t$ is placed in the first queue and has a boarding duration $c$. If $d$ is $2$, $3$, or $4$, then it is a group of $d$ people who at time $t$ are placed in the second queue and have a boarding duration $c$. The times given in the input file are in ascending order.

## Output data

The output file `tractor2.out` must contain a single integer $T$ representing the minimum time in which all the individuals from the first queue and groups from the second queue can ride the tractor.

## Restrictions and clarifications

$0 \leq N \leq 3\ 000$

$0 \leq M \leq 1\ 000$

$1 \leq P \leq 1\ 000\ 000\ 000$

$1 \leq t, c \leq 1\ 000\ 000\ 000$

$1 \leq d \leq 4$

The result can be represented in a 64-bit signed integer.

Moving in the queue and disembarking from the tractor happen instantaneously.

It is guaranteed that there is always a valid way for all individuals and groups from both queues to board the tractor.

Each person or group can ride the tractor only once.

For some test cases worth 10 points, $N+M \leq 18$.

For other test cases worth 10 points, $N = 0$ or $M = 0$.

The problem will be evaluated on test cases worth $90$ points.

## The examples will represent test cases worth $10$ "by default".

## Example

`tractor2.in`
```
3 3 2
1 1 1
2 2 1
3 4 1
4 3 2
10 1 1
11 1 1
20 4 4
30 13
2 2 13
1 3 16
2 4 18
2 7 22
1 3 24
1 4 29
2 5 31
1 1 121
```

`tractor2.out`
```
20
```

## Explanation

The following table explains the optimal boarding manner for the first example:
```
time                   event
1                      In the first queue, a person enters with a boarding duration of 1
2                      In the second queue, a group of 2 visitors enters with a boarding duration of 1
3                      In the second queue, a group of 4 visitors enters with a boarding duration of 1
4                      In the second queue, a group of 3 visitors enters with a boarding duration of 2
10                     In the first queue, a person enters with a boarding duration of 1
```

For the first trip, the selected people are those who arrived at times $1$ and $10$ and the group that arrived at time $2$. The boarding duration is $max(1,1,1) = 1$.

```
11                     In the first queue, a person enters with a boarding duration of 1
```

Boarding is finished, and the first tractor trip begins.

```
13                     The first tractor trip ends.
```

For the second trip, the selected group is the one that arrived at time $3$. The boarding duration is $max(1) = 1$.

```
14                     Boarding is finished, and the second tractor trip begins.
16                     The second tractor trip ends.
```

For the third trip, the selected person is the one who arrived at time $11$ and the group that arrived at time $4$. The boarding duration is $max(1,2) = 2$.

```
18                     Boarding is finished, and the third tractor trip begins.
20                     The third tractor trip ends.
```

All individuals and groups have ridden the tractor, so the answer is $20$.
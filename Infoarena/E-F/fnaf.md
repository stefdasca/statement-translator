## Task

Georgel is playing Five Nights at Freddy’s, a game where you control two doors. When a monster approaches the left door or the right door, you need to close the respective door to stop it. However, resources are limited, and you can't keep the doors closed all the time. You are given $N$ events in the form $(t, door)$, which means that at time $t$ the respective door needs to be closed (e.g., $(7, \text{LEFT})$). We can assume that the game begins at time $-\infty$. The doors are old, so after a door has been closed, it will remain closed for at least $d$ seconds. Also, only one door can be closed at a time, except when switching doors (clarifications in the ## example). If you close a door at time $t$, you need to keep it closed until time $t + d$. You can open it at time $t + d$ and close the other door at the same time $t + d$. Find the total minimum time the doors will stay closed if Georgel plays optimally, or specify if it is impossible to meet all the events.

## Input data

The input file `fnaf.in` will contain on the first line an integer $T$ representing the number of tests. Each test has the following format: the first line will contain two integers $N$ and $d$, representing the number of events and the minimum duration for which a door must stay closed; each of the following $N$ lines will contain the description of an event $(t, door)$, the integer $t$ being the time at which the event occurs and the character door representing the side from which the monster comes: $L$ for left, $R$ for right.

## Output data

The output file `fnaf.out` will contain the answers for the $T$ tests. The answer for a test consists of a single line containing the total minimum time the doors will stay closed if Georgel plays optimally, or $-1$ if it is impossible to meet all the events.

## Constraints and clarifications

$$
1 \leq T \leq 30 
$$
$$
1 \leq N \leq 2 \ast 10^5 
$$
$$
1 \leq t, d \leq 10^9 
$$

Events will be given in chronological order. At a given time moment, only one door can be attacked (two events do not happen simultaneously). There will be at most $10^6$ events in the input file.

## Example

`fnaf.in`
```
3
3 3
1 R
2 L
4 R
3 4
6 L
8 R
9 L
2 10
10 L
25 L
```

`fnaf.out`
```
9
-1
15
```

## Explanation

Test 1

Close the right door at time $1$ until $4$, then close the left door from time $4$ to $7$, and then the right door from time $7$ to $10$. 

Test 2

It's impossible because between the first and the last event there are $3$ seconds and the door needs to stay closed for at least $4$ seconds, so we can't satisfy the second event without missing either the first or the last event.

Test 3

Close the door at time $10$ and keep it closed until $25$.
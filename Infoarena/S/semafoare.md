# Traffic Lights

Laura lives in the city of Simplu. The map of the city Simplu has the form of a grid with dimensions $N$ and $M$, where the streets are represented by the lines of the grid. Thus, the city has $(N+1)*(M+1)$ intersections, and we will denote the intersection of the $i$-th horizontal street with the $j$-th vertical street by $(i, j)$. Laura knows that at every intersection there is a traffic light, which operates as follows: at any given minute $t$, cars entering the intersection can only come from either the north, east, south, or west. If at minute $t$, cars from the north enter the intersection, then at minute $t+1$ cars from the east can enter, at $t+2$ cars from the south, at $t+3$ cars from the west, and at $t+4$ cars from the north again, and so on. Once in the intersection, a car can continue straight or turn left or right. Laura also knows that it takes 1 minute to drive from a street between two consecutive intersections. You will receive a matrix $A$ with $N+1$ rows and $M+1$ columns, each element being a character from the set {'N', 'E', 'S', 'V'}. Each element of matrix $A$ encodes the direction from which cars enter the corresponding intersection at minute 0 ('N' for north, 'E' for east, 'S' for south, 'V' for west). Knowing that at time 0, Laura enters the intersection $(x1, y1)$ from direction $d$, determine the minimum time needed for the girl to reach the traffic light at intersection $(x2, y2)$ (without leaving the city).

## Task

## Input data

The first line of the input file `semafoare.in` contains two natural numbers, $N$ and $M$. The second line contains two integers and a character from the set {'N', 'E', 'S', 'V'}, separated by a single space, representing $x1$ $y1$ $d$. The third line contains two integers separated by a space, $x2$ $y2$. On the next $N+1$ lines, there is a string of $M+1$ characters from the set {'N', 'E', 'S', 'V'}, representing matrix $A$.

## Output data

The output file `semafoare.out` contains a single integer representing the required minimum time.

## Constraints and clarifications

$1 \leq N, M \leq 1\ 000$

The rows of the matrix are considered numbered from 0 to $N$, and the columns from 0 to $M$.

The problem tests are grouped in pairs.
For each group, one of the tests is available for partial evaluation.
(50% of the tests are available for partial evaluation.)

The required time does not include the time Laura spends waiting at the destination intersection's traffic light.

## Examples

`semafoare.in`
```
3 4
1 1 N
3 4
NSEV
VESN
SSNS
VVNS
```
`semafoare.out`
```
7
```

`semafoare.in`
```
5 5
0 5 S
3 1
ENSVVN
VNENVN
NEESEE
ENSSNE
SVVVNS
NESSNS
```
`semafoare.out`
```
19
```

## Explanation

For the first example, Laura will take the following route to reach the destination in minimum time. At minute 0, Laura is at the traffic light at intersection (1, 1) coming from the north. She waits 2 minutes to enter the intersection and spends 1 minute to reach intersection (1, 2). She enters intersection (1, 2) at minute 3 (since she is now coming from the east) and spends another 1 minute to reach intersection (2, 2). She does not wait at this traffic light and enters the intersection at minute 4, then heads towards intersection (2, 3). She does not wait at intersection (2, 3) (since she is coming from the west) and heads towards intersection (3, 3). She arrives at intersection (3, 3) at minute 6 and departs to (3, 4) in the same minute. Laura reaches the destination's traffic light at minute 7.
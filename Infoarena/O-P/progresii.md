## Task

At a sport-math competition aptly called "Progressions for All," $N$ contestants are participating. The track they run on is straight and has a length of $L$ meters. For each contestant $i$, the starting position $P_i$ from the start of the track is known. Each runner can run at a constant speed between $1$ meter/second and $M$ meters/second. Thus, if runner $i$ runs at $v_i$ meters/second, at second $j$, they will be at position $P_i + v_i * j$. Because the heat on the day of the competition is stifling, each participant drinks one deciliter of energy drink for every second they run on the track. As it is a charity event, the organizers wish to raise as much profit as possible. Therefore, they want to determine the speed at which each runner should run so that the total amount of energy drink consumed by the $N$ runners does not exceed $K$ deciliters. If there are multiple solutions, the lexicographically smallest one will be displayed.

## Input data

The input file `progresii.in` contains on the first line, separated by space, the natural numbers $N$, $M$, $K$, and $L$, as described in the statement. Each of the next $N$ lines contains a natural number. Thus, on line $i + 1$ will be $P_i$, the starting position of the runner with number $i$.

## Output data

The output file `progresii.out` will contain $N$ lines. On $a_i$ of these lines, the natural number $v_i$ will be written, the speed at which runner with number $i$ from the input file runs. If there is no solution, the output file will contain a single line with the number $-1$. If there are multiple solutions, the lexicographically smallest one will be displayed.

## Constraints and clarifications

$1 \leq N \leq 100000$

$1 \leq M \leq 2000000000$

$1 \leq P_i \leq 2000000000$

$1 \leq K \leq 260$

$1 \leq L \leq 260$

There may be two runners with the same starting position

The starting positions and speeds at which participants run the competition are natural numbers

A sequence of speeds $(X_1, X_2 \dots X_N)$ is lexicographically smaller than another sequence $(Y_1, Y_2 \dots Y_N)$ if there exists a position $p$ such that $X_p < Y_p$ and $X_1 = Y_1$, $X_2 = Y_2$ $\dots$ $X_{p-1} = Y_{p-1}$

## Example

`progresii.in`
```
3 3 8 4
1
2
3
```

`progresii.out`
```
1
1
2
```

## Explanation

There are 3 runners who can drink at most 8 deciliters of energy drink. A runner's speed can be at most 3 meters/second, and the track is 4 meters long. The first two contestants will run at 1 meter per second, while the last one will run at 2 meters per second. The first runner will drink one deciliter of energy drink at positions 1, 2, 3, and 4, after which their race ends. The second runner will drink a deciliter at positions 2, 3, and 4. The last runner will drink one deciliter of energy drink at position 3 at time 0, because the next second they will finish the race (they will be at a distance of 5 from the left end of the track, which has a length of 4). In total, 8 deciliters of energy drink were consumed. Another solution would have been (1, 1, 3), but this is lexicographically larger.
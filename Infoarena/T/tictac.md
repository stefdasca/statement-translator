## Task

Time is ticking... Tic Tac, Tic Tac. Penalties are increasing... Tic Tac, Tic Tac. Before the second round of ONIS, contestants thought about sabotaging the committee. They found the $N$ analog clocks of the committee and broke each one of them, adjusting the position of the hands. Knowing that the committee's analog clocks have two hands (for hours and minutes), and their movements are continuous, determine if each of the $N$ clocks indicates a valid time or not. The hand of a clock is given as the angle it forms with the hand showing the time 00:00.

## Input Data

The input file `tictac.in` contains on the first line the natural number $N$, and on each of the following $N$ lines two real numbers $H$ and $M$, representing the angle measure formed by the hour hand and the angular measure formed by the minute hand, respectively.

## Output Data

The output file `tictac.out` will contain $N$ lines, each line containing a number. The $i$-th number will have the value $1$ if the $i$-th clock indicates a valid time, $0$ otherwise.

## Constraints and clarifications

$1 \leq N \leq 10^5$

$0 \leq H, M < 360$

The numbers in the input file are given with $6$ exact decimal places.

The clocks do not have perfect accuracy, Tic Tac, Tic Tac, so you can consider correct a pair of angles with a maximum difference of $0.001$ degrees.

## Example

`tictac.in`:
```
6
0.000000 0.000000
0.000000 180.000000
15.000000 180.000000
50.000000 240.000000
270.000000 90.000000
29.916666 359.000000
```

`tictac.out`:
```
1
0
1
1
0
1
```

## Explanation

For the first test, the time described by the clock is 00:00 because both the hour hand and the minute hand are above "12".

For the second test, the time is not correct because the hour hand is above "12", which would mean it is an exact hour. However, the minute hand is halfway around the clock, above 6 o'clock, indicating that 30 minutes have passed from the current hour.
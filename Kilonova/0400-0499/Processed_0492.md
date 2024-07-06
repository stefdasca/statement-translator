In the time of the dragons, the temperature never dropped below $0^{\circ}$C, but after they left for other worlds, winters appeared.

We say that a day is a winter day if the temperature is negative $(<0)$, and $T$ consecutive winter days form a winter period of length $T$.

The elders of the village, tired of being cold, annoy the others by always saying that winter is coming. For this reason, a law had to be created that only allows you to suggest to your fellow citizens that winter is coming on certain days.

Thus, you can say that winter is coming at most $ 2*T $ days before a winter period of length $T$ OR, for the longest winter period of the season, it is allowed to say that winter is coming at most $3*T$ days before.
If you are in a winter period, you can no longer notify others about the period you are in (they also know it's winter), but you can notify them about the next period that is about to come (respecting the law, of course), and if there are several winter periods of maximum length, a single period for which the $3*T$ rule applies will be chosen.

Knowing the temperatures of $N$ consecutive days, find out the maximum number of days in which it is allowed to announce winter periods. Thus, you help those who are annoyed by the elders to know how many days they have to put up with them.

**Note: The input data is read from the keyboard, and the output data is displayed in the console.**

# Task
1. Knowing the temperatures of $N$ consecutive days, find the number of winter periods.
2. Knowing the temperatures of $N$ consecutive days, find the maximum number of days in which it is allowed to announce winter periods.

# Input data
The first input line will contain a number $t$ equal to $1$ or $2$.
The second input line contains the natural number $N$, the duration of the season we consider.
The next input line contains $N$ integers, the temperatures of the consecutive days of the season. The absolute values of these integers will not exceed $100$.

# Output data
1. If $t = 1$, print on the first line a single number, the number of winter periods.
2. If $t = 2$, print on the first line a single number, the maximum number of days in which it is possible to announce that winter is coming.

# Constraints and clarifications
- $ 1 \le N \le 100\ 000 $
- $ 0 \le |j| \le 100 $, where $j$ is the temperature of a day.
- For tests worth 20 points, $t = 1$.
- For other tests worth 30 points, there will be a single winter period of maximum length.
- For the remaining 50 points, there are no other constraints.

# Example 1
`stdin`
```
1
8
1 -1 4 3 8 -2 3 -3
```

`stdout`
```
3
```

# Example 2
`stdin`
```
1
15
1 2 -1 2 3 4 5 6 1 4 8 3 -1 -2 1
```
`stdout`
```
2
```

# Example 3
`stdin`
```
2
8
1 -1 4 3 8 -2 3 -3
```

`stdout`
```
6
```

# Example 4
`stdin`
```
2
15
1 2 -1 2 3 4 5 6 1 4 8 3 -1 -2 1
```
`stdout`
```
8
```

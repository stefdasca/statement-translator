## Task

Mountain enthusiasts, Mars and Stefan, decide to go on a trip to a mountain range consisting of $N$ mountains. These mountains are located one after another and are arranged circularly (the $i$-th mountain has as neighbors the mountains $i-1$ and $i+1$, and the $N$-th mountain is adjacent to the first and the $(N-1)$-th mountain). The direction of travel is from mountain $1$ to mountain $2$. Having great experience in the field, they can very accurately estimate the time required (expressed in hours) to climb each mountain. However, with each climbed mountain, they get tired and the initially estimated climbing time will increase. Thus, after climbing the starting mountain, the climbing time for the next mountain will increase by an hour. After climbing the starting mountain and the next one, the climbing time for the third mountain will increase by two hours. Thus, after climbing $i$ mountains, the time required for climbing the next mountain will be $i$ hours more than the initially estimated time. The trip can start from the base of any mountain, so they worry about where to start the trip so that in the end, the maximum time to climb a mountain is minimized.

## Input data

The input file `munte4.in` contains a natural number $N$ on the first line representing the number of mountains.  
The second line will contain a sequence of $N$ natural numbers, separated by a space. The $i$-th number on the line represents the number of hours required to climb the $i$-th mountain from the range, not taking into account the fatigue.

## Output data

The output file `munte4.out` will contain on the first line two natural numbers separated by a space: the mountain from which the two start the trip and the maximum time to climb a mountain during the trip, having the minimum possible value considering all other starting options.

## Constraints and clarifications

$1 \leq N \leq 1\ 000\ 000$

## Example

`munte4.in`
```
4
5 9 10 3
```

`munte4.out`
```
2 11
```

## Explanation

We start the trip from mountain $2$. The climbing times are: $9$, $10 + 1$, $3 + 2$, $5 + 3$ with a maximum of $11$. Any other choice of the starting mountain leads to larger maximum times.
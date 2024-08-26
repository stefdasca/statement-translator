# Intfm

The night of the theater plays is approaching, and our friend Nocam wants to become more cultured. The event features $N$ shows. Reading the complete schedule, Nocam noticed that each play consists of $4$ acts of equal duration. There is a break between acts $2$ and $3$ that lasts as long as one act, which is one-fifth of the total duration of the play. Given the number $N$ and the $N$ time intervals corresponding to the periods during which each play runs (expressed in seconds), determine the maximum number of shows that Nocam can attend completely (presence is mandatory for all $4$ acts).

## Input data

The input file `intfm.in` will contain on the first line the number $N$, and on the next $N$ lines, there will be $2$ natural numbers, $start_i$ and $finish_i$ representing the start and end times for play $i$.

## Output data

The output file `intfm.out` will contain a single value, the maximum number of theater plays Nocam can attend.

## Constraints and clarifications
1 $ \leq N \leq 2000$
0 $ \leq start_i \leq finish_i \leq 10^9$ 
The duration of any show is divisible by $5$
During the break of a theater play, Nocam can also go to other plays, provided he returns in time for act $3$ of the initial play
Traveling between shows is instantaneous (if a show takes place in the interval $(a, b)$ and another show takes place in the interval $(b, c)$, Nocam will be able to attend both).
All shows have a positive duration (greater than $0$)

## Example

intfm.in
```
5
0 625
625 700
343 668
301 326
311 316
```

intfm.out
```
4
```

## Explanation

The intervals $(0, 625)$, $(625, 700)$, $(301, 326)$, $(311, 316)$ are taken.
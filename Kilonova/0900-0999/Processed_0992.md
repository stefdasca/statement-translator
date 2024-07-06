~[barcode.png|align=right]

Tired of eating steaks and salads, Raul became a *light artist*. For his next show, he has $N$ lights lined up in a row, numbered from $1$ to $N$, which are initially off. Subsequently, every second, for $M$ seconds, he will choose a continuous subsequence of lights and toggle their state; that is, the lights that are off will turn on, and the lights that are on will turn off. The show ends one second after the last switch.

# Task

After the show ends, he wonders, for $Q$ intervals of lights, for how many seconds was each interval fully lit (i.e., all lights in the interval are on at the same time).

# Input data

The first line contains three natural numbers $N$, $M$, and $Q$, representing the number of lights, the number of switches, and the number of intervals for which Raul wants an answer, respectively.

The next $M$ lines contain two natural numbers $l$ and $r$, representing, in order, the endpoints of the switched sequences.

The next $Q$ lines contain two natural numbers $l$ and $r$, representing the intervals of lights for which Raul wants to answer the question.

# Output data

On a single line, print $Q$ natural numbers, separated by a space, representing the answers to the $Q$ questions.

# Constraints and clarifications

* $1 \leq N, M, Q \leq 200\ 000$;
* $1 \leq l_i, r_i \leq N$, for any $1 \leq i \leq M$ in the switched intervals, and $1 \leq i \leq Q$ in the queried intervals.

|# | Points | Restrictions|
| - | - | ------------|
|1|9|$1 \leq N, M, Q \leq 100$|
|2|8|$1 \leq N, M, Q \leq 2\ 000$|
|3|21|$1 \leq N, M \leq 2\ 000$|
|4|27|$l_i = r_i$ for the switched intervals.|
|5|35|No additional restrictions.|

# Example 1

`stdin`
```
5 4 3
2 4
1 2
3 5
2 4
1 2
2 4
3 3
```

`stdout`
```
1 2 3
```

## Explanation

The sequence will look like this, row by row:

$t = 0: \quad \texttt{0 0 0 0 0}$
$t = 1: \quad \texttt{0 \textcolor{red}{1 1 1} 0}$
$t = 2: \quad \texttt{\textcolor{red}{1 0} 1 1 0}$
$t = 3: \quad \texttt{1 0 \textcolor{red}{0 0 1}}$
$t = 4: \quad \texttt{1 \textcolor{red}{1 1 1} 1}$

It can be observed, for the third query, that light $3$ is on for $3$ seconds.

# Example 2

`stdin`
```
7 7 7
1 5
3 7
2 6
3 4
1 5
2 4
3 6
1 2
3 5
4 6
2 4
4 6
1 3
2 3
```

`stdout`
```
2 3 1 2 1 1 2
```

## Explanation

The sequence will look like this, row by row:

$t = 0: \quad \texttt{0 0 0 0 0 0 0}$
$t = 1: \quad \texttt{\textcolor{red}{1 1 1 1 1} 0 0}$
$t = 2: \quad \texttt{1 1 \textcolor{red}{0 0 0 1 1}}$
$t = 3: \quad \texttt{1 \textcolor{red}{0 1 1 1 0} 1}$
$t = 4: \quad \texttt{1 0 \textcolor{red}{0 0} 1 0 1}$
$t = 5: \quad \texttt{\textcolor{red}{0 1 1 1 0} 0 1}$
$t = 6: \quad \texttt{0 \textcolor{red}{0 0 0} 0 0 1}$
$t = 7: \quad \texttt{0 0 \textcolor{red}{1 1 1 1} 1}$

It can be observed, for the first query, that lights $1$ and $2$ are simultaneously on for $2$ seconds.
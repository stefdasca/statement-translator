## Task

SETI researchers have discovered life on the planet Mars. They observed that a day on Mars lasts $N$ seconds and that there are $M$ songs, with two radio stations playing each song exactly once every day, in a random order. The total duration of all the songs is $N$ seconds. Knowing the numbers $N$ and $M$, as well as the duration of each song, the researchers want to determine the average time during which both stations are playing the same song simultaneously over the course of a Martian day.

## Input data

The input file `marsmusic.in` contains on the first line two natural numbers $N$ and $M$ as described in the statement. On the next line, there are $M$ natural numbers, representing the durations of the $M$ songs.

## Output data

The output file `marsmusic.out` will contain on the first line a single real number, representing the average time during which both radio stations play the same song simultaneously.

## Constraints

$1 \leq N \leq 10\ 000$

$1 \leq M \leq 50$

It is recommended to display the result with a precision of 9 decimals.

The displayed result is considered correct if it differs by a relative error of at most $0.00001$ from the official solution. This means that:

1. If the displayed result differs by at most $0.00001$ from the commission's solution, then it is accepted.
2. Let $x$ be the displayed result and $y$ be the commission's solution. If $\left|x - y\right| / \max(x, y) \leq 0.00001$ then the result is accepted.
3. In any other case, the result is rejected.

## Example

`marsmusic.in`
```
6 2
4 2
```

`marsmusic.out`
```
4.000000000
```

## Explanation

There are four ways in which the songs can be played on the two radio stations: $(1, 2)(1, 2)$ , $(1, 2)(2, 1)$ , $(2, 1)(1, 2)$ , and $(2, 1)(2, 1)$. The duration of time during which a song is played on both stations at the same time is $6$ for the first and fourth cases and $2$ for the other two. Therefore, the answer will be $\frac{1}{4} \cdot 6 + \frac{1}{4} \cdot 2 + \frac{1}{4} \cdot 2 + \frac{1}{4} \cdot 6 = 4$.
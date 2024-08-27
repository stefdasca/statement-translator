## Task

We're not letting it slide this time! The dates for the Algorithms rounds slide through time easier than a child on ice (as evidence, this statement was written in winter when the comparison was seasonal), usually due to many unforeseen events such as national and international competitions, exam sessions, and internships. But enough, from next year everything will be planned in advance, and unforeseen events will all occur within a single hour! The competition calendar of the Algorithms has $N$ hours and is represented by a string formed from $N$ characters of types $#$ , $@$ , and $.$ . Positions marked with $#$ and $@$ in the string represent hours when Algorithms rounds are held, a round being represented by a maximal length subarray of characters of the same type. Positions marked with $.$ represent free hours. For example, the string $"###..@@#..##"$ represents a calendar with $12$ hours and $4$ rounds of competition (in intervals $[1, 3]$, $[6, 7]$, $[8, 8]$, $[11, 12)]$ ). The old infoarena interface allows the shifting of rounds; unfortunately, a shift represents moving a round by one hour forward or backward (keeping its length), provided that after shifting it does not overlap with another round. Note that the beginning and/or end of a round may be outside the $N$ hours of the initial representation after one or more shifts. For example, for the calendar $"##..@."$ , the first round can be shifted by two hours forward, obtaining the calendar $"..##@."$ , but also by two hours backward, obtaining the calendar $"##....@$" . For the calendar $"##@"$ we cannot shift the first round by one hour forward, unless we first shift the second round by one hour forward. Let $T(i)$ denote the minimum number of shifts required for hour $i$ in the initial representation to become free. Calculate $S = T(1) + T(2) + \dots + T(N)$ ! 

## Input data

The input file `slide.in` contains, on the single line, a string of $N$ characters $#$ , $@$ , and $.$ representing the competition calendar. 

## Output data

In the output file `slide.out` you will print a single natural number $S = T(1) + T(2) + \dots + T(N)$ . 

## Constraints and clarifications

1 $\leq$ $N$ $\leq$ 1\ 000\ 000 

For 30% of the tests, $N \leq 1\ 000$ . 

## Example

`slide.in` 

`#@##..@` 

`slide.out` 

`7` 

## Explanation

$T(1) = 1$ (shift the first round by one hour backward),

$T(2) = 2$ (shift the first round by one hour backward and then the second round by one hour backward),

$T(3) = 1$,

$T(4) = 2$ (shift the third round by two hours forward),

$T(5) = 0$,

$T(6) = 0$,

$T(7) = 1$. 

`#@.####@#@`

`23`

...
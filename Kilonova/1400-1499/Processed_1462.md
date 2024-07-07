
The National Audiovisual Council (CNA) is the authority that coordinates the activity of media stations in Romania. The head of CNA wants a statistic regarding the advertising broadcasted by TV stations. To this end, he receives daily information in the following format: $d \ \ \text{hh}:\text{mm}:\text{ss}$, where $d$ is the duration expressed in seconds of the advertising, and $\text{hh}:\text{mm}:\text{ss}$ is the start time of the advertising ($\text{hh}$ is the hour, $\text{mm}$ is the minute, and $\text{ss}$ is the second). Note that $d$ is separated from $\text{hh}$ by a single space, and the following values are separated by the `:` character.
For example, a line in the form: $150 \ 05:02:45$ is interpreted as follows: there is a TV station that broadcasted an advertisement with a duration of $150$ seconds, starting at $5$ hours, $2$ minutes, and $45$ seconds.
The "golden second" is a second in which the most advertising is broadcasted, meaning that the maximum number of TV stations are broadcasting advertisements during that second. If there are multiple such seconds, the "golden second" is considered to be the first such second during the day.
The head of CNA receives every morning the list of the previous day's activity as a sequence of lines, each line having the format described above.

# Task

Write a program that, knowing the list from the previous day, solves the following requirements:
1. Determines the total duration during which no TV station broadcasted advertisements;
2. Determines the "golden second".

# Input data

The input file `tv.in` contains on the first line the natural number $c$, which can be $1$ or $2$, representing the requirement to be solved. The second line contains the natural number $N$, representing the number of lines in the list with information received by the head. The next $N$ lines describe the information, in the format specified in the statement.

# Output data

The output file `tv.out` will contain a single line with $3$ natural numbers separated by the `:` character in the following format: $\text{hh}:\text{mm}:\text{ss}$, representing the total duration expressed in hours $(\text{hh})$, minutes $(\text{mm})$, and seconds $(\text{ss})$ during which no TV station broadcasted advertisements on the respective day (if $c = 1$), respectively the "golden second" (if $c = 2$).

# Constraints and clarifications

* $1 \leq N \leq 100 \ 000$
* $\text{hh}$ will be a two-digit number between $00$ and $23$
* $\text{mm}$, and $\text{ss}$ will be two-digit numbers between $00$ and $59$
* The duration $d$ is non-zero and the end of the advertising broadcast is within the current day.
* For tests worth $60\%$ of the score, the requirement is $1$.

# Example 1

`tv.in`
```
1
6
120 12:00:00
200 12:01:50
1000 13:00:00
2000 13:01:00
100 14:05:05
10 23:59:49
```

`tv.out`
```
23:18:40
```

## Explanation

For example $1$, the requirement is $1$. During the day, for $23$ hours, $18$ minutes, and $40$ seconds, no advertisements were broadcasted.

# Example 2

`tv.in`
```
2
6
1200 12:00:00
2000 12:01:50
1000 12:00:00
2000 13:01:00
100 14:05:05
10 23:59:49
```

`tv.out`
```
12:01:50
```

## Explanation

For example $2$, the requirement is $2$. The golden second is $12:01:50$ because there is a maximum number of stations broadcasting advertisements ($3$ stations).

## Task

Two out of the $3$ members of the winning team of one of the $ACM ICPC$ regional contests are going to meet to practice for the finals. They decided to meet sometime between hour $X$ and hour $Y$. Since they never arrive anywhere on time, they did not set an exact time for the meeting. However, they decided that whoever arrives first at the meeting point will wait for the other for at most $Z$ minutes. Knowing that both of them will eventually arrive at the meeting point sometime between hour $X$ and hour $Y$ (not necessarily after an exact integer number of minutes), calculate the probability that the two will meet.

## Input data

The input file `meeting.in` will contain $2$ integers, $X$ and $Y$, and a real number $Z$. The numbers will be separated by a space.

## Output data

In the output file `meeting.out` you will print the required probability with $7$ digits after the decimal point. An error of $10^{-7}$ will be accepted.

## Constraints and clarifications

$0 \leq X < Y \leq 24$

$0 < Z \leq 60*(Y-X)$

## Example

`meeting.in` `meeting.out` $11 \ 12 \ 20.0$ `0.5555556`
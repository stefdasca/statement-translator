# Task

Cătălin, like any other Romanian, has stocked up for the upcoming crisis. He now possesses a sufficient quantity ("without number") of each type of banknote. In Alexandria, the city where he lives, only banknotes with values equal to prime numbers are used. He calls a number “ace” if it is a strictly greater power than $1$ of a banknote and bets all his money that you cannot answer $Q$ questions of the form: "How many aces are there in the interval $[A, B]$? $\dots$ Try to answer Cătălin's questions to win the bet.

## Input data

The input file `asi.in` contains on the first line a natural number $Q$ representing the number of questions. The next $Q$ lines contain $2$ numbers $A$ and $B$, representing the endpoints of the intervals.

## Output data

The output file `asi.out` will contain $Q$ lines, each containing the answer to the respective question.

## Constraints and clarifications

$1 \leq A \leq B \leq 10^{12}$

$1 \leq Q \leq 10^5$

Cătălin from Alexandria considers a number "ace" if it can be written as $p^i$ where $p$ is prime and $i \geq 2$

$1$ is not considered a prime number

Clarifications

For tests worth 5 points:

$1 \leq A \leq B \leq 10^2$

$1 \leq Q \leq 10^3$

For other tests worth 5 points:

$1 \leq A \leq B \leq 10^3$

$1 \leq Q \leq 10^3$

For other tests worth 15 points:

$1 \leq A \leq B \leq 10^9$

$1 \leq Q \leq 10^3$

For other tests worth 15 points:

$1 \leq A \leq B \leq 10^6$

$1 \leq Q \leq 10^5$

For other tests worth 20 points:

$1 \leq A \leq B \leq 10^9$

$1 \leq Q \leq 10^5$

## Example

asi.in

```
1
7 20
```

asi.out

```
3
```

## Explanation

Between $7$ and $20$, the only numbers that follow the rule are $8 = 2^3$, $9 = 3^2$, and $16 = 2^4$.
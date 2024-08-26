## Task

Bujor is very passionate about gambling. He has $n$ casinos in his city, each of which has $m$ slot machines. Every day for the next $d$ days, he visits every machine in each casino and plays a certain number of times. Specifically, he has a matrix $A$ where $a_{ijk}$ = the number of times he plays on the $k$-th machine at the $j$-th casino, each day. The casinos belong to the same company, PCGE – Por Costel Gambling Enterprise. Por Costel has since become a respected business pork. Each day before it starts, the slot machines can be 'manipulated'. Thus, at the beginning of each day, Por Costel can send a command to each casino, a list of $m$ numbers that represent the expected-winnings (the average amount of lei Bujor wins if he plays once on that machine - a real number, possibly negative) with which to set each machine. The $k$-th number on the list will represent the expected-winnings for the $k$-th machine in the casino. Specifically, Por Costel has matrix $B$, where $b_{ij}$ = expected-winnings for the $k$-th machine in any casino, on the $j$-th day, each time you play on it. Por Costel pities Bujor and his gambling habit. For now, he wants to help him but without causing significant losses to the company. Therefore, he wants Bujor's sum of expected winnings to be exactly 1 leu each day out of the $d$ days. Moreover, he wants Bujor to win 1 leu at exactly one casino each day (0 lei at the rest) and for there not to be any casino at which he hasn't won anything by the end of the $d$ days. Knowing Bujor's matrix $A$, you need to choose Por Costel's matrix $B$ so that the above conditions are met.

## Input data

The input file `bujor.in` contains on the first line $t$, the number of tests. Each of the $t$ tests will follow the format below: The first line will contain the number of $d$ days, $n$ casinos, and $m$ slot machines in a casino. Each of the next $d$ lines will contain a sequence of $n \times m$ numbers separated by spaces - the numbers from matrix $A$.

## Output data

In the output file `bujor.out` the answer for each of the $t$ tests will be printed, namely $d$ lines each containing $n \times m$ numbers separated by spaces: a possible choice for Por Costel's matrix $B$.

## Constraints and clarifications

$d \leq 10$

$n \leq 50$

$m \leq 50$

$1 \leq a_{ijk} \leq 1\ 000\ 000\ 000$ any value in matrix $B \leq 10\ 000$

It is guaranteed that there is at least one solution for each test.

Any correct solution can be printed.

It is recommended to print floating-point numbers with a precision of at least $10^{-9}$.

## Example

`bujor.in`

```
1
3 2 1
2 3
2 2
0 1
```

`bujor.out`

```
0.333333333 -0.666666667
0.000000000 0.666666667
0.666666667 -1.00000000
-0.666666667 0.333333333
1.000000000
```
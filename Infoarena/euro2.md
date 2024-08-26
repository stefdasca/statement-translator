# Euro2

The Stock Exchange reports the Euro-RON exchange rate many times throughout the day, reflecting all the fluctuations that occur during the day. Since short-term fluctuations are not very important for the public, the National Bank wants to communicate the fluctuation in such a way that it is understood that it increased up to a certain point, and then decreased.

## Task

Determine the maximum number of reports that can be selected and made public so that the public understands that on that day the exchange rate increased to a certain point and then decreased. The reports that are made public must be chosen in chronological order.

## Input data

The first line of the input file `euro2.in` contains the natural number $N$, representing the number of reports. The next $N$ lines contain the $N$ values of the exchange rate, one per line.

## Output data

The first and only line of the output file `euro2.out` will contain a natural number, representing the number of reports chosen by the National Bank.

## Constraints and clarifications

$2 < N \leq 10\,000$

$3.0000 \leq raportare_i \leq 4.0000$

The numbers representing the value of one Euro in RON all have exactly four decimal places and are distinct.

The reports chosen by the National Bank must contain an increasing subsequence (formed by at least two elements), followed by a decreasing subsequence (formed by at least one element).

## Example

`euro2.in`

```
12
3.1120
3.2470
3.2110
3.2090
3.2440
3.3500
3.4700
3.5100
3.3120
3.2150
3.1170
3.2170
```

`euro2.out`

```
9
```

## Explanation

The chosen reports are: $3.1120$, $3.2110$, $3.2440$, $3.3500$, $3.4700$, $3.5100$, $3.3120$, $3.2150$, and $3.1170$.
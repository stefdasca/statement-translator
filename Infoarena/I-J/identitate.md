## Task

You are given $N \leq 200$ decimal digits. You would like to choose $13$ of these $N$ numbers and arrange them in a convenient order to form a valid CNP. How many distinct valid CNPs can you form? Attention: The definition of a CNP in this problem may differ from the real-world definition of a CNP! A valid CNP is a sequence of $13$ numbers:

- sex (one digit): $1$ for male, $2$ for female;
- year of birth $(1901$-$2000$, $2$ digits): last two digits of the year; example: $(19) 25$, $(19) 02$;
- month of birth ($2$ digits): $01$ for January, $02$ for February, $\dots$, $12$ for December;
- day of birth ($2$ digits): $01$ - $28/29/30/31$, depending on the month of birth;
- identifier ($6$ digits): no restrictions.

For example, $1960313666999$ is a valid CNP, whereas $2981131123456$ is not a valid CNP. (November has only $30$ days)

## Input data

The input file `identitate.in` will contain a sequence of at least $13$ and at most $200$ decimal digits.

## Output data

The output file `identitate.out` will contain a single natural number, representing the total number of valid CNPs for the given input sequence.

## Constraints and clarifications

$13 \leq N \leq 200$

Within the interval of years $1901$-$2000$, leap years are all those that are divisible by $4$: $1904$, $1908$, $\dots$, $2000$.

For tests worth $40$ points, it is guaranteed that the answer will not exceed $5\,000\,000$.

## Example

`identitate.in`
```
91919191919999
```

`identitate.out`
```
10
```

`identitate.in`
```
1960313666999
```

`identitate.out`
```
3220
```

`identitate.in`
```
987984483745978347
```

`identitate.out`
```
0
```
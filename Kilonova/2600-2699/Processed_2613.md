
The computer science lab of Linear School has a single row of $N$ computers numbered from 1 to $N$. Each of them has a "PWR" button that if pressed will turn on the computer (if it was off) or turn it off (if it was on).
Due to the positioning of the window, each computer has accumulated over time a different amount of dust: the first one has $N$ units of dust, the second $N-1$, the third $N-2$, etc. The last one has a single unit.
Before the cleaning staff arrived, the teacher turned off all computers but forgot to close the lab door. Therefore, $N$ students entered the lab. The first student pressed the "PWR" button on each computer, the second pressed it on every second computer, the third on every third computer, etc. The last student pressed the button only on the last computer.
To avoid accidents, the cleaning staff will only clean the dust off the turned-off computers; those that are turned on will retain a total amount of $C$ units of dust.

# Task

Determine the last four digits of $C$.

# Input data

The input file `calculatoare.in` contains a single natural number $N$, with the meaning from the statement.

# Output data

The output file `calculatoare.out` must contain a single natural number, which consists of the last four digits of the total amount of dust $C$.

# Constraints and clarifications

* $1 \leq N \leq 2 \cdot 10^9$
* For 60% of the tests, $1 \leq N \leq 10^6$
* If $C < 1000$ the value must be displayed as is (without leading zeros)

# Example 1

`calculatoare.in`
```
1
```

`calculatoare.out`
```
1
```

# Example 2

`calculatoare.in`
```
10
```

`calculatoare.out`
```
19
```

## Explanation

The state of the computers at the end of the day:
```
nr:    1 2 3 4 5 6 7 8 9 10
dust:  10 0 0 7 0 0 0 0 2  0
```

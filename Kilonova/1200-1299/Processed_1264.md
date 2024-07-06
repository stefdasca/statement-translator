~[ceas.png|align=right]

Andrei bought a wall clock that marks the hours of a day using numbers from $1$ to $12$, and the minutes are marked with dots. The clock has two hands. The first hand shows the hour and changes its position every hour. The second hand shows the minute and changes its position every minute. For example, if it is $10$ o'clock and $11$ minutes, the hour hand is positioned at the number $10$ marked on the clock, and the minute hand is positioned on the dot corresponding to the $11$th minute (as in the adjacent image). After one minute, the hour hand will still be positioned at the number $10$, and the minute hand will move one dot to indicate the $12$th minute.

After a few days of operation, Andrei notices that the clock does not work correctly, because whenever the two hands overlap, the clock stops for $5$ minutes (the two hands remain overlapped for $5$ minutes). Knowing the hour and minute at which Andrei fixed the clock correctly, determine what time the clock shows after a certain period (expressed in hours and minutes).

# Task

Write a program that reads the hour and minute at which the clock is fixed and shows the hour and minute indicated by Andrei's clock after a certain number of hours and minutes.

# Input data

Read from the input file `ceas.in` in this order, separated by a space, four numbers $h_1$, $m_1$, $h_2$, $m_2$, where $h_1$ and $m_1$ represent the hour and minute at which the clock is fixed, $h_2$ and $m_2$ represent the number of hours and the number of minutes that have passed since fixing it.

# Output data

Print into the output file `ceas.out`, on a single line, in this order, separated by a space, two numbers $h_3$ and $m_3$ which will represent the hour and minute indicated by the clock.

# Constraints and clarifications

* The hour hand does not have intermediate positions, it will always be positioned on one of the natural numbers in the interval [$1, 12$]
* $1 \leq h_1, h_3 \leq 12$;
* $0 \leq h_2 \leq 1 \ 000$;
* $0 \leq m_1, m_2, m_3 \leq 59$;

# Example 1

`ceas.in`
```
2 30 1 10 
```

`ceas.out`
```
3 35
```

## Explanation

The clock is fixed at $2$ o'clock and $30$ minutes. After $30$ minutes the clock will show $3$ o'clock and $0$ minutes. After another $15$ minutes, the hour hand and the minute hand will overlap, because it will be $3$ o'clock and $15$ minutes. In this position, the two hands remain together for another $5$ minutes (because the clock delays $5$ minutes). After another $20$ minutes the clock will show $3$ o'clock and $35$ minutes.

# Example 2

`ceas.in`
```
3 7 2 19
```

`ceas.out`
```
5 16
```
    
## Explanation

The clock is fixed at $3$ o'clock and $7$ minutes. After $2$ hours and $19$ minutes the clock will show $5$ o'clock and $16$ minutes.
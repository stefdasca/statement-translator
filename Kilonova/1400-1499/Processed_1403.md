G has a digital clock that displays the time in the format of a value between $0$ and $23$ for the hour as a one- or two-digit number, a value between $0$ and $59$ for the minute as a two-digit number (the first digit is $0$ if the number of minutes to be displayed is less than $10$), and a value between $0$ and $59$ for the second as a two-digit number (if the number of seconds to be displayed is less than $10$, the first digit is $0$). These pieces of information appear in the order: number of hours, number of minutes, number of seconds and are separated by a space. Examples: $23 \\ 39 \\ 17$ (for $23$ hours, $39$ minutes, and $17$ seconds), $1 \\ 00 \\ 01$ (for $1$ hour, $0$ minutes, and $1$ second) or $0 \\ 02 \\ 02$ (for $0$ hours, $2$ minutes, and $2$ seconds).

G observes that if he concatenates these three values, he can construct a natural number. Thus, for the above examples, he obtains the numbers $233917$, $10001$ and respectively $202$ (Attention! The resulting number does not start with $0$ – any leading zeros are eliminated!). G also notices that there are times when the number thus formed is a palindrome, as is the case with the second and third examples. G names these moments of time palindromic moments and wants to find out how many such moments there are within a given time interval.

A time interval is specified during the year $2013$ and is given by the exact date and time when it starts and the exact date and time when it ends. The date is specified by two numbers representing the month and the day, and the exact time is given in the format displayed by G's digital clock.

# Task

Determine how many palindromic moments occur within $k$ given time intervals.

# Input data

The input file `momente.in` contains on the first line the natural number $k$ with the significance given in the statement.

Each of the next $k$ lines contains $10$ natural values separated by spaces. The first five numbers represent the month, day, hour, minute, and second when the given time interval starts. The next five numbers represent the month, day, hour, minute, and second when the given time interval ends.

# Output data

The output file `momente.out` will contain $k$ lines. On line $i$ ($1 \\leq i \\leq k$) there will be a single number which will represent the number of palindromic moments in interval $i$.

# Constraints and clarifications

* $k \\leq 10^5$
* The start date precedes the end date for each time interval
* In the year $2013$, the month of February has $28$ days
* For $50$% of the tests we will have $k = 1$
* A palindrome is defined as a number that reads the same from left to right as from right to left
* If the given time interval starts or ends with a palindromic moment, it is counted.

# Example

`momente.in`
```
1
2 28 23 44 32 3 1 0 02 02
```

`momente.out`
```
24
```

# Explanation

The input file contains a single time interval, from $28$ February at $23$ hours, $44$ minutes and $32$ seconds to $1$ March at $0$ hours, $2$ minutes and $2$ seconds.

In this time interval, there are $24$ palindromic moments as follows:

* On $28$ February at $23 \\ 44 \\ 32$ and $23 \\ 55 \\ 32$;
* On $1$ March at $0 \\ 00 \\ 00$, $0 \\ 00 \\ 01$, $0 \\ 00 \\ 02$, $0 \\ 00 \\ 03$, $0 \\ 00 \\ 04$, $0 \\ 00 \\ 05$, $0 \\ 00 \\ 06$, $0 \\ 00 \\ 07$, $0 \\ 00 \\ 08$, $0 \\ 00 \\ 09$,
$0 \\ 00 \\ 11$, $0 \\ 00 \\ 22$, $0 \\ 00 \\ 33$, $0 \\ 00 \\ 44$, $0 \\ 00 \\ 55$, $0 \\ 01 \\ 01$, $0 \\ 01 \\ 11$, $0 \\ 01 \\ 21$, $0 \\ 01 \\ 31$, $0 \\ 01 \\ 41$, $0 \\ 01 \\ 51$ and $0 \\ 02 \\ 02$
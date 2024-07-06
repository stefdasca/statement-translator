# Gigel is a strange guy. He likes to impress his colleagues by expressing durations only in seconds. For example, if you ask him what time it is, he will tell you how many seconds have passed since "00:00" of that day. If you ask him how old he is, he will tell you how many seconds have passed since he was born.

Gigel's colleagues have decided that they don't need to be impressed; therefore, they need a program that reads from the keyboard a natural number $N$ which represents Gigel's age expressed in seconds and will display on the screen how many years, months, and days old Gigel is (remaining hours and minutes are considered insignificant).

Don't forget that leap years are those divisible by $4$, but not divisible by $100$ or divisible by $400$. For example, $1992$ and $2000$ were leap years. But the year $1900$ was not a leap year. Leap years have $366$ days, unlike the others which have only $365$.

**Assume we are on the last day of school in the $\\text{2001-2002}$ school year ($\\textbf{June 15, 2002}$).**

# Task
Write this program for Gigel's colleagues!

# Input data

The input file `gigel.in` contains a single integer $n$, Gigel's age expressed in seconds.

# Output data

The output file `gigel.out` will contain 3 numbers, representing Gigel's age at that particular moment in years, months, and days.

# Constraints and clarifications

* $1 \leq n \leq 10^{18}$
* For tests worth 60 points, $1 \leq n \leq 10^{9}$.
* We consider that year $0$ exists, and it is a leap year.
* We will consider that time has always been measured the same way, and years before our era (negative numbered years) follow the same rules as present years.
* The sequence of years is $\\dots, -3, -2, -1, 0, 1, 2, \\dots$.
* The tests and constraints have been revised, and the display format has also been modified compared to the original statement.

# Example

`gigel.in`
```
69206400
```

`gigel.out`
```
2 2 10
```

## Explanation

Gigel is $2$ years, $2$ months, and $10$ days old.


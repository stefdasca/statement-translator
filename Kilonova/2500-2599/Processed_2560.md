```markdown
# Task

On the alien planet PPR-5, the structure of the year is slightly different from that of the Earth year. 

Specifically, the year on planet PPR-5 is divided into $n$ months, numbered from $1$ to $n$. For each month $i$, the number of days $z_i$ of that month is known. The days of month $i$ are numbered from $1$ to $z_i$.

As the discoverer of this planet, you will need to find the *relative value* of the alien year. The *relative value* of the alien year is equal to the sum of the ordinal numbers of all the days in the year. The ordinal number of a day is equal to its position in the month to which it belongs.

# Input data

The first line of the input file `an.in` will contain a number $n$ ($1 \le n \le 100\ 000$) — the number of months in the alien year.

The second line will contain $n$ numbers ($1 \le z_1, z_2, \ldots, z_n \le 10\ 000\ 000$) — the number of days in each month.

# Output data

Print to the output file `an.out` a natural number, the *relative value* of the alien year.

# Constraints and clarifications
|#|Points|Constraints                            |
|-|-------|--------------------------------------|
|1| 15    | $n=1$                                |
|2| 20    | $1 \le z_1, z_2, \ldots z_n \le 31$  |
|3| 25    | $1 \le z_1, z_2, \ldots z_n \le 200$  |
|4| 15    | $1 \le z_1, z_2, \ldots z_n \le 40\ 000$|
|5| 25    | No additional constraints             |

# Example 1

`an.in`

```
3
4 1 2
```

`an.out`
```
14
```

In the first example, the alien year has $3$ months. The first month has $4$ days, numbered from $1$ to $4$. The second month has a single day, with the ordinal number $1$. The third month has $2$ days, with ordinal numbers $1$ and $2$.

The *relative value* of the year is equal to $1 + 2 + 3 + 4 + 1 + 1 + 2 = 14$.

# Example 2

`an.in`

```
12
31 28 31 30 31 30 31 31 30 31 30 31
```

`an.out`

```
5738
```
```
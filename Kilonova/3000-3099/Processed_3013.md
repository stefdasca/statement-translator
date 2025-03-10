# Task:

During the winter vacation, Adelina decided to take a break from homework and chose to read some of the books brought by Santa Claus: those with historical or SF themes. As she read, she noted down in her notebook the calendar dates of those events that impressed her. After the vacation, she tells her desk-mate about these events and remarks that some calendar dates have a special form, a palindrome: read from right to left they represent the same date as when read normally, from left to right.

# Task:

For the $n$ calendar dates in Adelina's diary, count and display how many palindromic dates were found and then specify the centuries with the most palindromic dates.

# Input data:

The input file `datapal.in` contains the following information:
- the first line contains a number $n$, representing the number of calendar dates;
- each of the next $n$ lines contains a calendar date in the format `zz/ll/aaaa` (two digits for day, two digits for month, four digits for year).

# Output data

The output file `datapal.out` will contain on the first line the number of palindromic calendar dates, and on the second line the centuries with the most palindromic dates, in chronological order, separated by a space, or the message `NO PALINDROMIC DATES` if no such dates were found.

# Constraints and clarifications

* $0 < n \leq 1\ 000$
* all calendar dates are valid;
* in the test data collection, there is always at least one palindromic date;
* the years belong to the period $10 - 9\ 999$ and are A.D.

# Example

`datapal.in`
```
5
01122110
11111111
19111111
09122190
12111121
```

`datapal.out`
```
4 
12 22
```

## Explanation

There are $4$ palindromic dates: two in the $12^{th}$ century and two in the $22^{nd}$ century.
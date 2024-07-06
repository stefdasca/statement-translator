I have a terribly disorganized secretary. Instead of organizing my schedule by days and hours chronologically, she writes the activities in my work agenda randomly. It’s no wonder that my schedule includes overlapping activities, lack of free time, or a variety of confusions. To be able to fire her, I took the agenda for the entire year $2013$. The recordings in the agenda are written each on one line in the form: `datas-dataf activity`, where `datas` represents the start date, and `dataf` represents the end date of the specified activity, meaning that the activity took place in the interval `[datas, dataf)`, where `datas` precedes `dataf`. 

The dates are specified in the following format: `D M H.MM`, where `D` represents the day of the month, `M` represents the month name, `H` represents the hour, and `MM` represents the minute. For example:
* `1 May 8.30-1 May 9.30 Breakfast at Tiffany’s`
* `28 February 8.00-05 March 23.59 Concert in Vienna`

The hour is separated from the minute by the character `.` (dot) and the recording can contain any number of spaces (even none), placed anywhere in the entry.

# Task

Write a program that solves the following tasks:

1. Determine the duration of the longest planned activity in $2013$.
2. Determine the maximum number of activities that were planned simultaneously (occur at the same time, i.e., overlap fully or partially) in $2013$.
3. Determine the duration of the longest uninterrupted free time period between two activities in the agenda.

# Input data

The input file `agenda.in` contains:
* The first line contains the natural number $c$, representing the task to be solved ($1$, $2$ or $3$).
* Each of the following lines contains an entry in the format described in the statement.

# Output data

The output file `agenda.out` will contain a single line with the answer to the task $c$ specified in the input file. 
* If the task is $2$, the answer is a natural number representing the maximum number of activities that overlapped in $2013$.
* If the task is $1$ or $3$, the answer is a duration specified by 3 natural numbers separated by a space: `D H MM`, representing the duration (`D` days, `H` hours, and `MM` minutes).

# Constraints and clarifications

* The number of lines in the input file does not exceed $1 \ 000$.
* The length of a line in the input file is at most $1 \ 000$ characters.
* In the input file and in the output file, hours are between $0$ and $23$, and minutes are between $0$ and $59$.
* The days, hours, and minutes in the input file dates can contain leading zeros.
* The calendar dates, hours, and minutes specified in the entries are correct.
* For tests worth $20$ points, the task is $1$; for tests worth $40$ points, the task is $2$, and for tests worth $40$ points, the task is $3$.

# Example 1

`agenda.in`
```
1
1 May 8.30-1 May 09.30 Breakfast at Tiffany’s
28 February 8.30- 5 March 23.59 Concert in Vienna
2 January 9.00 - 2 January 12.30 Meeting
```

`agenda.out`
```
5 15 29
```

## Explanation

The task is $1$. There are $3$ activities in the agenda. The first lasts $1$ hour, the second lasts $5$ days $15$ hours and $29$ minutes, the third lasts $3$ hours and $30$ minutes.

# Example 2

`agenda.in`
```
2
1 May 8.30-1 May 13.20 Shareholders Meeting
1 May 13.30- 1 May 16.00 Audiences
1 May 13.00-1 May 15.00 Lunch with Deputies
1 May 14.00-1 May 20.00 Inspection
2 May 9.00-2 May 14.00 Work Meeting
30 April 19.00-30 April 22.00 Charity Dinner
```

`agenda.out`
```
3
```

## Explanation

The task is $2$. There are $6$ activities in the agenda. The maximum number of activities that occur simultaneously is $3$ (activities $2$, $3$, $4$).

# Example 3

`agenda.in`
```
3
1 May 8.30-1 May 13.20 Shareholders Meeting
1 May 13.30- 1 May 16.00 Audiences
1 May 13.00-1 May 15.00 Lunch with Deputies
1 May 14.00-1 May 20.00 Inspection
2 May 9.15-2 May 14.00 Work Meeting
30 April 19.00-30 April 22.00 Charity Dinner
```

`agenda.out`
```
0 13 15
```

## Explanation

The task is $3$. There are $6$ activities in the agenda. Free time exists between activities $6$ and $1$ ($10$ hours and $30$ minutes) and between activities $4$ and $5$ ($13$ hours and $15$ minutes). The maximum length of free time is $0$ days $13$ hours and $15$ minutes.
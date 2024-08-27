## Task

You are a student at the Faculty of Computer Science. You have $n$ years of study. In each year of study, you have a certain number $m$ of assignments (the number of assignments each year is not necessarily the same). The $i$ -th assignment in the $j$ -th year takes $t_{i,j}$ units of time. Unfortunately, it must be submitted within at most $d_{i,j}$ units of time from the beginning of the academic year. As a student, you can only work on one assignment at a time. If you start the $i$ -th assignment at $t$ units of time after the beginning of the academic year, you finish it after $t + t_{i,j}$ units of time. If $t + t_{i,j} > d_{i,j}$, you will submit the assignment after the deadline has passed. The professor who gave the assignment is upset if you are late. His displeasure is equal to the time by which you are late: $(t + t_{i,j}) - d_{i,j}$. Your goal is to minimize the displeasure of the angriest professor.

## Input data

The input file `teme.in` contains on the first line the number of years of study. The input data for each of the $n$ years follows. For a year, the input file contains the number $m$ of assignments; for each of the $m$ assignments, the file contains two numbers: the duration of the assignment and the deadline by which it must be submitted.

## Output data

In the output file `teme.out` print for each year on a new line the displeasure of the angriest professor, considering that you try to do the assignments in such a way as to minimize this displeasure.

## Constraints and clarifications

1 $ \leq n \leq $ 100

0 $ \leq m \leq $ 10000

a year of study is long enough to finish all the assignments for that year (there is no risk of working on an assignment from year 1 in year 2, $\dots$ etc)

deadlines and durations of the assignments are integers between 1 and 10000

## Example

`teme.in`
```
1
6
3 6
2 8
1 9
4 9
3 14
2 15
1
```

`teme.out`
```
1
```
Here's the translated statement:

---

At the Mititelu’ Gates contest, for the proper conduct of the competition, a given amount $S$ is necessary; for this purpose, a list of $n$ people who can and want to sponsor this event was created. Each of the $n$ people confirmed their participation and the amount offered. Determine the selected values for sponsoring the contest, knowing that the number of people must be minimal and the total amount should cover the expenses.

# Input data

The input file `mititelu-gates.in` contains two integers, $n$ and $S$ on the first line.

The next line contains $n$ natural numbers, representing the amounts offered by the $n$ participants.

# Output data

The output file `mititelu-gates.out` should contain the chosen numbers in descending order. If there are multiple solutions, the one with the maximum collected sum will be displayed.

# Constraints and clarifications

* $1 \leq n \leq 100 \ 000$;
* $1 \leq S \leq 10^9$;
* $1 \leq v_i \leq 10^6$;
* The tests and constraints have been updated to the standards of the year $2023$, and the output format has also been modified compared to the original statement.

# Example 1

`mititelu-gates.in`
```
8 30
2 3 2 5 15 7 4 1 
```

`mititelu-gates.out`
```
15 7 5 4
```

# Example 2

`mititelu-gates.in`
```
7 37
6 4 2 17 2 5 10 
```

`mititelu-gates.out`
```
17 10 6 5
```

---
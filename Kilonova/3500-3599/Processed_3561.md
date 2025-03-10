
~[Sigla.png|align=right]

# Task

The University of Bologna is one of the oldest universities in the world, having started accepting students since the year 1088. Due to an unforeseen fire, the University lost all student records. Fortunately, a chronological list of students admitted to the university and those who graduated was found in an archive. The university committee asks you to determine the students enrolled at the University at the end of each year.

# Input data

The first line of the file `universitate.in` contains a number $k$, representing the total number of events in the list.

This is followed by $k$ lines of the form:
`year action student`

# Output data

In the output file `universitate.out`, there will be $937$ lines, each representing the students enrolled at the university at the end of each year from $1088$ to $2024$. The order in which the students are displayed is not important.

# Constraints and clarifications

* $0 \leq k \leq 100 \ 0000$, where $k$ is the number of events in the list.
* It is guaranteed that the years will be given in increasing order.
* It is guaranteed that the years are only values between $1088$ and $2024$ inclusive.
* The action can only have the values $0$ and $1$, where $0$ means that the student enrolled at the university and $1$ that the student graduated.
* Student IDs are integer values between $0$ and $1 \ 000 \ 000$ inclusive.
* It is guaranteed that at the end of each year there will be no more than $1 \ 000$ students in the university. Note: this restriction is only for the end of the year; during the year there can be more students in the university.
* It is guaranteed that the actions are correct, therefore a student who enrolls at the university is not already enrolled, and if they graduate from the university, they are already there.
* If a student has graduated, they can enroll again.

Let $n$ be the maximum ID number of a student. $0 \leq$ student ID $\leq n$. Then:

* For $11$ points: $n \leq 1 \ 000$ and $k \leq 1 \ 000$
* For another $32$ points: $n \leq 1 \ 000$ and $k \leq 1000 \ 000$
* For another $20$ points: $n \leq 1 \ 000 \ 000$ and $k \leq 100 \ 000$
* For the remaining $37$ points: $n \leq 1 \ 000 \ 000$ and $k \leq 1 \ 000 \ 000$

# Example

`universitate.in`
```
11
2020 0 0
2020 0 1
2021 0 2
2021 0 4
2021 1 1
2022 0 5
2022 0 6
2023 1 4
2023 0 1
2023 1 0
2024 1 1
```

`universitate.out`
```
0 1
0 2 4
0 2 4 5 6
2 5 6 1
2 5 6
```

## Explanation

We only display the years $2020 - 2024$ for readability. For your solutions, the output file will contain all $937$ lines, even if in that year there are no students enrolled in the university.

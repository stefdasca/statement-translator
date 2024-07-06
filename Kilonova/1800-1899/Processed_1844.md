At the end of the running contest organized for the city's anniversary, the results were displayed in alphabetical order by the participants' names.
Dan wants to participate in the competition next year and, seeing the list, begins to ask himself various questions.
Question type $1$: If I had scored $x$, how many competitors would have had a strictly lower score than mine?
Question type $2$: If I had scored $x$, how many competitors would have had the same score as mine?
Question type $3$: If I had scored $x$, how many competitors would have had a strictly higher score than mine?

# Task

You will write a program that quickly answers Dan's questions.

# Input data

In the input file `intrebari.in`:
The first line contains the number of competitors, denoted by $n$, and the second line (in the order displayed by the organizers) contains the time each competitor took to complete the route, as a natural number, expressed in seconds.
The third line contains the number of questions posed by Dan, denoted by $m$.
Each of the next $m$ lines contains two natural numbers $T$ and $x$, separated by space. $T$ represents the type of question (it can be $1$, $2$, $3$) and $x$ represents the score for which information is desired.

# Output data

In the output file `intrebari.out`:
$m$ natural numbers, one per line, representing, in the order from the input, the answer for each question.

# Constraints and clarifications

* $1 \leq n \leq 100\ 000$;
* $1 \leq m \leq 100\ 000$;
* The scores obtained by competitors and the values $x$ are natural numbers between $1$ and $1\ 000\ 000\ 000$ (one billion), inclusive.
* For $18$ points, all questions are of type $1$.
* For another $18$ points, all questions are of type $2$.
* For another $18$ points, all questions are of type $3$.
* For the remaining $46$ points, the test contains questions of all types.
* For $34$ points, all numbers in the input file are at most $1\ 000$.
* For $76$ points, all numbers in the input file are less than or equal to $100\ 000$.

# Example 1

`intrebari.in`
```
5
4 1 8 1 6
3
1 3
1 4
1 10
```

`intrebari.out`
```
2
2
5
```

# Example 2

`intrebari.in`
```
5
4 1 8 1 6
3
1 3
2 4
3 10
```

`intrebari.out`
```
2
1
0
```
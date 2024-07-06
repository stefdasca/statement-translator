Here is the translated problem statement:

At a computer drawing contest, there are $n$ students participating, numbered from $1$ to $n$. Students present in the order $1$, $2$, $3$, $\\ldots$, $n$. Each student presents a drawing that is evaluated, and the jury grants a score. This represents one stage. According to this score and the scores granted so far, a provisional ranking is established. Each contestant is informed immediately after presenting their drawing, of the position they hold in the provisional ranking. The drawings are evaluated such that no two works have the same score.

# Task:

Given the number $n$ of students and the positions announced by the jury for each student (in the order they are presented in the contest), write a program that determines:
* The final ranking of the students.
* Which contestants led the ranking for the most time (multiple stages).

# Input data

The file `concurs.in` contains the natural number $n$ representing the number of students in the contest and then $n$ natural numbers representing the ranking positions announced by the jury for the $n$ contestants in the order of presentation (first for student $1$, then for student $2$, $\\dots$).

# Output data

- The first line of the output file `concurs.out` will contain the order numbers of the students, starting with the top-ranked; the numbers are separated by a space;
- The second line will contain the order number of the student who occupied the first place the most time; if there are multiple students in this situation, the order numbers of these students will be printed, separated by a space, **in ascending order**.

# Constraints and clarifications

- $n$ is a natural number, $1 < n < 30$;
- The $n$ read numbers are correct: natural numbers, from $1$ to $n$, and each number cannot be greater than its position in the sequence (the $i$-th student cannot occupy (immediately after their presentation) a place greater than $i$).
- Every student who was announced to occupy the first place will lead the ranking for at least one stage, even if they are the last student entered in the contest (see the second example).
- Partial scores will be granted as follows: for displaying the complete final ranking, $60\\%$ of the score is awarded, and for the second task in the statement, $40\\%$ of the score is awarded.

# Example 1

`concurs.in`
```
5
1 1 3 1 2
```

`concurs.out`
```
4 5 2 1 3
2 4 
```

## Explanation

* After the first student, the ranking is: $1$;
* After the second student, the ranking is: $2$, $1$;
* After the third student, the ranking is: $2$, $1$, $3$;
* After the fourth student, the ranking is: $4$, $2$, $1$, $3$;
* After the fifth student, the ranking is: $4$, $5$, $2$, $1$, $3$.
The first line displays the final ranking, and the second line displays the order numbers of the two contestants who led the ranking for the most number of stages: student $2$ led in stages $2$ and $3$, and student $4$ in stages $4$ and $5$.

# Example 2

`concurs.in`
```
3
1 1 1
```

`concurs.out`
```
3 2 1 
1 2 3
```

## Explanation

* After the first student, the ranking is $1$;
* After the second student, the ranking is $2$, $1$;
* After the third student, the ranking is $3$, $2$, $1$;
Each student led for a maximum number of stages, that is, one stage, so the order numbers of all the contestants are displayed.


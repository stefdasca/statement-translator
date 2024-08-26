# Attendance

In a group, there are $N$ students, numbered from $1$ to $N$. During roll call, they are listed in any order on the attendance sheet for that session. In the teacher's cabinet, there is a file with the total number of attendances for each student. In this file, students are listed in order from $1$ to $N$. At the end of the session, the teacher returns to the cabinet and adds a point for each present student in the order they appear on the attendance sheet. To update the file from student $i$ to student $j$ where $j > i$, the teacher moves forward in the file. However, if after student $i$, a student $j$ appears on the sheet such that $j < i$, the teacher has to backtrack in the file (because student $j$ appears earlier in the file than student $i$). The teacher dislikes backtracking in the file. When updating attendance in the computer, the teacher backtracked $K$ times. He wonders about the probability of this happening (backtracking $K$ times). Since students dislike probabilities, it is enough to find out how many ways the attendance sheet can be completed by the $N$ students such that the teacher backtracks $K$ times. Moreover, it is sufficient to display the answer modulo $10007$.

## Input data

The file `prezenta.in` contains on the first line the number $T$ of tests. Each of the next $T$ lines contains a test, given by the two natural numbers $N$ and $K$.

## Output data

The $i$-th line of the file `prezenta.out` should contain the answer to the $i$-th test: the number of ways the attendance sheet can be completed by the $N$ students such that the teacher backtracks $K$ times (modulo $10007$).

## Constraints

$1 \leq T \leq 30$

$1 \leq K < N \leq 127$

## Example

`prezenta.in`

```
2
2 1
3 1
```

`prezenta.out`

```
1
4
```
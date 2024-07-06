## In Dexter's class, there are $N$ students of distinct heights. In the sports class, they are lined up from left to right. Their teacher, Johnny, will select students positioned consecutively in the line so that the tallest student among those selected is in the first half of them.

For example, if the students have heights of 1, 5, 4 in order, the teacher can select those with heights 5 and 4, but cannot select those with heights 1 and 5. Of course, there are multiple ways to select students to meet the above condition. Johnny would like to find out in how many ways this can be done.

## Task
Given $N$ and the heights of the students in the class, find out in how many ways any number of students positioned consecutively can be selected, so that the condition from the statement is met.

## Input data
The input file `leftmax.in` contains in the first line the number $N$, and in the second line the heights of the students in the order they are lined up.

## Output data
The output file `leftmax.out` contains in the first line the answer to the task, in the form of the remainder of the division by $1\ 000\ 000\ 007$ ($\text{modulo }1\ 000\ 000\ 007$).

## Constraints and clarifications
- $1 \leq N \leq 100\ 000$
- The height of any student is an integer between $1$ and $N$, inclusive.
- If an odd number of students are selected, then the one in the middle of the selection is considered to be in the first half of the selected students.
- For 10 points, $N \leq 1\ 000$ and the students are sorted in descending order by height.
- For another 35 points, $N \leq 1\ 000$.
- For another 20 points, $N \leq 30\ 000$.

## Example 1
`leftmax.in`
```
4
1 4 2 3
```
`leftmax.out`
```
8
```
### Explanation
There are 4 ways to select one student.
There is only one way to select two students (those with heights 4, 2).
There are 2 ways to select three students (with heights 4, 2, 3 and 1, 4, 2).
There is only one way to select all 4 students.
In total, there are $8\ mod\ 1\ 000\ 000\ 007 = 8$ ways.

## Example 2
`leftmax.in`
```
7
1 2 3 4 5 6 7
```
`leftmax.out`
```
7
```
### Explanation
Only one student can be selected at a time.

## Example 3
`leftmax.in`
```
7
7 6 5 4 3 2 1
```
`leftmax.out`
```
28
```
### Explanation
Any number of students can be selected consecutively.
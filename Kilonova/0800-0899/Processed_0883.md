
In a summer camp, courses are to be held in $K$ classrooms. There are $N$ teachers who have expressed their desire to participate, each specifying the time interval [$a_i, b_i$] during which they can hold their course. The scheduling of the teachers in the classrooms must take into account the fact that at any given time, only one teacher can teach in a classroom.

# Task

Knowing that the organizers want to hold as many courses as possible, determine:

1) The maximum number of courses that can be scheduled in the $K$ classrooms, considering the indicated restriction.
2) In the desire to schedule all the courses in the $K$ classrooms, the organizers decide to modify the duration of the courses, but keep the start time unchanged. Thus, they decide that all courses will last an equal interval of time, which however will not exceed the duration of the longest course initially proposed by one of the $N$ teachers. Determine the maximum duration that the courses can have under these conditions.

# Input data

In the input file `cursuri.in`, the first line contains a natural number $C$. For all tests, $C$ can only take the values $1$ or $2$. The second line contains a pair of natural numbers $N \\ K$, separated by a space, representing the number of teachers and the number of classrooms. The next $N$ lines contain pairs of natural numbers $a_i \\ b_i$, which represent the time intervals during which the $N$ teachers will hold their courses. The numbers on each line are separated by a space.

# Output data

If the value of $C$ is $1$, only point $1$) of the task will be solved. In this case, the output file `cursuri.out` will contain on the first line a natural number representing the maximum number of courses that can be scheduled in the K classrooms, considering the indicated restriction.

If the value of $C$ is $2$, only point $2$) of the task will be solved. In this case, the output file `cursuri.out` will contain on the first line a natural number representing the maximum duration that the $N$ courses can have, so that they can all be held in the available $K$ classrooms.

# Constraints and clarifications

* $1 \\leq N \\leq 1 \\ 000$;
* $1 \\leq K \\leq 1 \\ 000$;
* $1 \\leq a_i < b_i \\leq 100 \\ 000$;
* For the second task, it is guaranteed that a solution exists for all tests.
* 45 points are awarded for a correct solution to the first task, and 45 points for a correct solution to the second task. 10 points are awarded by default.

# Example 1

`cursuri.in`
```
1
4 2
2 16
1 3
3 18
1 20
```

`cursuri.out`
```
3
```

## Explanation

An optimal scheduling variant is as follows:
- In the first classroom, the courses scheduled between $[1,3]$ and $[3,18]$ will be held.
- In the second classroom, the course scheduled between $[1,20]$ will be held.

# Example 2

`cursuri.in`
```
2
4 2
5 12
9 18
1 3
1 7
```

`cursuri.out`
```
4
```

## Explanation

The maximum duration that all the courses can have is $4$. The third course will be extended and will take place between $[1,5]$, the others will be shortened. The courses will be distributed in the two classrooms as follows:
Classroom 1: the third and first teachers scheduled between $[1,5]$ and $[5,9]$ respectively;
Classroom 2: the fourth and second teachers scheduled between $[1,5]$ and $[9,13]$ respectively;

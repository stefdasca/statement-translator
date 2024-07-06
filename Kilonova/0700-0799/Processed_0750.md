# Task

At the Hogwarts School of Wizardry, Harry Potter and his colleagues test their magic wand power. A spell consists of moving one or more objects from the school's rooms to the "wizard's room" where all the students gather.

Each of the $n$ "wizard students" is endowed with a certain power: if a student has power $1$, with a spell he brings $1$ object, if the power is $2$ with a spell he brings $2$ objects, ..., for a student with power $p$, with a spell he will bring $p$ objects. On the other hand, each student has a certain speed in performing spells. Thus, during an hour, a student with speed $1$ will manage to make a single spell, a student with speed $2$ will manage two spells one after another, etc. Obviously, a student with power $3$ and speed $4$, will manage to bring up to $12$ objects by the end of the hour ($3$ at the first spell, another $3$ at the second spell, another $3$ at the third spell, and another $3$ at the last spell).

By the end of the hour of wizardry, each student receives a number of boxes to pack only the objects he brought so that each of his boxes contains the same number of objects. Professor Dumbledore also wants each student to receive the same number of boxes. A simple solution would be to distribute one box to each student, but he would like to distribute as many boxes as possible.

# Task

Knowing for each of the $n$ "wizard students" at Hogwarts, the power he is endowed with and the speed with which he manages to make spells, determine:

1. the largest number of objects that can be brought by the end of the hour by a single "wizard student";
2. the maximum number of boxes that each student will receive considering that each student must distribute his objects evenly in these boxes.

# Input data

From the input file `vraji.in` read on the first line the natural number $n$, representing the number of students. From the next $n$ lines, read the information about the students, one student per line, in the form of two numbers separated by a space, representing the student's power and speed.

# Output data

The output file `vraji.out` will contain on the first line the largest number of objects that can be brought to the "wizard's room" by a single "wizard student" by the end of the hour. On the second line, the maximum number of boxes that each student can receive considering the conditions in the problem.

# Constraints and clarifications

* The number $n$ of students, their power, and their speed are natural numbers greater than $0$ and less than or equal to $100$.
* Each box will contain only objects of a single "wizard student".
* Each student will receive the same number of boxes.

# Example 1

`vraji.in`
```
5
5 2
6 4
3 10
20 2
7 2
```

`vraji.out`
```
40
2
```

## Explanation

There are $5$ "wizard students":

- student $1$: The total number of objects is $5 \cdot 2 = 10$;
- student $2$: The total number of objects is $6 \cdot 4 = 24$;
- student $3$: The total number of objects is $3 \cdot 10 = 30$;
- student $4$: The total number of objects is $20 \cdot 2 = 40$;
- student $5$: The total number of objects is $7 \cdot 2 = 14$.

$40$ is the largest number of objects brought by a wizard student.
$2$ is the maximum number of boxes that each student can receive.

# Example 2

`vraji.in`
```
3
4 2
6 8
6 6
```

`vraji.out`
```
48
4
```

## Explanation

There are $3$ "wizard students":

- student $1$: The total number of objects is $4 \cdot 2 = 8$;
- student $2$: The total number of objects is $6 \cdot 8 = 48$;
- student $3$: The total number of objects is $6 \cdot 6 = 36$.

$48$ is the largest number of objects brought by a wizard student.
$4$ is the maximum number of boxes that each student can receive.
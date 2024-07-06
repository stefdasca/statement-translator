Here is the translated text:

~~~markdown
The $N$ students of a class have decided to form a "wireless telephone". For this, the students have been numbered from $1$ to $N$, and then each student chose a single colleague (we will call him neighbor), the only one to whom he will be able to directly transmit the received messages. The wireless telephone works as follows:

- Initially, a student sends a message (obviously, only to his neighbor);
- Each student who received the message (directly or indirectly), transmits the received message further to his neighbor.

The wireless telephone works correctly if any student starts sending a message, it will reach every one of the $N$ students (including back to the student who initiated the message transmission). The students observed that their wireless telephone does not work correctly. To make the wireless telephone work correctly, they think of making a series of changes. With a change, a student can change his chosen neighbor.

# Task

Determine a sequence with the minimum number of changes, after which the wireless telephone will work correctly.

# Input data

The first line of the input file `telefon.in` contains the natural number $N$, representing the number of students. The second line contains $N$ natural numbers, separated by a space; the $i$-th number represents the neighbor chosen by child $i \\ (1 \\leq i \\leq N)$.

# Output data

The first line of the output file `telefon.out` will contain a natural number $k$, representing the minimum number of changes needed for the wireless telephone to work correctly. On the next $k$ lines, the sequence of changes made will be written, one change per line. A change is specified by two natural numbers separated by space, $c \\ v$, meaning that student $c$ changes his neighbor, the new neighbor being $v$.

# Constraints and clarifications

* $1 < N \\leq 100 \\ 000$
* If there are multiple solutions, you can display any of them.
* For $30\\%$ of the tests, it is guaranteed that each student will be chosen as a neighbor by another student
* For another $30\\%$ of the tests, at least one student will receive the message transmitted by any student (directly or indirectly), including himself.
* For another $20\\%$ of tests $N \\leq 1 \\ 000$
* Partial scores will be awarded as follows:
    * $30\\%$ of the score for each test represents the minimum number of changes
    * The remaining $70\\%$ for reconstructing the solution

# Example 1

`telefon.in`
```
10
6 9 2 7 3 1 9 3 7 9
```

`telefon.out`
```
5
2 4
6 10
8 5
9 1
10 8
```
~~~
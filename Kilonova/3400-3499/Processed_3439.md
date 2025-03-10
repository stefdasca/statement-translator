
~[taxscam.jpg|align=right|width=30%]

Baiatu' Bombonel has just finished setting up the curriculum for the Scam School. The first lesson in the Scam School curriculum is that to be a successful scammer, you must know how not to get scammed. To teach this introductory lesson, Baiatu' Bombonel promised to place as many students as friends with each other in a classroom. However, being an expert scammer, Baiatu' Bombonel wants to scam them to the maximum; he wants to place as many students in a classroom as possible who do not know each other. Each of the $N$ students is identified by a binary string of length $M$, and students $i$ and $j$ are considered friends if and only if their IDs differ by exactly one bit.

# Task

Given $N$, $M$, and the $N$ IDs of the students, determine the maximum number of students Baiatu' Bombonel can place in a classroom such that none of them knows any other student in the classroom.

# Input data

The first line contains the numbers $N$ and $M$, representing the number of students and the length of the IDs, respectively.  
Each of the following $N$ lines contains a binary string of length $M$, representing the IDs of the students.

# Output data

Print the maximum number of students Baiatu' Bombonel can put in a classroom, with the condition that none of them knows any other student in the classroom.

# Constraints and clarifications

* $1 \leq N, M \leq 1 \ 000$;
* For tests worth $10$ points, $N \leq 17, M \leq 10$;
* For other tests worth $10$ points, $N \leq 17, M \leq 1\ 000$;
* For other tests worth $30$ points, $N \leq 1\ 000, M \leq 30$;
* Each of the $N$ students has distinct IDs.

# Example 1

`stdin`
```
4 4
0000
1100
0011
1111
```

`stdout`
```
4
```

## Explanation

Since none of the students are friends with each other, we can put them all in the same classroom.

# Example 2

`stdin`
```
4 4
0000
1100
0011
1000
```

`stdout`
```
3
```

## Explanation

We can place students $0$, $1$, and $2$ in the same classroom and leave $3$ out.

Ana and Bogdan found a box with $N$ sticks of the same length at their grandfather's place. After playing for a few minutes, they started to argue. Their grandfather suggested breaking the $N$ sticks, with Ana receiving the fragments in the left hand and Bogdan the ones in the right hand. Said and done. The children took the fragments, numbered them from $1$ to $N$, measured them, and now they wish to glue the received fragments together, but they need some additional information.

# Task

Knowing $N$ (the number of sticks), $A_1$, $A_2$, ..., $A_N$ (the lengths of fragments received by Ana) and $B_1$, $B_2$, ..., $B_N$ (the lengths of fragments received by Bogdan), write a program to determine:

* the initial length of the sticks;
* the length of the longest stick that can be obtained by gluing a fragment belonging to Ana to a fragment belonging to Bogdan;
* the number of sticks of maximum length that can be obtained by gluing a fragment belonging to Ana to a fragment belonging to Bogdan.

# Input data

The input file `bete.in` contains the following:
On the first line, it contains the natural number $N$ representing the number of sticks. 
On the second line, it contains $N$ natural numbers $A_1$, $A_2$, ..., $A_N$ representing the lengths of the fragments received by Ana. 
On the third line, it contains $N$ natural numbers $B_1$, $B_2$, ..., $B_N$ representing the lengths of the fragments received by Bogdan.

# Output data

The output file `bete.out` will contain three lines. 
The first line will contain the natural number $L$ representing the initial length of the sticks. 
The second line will contain the natural number $K$ representing the length of the longest stick that can be obtained by gluing a fragment belonging to Ana to a fragment belonging to Bogdan. 
The third line will contain the natural number $P$ representing the number of sticks of maximum length that can be obtained by gluing a fragment belonging to Ana to a fragment belonging to Bogdan.

# Constraints and clarifications

* $1 \leq N \leq 1\ 000$;
* $1 \leq A_i \leq 10\ 000$;
* $1 \leq B_i \leq 10\ 000$;
* $1 \leq L \leq 20\ 000$;
* $1 \leq K \leq 20\ 000$;
* $1 \leq P \leq 1\ 000$;
* Once two fragments are glued, they cannot be separated.
* Determining the correct value of L will yield 30% of the points, determining the correct value of K will yield 30% of the points, and determining the correct value of P will yield 40% of the points.

# Example

`bete.in`
```
6
2 6 7 1 3 5
5 4 7 8 9 3
```

`bete.out`
```
10
16
1
```

## Explanation

The initial length is $10$, the maximum length is $16$, and a single stick of length $16$ can be formed.


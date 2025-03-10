
# Task

At the parade organized for the national day, the students of the military high schools from the cities $A$ and $B$ were initially arranged in column in increasing order of their heights (one column with students from city $A$ and one with students from city $B$). Subsequently, they are to be rearranged so that they form a single column that fulfills the following conditions:
- The students should be arranged in increasing order;
- Any two students should maintain their relative order from the initial arrangement (if students $x$ and $y$ were in the same city and $x$ was placed before $y$, in the merged column, $x$ must also be before $y$, obviously not necessarily immediately before).

You are asked to calculate the number of rearrangement variants. Two variants differ if there is at least one position where in the first variant a student $n$ was placed and in the second variant a different student was placed.

# Input data

The first line of the file `parada.in` contains a number $n$ representing the number of students from city $A$. The second line contains $n$ positive natural numbers, separated by spaces, in increasing order, representing the heights of the students from city $A$. The third line contains a number $m$ representing the number of students from city $B$. The fourth line contains $m$ positive natural numbers, separated by spaces, in increasing order, representing the heights of the students from city $B$.

# Output data

The file `parada.out` will contain the remainder when the requested value is divided by $1 \ 000 \ 000 \ 007$.

# Constraints and clarifications

* $1 \leq n, m \leq 2 \ 000$;
* The heights of the students are positive natural numbers of at most $9$ digits.
* For tests worth $66$ points, the heights are positive natural numbers of at most $6$ digits;
* For tests worth $34$ points, the numbers representing the heights of the students have at least $8$ digits;
* For tests worth $33$ points, the students from the same city have distinct heights.

# Example 1

`parada.in`
```
5
1 3 3 3 4
3
3 3 5
```

`parada.out`
```
10
```

## Explanation

1(A1) 3(A2) 3(A3) 3(A4) 3(B1) 3(B2) 4(A5) 5(B3)  
1(A1) 3(A2) 3(A3) 3(B1) 3(A4) 3(B2) 4(A5) 5(B3)  
1(A1) 3(A2) 3(B1) 3(A3) 3(A4) 3(B2) 4(A5) 5(B3)  
1(A1) 3(B1) 3(A2) 3(A3) 3(A4) 3(B2) 4(A5) 5(B3)  
1(A1) 3(A2) 3(A3) 3(B1) 3(B2) 3(A4) 4(A5) 5(B3)  
1(A1) 3(A2) 3(B1) 3(A3) 3(B2) 3(A4) 4(A5) 5(B3)  
1(A1) 3(B1) 3(A2) 3(A3) 3(B2) 3(A4) 4(A5) 5(B3)  
1(A1) 3(A2) 3(B1) 3(B2) 3(A3) 3(A4) 4(A5) 5(B3)  
1(A1) 3(B1) 3(A2) 3(B2) 3(A3) 3(A4) 4(A5) 5(B3)  
1(A1) 3(B1) 3(B2) 3(A2) 3(A3) 3(A4) 4(A5) 5(B3)

# Subway

We live in a strange world, where subway stations are even stranger. And as strange as they are, they are just as crowded. Because of the crowd, we need your help to bring order to the masses. A subway has $N$ doors. When the subway arrives at the station, we know that at each door $i$, located at position $x[i]$ on the Ox axis $(1 \leq i \leq N)$, there are $a[i]$ people who want to enter the subway and $b[i]$ people who want to exit the subway. The only problem is that, due to new rules, a door can either be used for entering or exiting, one of these actions being always prohibited. None of the people who either want to enter the subway or exit know whether the door they are at is for entry or exit. For example, if door $i$ at position $x[i]$ $(1 \leq i \leq N)$ is for entry, the $b[i]$ people at this door will need to move to the nearest exit door to get off at this station. It is also known that the effort of a person moving from door $i$ to door $j$ is $\|x[i] - x[j]\|$ $(1 \leq i, j \leq N)$. Given the number $N$ of doors, their positions on the Ox axis, and the number of people who want to enter and exit the subway at each door, determine the minimum effort expended by people for moving as a result of entering and exiting the subway.

## Input data

In the input file `subway.in`, the first line contains the natural number $N$, representing the number of doors of the subway. The second line contains the values of the array $x$, where $x[i]$ represents the position of door $i$. The third and fourth lines contain the values of the arrays $a$ and $b$, respectively, representing the number of people who want to enter and exit the subway through its doors.

## Output data

In the output file `subway.out`, the first and only line contains a single natural number representing the minimum effort expended by people to achieve their goal (enter/exit the subway).

## Constraints and clarifications

$2 \leq N \leq 2000$

$0 \leq x[i] \leq 100\ 000$

$1 \leq a[i], b[i] \leq 1\ 000$

The elements of the array $x$ are in ascending order.

It is guaranteed that the answer fits in a signed 32-bit integer.

## Example

`subway.in`
```
4
1 3 4 5
1 2 3 5
2 3 3 1
```

`subway.out`
```
9
```

## Explanation

The first and third doors will be for exiting, and the second and fourth doors for entering.

The effort expended by people who want to enter is $1*2 + 2*0 + 3*1 + 5*0 = 5$

The effort expended by people who want to exit is $2*0 + 3*1 + 3*0 + 1*1 = 4$

The total effort is $4 + 5 = 9$
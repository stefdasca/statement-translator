## Task

A group of $N$ students came to college to take an exam, and there are 3 available rooms where they can be allocated. Each student has a certain height and weight. Thus, each student $i$ has height $H_i$ and weight $G_i$. The challenge is to allocate the students to the rooms as balanced as possible. In each room, at least one student must be allocated, and obviously, each student must be allocated to exactly one room. Let $S1$, $S2$, and $S3$ be the three rooms where the students are allocated. An allocation is more balanced if the value $[Gmax(S1)+Gmax(S2)+Gmax(S3)]*[Hmax(S1)+Hmax(S2)+Hmax(S3)]$ is smaller (let's call this value the balance of an allocation). $Gmax(S_i)$ represents the maximum weight of a student in room $S_i$, and $Hmax(S_i)$ represents the maximum height. Determine the minimum possible balance of an allocation.

## Input data

The input file studenti.in contains a single line which contains the number $N$ as described above. Following that are $N$ lines, where the $i+1$ line contains the values $H_i$ and $G_i$, separated by a space.

## Output data

The output file studenti.out will contain a single line that prints the minimum possible balance of an allocation.

## Constraints and clarifications

$3 \leq N \leq 300$

All heights of the students are different from each other

All weights of the students are different from each other

$1 \leq H_i, G_i \leq 2000$

## Example

`studenti.in`
```
3
1 1
2 2
3 3
```

`studenti.out`
```
36
```

## Explanation

There is only one possibility of placing one student in each room, and the balance obtained is $(2+3+1)*(2+3+1) = 36$.
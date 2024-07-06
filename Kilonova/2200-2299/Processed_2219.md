# Task

Liceul de Cultură Generală nr. $2$ din Dorohoi organizes a team competition. Each team must be composed of $K$, $3 \leq K \leq 4$ students from consecutive generations: one 9th-grade student (generation $0$), one 10th-grade student (generation $1$), one 11th-grade student (generation $2$), and optionally one 12th-grade student (generation $3$), if the latter is not busy with the baccalaureate. Interestingly, all classes in the high school are composed of $N$ students each, $1 \leq N \leq 2\ 000$.

The competition organizers have measured each student's intelligence accurately and observed that no two students have the same intelligence level in the entire school. Each student received an ID ranging between $1$ and $N \cdot K$. Thus, if a child $a$ is more intelligent than a child $b$, then $ID(a) > ID(b)$. They also observed that no student wants to be in the same team with a more intelligent student from a younger generation, as they would feel bad (in a figurative sense). The organizers wonder in how many ways $T$ teams of $K$ students can be chosen, so that every student of the high school is part of at most one team.

Formally, let $K$ sequences of $N$ elements $ID_0, ID_1, \dots, ID_{k-1}$, representing the IDs of students from the $K$ generations, respectively. It is required to count in how many ways $T$ teams of the form $(e_{i,0}, e_{i,1}, \dots, e_{i,K-1})$, $0 \leq e_{i,j} \leq N-1$ for any $0 \leq i \leq T-1$, $0 \leq j \leq K-1$ can be chosen. All teams must respect the property $ID_{j, e_{i,j}} < ID_{j+1, e_{i,j+1}}$, for any $0 \leq i \leq T-1$, $0 \leq j \leq K-2$. Additionally, no student can appear in more than one team. Two ways of choosing teams are considered distinct if there is at least one team that appears in one way and not in the other.

# Input data

The input file `teams.in` has the following structure:

* line $1$: $K \ N \ T$, representing the number of generations, the number of students from each generation, and the number of teams that need to be formed.
* line $2 + i$: $ID_{i,0} \ ID_{i, 1} \dots ID_{i,N-1}$, $(0 \leq i \leq K-1)$

# Output data

The first line of the output file `teams.out` will contain a single integer, the number of teams that can be formed modulo $6 \ 700 \ 417$

# Constraints and clarifications

* $3 \leq K \leq 4$;
* $1 \leq T, N \leq 2\ 000$;

|#|Score|Constraints|
|-|-|--------|
|1|6|$1 \leq T \leq N \leq 5$, $K = 3$|
|2|6|$1 \leq T \leq N \leq 20$, $K = 3$|
|3|31|$1 \leq T \leq N \leq 40$, $K = 3$|
|4|16|$1 \leq T \leq N \leq 300$, $K = 3$|
|5|16|$1 \leq T \leq N \leq 2000$, $K = 3$|
|6|16|$1 \leq T \leq N \leq 25$, $K = 4$|
|7|9|$1 \leq T \leq N \leq 300$, $K = 4$|

# Example 1

`teams.in`
```
3 3 2
5 4 2
7 1 3
6 8 9
```

`teams.out`
```
8
```

## Explanation

The IDs of the students from the $8$ solutions in the first example are:

$(5, 7, 8)$ and $(2, 3, 6)$
$(5, 7, 8)$ and $(2, 3, 9)$
$(5, 7, 9)$ and $(2, 3, 6)$
$(5, 7, 9)$ and $(2, 3, 8)$
$(4, 7, 8)$ and $(2, 3, 6)$
$(4, 7, 8)$ and $(2, 3, 9)$
$(4, 7, 9)$ and $(2, 3, 6)$
$(4, 7, 9)$ and $(2, 3, 8)$

# Example 2

`teams.in`
```
4 3 1
2 1 4
3 7 5
11 6 10
9 8 12
```

`teams.out`
```
31
```

# Example 3

`teams.in`
```
3 8 8
1 2 3 4 5 6 7 8
9 10 11 12 13 14 15 16
17 18 19 20 21 22 23 24
```

`teams.out`
```
4201486
```
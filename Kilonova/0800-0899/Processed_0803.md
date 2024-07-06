Ilinca is a girl who loves to draw very much; she has made many drawings that she has numbered from $1$ to $d$ and then multiplied them (all the copies bear the same number as the original from which they were made). During the holiday, she decided to open her own exhibition on her grandparents' fence, which has multiple boards; on each board, she places a panel (an original drawing or a copy). Ilinca cares very much about her drawings and wants each drawing to appear at least $k$ times (using the original and its copies). Ilinca wonders in how many ways the exhibition can be arranged. Two ways of arranging are considered distinct if they differ at least by the number of one panel (for example: $2 \\ 1 \\ 3 \\ 3$ is the same exhibition as $2 \\ 3 \\ 1 \\ 3$, but different from $2 \\ 1 \\ 3 \\ 1$ and $1 \\ 3 \\ 3 \\ 1$).

# Task

Given $n$ — the number of boards on the fence, $d$ — the number of original drawings, and $k$ — the minimum number of appearances of each drawing, determine in how many ways the exhibition can be arranged, knowing that Ilinca has as many copies as she wants at her disposal.

# Input data

The input file `expozitie.in` will contain 3 numbers, $n$, $d$, $k$ — the number of boards, the number of original drawings, and the minimum number of appearances.

# Output data

The output file `expozitie.out` will contain a single number — the number of distinct ways to arrange the exhibition.

# Constraints and clarifications

* $n$, $k$, $d$ are natural numbers
* $1 \leq n \leq 500$
* $1 \leq d \leq 500$
* $0 \leq k \leq n$

# Example

`expozitie.in`
```
3 2 1
```

`expozitie.out`
```
2
```

## Explanation

There are $3$ boards, $2$ original drawings, and each drawing must appear at least once. There are $2$ ways to arrange the panels. The panels could be arranged as follows:
1. $1 \\ 2 \\ 1$
2. $1 \\ 2 \\ 2$

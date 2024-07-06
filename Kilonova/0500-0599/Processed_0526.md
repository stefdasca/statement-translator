At a special lottery draw, $M$ distinct numbers are drawn from the set $\{1, 2, 3, ..., 49\}$. A person playing this game writes $K$ distinct numbers on a ticket from the 49 possible numbers. The categories of winnings are as follows in descending order of prize value (category 1 is the most valuable):
* category **1**: $K$ numbers written on the ticket match the first $K$ drawn officially;
* category **2**: $K$ numbers written match any of the $M$ numbers drawn officially;
* category **3**: $K-1$ numbers written match the first $K-1$ numbers drawn officially;
* category **4**: $K-1$ numbers written match the first $K$ numbers drawn officially;
* category **5**: $K-1$ numbers written match any of the $M$ numbers drawn officially;
* category **6**: $K-2$ numbers written match any of the $M$ numbers drawn officially.

During the draw, $J$ players bought tickets. **A player wins in the most valuable category they qualify for.**

# Task

Write a program to determine:
1. The number of players who win for a specific prize category $C$. The categories are numbered $\{1, 2, \ldots, 6, 7\}$. Category 7 is intended for non-winners.
2. The numbers that are chosen by the maximum number of players, written in ascending order.

# Input data

The input file `loto.in` contains the task (1 or 2) on the first line. The second line contains the numbers $M \ K \ C$ separated by a space. The third line contains, in the order they were drawn, the $M$ official numbers drawn, separated by a space. The fourth line contains a natural number $J$, representing the number of players, and each of the next $J$ lines contains $K$ natural numbers, in the order they were played, representing the numbers chosen and written on the ticket by the $J$ people.

# Output data

For task $1$, the output file `loto.out` will contain on the first line a natural number, representing the number of winners for the prize category $C$.
For task $2$, the output file `loto.out` will contain on the first line the numbers chosen by the maximum number of players, written in ascending order, separated by a space.

# Constraints and clarifications
* $1 \leq M \leq 49$;
* $5 \leq K \leq M$;
* $1 \leq C \leq 7$;
* $1 \leq J \leq 1\ 000$;
* For task $1$, 70 points are awarded, and for task $2$, 30 points are awarded;
* For 15 points, $1 \leq J \leq 10$;
* For 30 points, $11 \leq J \leq 100$;
* For 55 points, $101 \leq J \leq 1\ 000$;

# Example 1

`loto.in`
```
1
6 5 1
1 2 3 4 5 6
1
5 4 3 2 1
```

`loto.out`
```
1
```

## Explanation

Task $1$. At the official draw, $6$ numbers were drawn. Players can complete $5$ numbers. The official numbers drawn are, in order, $1 \ 2 \ 3 \ 4 \ 5 \ 6$. There is only one player. They wrote the numbers $5 \ 4 \ 3 \ 2 \ 1$ on their ticket. The person who played won in category $1$ because they wrote the first $5$ numbers drawn officially.

# Example 2

`loto.in`
```
1
6 5 4
1 2 3 4 5 6
2
9 1 5 3 2
3 1 5 2 4
```

`loto.out`
```
1
```

## Explanation

Task $1$. There are $2$ players. One of the players won in category $1$ and one won in category $4$. We are asked for the number of winners in category $4$, so $1$.

# Example 3

`loto.in`
```
1
6 5 7
1 2 3 4 5 6
3
2 33 7 8 19
21 3 47 8 29
12 32 17 8 39
```

`loto.out`
```
3
```

## Explanation

Task $1$. There are $3$ players. None of those who played won in any category.

# Example 4

`loto.in`
```
2
6 5 4
1 2 3 4 5 6
2
9 1 5 3 2
3 1 5 2 4
```

`loto.out`
```
1 2 3 5
```

## Explanation

Task $2$. The numbers $1 \ 2 \ 3 \ 5$ were written by both people, so the maximum number of players is $2$.
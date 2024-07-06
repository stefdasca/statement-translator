An art exhibition is organized in a circular building consisting of $N + 1$ rooms numbered from $0$ to $N$ counterclockwise. Initially, all rooms are empty. The first room is numbered $0$ and in it $Y$ people enter every minute. The next $N$ rooms have exit doors. From room $i$, $1 \leq i \leq N$ will exit $x_i$ people every minute, but only if there are at least $x_i$ people in that room. After people enter room $0$ and possibly leave the other rooms, in the same minute, all remaining people in the exhibition move to the next room. More precisely, if a person is in room $i \leq N - 1$, then they move to room $i + 1$, and if they are in room $N$ then they move to room $0$.

# Task

Write a program that for known numbers $N$, $Q$, $y$ and the known sequence $x_i$, $1 \leq i \leq N$, answers questions of the form: "How many people are after $t$ minutes in room $s$?".

# Input data

The input file `expozitie.in` contains on the first line the numbers $N$, $Q$ and $y$. The second line will contain $N$ numbers separated by a space representing the elements of the array $x$. The following $Q$ lines will describe the $Q$ questions and will contain two numbers $t$ and $s$ separated by space representing a number of minutes and a corresponding room number for a question.

# Output data

The output file `expozitie.out` will contain $Q$ lines. On these lines, there will be the answers to the $Q$ questions in the order they appear in the input file.

# Constraints and clarifications

* $1 \leq N \leq 1 \ 000$;
* $1 \leq Q \leq 1 \ 000 \ 000$;
* $1 \leq y \leq 1 \ 000$;
* $1 \leq x_i \leq 100$;
* $0 \leq s \leq N$ for each question;
* $1 \leq t \leq 1 \ 000 \ 000 \ 000$ for each question;

# Example

`expozitie.in`
```
3 5 4
3 2 2
1 2
4 1
6 2
5 1
4 0
```

`expozitie.out`
```
0
4
2
5
1
```

## Explanation

Starting at minute $1$, the distributions in the $4$ rooms will be as follows:

```
0 4 0 0
0 4 1 0
0 4 1 1
1 4 1 1
1 5 1 1
1 5 2 1...
```
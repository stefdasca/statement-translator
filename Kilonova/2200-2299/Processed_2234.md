Certainly! Here is the translated competitive programming problem statement:

---

A long time ago, in the Land of Friendship, every person had all the other people as friends. Now, when envy is everywhere, there are divergences between people. More exactly, there are $N$ numbered persons from $1$ to $N$ and $M$ pairs of two numbers representing two people who are quarreled. Two people are considered to be in a friendship relationship if they are not quarreled.

After a stormy night, each of the $N$ persons wants to move to the house of a friend, such that exactly one person moves into each house. Also, they do not want any pair of friends to exchange places (if $A$ moves to $B$'s house, then $B$ should not move to $A$'s house).

# Task

Given $T$ lands of the type Friendship and knowing for each land: $N$ – the number of persons and $M$ – the number of pairs of quarreled people, determine for each person the number of the friend in whose house they move.

# Input data

The input file `amici.in` contains the number $T$ on the first line, and on the following lines each land will be described separately. The description of each land starts with a line containing $N$ and $M$, and on the next $M$ lines there are two natural numbers $A$ and $B$ representing that people $A$ and $B$ are quarreled.

# Output data

The output file `amici.out` contains $T$ lines, one for each land from the input file. If there is a solution, on the $i$-th line there will be $N$ distinct numbers. The $k$-th number represents the friend in whose house person $k$ moves. If there is no solution, $-1$ will be written (quotes are for clarity).

# Constraints and clarifications

* $1 \leq T \leq 13$
* $3 \leq N \leq 1\ 000$
* It is guaranteed that a person is quarreled with less than half of the total number of persons.
* If there are multiple solutions, any of them can be shown.
* For $15\\%$ of the tests $N \leq 13$.
* For another $25\\%$ of the tests $N \leq 300$.

# Example

`amici.in`
```
2
6 0
7 1
1 2
```

`amici.out`
```
2 5 6 3 1 4
3 4 2 1 6 7 5
```

---

I have reviewed and corrected any grammatical or syntactic errors according to the rules of the English language.
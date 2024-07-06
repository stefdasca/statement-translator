# Task

Football is considered the king of sports, having approximately $3.5$ billion fans. Among these fans is a child named Messi, who is only six years old. His friend Ronaldo, who is two years older, taught him both the rules of the game and how to calculate the teams' scores in the league. Ronaldo explained that for each match won, the team receives $3$ points, for each lost match the team receives no points, and for matches that end in a draw, the team receives $1$ point. After explaining the rules, Ronaldo wants to check if Messi understood with an example.

# Task

Given the number of teams and for each team the number of matches won, the number of matches lost, and the number of matches drawn, determine, based on the parity of $n$, two results: if the number of teams is even, find the highest score among all teams; and if the number of teams is odd, find the smallest number of matches lost.

# Input data

The input file `fotbal.in` contains on the first line the natural number $n$, representing the total number of teams in the league. The following $n$ lines contain triplets of natural values $(c, p, e)$, representing:
- $c$ — the number of matches won;
- $p$ — the number of matches lost;
- $e$ — the number of matches that ended in a draw.

# Output data

The output file `fotbal.out` will contain on one single line one of the following values:
- The highest score obtained, if $n$ is an even number;
- The smallest number of matches lost, if $n$ is an odd number (a lost match count of $0$ will not be considered).

# Constraints and clarifications

* $n \leq 10 \ 000$
* $c, p, e \leq 10 \ 000$

# Example 1

`fotbal.in`
```
4
10 2 3
5 5 5
12 3 0
12 1 2
```

`fotbal.out`
```
38
```

## Explanation

According to the rules, we have the following scores: $33$, $20$, $36$, $38$. The highest score is $38$.

# Example 2

`fotbal.in`
```
5
1 2 3
3 2 1
0 1 5
1 0 5
0 6 0
```

`fotbal.out`
```
1
```

## Explanation

The smallest number of matches lost is $1$ (team $4$ has $0$ lost matches, which is very good for them, but it is not considered for calculating the minimum number of matches lost).
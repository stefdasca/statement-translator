# Task

At Iulia's school, in the 5th grade, there are $n$ students. Because this is the trend at this school, each of the $n$ students has created a club. Each club initially has only one member: the student who created it. The students decided that the number of members in a club can increase by merging with another club according to the following rule: two clubs can merge if they have the same number of members. By merging, one of the clubs continues to exist, and the other one ceases to exist. The club that continues to exist takes over all the members of the club that ceases to exist.
Since students have more fun when the club has more members, they decided to merge the clubs according to the above rule as long as merging is possible.

# Task

Write a program that reads the natural number $n$ and determines:

1. the smallest natural number $k$ of clubs that continue to exist after all possible mergers have occurred;
2. for each of the clubs, the number of members.

# Input data

The input file `cluburi.in` contains a single line which contains a single non-zero natural number $n$, representing the number of students in the 5th grade.

# Output data

The output file `cluburi.out` will contain:

* the first line will contain a natural number $k$, representing the smallest number of clubs that continue to exist after all possible mergers
* the second line will contain $k$ non-zero natural numbers, separated by a space, representing the number of members in each club, in ascending order of the number of members.

# Constraints and clarifications

* $1 \leq n \leq 30 \ 000$
* If the number of students is odd, the remaining student is considered to form a club on their own.
* For each input test, at least one club can be determined.
* Partial scoring is given: task $1$, $30\%$ of the score, and for task $2$, $70\%$ of the score.

# Example 1

`cluburi.in`
```
7
```

`cluburi.out`
```
3
1 2 4
```

## Explanation

$6$ students form $3$ clubs, each having $2$ members, and the remaining student also forms a club (with one member).
Then $2$ of the clubs with $2$ members each merge and form a single club with $4$ members, so there are $3$ clubs: $1$ with one member, $1$ with $2$ members, and $1$ with $4$ members.

`cluburi.in`
```
24
```

`cluburi.out`
```
2
8 16
```

## Explanation

Initially, $12$ clubs are formed with $2$ members each, then $6$ with $4$ members each.
From the $6$ clubs, $3$ of them are formed with $8$ members each.
Two of the clubs with $8$ members merge to form one with $16$ members. Finally, there are $2$ clubs left, one with $8$, and the other with $16$ members.
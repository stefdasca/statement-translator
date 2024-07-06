~[partitura.png|align=right|width=25%]

Mihai has finally decided to compose a melody. Without knowing where to start, he wrote $n$ musical notes on a sheet. Each musical note is defined by two values representing its duration and pitch as follows:
* **duration** is expressed as a fraction of the form $\\displaystyle \\frac{1}{2^x}$, where $x$ is a non-zero natural number;
* **pitch** is expressed by a non-zero natural number $y$.

The duration of a group of notes is equal to the sum of the durations of the notes in the group. To compose a musically correct melody, he must distribute all the notes into disjoint groups such that the duration of each group is $1$. Mihai defines the **score of a group** of notes as the sum of the pitches of all the notes in the group, squared. He also defines the **score of a melody** as the sum of the scores of all the formed groups of notes.

Mihai wants to find out what the maximum score of a melody he can achieve is after grouping all the given notes.

# Task

Given $n$ notes in the form of $n$ pairs of numbers, $x$ and $y$, display the maximum score that can be obtained after grouping all the given notes into disjoint groups.

# Input data

The input file `partitura.in` will contain on the first line a natural number $n$, representing the number of notes, and on the following $n$ lines will contain two natural numbers $x$ and $y$ separated by a space with the meaning from the statement, for each of the $n$ notes.

# Output data

The output file `partitura.out` will contain a single natural number representing the required maximum score.

# Constraints and clarifications
* $1 \\leq n \\leq 300\\ 000$;
* $1 \\leq x \\leq 18$;
* $1 \\leq y \\leq 10\\ 000$;
* It is guaranteed that all given notes can be distributed into groups of duration $1$.
* For $20$ points, $n \\leq 4$, $x = 1$;
* For $22$ points, $x = 1$;
* For $17$ points, for all notes, $x$ has the same value;
* For $41$ points, there are no additional restrictions.

# Example 1

`partitura.in`
```
5
2 3
3 2
2 1
2 2
3 5
```

`partitura.out`
```
169
```

## Explanation

To determine the maximum score of a melody, the only possible solution is obtained by forming a single group.

This group is formed from all the notes and has a duration of $\\displaystyle \\frac{1}{2^2}+\\frac{1}{2^3}+\\frac{1}{2^2}+\\frac{1}{2^2}+\\frac{1}{2^3}=1$ and the score $(3+2+1+2+5)^2 = 169$.

The score of the melody is also $169$.

# Example 2

`partitura.in`
```
6
1 3
2 2
1 4
2 2
2 2
2 2
```

`partitura.out`
```
113
```

## Explanation

To determine the maximum score of a melody, a possible solution is obtained by forming two groups.

The first group is formed from the first, second, and fourth notes and has a duration of $\\displaystyle \\frac{1}{2}+\\frac{1}{2^2}+\\frac{1}{2^2}=1$ and a score of $(3+2+2)^2=49$.

The second group is formed from the third, fifth, and sixth notes and has a duration of $\\displaystyle \\frac{1}{2}+\\frac{1}{2^2}+\\frac{1}{2^2}=1$ and a score of $(4+2+2)^2=64$.

The score of the melody is $49+64=113$ and it is the maximum that can be obtained for these notes.

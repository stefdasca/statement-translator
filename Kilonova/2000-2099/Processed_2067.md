```markdown
# Task

Advent of Code 2023 has begun and has already proven to be a huge success. To experiment with the format, Vlad and Ștefan decided to try out different settings regarding the number of participants and days.

Practically, it is known that there are $n$ participants and $m$ days of the contest. Each day, we know how many participants solved the problem and the order in which they solved it.

On a given day, the first participant to solve the problem receives $n$ points, the second receives $n-1$ points, and so on. It does not matter if not all participants solve the problem on a given day.

The final ranking is to be determined. In case of a tie, participants with a lower order number will be displayed first.

# Input data

The first line contains $n$ and $m$, representing the number of participants and days.

On the next $m$ lines, the days will be displayed. Each day, first, the number of participants who solved the problem is read, and then the order in which the participants solved the problem.

# Output data

The first line will contain the final ranking, in decreasing order of the final score.

In case of a tie between two or more participants, they will be displayed in ascending order of their order number.

# Constraints and clarifications

* $1 \leq n \leq 100$
* $1 \leq m \leq 1000$

# Example

`stdin`
```
4 5
4 1 2 3 4
2 4 2
3 3 1 2
4 4 1 2 3
1 2
```

`stdout`
```
2 1 4 3
```
```
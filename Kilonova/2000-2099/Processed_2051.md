```markdown
# Task

In this version of the problem, $n = 1$.

In a country at the edge of the world, the government has discovered that there is a real problem concerning the presence of casinos and gambling halls too close to locations such as schools, hospitals, or other places of public interest.

Since this country is one of all possibilities, a public official has proposed moving the casinos to be as far away from schools as possible.

However, we have a major problem, namely the fact that in this country, represented as a matrix with $n$ rows and $m$ columns, there are already many open casinos, and moving them would be impractical and logistically impossible, so a backup solution was found.

Practically, our goal is to move the school in this country somewhere on the matrix, so that it is as far away from casinos as possible. In other words, we want the nearest casino to be as far away as possible.

# Input data

The first line contains $n$ and $m$, the number of rows and columns of the matrix. The next $n$ lines contain the description of the matrix, where `C` denotes the casinos, and `.` denotes the free spaces.

# Output data

Find the maximum minimum distance from a casino for an optimal placement of the school.

# Constraints and clarifications

* $n = 1$
* $1 \leq m \leq 1000$.

# Example

`stdin`
```
1 8
.C.....C
```

`stdout`
```
3
```
```

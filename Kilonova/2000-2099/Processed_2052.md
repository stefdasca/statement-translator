
# Task

In a country at the edge of the world, the government discovered a real problem regarding the presence of casinos and gambling halls too close to locations such as schools, hospitals, or other places of public interest.

Since this country is one of all possibilities, a public servant suggested moving the casinos to be as far as possible from schools.

However, we have a major problem, namely that in this country, represented as a matrix with $n$ rows and $m$ columns, there are already many open casinos, and moving them would be practically and logistically impossible, so a fallback solution was found.

Practically, our objective is to move the school in this country somewhere on the matrix so that it is as far as possible from the casinos. In other words, we want the nearest casino to be as far as possible.

# Input data

The first line contains $n$ and $m$, the number of rows and columns of the matrix. The next $n$ lines contain the description of the matrix, where `C` denotes casinos, and `.` denotes free spaces.

# Output data

Print the maximum minimum distance from a casino of an optimal placement of the school.

# Constraints and clarifications

* $1 \leq n \leq 1000$.
* $1 \leq m \leq 1000$.

# Example

`stdin`
```
5 6
C.....
...C..
......
......
....C.
```

`stdout`
```
4
```
```

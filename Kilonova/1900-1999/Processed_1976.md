For not getting a perfect score in the simulation, the school administration decided to punish the students in an inhumane way: they were no longer allowed to go to the theater or read the great classics of literature. Their only comfort was a matrix with $N$ rows and $N$ columns containing only lowercase letters of the English alphabet, from which they had to identify the valid submatrices. A submatrix is considered valid if it simultaneously meets the following conditions:

* It has at least two rows and at least two columns.
* The letters in the top-left and bottom-right corners of the submatrix are strictly lexicographically larger than all other letters in the submatrix.

# Task

Help the high school students find out the number of valid submatrices that exist in the matrix and thus escape the dreadful punishment.

# Input data

The file `ssdj.in` contains on the first line the natural number $N$, and on the following $N$ lines contain $N$ lowercase letters each, not separated by spaces.

# Output data

The file `ssdj.out` contains a single natural number representing the number of valid submatrices.

# Constraints and clarifications

* $1 \leq N \leq 1 \ 000$
* For tests worth $10$ points, $N \leq 50$
* For tests worth $20$ points, the matrix will contain only letters `a` and `b`

# Example

`ssdj.in`
```
4
maea
bcda
aaae
aaaa
```

`ssdj.out`
```
3
```

## Explanation

The valid submatrices are:

```
ma
bc
ea
da

ea
da

ae
ae

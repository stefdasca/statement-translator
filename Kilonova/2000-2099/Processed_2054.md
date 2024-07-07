
# Task

In Australia, there is a kangaroo competition where $n$ kangaroos participate, each kangaroo having a known jump length.

The organizers want to know the first point where the roads of the $n$ kangaroos will intersect.

Since this point can be very large, they want to receive the message `No` if they do not meet after at most $10^9$ meters.

# Input data

The first line of the input file will contain a number $n$.

The second line of the input file will contain $n$ numbers, representing the jump lengths of the $n$ kangaroos.

# Output data

The first and only line of the output file will contain the first point where the roads of the $n$ kangaroos intersect, or the message `No` if they do not meet after at most $10^9$ meters.

# Constraints and clarifications

* $2 \leq n \leq 1000$
* $1 \leq S_i \leq 100$

# Example 1

`stdin`
```
5
2 9 3 4 6
```

`stdout`
```
36
```

# Example 2

`stdin`
```
6
2 45 97 67 73 31
```

`stdout`
```
No
```

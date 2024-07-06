Micul Gates receives a box with $N$ rectangular pieces from his mother, on which natural numbers are written. She asks him the following question:

Can the $N$ pieces be arranged such that the sum of any two consecutive pieces is the same?

# Task

If the pieces can be arranged in the manner requested by his mother, Micul Gates will display the message `YES` and the sum of two consecutive values in the arranged array.

If the pieces cannot be arranged in the desired form, the message `NO` will be displayed along with the largest value that appears on a piece in the given array.

# Input data

The file `arrange.in` contains:
- The first line contains the natural number $N$, representing the number of pieces in the box,
- The second line contains $N$ natural numbers, separated by a space, representing the values written on the pieces.

# Output data

The file `arrange.out` will contain:
- The first line will contain the message `YES` or `NO`,
- The second line will contain the required value.

# Constraints and clarifications

* $2 \leq N \leq 1\ 000$;
* For $80\%$ of the tests, the values written on the pieces are $\leq 1\ 000$;
* For $20\%$ of the tests, the values written on the pieces are $\leq 10^9$;

# Example 1

`arrange.in`
```
10
2 1 2 2 2 2 1 1 1 1
```

`arrange.out`
```
YES
3
```

# Example 2

`arrange.in`
```
10
2 1 2 2 3 2 1 1 1 1
```

`arrange.out`
```
NO
3
```
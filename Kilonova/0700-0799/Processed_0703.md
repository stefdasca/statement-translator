Given an array with $N$ natural numbers (with a maximum of $8$ digits).

# Task

* Display how many elements in the array are slope values (numbers that, viewed from the left or the right, have digits in ascending order). For example, $136$ and $931$ are slope values.
* Display the largest and smallest slope value, as well as the positions they are located at in the array.

# Input data

The first line of the input file `valori-panta.in` contains $N$, the number of values in the array.

The second line contains the array of $N$ values.

# Output data

The first line of the output file `valori-panta.out` will contain a single integer, the number of slope values.

The second line will contain the largest slope value, followed by the positions where it is located, and the third line, the smallest slope value, followed by the positions where it is located. If there are $0$ slope values, the message `NU EXISTA` will be displayed.

# Constraints and clarifications

* $1 \leq n \leq 200\ 000$;
* For tests worth $30$ points, $1 \leq n \leq 2\ 000$;
* The tests and constraints have been modified.

# Example

`valori-panta.in`
```
6
126 9621 1212 3678 9231 9621
```

`valori-panta.out`
```
4
9621 2 6
126 1

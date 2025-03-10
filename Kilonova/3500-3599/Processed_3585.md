
# Task

Iustin and Radu are playing Clash Royale again, and while they were playing, they started to discuss the spells they can use. Having enough aura after winning trophies instead of preparing for the IOI, they came up with the following problem idea:

You are given an array with $n$ natural numbers and $q$ updates, which can be of two types, as follows:

* $1 \\ x \\ val$: the value at position $x$ becomes equal to $val$.
* $2 \\ val$: all values in the sequence become equal to $val$.

After each operation, you must display the sum of the elements in the sequence.

Now that they saw a preOJI being organized, they decided to propose this problem here. Help them solve it!

# Input data

The first line of the input file `aura.in` contains two integers, $n$ and $q$.

The next line contains the sequence of numbers of length $n$, which contains natural values.

The following $q$ lines contain two or three natural numbers, depending on the type of update.

# Output data

The output file `aura.out` will have $q$ lines, each containing the sum of the numbers after the first $i$ operations.

# Constraints and clarifications

* $1 \leq n, q \leq 200\ 000$;
* $1 \leq val \leq 1\ 000\ 000\ 000$, where $val$ is a value in the sequence or an updated value.
* For tests worth $20$ points, $1 \leq n, q \leq 1\ 000$;
* For other tests worth $20$ points, there will be at most $10$ operations of type $2$;
* For other tests worth $40$ points, $1 \leq val \leq 1\ 000$;

# Example

`aura.in`
```
6 7
5 4 1 2 3 4
1 2 5
1 5 8
2 5
1 4 3
2 6
1 5 9
1 3 2
```

`aura.out`
```
20
25
30
28
36
39
35
```

## Explanation

After the first operation, the sequence will be $[5, 5, 1, 2, 3, 4]$.
After the second operation, the sequence will be $[5, 5, 1, 2, 8, 4]$.
After the third operation, the sequence will be $[5, 5, 5, 5, 5, 5]$.
After the fourth operation, the sequence will be $[5, 5, 5, 3, 5, 5]$.
After the fifth operation, the sequence will be $[6, 6, 6, 6, 6, 6]$.
After the sixth operation, the sequence will be $[6, 6, 6, 6, 9, 6]$.
After the seventh operation, the sequence will be $[6, 6, 2, 6, 9, 6]$.
```

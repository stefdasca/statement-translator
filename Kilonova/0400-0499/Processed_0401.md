Andrei is visiting an old castle with multiple rooms. He has at his disposal $n$ access codes. Each code is a natural number consisting of at most $9$ digits. To open the door of a room, Andrei must figure out which key to choose from a given set. Each key is labelled with a digit. The key that opens the door of the first room is labelled with the digit that appears the most times in the access codes.

# Task
Write a program that determines the key that will open the first door, given the number $n$, the $n$ access codes, the number of keys, denoted by $k$, and the values of the $k$ given keys.

# Input data
The input file `castel.in` contains on the first line the number $n$. The second line of the file contains $n$ natural numbers representing the access codes. The third line contains the natural number $k$ representing the number of given keys. The fourth line of the file contains $k$ digits representing the values of the keys.

# Output data
The output file `castel.out` contains on the first line two natural numbers, separated by a single space. The first number in the file represents the key that will open the door of the first room, and the second number represents the number of times the key appears in the sequence of access codes.

# Constraints and clarifications
* $1 \leq k \leq 10$;
* $1 \leq n \leq 1\ 000$;
* Each access code is a number with at most $9$ digits;
* Each key is labelled with a digit;
* The keys have distinct values and are given in ascending order;
* A door can be opened by only one key.

# Example

`castel.in`
```
5
1243 527 89722 6232 678
3
2 5 7
```

`castel.out`
```
2 6
```

## Explanation

Out of the $3$ given keys, the key that appears the most times in the sequence of codes from the second line is $2$, and it appears $6$ times. The key $5$ appears once, and the key $7$ appears $3$ times.
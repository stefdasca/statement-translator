In the winter holiday, Alex received an engaging game and thus kept postponing his holiday readings, for which he received a low grade at school in the first week of the second semester. Upset, his father password-protected the game with an access code. Since Alex started catching up on his readings, his father gives him a hint to obtain the access code: he shows him a number, but once it is written, the digits start disappearing in the order they are written (from left to right), the access code being the sum of all visible numbers (obtained by successively eliminating one digit).

# Task

Do you want to help Alex find this access code for a number $n$ given? Write a program that determines and displays the game's access code. You can earn $100$ points.

# Input data

The input file `codjoc.in` contains a number $n$ on the first line, representing the number shown to Alex by his father.

# Output data

The output file `codjoc.out` will contain the number that represents the access code of Alex's game.

# Constraints and clarifications

* $0 < n \leq 2\ 000\ 000\ 000$, where $n$ is a natural number.

# Example 1

`codjoc.in`
```
123456
```

`codjoc.out`
```
150886
```

## Explanation

The sum of the numbers $123456, 23456, 3456, 456, 56, 6$ equals $150886$.

# Task

Three strings of length $L$ are given. The task is to find another string of length $L$, such that the maximum Hamming distance from it to the three strings is minimized.

# Input data

The first line of the file `cstring.in` contains a natural number $L$, representing the length of the strings. The next three lines contain the three strings.

# Output data

The file `cstring.out` will contain a single line that will contain the desired string. If there are multiple solutions, you can print any of them.

# Constraints and clarifications

* $1 \leq L \leq 1 \ 000 \ 000$
* The characters in the three strings are lowercase letters of the English alphabet.
* *Hamming distance* between two strings is equal to the number of positions at which they contain different characters.

# Example

`cstring.in`
```
5
xabbb
yaabb
zaaab
```

`cstring.out`
```
xaaab
```

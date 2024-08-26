## Task

Inside a safe, there are some documents that you need to extract. The problem is that the safe is equipped with a terminal that requires the input of a password to open it. When accessing the safe, a keyword composed of lowercase English alphabet letters is displayed on the terminal screen. The password is given by the smallest left rotation (in lexicographical order) of the keyword.

## Input data

The input file `password.in` contains a string of characters composed of lowercase English alphabet letters on the first line.

## Output data

The output file `password.out` must contain a single number that represents the number of circular left shifts of the string from the input file required to obtain the requested access password.

## Constraints and clarifications

- The length of the string from the input file is an integer between $1$ and $100\ 000$.
- If there are multiple solutions, the one requiring the minimum number of left circular shifts will be chosen.

## Example

`password.in`
```
mississippi
```

`password.out`
```
10
```
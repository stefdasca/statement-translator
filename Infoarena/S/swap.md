## Task

You are given $2$ strings consisting only of lowercase letters (from `a` to `z`). On the first string, you can repeatedly perform the operation called $swap$: choose two characters that are in consecutive positions and interchange them. Determine the minimum number of $swap$ operations required to transform the first string into the second string.

## Input data

The first line of the input file `swap.in` contains the first string. 
The second line of the file contains the second string.

## Output data

In the output file `swap.out` you will print the minimum number of $swap$ operations needed to transform the first string into the second string. If the first string cannot be transformed into the second string, print $-1$.

## Constraints and clarifications

- Both strings have the same length.
- The length of each string is a number between $1$ and $50\ 000$.
- Each of the two lines in the input file ends with a "newline" character.
- For $40\%$ of the tests, the strings will have a length $\leq 2\ 000$.

## Example

`swap.in`
```
anaaremere 
mereareana
```

`swap.out`
```
26
```

`swap.in`
```
mumu 
bubu
```

`swap.out`
```
-1
```
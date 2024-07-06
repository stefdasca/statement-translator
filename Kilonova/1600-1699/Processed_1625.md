Gigel battles fervently, in a game received during the Easter holidays, with all kinds of dragons. One day, he encountered a dragon that could not be defeated with any of the usual weapons. Lur Ualab, as the dragon was called, could only be defeated if someone managed to solve his riddle.

In each fight, Lur Ualab gives Gigel a very long string composed **only of lowercase English letters**. Gigel must delete all occurrences, except one, of each letter, so that in the final obtained string, all the distinct letters from the given string remain. At the end, Gigel must give Lur Ualab the smallest lexicographically string that can be obtained from the string he received.

# Task

Write a program that determines the smallest lexicographically string that can be obtained from a given string by applying all necessary deletions.

# Input data

The input file `cmmstr.in` contains a string of lowercase letters on the first line.

# Output data

The output file `cmmstr.out` will contain the minimum obtained string on the first line.

# Constraints and clarifications

* $1 \leq $ length of the string $< 3\ 000\ 000$;
* It is not recommended to read the given string character by character.

# Example

`cmmstr.in`
```
ccbaba
```

`cmmstr.out`
```
cab
```

## Explanation

c**c**baba $\\Rightarrow$ c**b**aba $\\Rightarrow$ cab**a** $\\Rightarrow$ cab
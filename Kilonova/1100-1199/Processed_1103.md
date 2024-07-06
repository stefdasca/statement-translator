```markdown
Given a sequence of hexadecimal numbers, that is, numbers in which the 16 digits are from the set {`0`,`1`,`2`,`3`,`4`,`5`,`6`,`7`,`8`,`9`,`A`,`B`,`C`,`D`,`E`,`F`}. We say that two numbers match if they have no common hexadecimal digits and together contain all the digits in base $16$ at least once. For example, `24FFA032` and `EDCB1998765` are numbers that match.

# Task

Determine the number of pairs of hexadecimal numbers that match.

# Input data

The input file `perechi.in` contains the sequence of hexadecimal numbers on multiple lines, so the numbers are separated by spaces or enters.

# Output data

The output file `perechi.out` will contain a single natural number representing the number of pairs of matching numbers.

# Constraints and clarifications

* The sequence contains at least two numbers and at most $200\ 000$ numbers
* The numbers contain at least one digit and at most $30$ digits
* Hexadecimal digits from $10$ to $15$ are written with the capital letters `A`, `B`, `C`, `D`, `E`, `F`.

# Example

`perechi.in`
```
24FFA032 EDCB1998765
24FA03 24FFA032 0
123456789ABCDEF12
```

`perechi.out`
```
4
```

## Explanation

The four pairs are: (`24FFA032`, `EDCB1998765`), (`EDCB1998765`, `24FA03`), (`EDCB1998765`, `24FFA032`) and (`0`, `123456789ABCDEF12`).
```
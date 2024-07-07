A circular string is a string composed only of the characters `A` and `B` which has the following properties:
- It has a length `N \geq 1` (it cannot be an empty string);
- It is considered that after the last character of the string follows the first character of the string.

This property implies that any circular string has `N` subarrays of length `L` (`1 \leq L \leq N`).

A subarray of length `L` of a circular string `S` is a string of characters (ordinary, not circular) consisting of `L` characters located in consecutive positions in the string `S`. For example, the circular string `ABAAB` has `5` subarrays of length `3`: `ABA`, `BAA`, `AAB`, `ABA`, and `BAB` (they are not distinct in value, but differ in their starting position in the string they belong to).

A **csir** is a circular string that has the following additional property: for any `L` (`1 \leq L \leq N`) and any two subarrays of length `L` (let's call them `S1` and `S2`), the number of `A` characters in `S1` differs from the number of `A` characters in `S2` by at most `1` (in absolute value).

Let's consider the circular string `BBAABAA`. This string is not a **csir**, because there exist subarrays `BBAAB` and `AABAA` (of length `5`), which contain `2` and `4` `A` characters, respectively (the difference in the number of `A` characters is thus `2`). Also, the string `ABABAABAAB` is not a **csir**, because it contains subarrays `AABAA` and `BABAB` for which the difference in the number of `A` characters is more than `1` (in absolute value).

However, the circular strings `ABA` and `AABABAAB` are **csir**-s, because for any two subarrays `S1` and `S2` of the same length, the difference in the number of `A` characters in `S1` and the number of `A` characters in `S2` is less than or equal to `1` (in absolute value).

# Task
Given multiple circular strings, determine if they are **csir**-s.

# Input data
The first line of the input file `csir.in` contains the integer `S`, representing the number of strings contained in the file. Each of the following `S` lines contains a circular string.

# Output data
In the output file `csir.out` `S` lines will be written. The `K`-th line of this file will contain `1`, if the `K`-th string from the input file is a **csir**, or `0` otherwise.

# Constraints and clarifications
* `1 \leq S \leq 20`
* The length of each circular string in the input file is between `1` and `50000` (inclusive).
* The strings contain only characters `A` and `B` (not `a` or `b`).
* No partial scores are awarded.

# Example

`csir.in`
```
4
BBAABAA
ABABAABAAB
ABA
AABABAAB
```

`csir.out`
```
0
0
1
1

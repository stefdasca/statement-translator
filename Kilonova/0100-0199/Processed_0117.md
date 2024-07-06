```markdown
Three numbers written in base `3` (using the digits `0, 1` and `2`) are given. The task is to find a number `N` in base `3` that has an odd number of digits, with the digit in the middle position having the value `1`. This number `N` must be obtained by concatenating the three given numbers; in this concatenation, each of the `3` numbers can be used zero or more times.

# Task
Determine the minimum number of digits that a number having the above properties can have.

# Input data
The input file `base3.in` contains `3` lines. Each line contains a number in base `3`.

# Output data
The output file `base3.out` will contain the minimum number of digits that a number `N` with the specified properties can have. If no such number can be obtained, print the value `0` in the file.

# Constraints and clarifications
* The number of digits of each of the `3` numbers is an integer between `1` and `16000`.
* The given numbers can contain leading zeros; these must be considered if the respective number is used in the concatenation.

# Example

`base3.in`
```
001
020
2020
```

`base3.out`
```
13
```

Explanation:
---

The number *2020* $ \mathbf{001} $ *001* $ \mathbf{001} $ can be obtained.
```
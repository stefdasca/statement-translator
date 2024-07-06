```markdown
A text and a mask are given, both consisting of lowercase English letters. Additionally, the mask can contain the special characters `?` and `*`.

We say that the mask matches a subarray $S$ of the text if and only if:
- Replacing each `?` with exactly one letter (a different letter for each `?` in the mask) and 
- Each `*` with a sequence of letters (possibly empty; a different sequence for each `*` in the mask)
results in the subarray $S$.

Two matches over the same subarray $S$ are considered different if there is at least one special character that is replaced by a letter/sequence from different positions in $S$ in the two matches. Similarly, two matches over different subarrays of the text are considered distinct. Two subarrays are considered different if they are found at different positions in the text, even if they are equal when compared as strings.

# Task

Find the number of distinct matches of the mask in the text.

# Input data

The first line of the input file `pattern.in` contains a number $T$ which represents the number of tests. Each test is described by two lines: the first line contains the text and the second line contains the mask for that test.

# Output data

The output file `pattern.out` will contain $T$ lines, each containing a single number equal to the number of ways the mask can match the text modulo $1\ 000\ 000\ 007$ for each test.

# Constraints and clarifications

* $1 \leq T \leq 3$
* $1 \leq \text{length(text)} \leq 100\ 000$
* $1 \leq \text{length(mask)} \leq 50\ 000$
* For $40\%$ of the tests: $\text{length(text)} \leq 3\ 000$ and $\text{length(mask)} \leq 1\ 000$
* The number of special characters in the mask will be less than $101$.
* In the mask, there will be no two consecutive `*`, and there is at least one letter.

# Example

`pattern.in`
```
3
aababba
a?b*
abbabbcbaba
?c?
aaa
a*a*
```

`pattern.out`
```
7
1
4
```

## Explanation

In the first test, we have the following matches: `aababba`, `aababba`, `aababba`, `aababba`, `aababba`, `aababba`, `aababba`.
For the second test, there is a single match: `abbabbcbaba`.
For the third test, we have the matches (the characters matched over `*` are underlined): aaa, aaa, a$\underline{a}$a, aa$\underline{a}$
```

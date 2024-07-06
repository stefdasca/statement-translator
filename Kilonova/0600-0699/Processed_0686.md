The text provided contains a competitive programming problem statement. Here is the translated version:

---

We consider an initially empty string on which we want to perform $Q$ operations of the following types:
* a character is added to the end of the string;
* a character is removed from the beginning of the string.

The characters will only be parentheses, specifically, the characters `(` or `)`.

# Task

Determine after each operation whether the sequence $S$ formed from the elements of the string is correctly parenthesized. A sequence is considered correctly parenthesized if it can be transformed into a valid arithmetic expression by adding only the characters `1` and `+` to the initial sequence. For example, `()` and `(())` are correctly parenthesized because we can write `(1)` respectively `((1+1)+1)`, while `)()` or `())` are not. An empty string is also considered correctly parenthesized.

# Input data

From the keyboard, the first line will contain $Q$, representing the number of operations. The second line will contain $Q$ characters without spaces between them of three types:
1. `(` means that it requires adding the character `(` to the end of the string.
2. `)` means that it requires adding the character `)` to the end of the string.
3. `P` means that it will remove the character from the beginning of the string.

# Output data

On the screen will be printed $Q$ characters, without spaces between them, one after each operation, encoded as follows:
1. `0` means that as a result of the operation the string is not correctly parenthesized.
2. `1` means that as a result of the operation the string is correctly parenthesized.

# Constraints and clarifications

* $ 1 \leq Q \leq 2 \cdot 10^6$
* It is guaranteed that for each `P` read, the string contains at least one parenthesis that can be deleted.

## Subtask 1 (13 points)

* There is no `P` in the input data.

## Subtask 2 (21 points)

* $Q \leq 2 \ 000$

## Subtask 3 (24 points)

* $Q \leq 10^5$

## Subtask 4 (42 points)

* No additional constraints.

# Example

`stdin`
```
12
(()P)PPP)(P)
```

`stdout`
```
000100010001
```

Explanations
---
```
(
((
(()
()
())
))
)
)
)(
(
()
```

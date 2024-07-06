Alis has discovered a new passion: strings. Being a 12th-grade student, she is preparing for the baccalaureate exam. After solving some proposed problems, she realized that they were too easy, so she thought of a problem herself. Thus, Alis has two strings $A$ and $B$ consisting only of lowercase English letters. For a given $x$, she wonders how many times the string $B$ appears as a subsequence in the string $A$, knowing that the first $x$ and the last $x$ characters of $B$ remain fixed, while the others can be replaced with any character.

# Task
Given the two strings $A$ and $B$. For each $x$ from $1$ to half the length of string $B$, determine how many times the string $B$ appears in $A$ knowing that the first $x$ and the last $x$ characters of $B$ remain fixed, while the others can be replaced with any character.

# Input data
The input file `aparitii.in` contains on the first line the string $A$ and on the second line the string $B$.

# Output data
The output file `aparitii.out` will contain $[|B|/2]$ lines, on each line $i$ containing the number of appearances of the string $B$ in string $A$, with the specified constraints.

# Constraints and clarifications
* $ 1 \leq |A|, |B| \leq 1 \ 000 \ 000$;
* $ 1 \leq x \leq [|B|/2], |B| =$ length of string $B$.

# Example

`aparitii.in`
```
abzdeazxye
abcde
```

`aparitii.out`
```
2
1
```

## Explanation

On the first line is the answer for $i=1$, thus, the first and last characters of string B remain fixed: ```a***e```. Thus, there are two appearances in string $A$: **abzde**, **azxye**. On the second line is the answer for $i=2$, thus, the first two and last two characters remain fixed: ```ab*de```. There is one appearance in $A$: **abzde**.
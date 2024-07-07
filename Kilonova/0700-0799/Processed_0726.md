
At a math competition, students from multiple schools in different cities participate. To distinguish between their papers, each paper is coded with a natural number of 3 digits, say $abc$, where $a$ (the hundreds digit) is the city code, $b$ (the tens digit) is the school code in city $a$, and $c$ (the units digit) is the student code from school $b$ in city $a$. Example: the paper with the code $328$ belongs to the student with code $8$ from the school with code $2$ in the city with code $3$.

Known data: a code (for the paper of a student $H$, our friend), the number $n$ of awarded papers, and their codes.

# Task

You are required to solve the following tasks:

1. Check if $H$ is an award recipient, or not.
2. Determine the number of awards obtained by students in $H$'s city (including $H$, if awarded).
3. Determine the number of awards obtained by students in $H$'s school (including $H$, if awarded).

# Input data

The first line of the input file `concurs.in` contains the code of $H$; the second line of the file contains the value $n$, and the third line contains the $n$ award codes. The awarded codes are separated by spaces.

# Output data

The 3 answers will be displayed in the output file `concurs.out`, one per line. For the first task, display on the first line of the file a message (`YES` or `NO`), depending on whether $H$ received an award or not. For tasks 2 and 3, print one number on the second line and third line of the output file, respectively.

# Constraints and clarifications

* $1 \leq n \leq 20$
* City codes (the hundreds digit from each code) range from $1$ to $5$, inclusive.
* School codes in each city (the tens digit) range from $0$ to $9$, inclusive.
* Student codes (the units digit) range from $0$ to $9$ inclusive.
* $30\%$ of the score is awarded for correctly solving the first task, $70\%$ of the score for correctly solving the first two tasks, and the full score for solving all 3 tasks correctly.

# Example

`concurs.in`
```
234
6
123 232 125 222 421 235
```

`concurs.out`
```
NO
3
2
```

## Explanation

1. The code of $H$ is not found among the awarded codes, so the message is `NO`.
2. The awarded papers from $H$'s city (with hundreds digit equal to $2$) total $3$: $232$, $222$, and $225$.
3. The awarded papers from $H$'s school (with hundreds digit equal to $2$ and tens digit equal to $3$) total $2$: $232$ and $235$.

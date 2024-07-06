```markdown
The value of a letter is given by its position in the alphabet (`A` has the value $1$, `B` has the value $2$, `C` has the value $3$, etc.). A *special text* is composed of one or more uppercase letters of the English alphabet and does not contain other types of characters.

The value of a special text is defined as equal to the sum of the values of the letters that compose it. For example, the special text `ABAC` has the value $7$ ($7 = 1+2+1+3$).

A special text can be transcribed into a *compact* form using pairs of parentheses and natural numbers. For example, the compact form transcription of the text `ABACABACEECDCDE` is the text `(ABAC)2E2(CD)2E` because the sequence `ABAC` appears twice consecutively, the letter `E` appears twice consecutively, as does the sequence of letters `CD`.

The transcription into the compact form of a special text is done by replacing any sequence that has consecutive occurrences in the text with the sequence written between a pair of round parentheses followed by the number of repetitions. For example, the special text `ABABAB` is transcribed into the compact form as `(AB)3`. If, after transcription, the text in the compact form contains sequences with consecutive occurrences in the text, this will also be transcribed into the compact form. For example, the special text `ABABCABABC` can initially be transcribed into the compact form as `(ABABC)2` or `(AB)2C(AB)2C`, and then into `((AB)2C)2`. If the special text does not contain any sequence with consecutive occurrences, then the compact form of the text is identical to the initial form. For example, the special text `ABAC` has the compact form `ABAC`, which is identical to this special text.

# Task

Write a program that reads a string $S$ representing the compact form of a special text, and then determines:
1. the number of distinct letters that appear in the special text;
2. the sum of the numbers appearing in the compact form of the special text;
3. the value of the special text given in the compact form.

# Input data

The input file `valoare.in` contains:
* The first line contains a natural number $C$ ($1$, $2$, or $3$) representing the task that needs to be solved;
* The second line contains the string $S$ representing the compact form of a special text.

# Output data

The output file `valoare.out` will contain:
* if $C = 1$, the first line will contain a natural number representing the number of distinct letters that appear in the special text (the answer to task 1);
* if $C = 2$, the first line will contain a natural number representing the sum of the numbers that appear in the compact form of the special text (the answer to task 2);
* if $C = 3$, the first line will contain a natural number representing the value of the special text given in the compact form (the answer to task 3).

# Constraints and clarifications

* The string $S$ that represents the compact form of a special text can have at most $1\ 000$ characters (uppercase letters of the English alphabet, pairs of round parentheses, digits).
* The natural numbers that appear in the compact form of a special text are nonzero and belong to the closed interval $[2, 9\ 999]$.
* The value of a special text is a natural number consisting of at most $12$ digits.
* For task 1, 10 points are awarded, for task 2, 20 points are awarded, and for task 3, 70 points are awarded.
* For tests worth 10 points, the compact form of the special text is identical to the special text, and the task is 3.

# Example 1

`valoare.in`
```
1
(ABAC)2E2(CD)2E
```

`valoare.out`
```
5
```

## Explanation

Task 1 is solved. The compact form of the special text is `(ABAC)2E2(CD)2E`. In the special text, only the letters `A`, `B`, `C`, `D`, and `E` appear.

# Example 2

`valoare.in`
```
2
(ABAC)2E2(CD)2E
```

`valoare.out`
```
6
```

## Explanation

Task 2 is solved. The compact form of the special text is `(ABAC)2E2(CD)2E`. The only number that appears in the special text is 2, three times. Therefore, the sum is $6$ ($=2+2+2$).

# Example 3

`valoare.in`
```
3
(ABAC)2E2(CD)2E
```

`valoare.out`
```
43
```

## Explanation

Task 3 is solved. The compact form `(ABAC)2E2(CD)2E` represents the transcription of the special text `ABACABACEECDCDE`. In the special text, there are $4$ `A`s, $2$ `B`s, $4$ `C`s, $2$ `D`s, and $3$ `E`s. Thus, the value of the special text is equal to $43$ ($=4*1+2*2+4*3+2*4+3*5$).
```
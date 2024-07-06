In the night before the great battle, on January 10th, 1475, a Turkish spy infiltrated the Moldavian camp to uncover the battle plans. The spy managed to reach Stephen's secret chamber, where he found a document containing a clue on how to determine the code to unlock the chest hiding the battle plans. The clue in the document was as follows:
*expression=value*

The expression is a sequence consisting of one or more operands; between any two consecutive operands there is exactly one operator. The operands can be of two types:
* a string of characters;
* the code, denoted by #c.

The expression contains only two operators, whose meanings the spy already knew:

|Operator|Meaning|Example|
|--------|-------|-------|
|`+`     |concatenates two strings|`con+tact=contact`|
|`*`     |inserts the second string after each letter of the first string|`Ctrm*a=Catarama`|

The operations in the expression are executed in order from left to right.

The value is a string of characters that represents the result of evaluating the expression.

# Task

Write a program that, knowing the clue, determines the code.

# Input data

The input file `indiciu.in` contains on the first line the clue, in the form described in the statement.

# Output data

The output file `indiciu.out` will contain a single line that will be written with the determined code.

# Constraints and clarifications
* The strings of characters mentioned in the statement (operands or value) contain ASCII characters with codes  $\\ge 32$ and $\\le 127$, different from the characters # (hash), + (plus), * (asterisk) or = (equal);
* The length of the operands is at most $255$ characters;
* The length of the value is at most $20\\ 000$ characters;
* The expression contains at most $10\\ 000$ operators;
* #c appears at least once as an operand in the expression;
* The input data is correct;
* For $20$ points, the expression uses only the `+` operator;
* For $24$ points, the expression uses only the `*` operator;
* For $32$ points, the code appears only once in the expression.

# Example 1

`indiciu.in`
```text
con+#c+are=contactare
```

`indiciu.out`
```
tact
```

# Example 2

`indiciu.in`
```text
NTS*#c+ MI+#c+U=NATASA MIAU
```

`indiciu.out`
```
A
```
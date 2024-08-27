## Task

You are given a string of characters representing an arithmetic expression. Write a program that answers $M$ questions of the type: "At what position is the closing parenthesis $')'$ corresponding to the opening parenthesis $'('$ at the $i$-th position in the considered string of characters?"

## Input data

The input file `parantezare.in` will contain on the first line a string composed of digits ($'0' - '9'$), operators ($'+', '-', '*', '/'$), and parentheses ($'(', ')'$. The second line contains the number $M$ of questions. The last line of the input file contains $M$ natural numbers representing the values of $i$ which define the questions mentioned previously.

## Output data

In the output file `parantezare.out`, $M$ values separated by a space will be printed. Thus, the $i$-th value in the output file will represent the answer to the $i$-th question.

## Constraints

$1 \leq$ length of the string $\leq 100\,000$

$1 \leq M \leq 100\,000$

## Example

`parantezare.in`

```
(1+1*(2+3))
2
0 5
```

`parantezare.out`

```
10 9
```
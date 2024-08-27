## Task

The Great Leader has decided to print a new series of flyers for propaganda purposes. This time he thought his picture should occupy most of the flyer and wants to reduce the text to a single line, considering it unimportant. For flyer editing, a text of length $L$ composed only of lowercase Latin alphabet letters and spaces is provided. Each symbol (letter or space) has an associated width measured in pixels. The Great Leader wants this text to be printed in a text field of width $W$, on a single line. If the text does not fit on a single line, a minimal number of characters from the end will be replaced by "..." (with a total width of $3$), so that it fits within the text field.

## Input data

The input file `texttrim.in` will contain $3$ lines. The first line will contain $27$ numbers, each representing the width of each character in the order: space, a, b, c, $\dots$, z. The second line will contain the text of length $L$ that is to be printed, and the third line of the input file will contain $W$, the width of the text field where the text will be printed.

## Output data

The output file `texttrim.out` will contain a single line containing the formatted text that will be printed on the text field.

## Constraints

$1 \leq L \leq 10^6$

$3 \leq W \leq 10^9$

The width of a letter is at most $10^9$

## Example

`texttrim.in`

```
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 
abc def ghi jkl mno pqr stu vxy z 
20 
```

`texttrim.out`

```
abc def ghi jkl m...
```
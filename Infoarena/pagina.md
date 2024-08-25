# Page Layout

Among the new obsessions of the world we live in is page layout. We are given a text consisting of $N$ words, where the words are separated by a space (" "), and at the end of the text is a period ("."). It is considered that the width of each letter in the text is equal to $1$, and the width of the period (".") and space (" ") characters is equal to $0$. We want to find the minimum width of a page so that the text can be written continuously (without words being syllabically divided). More precisely, we want each line to end either with the space that separates two words or with the period at the end of the text. Given $N$ - the number of words in a text and $L[i]$ - the lengths of the words in the text, in the order in which they appear, determine the minimum width of a page such that the text can be written continuously.

## Input data

The input file `pagina.in` will contain on the first line the natural number $N$, and on the second line it will contain the $N$ natural numbers $L[i]$, representing the lengths of the words in the text.

## Output data

The output file `pagina.out` will contain a single natural number, representing the minimum width of a page that respects the required property.

## Constraints

$1 \leq N \leq 100\\ 000$

$1 \leq L[i] \leq 10^9$

## Example

`pagina.in`
```
11
11 1 8 3 1 3 9 6 6 4 8
```

`pagina.out`
```
12
```

## Explanation

The lines will be divided as follows:

Line 1 will contain words 1 and 2

Line 2 will contain words 3, 4, 5

Line 3 will contain words 6 and 7

Line 4 will contain words 8 and 9

Line 5 will contain words 10 and 11
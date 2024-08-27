# Parentheses

Ţirbi has just learned about round brackets $($, $)$ , square brackets $[$, $]$ , and curly brackets $($, $)$ in a Silverlight course. A sequence is correctly parenthesized if it is constructed according to the rules: $<$correctly parenthesized sequence$>$ = $<$empty sequence$>$ $<$correctly parenthesized sequence$>$ = $($ + $<$correctly parenthesized sequence$>$ + $)$ $<$correctly parenthesized sequence$>$ = $[$ + $<$correctly parenthesized sequence$>$ + $]$ $<$correctly parenthesized sequence$>$ = ${$ + $<$correctly parenthesized sequence$>$ + $}$ $<$correctly parenthesized sequence$>$ = $<$correctly parenthesized sequence$>$ + $<$correctly parenthesized sequence$>$ 

## Task

As in any course, there are homework assignments, and Ţirbi received the following problem: Given a sequence with $N$ parentheses, find the maximum length of a correctly parenthesized subsequence. 

## Input data

The input file `paranteze.in` contains on the first line the natural number $N$, and on the following line a sequence with $N$ parentheses. 

## Output data

The output file `paranteze.out` contains the maximum length of a correctly parenthesized subsequence. 

## Constraints and clarifications

$1 \leq N \leq 1\,000\,000$ 

For 50$\%$ of the tests $N \leq 1\,000$ 

## Example

`paranteze.in`
```
13
{)([({})]([
```

`paranteze.out`
```
6
```

## Explanation

The correctly parenthesized subsequence is in bold. ${)($ $[$({})$]$ ([{}
# Keyboard

On his birthday, Gigel received a new, much more powerful laptop as a gift, so he can play the most popular games of the moment. Enthusiastic, he began to study it. It didn't take him long to notice that its keyboard is a bit strange, or maybe too advanced for him: besides digit buttons ($0 - 9$), it also contains number buttons (a natural number with up to 50 digits). So, instead of installing his beloved Assassin's Creed III, he asked himself the following question: What is the minimum number of buttons that need to be pressed to write a number $X$, with a maximum of $1000$ digits? Given $X$ - the number for which Gigel wants to find the answer, $N$ - the number of number buttons on the keyboard, and $N$ natural numbers $A[i]$ - the numbers inscribed on the keyboard buttons, help Gigel to find the answer.

## Input data

The input file `tastatura.in` will contain:
- The first line contains the number $X$.
- The second line contains the number $N$.
- The following $N$ lines each contain a natural number $A[i]$, representing the keyboard buttons.

## Output data

The output file `tastatura.out` will contain a single natural number, the answer to Gigel's question.

## Constraints and clarifications

$1 \leq N \leq 10\ 000$

$1 \leq X < 10^{1000}$

$10 \leq A[i] < 10^{50}$

## Example

`tastatura.in`
`1961996`
`2`
`19`
`96`

`tastatura.out`
`4`

## Explanation

Gigel will press the "19" key once, the "6" key once, the "19" key again, and finally the "96" key.
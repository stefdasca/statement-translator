# Great Playwright BONIFACCI amazed the world with his new masterpiece, *Dada?!*

Because modern theater is a bit minimalist, the play has a single actor. Because modern theater is a bit absurd, Act 1 consists only of the line `A`, and Act 2 consists only of the line `D`. As you will see, in each play, **the line** is described by a single character. And because modern theater is a bit repetitive, each act $K$, starting with the third inclusive, is obtained by concatenating the acts $K-2$ and $K-1$, in this order. The play has $N$ acts, numbered from $1$ to $N$, all constructed according to this rule. In each act, the lines are numbered starting from $1$.

For example, the first 7 acts are (please do not applaud until the end):

|    Act | Text|
|----------|-------|
|1|`A`|
|2|`D`|
|3|`AD`|
|4|`DAD`
|5|`ADDAD`
|6|`DADADDAD`
|7|`ADDADDADADDAD`

# Task

During rehearsal, the actor plans to recite, with intonation, $L$ adjacent lines from the $N$-th act, starting with line number $P$, up to line number $P + L - 1$. Determine the sequence of characters uttered by the actor at the rehearsal.

# Input data

The input file contains three non-zero natural numbers $N$, $P$, and $L$, each separated by a space, on the first line.

# Output data

The output file will contain, on the first line, $L$ characters `A` or `D`, representing in order, the lines spoken by the actor at the rehearsal.

# Constraints and clarifications

* Let $S_N$ be the number of lines in the $N$-th act. It is guaranteed that $S_N \leq 10^{18}$.
* $1 \leq L \leq 2 \ 000 \ 000$.
* $1 \leq P \leq S_N - L + 1$ (in other words, there exist $L$ lines in act $N$ starting with line number $P$).

|#|Score|Constraints|
|-|-------|----------|
|1|7|$N \leq 35$, $L = 1$|
|2|13|$N \leq 35$, $L \leq 200 \ 000$|
|3|17|$N \leq 40$, $L \leq 200 \ 000$|
|4|19|$N \leq 46$, $L \leq 200 \ 000$|
|5|21|$L \leq 200 \ 000$|
|6|23|No other additional constraints.|

# Example 1

`theater.in`
```
7 3 9
```
`theater.out`
```
DADDADADD
```
## Explanations

The full text of the 7th act is `ADDADDADADDAD`. The characters from positions 3-11 need to be displayed.

# Example 2

`theater.in`
```
12 80 8
```
`theater.out`
```
ADDADADD
```


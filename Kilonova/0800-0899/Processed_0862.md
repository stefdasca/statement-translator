**Charlie** has decided to play with the letters of a string, a string that contains only **lowercase letters** of the English alphabet from `a` to `z`. The game consists of removing letters from the string according to the following rule: let $L_1$, $L_2$, $L_3$ be three letters on consecutive positions in the string, then letter $L_2$ can be removed if and only if it is strictly lexicographically smaller than letters $L_1$ and $L_3$.

To make the game more interesting, **Charlie** assigns a cost to the removal of letter $L_2$ equal to the maximum value of $f(L_1)$ and $f(L_3)$, where $f($`letter`$)$ is understood to be the ordinal number of the respective letter in the alphabet ($f($`a`$) = 1, f($`b`$) = 2, \\dots, f($`z`$) = 26$). **Charlie** repeatedly applies the removal process and calculates the sum of the removal costs.

# Task
Given a string of characters, determine:
1) The maximum length of a sequence of alternating letters, meaning a sequence for which the letters on consecutive positions have the form: $L_i > L_{i+1} < L_{i+2} > L_{i+3} < L_{i+4} > \\dots < L_j$.
2) The maximum sum **Charlie** can obtain by repeatedly applying the letter removal process, as well as the string obtained in the end.

# Input data
The input file `charlie.in` contains on the first line a natural number $p$. For all input tests, the number $p$ can only have the value $1$ or the value $2$. The next line contains a string of characters.

# Output data
If the value of $p$ is $1$, **only the first task will be solved**.
In this case, the output file `charlie.out` will contain a single natural number $L$ representing the maximum length of a sequence of alternating letters.

If the value of $p$ is $2$, **only the second task will be solved**.
In this case, the output file `charlie.out` will contain two lines. On the first line will be the string resulting from the repeated removal of letters respecting the stated rule, and on the second line the maximum sum obtained.

# Constraints and clarifications
- The number of letters of the initial string is between $3$ and $100\ 000$ inclusive.
- For the correct solution of the first task, 25 points are awarded, while for the second task, 75 points are awarded.
- For $30\%$ of tests, the number of letters of the string is $\\leq 1\ 000$.

# Example 1
`charlie.in`
```
1
cadgfacbda
```
`charlie.out`
```
5
```
$p = 1$, so **for this test only the first task is solved.**
The correctly formed alternating sequences are: `cad`, `facbd`. The maximum length is $5$.

# Example 2
`charlie.in`
```
2
cbcabadbac
```
`charlie.out`
```
ccdc
21
```
$p = 2$, so **for this test only the second task is solved.**
The initial string is `cbcaBADbac`.
We remove the letter `a` from the sequence `BAD` and add to the sum the value $4$. The new string is `cbcabdBAC`.
We remove the letter `a` from the sequence `BAC` and add to the sum the value $3$. The new string is `cbcabDBC`.
We remove the letter `b` from the sequence `DBC` and add to the sum the value $4$. The new string is `cbCABdc`.
We remove the letter `a` from the sequence `CAB` and add to the sum the value $3$. The new string is `cbCBDc`.
We remove the letter `b` from the sequence `CBD` and add to the sum the value $4$. The new string is `CBCdc`.
We remove the letter `b` from the sequence `CBC` and add to the sum the value $3$. The new string is `ccdc`.
No more removals are possible. The maximum sum obtained is $21$.
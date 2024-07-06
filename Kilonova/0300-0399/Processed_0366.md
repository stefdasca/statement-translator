### Problem Statement

Long time ago, in a very, very faraway land, there was a country named Tnamap. The inhabitants of this country could instantly apply transformations on the digits of a number using a correspondence array $T$. A digit $c$ of a number can be replaced with its corresponding digit $T_c$.

Dalv and Sogard, two special individuals of this strange society, were on their way to INO when they realized they could instantly transform any number $N$ into a palindrome divisible by a natural number $K$ using the minimum number of digit transformations. If there are multiple such numbers, they determine the largest one.

Can you do it?

### Task

Given the values $T_0$, $T_1$, ..., $T_9$, the number to be transformed $N$, and the number $K$ (the divisor of the palindrome), determine:
1. The maximum number that can be obtained by applying successive transformations to the given number $N$.
2. The largest among the palindromes divisible by $K$, which can be obtained from the number $N$, by performing a minimum number of digit transformations on the given number and on the intermediate numbers obtained.

### Input data

The first line of the input file `palindrom.in` contains 10 distinct digits separated by spaces, representing the values $T_0$, $T_1$, ..., $T_9$.  
The second line contains the digits of the number $N$.  
The third line contains the natural number $K$.

### Output data

The output file `palindrom.out` will contain on the first line the maximum number that can be obtained by applying successive transformations to the number $N$, and on the second line the palindrome divisible by $K$, with the maximum value, which can be obtained from the number $N$, by performing a minimum number of digit transformations on the digits.

### Constraints and clarifications

- $1 \leq N \leq 10^{1\ 000\ 000}$
- $N$ has an even number of digits.
- $2 \leq K \leq 20$
- It is guaranteed that all tests have a solution.
- Solving the first task grants $20\%$ of the score, while solving the second task grants $80\%$ of the score.

### Example

`palindrom.in`
```
0 4 6 5 1 2 7 8 9 3
1234
3
```
`palindrom.out`
```
4994
4224
```
$\\textcolor{red}{1}234 \\rightarrow 4\\textcolor{red}{2}34 \\rightarrow 4\\textcolor{red}{6}34 \\rightarrow 4\\textcolor{red}{7}34 \\rightarrow 4\\textcolor{red}{8}34 \\rightarrow 4\\textcolor{red}{9}34 \\rightarrow 49\\textcolor{red}{5}4 \\rightarrow 49\\textcolor{red}{2}4 \\rightarrow 49\\textcolor{red}{6}4 \\rightarrow 49\\textcolor{red}{7}4 \\rightarrow 49\\textcolor{red}{8}4 \\rightarrow \\textcolor{red}{4994}$

The number $N$ goes through the following stages before becoming a palindrome of maximum value, divisible by $3$: $\\textcolor{red}{1}234 \\rightarrow 42\\textcolor{red}{3}4 \\rightarrow 42\\textcolor{red}{5}4 \\rightarrow \\textcolor{red}{4224}$
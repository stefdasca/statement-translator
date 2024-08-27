## Task

The chief loan shark lives in ValoareLand, a wonderful country where digits are numbered from $0$ to $B - 1$, and numbers of any kind are considered in base $B$. He has received a direct order from the country's Boss, namely to find the value of the banknote with the Boss's face on it in the monetary system of other countries (simple countries that use the decimal system). The value of the banknotes in ValoareLand is much too large compared to normal countries, which is why the remainder of the actual value divided by $P$ is requested. The banknote with the Boss's face is worth $123\ldots(B - 1)$ coins (number written in base $B$). Since the chief loan shark does not want to be exiled from the country and is not too good at informatics, he asks for your help. A reformulated task of the problem, stripped of excess value, is, therefore, to calculate the remainder of the division of the number $123\ldots(B - 1)$ (considered in base $B$) by $P$ (as a result, $P$ is a number in base 10).

## Input data

The input file `valuare.in` contains on the first and only line two values $B$ and $P$ as described in the problem statement.

## Output data

The output file `valuare.out` must contain a single number representing the remainder of the division of the number $123\ldots(B - 1)$ (in base $B$) by $P$.

## Constraints and clarifications

$1 \leq B \leq 10^{18}$

$1 \leq P \leq 10^9 + 8$

Attention! Each subtask has grouped tests!

Subtask $1$ (20 points): $B \leq 51000$

(Feedback test $34$)

Subtask $2$ (20 points): $B < P$, $P = 1000000007$

(Feedback tests $1$ and $4$)

Subtask $3$ (20 points): $gcd(B - 1, P) = 1$, $P \leq 10^9 + 8$

(Feedback test $11$)

Subtask $4$ (20 points): $B \leq 10^9$, $P \leq 10^9 + 8$

(Feedback test $17$)

Subtask $5$ (20 points): $B \leq 10^{18}$, $P \leq 10^9 + 8$

(Feedback test $25$)

Attention! The tests are not evaluated in the usual order (i.e., evaluation does not start with test $1$).

## Example

`valuare.in` `valuare.out`

`5 12` `2`

`10 1000000007` `123456789`

`44444 666013` `235448`

## Explanation

In the first example, the numeral base used in ValoareLand is $5$, and the number written on the banknote with the Boss's face is $1234$ (in base $5$). We have $1234$ (in base $5$) = $1 * 5^3 + 2 * 5^2 + 3 * 5^1 + 4 * 5^0 = 125 + 50 + 15 + 4 = 194$ (in base $10$). This number gives the remainder $2$ when divided by $12$. In the second case, the numeral base used in ValoareLand happens to coincide with the usual decimal system, and $123\ldots(10 - 1)$ = $123456789$.
Taste

Azerah, the gentle emperor of programming, needs your help. To excel in the contests on his favorite problem site, Codefo $\dots$ ahem $\dots$ Infoarena, he needs a special keyboard for contests. A keyboard contains two types of keys: command keys and control keys. To print a character on the screen, Azerah presses a single command key and a subset of control keys. Any such combination of keys will print a different character. For example, let's say we have $4$ keys on the keyboard: two command keys (A and B) and two control keys (Ctrl and Shift). We can print a total of $8$ different characters as follows:
1. A
2. A $+$ Ctrl
3. A $+$ Shift
4. A $+$ Ctrl $+$ Shift
5. B
6. B $+$ Ctrl
7. B $+$ Shift
8. B $+$ Ctrl $+$ Shift
Azerah wants the ideal keyboard for programming contests. He wants the number of characters he can print to not be too small because he won't be able to write his program. He also wants the number of characters he can print to not be too large because, in that case, he risks getting confused. In this sense, he wants a keyboard that allows him to print between $X$ and $Y$ characters, inclusive. From all the keyboards with this property, he wants one with the minimum number of keys (command keys $+$ control keys). It is your duty to find the ideal keyboard.

## Input data

The input file `taste.in` contains on the first line two natural numbers $X$ and $Y$, the lower limit and upper limit of the number of characters the keyboard can print.

## Output data

The output file `taste.out` must contain on the first line two natural numbers separated by a space which describe the keyboard: $com$ represents the number of command keys on the keyboard and $con$ represents the number of control keys on the keyboard. These keys must form a number of characters in the interval $[X,Y]$ according to the rules described above. The pair $(com, con)$ must have $(com + con)$ minimum among all pairs with this property.

## Constraints and clarifications

$1 \leq X$

$X \leq Y$

$Y \leq 10^{18}$

For $30\%$ of the tests $X = Y$.

## Example

`taste.in`
$3\ 5$

`taste.out`
$1\ 2$

## Explanation

We choose a keyboard that prints $4$ distinct characters using $1$ command key and $2$ control keys. Other acceptable answers would be:
$2\ 1$ $\rightarrow$ prints $4$ characters.

$3\ 0$ $\rightarrow$ prints $3$ characters.
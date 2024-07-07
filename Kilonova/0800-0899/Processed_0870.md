
Natural numbers $A$ (composed of two or three distinct and non-zero digits) and $X$ (composed of $N$ digits, all non-zero) are considered.

From the number $X$, using all its $N$ digits, the largest natural number $Y$ **strictly less than $\textbf{X}$** can be constructed. For example, for $X=121621$, $Y=121612$ can be constructed.

Additionally, number $A$ can be obtained from $X$ by deleting some digits from $X$ and concatenating the remaining ones without changing their order. For example, if $X=121621$ and $A=12$, there are $Z=3$ distinct ways to obtain number $A$ from $X$, namely: 1) $\textbf{\textcolor{red}{12}} \sout{1621}$; 2) $\textbf{\textcolor{red}1} \sout{216} \textbf{\textcolor{red}2} \sout{1}$; 3) $\sout{12} \textbf{\textcolor{red}1} \sout{6} \textbf{\textcolor{red}2} \sout{1}$.

# Task

Given the numbers $A$, $N$, and the $N$ digits of $X$, determine:
1. the largest natural number $Y$, **strictly less than $\textbf{X}$**, that can be obtained by rearranging the digits of $X$;
2. the maximum number $Z$ of distinct ways in which the number $A$ can be obtained from $X$ by deleting some digits and concatenating the remaining ones without changing their order. 

# Input data

The input file `axyz.in` contains:
- the first line contains a natural number $p$; for all input tests, the number $p$ can only have the value $1$ or $2$;
- the second line contains the number $A$, as described in the problem statement;
- the third line contains the number of digits of the number $X$;
- the fourth line contains a sequence of $N$ digits, separated by a space, representing the digits of the number $X$ in that order.

# Output data

* If the value of $p$ is $1$, **only solve task $\textbf{1}$**. In this case, the output file `axyz.out` will contain a sequence of digits representing the determined natural number $Y$ (the answer to task $1$) on the first line.
* If the value of $p$ is $2$, **only solve task $\textbf{2}$**. In this case, the output file `axyz.out` will contain a natural number representing the determined number $Z$ (the answer to task $2$) on the first line.

# Constraints and clarifications

* $12 \leq A \leq 987$;
* $10 \leq N \leq 30\ 000$;
* For all test data, **the numbers $\textbf{Y}$ and $\textbf{A}$ can be obtained from the number $\textbf{X}$**.
* For correctly solving task $1$, $30\%$ of the score is awarded, and for correctly solving task $2$, $70\%$ of the score is awarded.

# Example 1

`axyz.in`
```
1
12
6
1 2 1 6 2 1
```

`axyz.out`
```
121612
```

## Explanation

Task $1$ is solved. $A=12$, $N=6$, $X=121621$.

The largest number $Y$ strictly less than $X$ is: $Y=121612$

# Example 2

`axyz.in`
```
2
12
6
1 2 1 6 2 1
```

`axyz.out`
```
3
```

## Explanation

Task $2$ is solved. $A=12$, $N=6$, $X=121621$.
There are $Z=3$ distinct ways to obtain the number $A$ from $X$:
1) $\textbf{\textcolor{red}{12}} \sout{1621}$;
2) $\textbf{\textcolor{red}1} \sout{216} \textbf{\textcolor{red}2} \sout{1}$;
3) $\sout{12} \textbf{\textcolor{red}1} \sout{6} \textbf{\textcolor{red}2} \sout{1}$.

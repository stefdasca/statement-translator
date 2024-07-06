The inhabitants of the planet Aritmo decided that in the famous year $2012$ they would explain to the Earthlings the "plus" method of adding natural numbers on their planet. Just like the planets, before addition, the numbers align so that they get as many identical digits as possible in the same positions. The identical digits, thus obtained, are eliminated from the two numbers. To get the final result, the two shifted numbers, obtained after elimination, are added together, as in the example.

~[ed2676e21dfefd43933c610366f07bcc.png|align=right]

*Example:* The numbers $18 \ 935$ and $85 \ 352$ align as in the adjacent figure. After elimination, the numbers $19$ and $52$ are obtained, which are added in a shifted manner to obtain the final result. Therefore, $18 \ 935 \ plus \ 85 \ 352 = 242$.

If there are multiple ways to align the numbers to eliminate the same maximum number of digits, then the numbers are aligned so that, after elimination and addition of the numbers according to the method described, a higher value is obtained.

~[cef02512f710ccbd2f8bf98819bc8978.png|align=right]

*Example:* $22 \ 331 \ plus \ 3 \ 322 = 33 \ 331$ (there are two ways in which the two numbers can be aligned to eliminate a maximum number of digits, with the maximum value obtained when the two digits $2$ are eliminated).

If two numbers $a$ and $b$ are identical or have no common digits, then $a \ plus \ b = 0$.

If all the digits of a number are eliminated, then the result is given by the remaining digits in the other number.

*Examples:* $23 \ plus \ 523 = 5, 562 \ plus \ 56 = 2.$

**Adding multiple numbers** is done from left to right: the first two numbers are added according to the method described above, then the result is added to the third number, and so on.

In an expression where multiple numbers are added, round brackets may appear. In the evaluation of such an expression, called a *parenthesized expression*, the additions inside the parentheses are performed first according to the method described above, with the parentheses then being replaced by the result of the additions inside the parentheses.

The **depth $A_E$** corresponding to a parenthesized expression $E$ is defined as follows:

* if the expression $E$ does not contain parentheses, then its depth is $0$;
* if the expression $E$ is of the form $(F)$, then $A_E=1+A_F$;
* if the expression $E$ is of the form $E1 \ plus \ E2 \ldots plus \ Ek$, then $A_E = \ max \ (A_{E1}, A_{E2}, \ldots , A_{Ek})$.

# Task

To help the Earthlings who wish to learn this new method of addition, write a program that reads a parenthesized expression and determines:

$a)$ the depth of the given expression;

$b)$ the value of this expression.

# Input data

The file `plus.in` contains the first line a natural number $n$. The next $n$ lines contain the description of the parenthesized expression. On each of these lines is a natural number or one of the values $-1$ or $-2$. The value $-1$ represents an open round bracket and the value $-2$ represents a closed round bracket.

# Output data

The output file `plus.out` will contain:
$a)$ the first line contains the natural number representing the depth of the given expression;

$b)$ the second line contains the natural number representing the result of evaluating the given expression, with the addition of the numbers according to the method described.

# Constraints and clarifications

* $1 < n \leq 2 \ 000$
* each of the other natural numbers in the file has at most $9$ digits
* in each parenthesis is at least one natural number
* if a parenthesis contains a single natural number, then the value of the expression is equal to the value of the number in the parenthesis
* for the correct solution of requirement $a)$ is awarded $20\%$ of the score, and for the correct solution of both requirements the full score is awarded.

# Example

`plus.in`
```
12
-1
1343
-1
234
4532
-2
-2
14091
-1
21
2
-2
```

`plus.out`
```
2
4639
```

# Explanation

The parenthesized expression to be evaluated is:

$(1 \ 343 \ plus \ (234 \ plus \ 4532)) \ plus \ 14 \ 091 \ plus \ (21 \ plus \ 2) = \\
(1 \ 343 \ plus \ 45 \ 334) \ plus \ 14 \ 091 \ plus \ (21 \ plus \ 2) = \\
4 \ 543 \ plus \ 14 \ 091 \ plus \ (21 \ plus \ 2)= \\
4 \ 543 \ plus \ 14 \ 091 \ plus \ 1= \\
46 \ 391 \ plus \ 1 = 4 \ 639$

The value of the expression is $4 \ 639$.

The depth of the expression is $2$, because:

* $A_{(1 \ 343 \ plus \ (234 \ plus \ 4 \ 532)) \ plus \ 14 \ 091 \ plus \ (21 \ plus \ 2)} = \ max \ (A_{(1 \ 343 \ plus \ (234 \ plus \ 4 \ 532))},A_{14 \ 091}, A_{(21 \ plus \ 2)} )=max \ (2,0,1)=2$
* $A_{(1 \ 343 \ plus \ (234 \ plus \ 4 \ 532))}= 1 + max \ (A_{1 \ 343}, A_{(234 \ plus \ 4 \ 532))} = 1 + max \ (0,1) = 2 A_{1 \ 343}=0$
* $A_{(234 \ plus \ 4 \ 532)} = 1 + A_{234 \ plus \ 4 \ 532} = 1 + 0 = 1$
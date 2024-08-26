The content of this page is not formatted according to formatting recommendations. If you have the necessary permissions, please improve it. Gigel, a second-year student (although he started college 4 years ago - what can you do, this Electronics..), has just learned about arithmetic expressions containing the operators $'+'$, $'*'$,$'^'$ and $'!'$, as well as parentheses ($'('$ and $')'$). However, being only in his second year, he gets confused when he has to work with numbers that are too large, so the only number that appears directly (i.e., not just as a result of an operation) in an expression is the number 1. We will call such an expression a 1-expression. For example, $( (1+(1*1))^(1+1+1*1)^(1+(1+1)!) )$ is a 1-expression, but $(2+5*7+6!+3^4^3!+1*6)$ is not a 1-expression (since the numbers 2, 3, 4, 5, 6, and 7 appear directly). A 1-expression can be viewed as a string consisting of the characters $'1'$, $'+'$, $'*'$, $'^'$, $'!'$, $'('$, $')'$ and can be described using the following grammatical rules:
1-expression = $'1' '(' 1-expression ')' 1-expression '+' 1-expression 1-expression '*' 1-expression 1-expression '^' 1-expression 1-expression '!'$
Although only the number 1 appears directly in the expression, the results of evaluating the operations can be numbers greater than 1, so Gigel will have to learn to use these numbers as well. To evaluate an arithmetic expression, the priorities of the operators must be known. 
The operator with the lowest priority is $'+'$ and performs the addition operation. The result of the 1-expression $ "1+1+1" $ is 3.
The $'*'$ operator has a higher priority than the $'+'$ operator and performs the multiplication operation. The result of the 1-expression $ "1+1*(1+1)*(1+1+1)+(1+1)*(1+1)" $ is $ 1+1*2*3+2*2=1+6+4=11 $.
The $'^'$ operator is more prioritized than the $'+'$ and $'*'$ operators and performs the exponentiation operation ($A^B$ represents $A$ raised to the power of $B$). The result of the 1-expression $ "(1+1)*(1+1+1)^(1+1)*(1+1+1)+(1+1)" $ is $ 2*3^2*3+2=2*9*3+2=54+2=56 $. Unlike the $'+'$ and $'*'$ operators which have the property that $A+B=B+A$ and $A*B=B*A$, in the case of $'^'$ it is not necessarily true that $A^B=B^A$ (except in some special cases). Another peculiarity of this operator is the order of application in the absence of parentheses: it is right-associative. For example, $ A^B^C^D$ is equivalent to $ A^(B^(C^D)) $. The result of the 1-expression $ ( (1+1)^(1+1)^(1+1+1) ) $ is $ 2^2^3=2^(2^3)=2^8=256$ and not $(2^2)^3=4^3=64$. Thus, if there are multiple $'^'$ operators not separated by parentheses, the order of operations is from right to left.
The operator with the highest priority is $'!'$ and performs the "factorial" operation. The result of the 1-expression $ ( (1+1+1)!) $ is $3!=6$. The factorial of a number $X$, denoted $X!$, is defined as $1 \cdot 2 \cdot \dots \cdot X$. The result of the 1-expression $( (1+1)*(1+1+1+1)!^(1+1+1)!!) $ is $ 2 \cdot 4!^3!!=2 \cdot (4!)^(3!!)=2 \cdot (4!)^((3!)!)=2 \cdot 24^(6!)=2 \cdot (24^720) $ (the result is a number too large to be displayed here).

The length of a 1-expression is defined as the number of characters in the string representing the 1-expression. The length of the 1-expression $ " (1+1)!^(1+1)*(1+1)+1 " $ is 20. The task that Gigel received at school is as follows: given a number $N$, find a 1-expression of minimum length whose result is equal to $N$. Help Gigel solve his homework.

## Input data
The first line of the input file `1expr.in` contains the integer $T$. The following $T$ lines each contain an integer $N$.

## Output data
In the output file `1expr.out` you will print $T$ lines. On the $K$-th line, you will print a 1-expression of minimum length whose result is equal to the $K$-th number among the $T$ given in the input file. If there are multiple 1-expressions of minimum length, you can print any of them.

## Constraints and clarifications
$ 1 \leq T \leq 100 $

$1 \leq N \leq 3^8$

## Example

`1expr.in`
```
3
1
3
200
```
`1expr.out`
```
1
1+1+1
(1+1)^(1+1+1)*(1+(1+1+1+1)!)
```
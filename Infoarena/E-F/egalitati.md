## Equalities

As homework, $Gigel$ has to write many equalities. The mathematics teacher, however, is too lazy to check the correctness of the calculations, so he prefers to make sure only that the parentheses are correctly placed. Thus, he writes all the parentheses in $Gigel$'s equalities (together with the equal sign between them - "$=$") on a single line, in the order $Gigel$ wrote them for his homework. The equalities are separated by "$;$". At the end of the string, the character "$.$" will be found. Due to the fact that this string is very large, the teacher seeks help: you have to tell him if these parentheses are correct or not.

## Input data

The input file `egalitati.in` contains a single line, the string of equalities written by the mathematics teacher.

## Output data

The output file `egalitati.out` will contain multiple lines, on each line $i$ containing the answer to the equality number $i$ from the string ($1$ for correct parenthesis placement, $0$ for incorrect parenthesis placement).

## Constraints

$1 \leq N \leq 100000$, where $N$ is the length of the string of equalities.

The string will always end with "$.$".

## Example

`egalitati.in`
`()=;()()=(((())()=()(())().`

`egalitati.out`
$1$ 
$0$ 

## Explanation

The first equality in $Gigel$'s homework is "`()=$`", in which the first equation is "`()`", and the second does not contain parentheses. Both being correct, the answer is $1$. The second equality consists of $3$ equations with the following parenthesis placements: "`()()`", "`(((())()`", "`()(())()`". Of these, the second is incorrect, so the answer is $0$.
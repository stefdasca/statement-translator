## Task

In the year $X$, the Maya people obtained $2$ strings composed of lowercase English letters. These $2$ strings could help them in predicting the future incorrectly and in finding out that on the date $21.12.2012$ the end of the world would appear. They had to correctly answer the following $Q$ questions in the form $(x, y)$ which represent: if we remove the sequence from the first string from position $x$ to position $y$ inclusive, and replace the sequence with the character $X$, how many odd-length palindromic sequences greater than $1$ exist that have their center fixed at the character $X$? Since initially they predicted the future well and found out that the end of the world would not come, they realized that the second string was of no use. Hence, they added an additional property which palindromic sequences must respect. At the first step of extending from the center $X$, the character extending the palindromic sequence must be the first character of the second string; at the second step of extension, the character must be the second character of the second string, and so on. More specifically, at the $i$-th step of extension, the character extending the palindromic sequence must be the $i$-th character of the second string. An extension step of a palindromic string is when you add a new character on both the left and right side of the string (it must be the same character to maintain the property of a palindromic string). Practically, an extension step enlarges the palindromic string by $2$ characters (one on the left and one on the right).

## Input data

The input file `x.in` will contain on the first line $3$ natural numbers $N$, $M$, $Q$. $N$ is the length of the first string, $M$ is the length of the second string, and $Q$ is the number of questions. The second line contains a string of $N$ characters representing the first string. The third line contains a string of $M$ characters representing the second string. The next $Q$ lines are the $Q$ questions in the form $(x, y)$.

## Output data

The output file `x.out` will contain $Q$ lines. On line $i$ you must print the answer to question $i$.

## Constraints and clarifications

$1 \leq N \leq 1 \ 000 \ 000$

$1 \leq M \leq 1 \ 000 \ 000$

$1 \leq Q \leq 500 \ 000$

## Example

`x.in`

```
5 4 1
badab
abac
3 3
```

`x.out`

```
2
```

## Explanation

The first step of extension will be done by the character $'a'$ and the second step will be done by the character $'b'$.
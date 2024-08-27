## Misakatelefon

Misaka recently started playing a new game on her phone. In this game, the phone displays a non-empty string of characters, with an initial length of at most $1000$. For this string, she can apply the following operations: 
1. Select a substring to delete ($a\ bc\ d$ becomes $ad$).
2. Select a substring to duplicate ($a\ bc\ d$ becomes $a\ bcbc\ d$).

After any operation, the string can have a length of at most $10^{18}$. The goal of the game is to generate a second string of characters, which also has a length up to $1000$, using at most $1011$ moves. Help Misaka win, or indicate if this is impossible!

## Input data

The input file `misakatelefon.in` will contain $T$ , the number of tests in the file. Each test will contain two lines. The first line contains the initial string that appears on Misaka's screen; the second line contains the final string that we want to generate.

## Output data

The output file `misakatelefon.out` will contain the answers for the various tests in order. For a test, if there is no solution, print the number $-1$. Otherwise, print a number $Q$, which represents the number of operations you use. Then print $Q$ lines, each of the form $t\ l\ r$ , meaning: delete (if $t = 0$) or duplicate (if $t = 2$) the substring that starts at position $l$ and ends before position $r$ (or up to the end of the string, if $r$ equals the length of the string), indexing from $0$.

## Constraints

$T \leq 1000$

The length of any input string $\leq 1000$

To solve the problem correctly, $Q \leq 1011$

To solve the problem correctly, the indices given in the output must refer to intervals that exist in the string at the time of the operation.

Any correct solution is accepted.

## Example

`misakatelefon.in`

```
2
abcabc
accc
abc
z
```

`misakatelefon.out`

```
8
2 0 6
2 0 12
2 0 24
0 24 48
0 18 23
0 12 17
0 4 11
0 0 3
-1
```
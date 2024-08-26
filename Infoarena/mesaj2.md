# Message2

A string of length $L$ is given. This string contains a hidden message and was obtained by concatenating the words forming the message and then inserting random characters at random positions in the string. $N$ lexicographers have decided to decipher the message. For this purpose, the lexicographers take turns (in order, from $1$ to $N$) and each lexicographer adds a word to a dictionary. Initially, the dictionary is empty. After adding the word, each lexicographer tries to discover the hidden message in the string. To do this, the lexicographer partitions the string into a maximum number of subarrays, such that each subarray contains as a subsequence one of the words existing in the dictionary at that moment. Therefore, the maximum number of subarrays the string is partitioned into actually represents the number of words in the message identified by the lexicographer (the words in the message are not necessarily distinct).

## Task

Find for each lexicographer the number of words in the message deciphered by them.

## Input data

The first line of the input file `mesaj2.in` contains the given string of characters. The second line contains the integer $N$ representing the number of lexicographers. Each of the following $N$ lines contains a string of characters. More precisely, the $i$-th line among these $N$ contains the word added to the dictionary by lexicographer $i$.

## Output data

The output file `mesaj2.out` will contain $N$ lines. The $i$-th line will contain the number of words of the message deciphered by lexicographer $i$.

## Constraints and clarifications

$1 \leq L \leq 1000$

$1 \leq N \leq 5000$

Both the words and the given string are composed of characters with ASCII codes from $33$ to $127$ (so they do not contain spaces)

The lengths of the words will not exceed $L$

There is a distinction between uppercase and lowercase letters ($a$ is different from $A$)

The sum of the lengths of the words is less than or equal to $10000$

A subarray of a string consists of consecutive characters from that string

A subsequence of a string consists of characters (not necessarily consecutive) of the respective string, in the order in which they appear in the string.

## Example

`mesaj2.in`
```
omuliosu
6
omul
iscusit
lis
om
ou
li
```

`mesaj2.out`
```
1
1
1
2
2
3
```

## Explanation

Possible messages (in the order they appear in the input file):
```
omul omul omul
or
lis om lis om lis
or
ou lis
or
om ou
or
ou ou om
li ou
or
ou li ou
```
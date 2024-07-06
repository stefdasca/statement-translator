**S**, a former informatics Olympiad participant, is trying to prevent security attacks on his network. Thus, he has a special character string he prefers to use as a password. To check if his password is strong enough, he created a list $L$ of size $K$ with hackers' preferred passwords. Being preventive by nature, he wants to perform the following operations on the password:

* **Insert**, a character $C$ is inserted at position $X$. In this case, all characters at positions greater than or equal to $X$ will move one position to the right, and the character $C$ will be inserted at position $X$.
* **Query**, it is asked whether the $Y$-th word in the password list matches the subarray of the same length ending at position $Z$ in the special string. The last character of the $Y$-th word must match the character at position $Z$, the penultimate character of the $Y$-th word must match the character at position $Z-1$, and so on.

# Task

Given the special character string, $K$ – the length of the word list, the $K$ words, and a sequence of $Q$ operations, answer the Query operations.

# Input data

The first line of the file `sir.in` contains the special string. The second line contains $K$, the length of the word list. The next $K$ lines contain the passwords in the list, one on each line. The next line contains $Q$, the number of operations. The next $Q$ lines describe these operations. A line describes an operation as follows:

* `0 poz c a b` - The first number, zero, represents the type of operation, i.e., **insert**. $C$ represents the character to be inserted. Using $poz, a$ and $b$, we calculate the position where the character will be inserted. If the result of the last Query operation was $0$, then the position where the character is inserted will be calculated using the formula: $poz \\oplus a$ (where the operator $\\oplus$ represents exclusive or – xor). If the result of the last Query operation was $1$, then the position where the character is inserted will be calculated using the formula: $poz \\oplus b$. If the current operation was not preceded by any Query operation, then the position where the character is inserted will be calculated using the formula: $poz \\oplus a$.
* `1 poz ind a b` - The first number, one, represents the type of operation, i.e., **query**. The third number, $ind$, represents the index of the word in the list on which we perform the query operation. Using $poz, a$ and $b$, we calculate the position where the $ind$-th word in the password list ends. If the result of the last Query operation was $0$, then the position for the query operation will be calculated using the formula: $poz \\oplus a$ (where the operator $\\oplus$ represents exclusive or – xor). If the result of the last Query operation was $1$, then the position for the query operation will be calculated using the formula: $poz \\oplus b$. If the current operation was not preceded by any Query operation, then the position for the query operation will be calculated using the formula: $poz \\oplus a$.

# Output data

For each query operation, print $0$ if the word does not match, and $1$ if it matches.

# Constraints and clarifications

* It is guaranteed that the sum of the lengths of the words from the dictionary is less than $800 \ 000$.
* It is guaranteed that the maximum length of the special string does not exceed $60 \ 000$ after all Insert operations have been performed.
* The number of operations is less than or equal to $85 \ 000$.

# Example

`sir.in`
```
photoshop 
2 
hoto 
goto 
4 
1 14643 1 14646 27787 
0 88412 g 38665 88415 
1 41453 2 37823 41451 
1 78120 1 98233 78125
```

`sir.out`
```
1 
1 
0
```

## Explanation

After the xor operation, the file transforms into:

```
photoshop 
2 
hoto 
goto 
4 
1 5 1
0 3 g
1 6 2 
1 5 1
```
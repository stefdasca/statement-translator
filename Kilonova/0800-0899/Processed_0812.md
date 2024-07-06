Algorel received a game that contains $n$ tokens with capital letters of the alphabet written on them. Each letter is associated with a code consisting of a single non-zero digit. The tokens are arranged in the given initial order, and by reading the letters from the first to the last token, a word is formed. If the numbers on each token are read starting from the first to the last, a number $k_1$ is obtained. The game continues in the same way, but the tokens are arranged starting from the second to the last, resulting in a new number $k_2$. Then, the tokens are arranged starting from the third to the last, resulting in a new number $k_3$, and so on, until only the last token is arranged, in which case the number $k_n$ is obtained.

# Task

Write a program that reads the number $n$ of tokens, the $n$ letters associated with the tokens, as well as the codes associated with the letters, in the order they appear, and displays:

* the number of pairs of consecutive letters in the initial word that have the property that one letter is a vowel and the other is a consonant (the order does not matter);
* the number $k_1$, formed from the initial arrangement of the tokens;
* the sum $k_1 + k_2 + \dots + k_n$.

# Input data

The input file `litere.in` will contain on the first line the value of $n$, representing the number of tokens, the second line will contain a word formed from $n$ capital letters (from `A` to `Z`); the letters are written one after another without being separated by spaces, so that the first letter is on the first token, the second letter on the second token, and so on. On the third line of the file there is a number $m$ representing the number of distinct letters, and on the fourth line $m$ values representing the codes of the distinct letters that appear in the word. The codes are given in the order of appearance of the letters in the word and are non-zero natural numbers consisting of a single digit, separated by a space, with the code for each letter given only once, even if the letter repeats.

# Output data

The output file `litere.out` will contain on the first line the number of pairs of consecutive letters in the word that have the property that one letter is a vowel and the other is a consonant (the order does not matter), on the second line the number $k_1$ (formed from the initial arrangement of the tokens), and on the third line the sum $k_1 + k_2 + \dots + k_n$.

# Constraints and clarifications

* $0 < n \leq 10 \ 000$;
* $0 < m < 27$;
* Partial scores are awarded as follows:
    - $20$% for correctly displaying the value on the first line of the output file (requirement $1$);
    - $40$% for correctly displaying the value on the second line of the output file (requirement $2$);
    - $40$% for correctly displaying the value on the third line of the output file (requirement $3$).

# Example 1

`litere.in`
```
3
CSC
2
1 2
```

`litere.out`
```
0
121
143
```

## Explanation

There are no pairs of consecutive letters that meet the requirement. There are $2$ distinct letters: `C` and `S`. $code($`C`$) = 1$, $code($`S`$) = 2$. $k_1 = 121$, $k_2 = 21$, $k_3 = 1$, and $k_1 + k_2 + k_3 = 121 + 21 + 1 = 143$.

# Example 2

`litere.in`
```
6
CABABE
4
2 5 6 7
```

`litere.out`
```
5
256567
320342
```

## Explanation

There are $5$ pairs of consecutive letters that meet the requirement: `CA`, `AB`, `BA`, `AB` and `BE`. There are $4$ distinct letters: `C`, `A`, `B` and `E`. $code($`C`$) = 2$, $code($`A`$) = 5$, $code($`B`$) = 6$, $code($`E`$) = 7$. $k_1 = 256567$, $k_2 = 56567$, $k_3 = 6567$, $k_4 = 567$, $k_5 = 67$, $k_6 = 7$, and $k_1 + k_2 + k_3 + k_4 + k_5 + k_6 = 256567 + 56567 + 6567 + 567 + 67 + 7 = 320342$.
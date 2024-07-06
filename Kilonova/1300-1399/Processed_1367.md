Maria and Ionuț want to communicate with each other through notes. To ensure their messages remain confidential and are not understood by their classmates, they decide to encode them. To encode a message, Maria and Ionuț follow these steps:
* They jointly select a word $s$ called the key, consisting of $p$ distinct letters, two by two.
* They split the message they want to transmit into sequences of adjacent characters of length $p$, except for the last sequence which might contain fewer than $p$ characters.
* They write the chosen key word on paper.
* Under the chosen key word, they write the previously determined sequences of length $p$, in the order they were obtained.
* The encoded message is obtained as follows:
  * They traverse the obtained table, column by column, from top to bottom.
  * The order of traversal of the columns is the alphabetical order of the letters in the key word.

# Task

Write a program that determines the letter in the encoded message that appears the least frequently, and if there are multiple such letters, the first one in alphabetical order, and to decode a message encoded in the manner previously presented.

# Input data

The input file `mesaj.in` contains:
* The first line contains the number $p$ of characters in the key
* The second line contains the key word chosen by Maria and Ionuț
* The third line contains the number $n$ of characters in the encoded message
* The fourth line contains the encoded message

# Output data

The output file `mesaj.out` will contain:
* On the first line the letter from the encoded message that appears the least frequently in the encoded message; if there are multiple such letters, the first one in alphabetical order
* On the second line print the decoded message

# Constraints and clarifications

* The key word contains only uppercase English letters (`A`, `B`, `C`, ..., `Z`) and has at most $26$ letters
* The encoded message contains uppercase English letters, and words are separated by one or more spaces
* $1 \leq p \leq 26$
* $p \leq n \leq 2\ 000$
* Partial scores:
  * $20\ \%$ for correctly displaying the value on the first line of the output file `mesaj.out` (requirement $a$)
  * $80\ \%$ for correctly displaying the message on the second line of the output file `mesaj.out` (requirement $b$)

# Example

`mesaj.in`
```
8
COMPUTER
44
SAAO T PTDMCOAANCU DNIICL LFALIIEASMA REINAO
```

`mesaj.out`
```
F
SUCCES LA OLIMPIADA NATIONALA DE INFORMATICA
```

## Explanation

Maria and Ionuț choose the key word $\\text{COMPUTER}$
The message they want to encode is $\\text{SUCCES LA OLIMPIADA NATIONALA DE INFORMATICA}$
The obtained table is as follows:
~[mesaj.png|align=center]
The required letter is `F` and the encoded message is $\\text{SAAO T PTDMCOAANCU DNIICL LFALIIEASMA REINAO}$


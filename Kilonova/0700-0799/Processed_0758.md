In order to ensure the most accurate transmission of information over the network, the transmission is done character by character, with each character given by its ASCII code, i.e., a group of 8 bits (octet). For each 8 bits transmitted, a parity bit is calculated, which is $0$ (if the ASCII code of the character contains an even number of binary digits $1$) or $1$ (otherwise). Since only standard ASCII characters, having ASCII codes in the range $[32, 127]$, are transmitted in our problem, their ASCII code has the 7th bit (the leftmost bit) equal to $0$. The parity bit will be placed in this position, thereby saving one bit for each transmitted character. For example, if the message to be transmitted contains the characters `Parity`, the transmitted bit sequence will be:
$\textcolor{red}{0}1010000\ \textcolor{red}{1}1100001\ \textcolor{red}{0}1110010\ \textcolor{red}{0}1101001\ \textcolor{red}{0}1110100\ \textcolor{red}{1}1100001\ \textcolor{red}{0}1110100\ \textcolor{red}{0}1100101$

Additionally, besides the mentioned characters, the message may also contain a special character indicating the transition to the beginning of a new line. This character has the ASCII code $10$.

# Task
Write a program that verifies whether a text has been transmitted correctly.

# Input data
The input file `parity.in` contains in the first line a sequence of `0` and `1` characters representing the transmitted message. There are no spaces between the characters. The line ends with the newline character (`\n`).

# Output data
The output file `parity.out` contains in the first line the message `YES` if the text was transmitted correctly or `NO` otherwise. If the message on the first line is `YES`, the following lines will contain the transmitted text in clear text. If the message on the first line is `NO`, the next line will contain the order numbers of the characters that were not transmitted correctly, in strictly increasing order, separated by a space.

# Constraints and clarifications
- The 8 bits of the ASCII code of a character are numbered from $0$ to $7$, from right to left, the leftmost bit being bit $7$ and the rightmost bit being bit $0$.
- The transmitted text has at most $60\ 000$ characters.
- The number of `0` and `1` characters in the first line of the input file is a multiple of $8$.
- The ASCII codes of the characters in the text belong to the set $\{10, 32, 33, 34, \dots, 127\}$, the code $10$ meaning the transition to the beginning of a new line (newline).
- No line in the output file will have more than $255$ characters.
- The characters in the text are numbered starting from $0$.
- The messages `YES`/`NO` in the first line of the output file are written in uppercase.

# Example 1
`parity.in`
```
0101000011100001011100100110100101110100111000010111010001100101
```
`parity.out`
```
YES
Parity
```
## Explanation
All codes are correct.

# Example 2
`parity.in`
```
1101000011100001111100100110100101110100111000010111010011100101
```
`parity.out`
```
NO
0 2 7
```
## Explanation
The first character was transmitted as the bit sequence $11010000$ which means that without the parity bit, there should have been an odd number of digits $1$, which is false. Therefore, the character was not transmitted correctly. The same applies for the characters with order numbers $2$ and $7$.

# Example 3
`parity.in`
```
010000011111101001101001000010100110010100001010011010100110111101101001
```
`parity.out`
```
YES
Today
is
Thursday
```
## Explanation
All codes are correct. The text contains two characters with ASCII code $10$.
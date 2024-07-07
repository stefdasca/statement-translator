
Great Mistrust between Ionel and Marioara, two students attending a camp at Galațiuc...! To avoid the curiosity of their colleagues, the two decided to send messages to each other using a simple encryption method: the text to be encrypted is written on a sheet, arranging the letters of the words in a table having $5$ characters on each line. The space between words is also a character. The text thus arranged on a sufficient number of lines to fit is read by columns, top down and left to right. Instead of spaces between words, dots are placed. Dots are also placed at the end of the text, as many free spaces are left at the end of the text placed in the table.

For example, the text: `Te astept dupa cina la ora 8`, will be arranged in a table as follows:

|1|2|3|4|5|
|-|-|-|-|-|
|T|e| |a|s|
|t|e|p|t| |
|d|u|p|a| |
|c|i|n|a| |
|l|a| |o|r|
|a| |8| | |

and will be encoded as: `Ttdclaeeuia..ppn.8ataao.s...r.`.

Decoding the message will be done in reverse of the encoding.

Help them by creating a program that encodes and decodes the messages of the two children. To differentiate the messages that need to be encoded from those that need to be decoded, the first character of the message will be $C$ or $c$ for encoding, and $D$ or $d$ for decoding. This character will not be part of the message.

# Input data

The first line of the input file `cod-secret.in` contains a string of characters. The strings of characters may also contain spaces.

# Output data

The first line of the output file `cod-secret.out` will contain the encoded or decoded string, as appropriate.

# Constraints and clarifications

* The length of the string of characters is at most $1\ 001$.

# Example 1

`cod-secret.in`
```
CAm un mar
```

`cod-secret.out`
```
A.mm.aurn.
```

# Example 2

`cod-secret.in`
```
dTaGia.aubllcaaa.r.c.
```

`cod-secret.out`
```
Tabara la Galaciuc
```

Gigel and Vasilică imagine a way to transmit messages that no one can decipher. The message is hidden in a text that has $N$ lines, with exactly $N$ characters on each line – uppercase letters of the English alphabet, digits, punctuation marks, and the space character.

Decoding is done with the help of a template, of the same dimensions as the text, which has several holes. By overlaying the template on the text, some characters become visible. They are read in the order of the lines, from top to bottom, and on the same line from left to right. Then the paper with the text is rotated to the left, counterclockwise, by ${90\\degree}$, with the template remaining fixed. Other characters become visible and they are read in the same way. The operation is repeated two more times (rotation by ${180\\degree}$, respectively by ${270\\degree}$), until the text reaches, through another rotation by ${90\\degree}$, the initial position again.

Unfortunately, the template for encoding/decoding has been lost. However, Gigel has kept the initial message while Vasilică has the text that contains the message.

# Task

Reconstruct the template that was used for encoding.

# Input data

The input file `sablon.in` contains on the first line the initial message. The second line of the input file contains the value $N$.

The following $N$ lines contain the text that hides the message.

# Output data

The output file `sablon.out` contains $N$ lines, each with $N$ characters. The characters are `O` (representing a hole) and `X`.

# Constraints and clarifications

* When rotating the text, none of the holes will overlap any positions taken by a hole in the previous positions of the text.
* $1 \leq N \leq 50$
* The message has a maximum of $1\ 000$ characters and ends with a character different from space.
* If there are multiple solutions, display one of them.

# Example

`sablon.in`
```
CODIFICARE CU SABLON
10
ABCDCEFAGH
IJOKLEMNOP
DQRSTUVWCX
YZAIBCRDEF
GFHIJKLMNI
AJKLMNOPSQ
RSTOUV WXY
ZBABCDEFGU
HIJKNLMCNO
PQLRS TUVW
```

`sablon.out`
```
XXXXOXXXXX
XXOXXXXXXX
OXXXXXXXXX
XXXOXXXXXX
XOXXXXXXXX
XXXXXXXXXX
XXXXXXXXXX
XXXXXXXXXX
XXXXXXXXXX
XXXXXXXXXX

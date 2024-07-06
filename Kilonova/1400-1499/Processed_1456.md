~[mesaj.png|align=right]

In Piticot's country, the words have only two letters, the first being an uppercase letter and the second a lowercase letter. The dwarves *Mi* and *Gi* entertain themselves and send messages by hiding words within sequences transmitted as strings of letters. Dwarf *Mi* writes and sends a message to dwarf *Gi* following these rules:

* A message contains one or more sequences;
* Any letter that appears in the message, at least twice, on consecutive positions, is called a *terminator*;
* A sequence ends when a succession of *terminator* letters is encountered;
* The word is formed from the first uppercase letter and the last lowercase letter from the sequence, without considering the sequence's *terminator* letter;
* A sequence hides a word if its *terminator* repeats **exactly** twice and if it contains at least one uppercase letter and one lowercase letter, ignoring the *terminator* of the sequence;
* The cost of a word is equal to the total number of appearances of the two letters it is made up of, within the sequence in which it was hidden, including the *terminator* letters.

For example, the sequence `s f u E e t R u E E` hides a word because it contains both uppercase and lowercase letters, and the sequence's *terminator* letter, `E`, repeats exactly twice. The sequence hides the word `Eu`, and the cost of the word is $5$ ($3$ letters `E` + $2$ letters `u`). Upon receiving the message, dwarf $Gi$ determines, for each uppercase letter, the maximum cost of the words that begin with it.

# Task

Write a program that determines:

1) the number of sequences sent that do not hide words;
2) the words in the message, in the order they were sent by dwarf *Mi*
3) for each uppercase letter, how many words that start with it have the maximum cost determined by *Gi*.

# Input data

The input file `mesaj.in` contains on the first line a natural number $P$. For all input tests, the number $P$ can only have one of the values $1$, $2$, or $3$. The second line of the input file contains the natural number $N$ representing the number of letters used by *Mi* for writing the message. The third line contains $N$ uppercase and lowercase letters of the English alphabet, separated by spaces, representing the message letters, in the order they were sent.

# Output data

If $P$ value is $1$, only requirement $1)$ from the task will be solved. In this case, the output file `mesaj.out` will contain on the first line a natural number representing the answer to requirement $1)$.  
If $P$ value is $2$, only requirement $2)$ from the task will be solved. In this case, the output file `mesaj.out` will contain the words from the message, each word written on a separate line, in the order they were sent.  
If $P$ value is $3$, only requirement $3)$ from the task will be solved. In this case, the output file `mesaj.out` will contain each line an uppercase letter followed by a non-zero natural number, separated by a space. The uppercase letters will be displayed in order from `A` to `Z`, but only those for which there were words in the message that started with them.

# Constraints and clarifications

* $1 \leq N \leq 2 \ 000 \ 000$
* The sequence's *terminator* letter can be either lowercase or uppercase;
* The last letters in the file are the *terminator* letters of the last sequence in the sent message;
* It is guaranteed that there is at least one hidden word in the string of letters from the input file;
* The uppercase letters of the English alphabet are `A`, `B`, ..., `Z`;
* For $50\%$ of the tests $N \leq 1 \ 000 \ 000$
* Solving requirement $1)$ earns $20$ points
* Solving requirement $2)$ earns $40$ points
* Solving requirement $3)$ earns $40$ points.

# Example 1

`mesaj.in`
```
1
34
w w w w e D o r F D o r r t R n e R e y y j j i M o e i t t t j w w
```

`mesaj.out`
```
4
```

## Explanation

The text contains six sequences:
1) `w w w w`
2) `e D o r F D o r r`
3) `t R n e R e y y`
4) `j j`
5) `i M o e i t t t`
6) `j w w`

There are $4$ sequences that do not hide words:
* the first and fourth sequences because they contain only the *terminator*;
* the fifth sequence does not decode because the *terminator* repeats more than twice;
* the sixth sequence does not contain uppercase letters

# Example 2

`mesaj.in`
```
2
34
u N a a e D o r F D o r r t R n e R e y y j j i M o e i t t t j w w
```

`mesaj.out`
```
Nu
Do
Re
```

## Explanation

The text contains six sequences:
1) `u N a a`
2) `e D o r F D o r r`
3) `t R n e R e y y`
4) `j j`
5) `i M o e i t t t`
6) `j w w`

The first sequence has the *terminator* `a` which repeats twice and hides the word `Nu`
The second sequence has the *terminator* `r` and hides the word `Do`.
The third sequence has the *terminator* `y` and hides the word `Re`.
The last three sequences do not hide words.

# Example 3

`mesaj.in`
```
3
24
A a t t B b B t t e A e a n n B w I I F i e F F
```

`mesaj.out`
```
A 2
B 1
F 1
```

## Explanation

The text contains five sequences:
1) `A a t t`
2) `B b B t t`
3) `e A e a n n`
4) `B w I I`
5) `F i e F F`

The words sent in the message are:
`Aa` (cost $2$)
`Bb` (cost $3$)
`Aa` (cost $2$)
`Bw` (cost $2$)
`Fe` (cost $4$)
The maximum cost of the words that start with `A` is $2$ and there were $2$ words sent. For the letter `B`, a single word with a maximum cost of $3$ was sent. For the letter `F`, one word with a maximum cost of $4$ was sent.

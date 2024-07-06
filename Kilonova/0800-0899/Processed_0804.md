Ion Petre, like any adolescent, is passionate about both games and computer science. The latest such game is to eliminate words from a text so that each remaining word is followed by a word that starts with the same letter as the previous word ends with. The only exception to this rule is the last word.

# Task

For a given text:
1) Display the **minimum** number of words that can be eliminated so that in the remaining text any word (except the last one) ends with the same letter that the next word starts with;
2) Display the number of words in the text;
3) Display the words in the text that remain after eliminating those in the first task, each word being displayed on a separate line.


# Input data

The file `text.in` contains a text written on multiple lines. Each line contains words made up of lowercase Latin letters. The words are separated by exactly one space.

# Output data

The file `text.out` will contain on the first two lines two numbers $x$ and $y$, where $x$ will be the minimum number of words that need to be eliminated, and $y$ the number of words in the text. On the following lines, the remaining words after eliminating those $y$ words will be printed, one word per line.

# Constraints and clarifications

* The maximum number of words in the text is $20\ 000$.
* The maximum length of a word is $20$.
* Each line of text in the input file has at most $200$ characters.
* There may be empty lines in the input file.
* $30\\%$ of the total score is awarded for correctly solving the first task.
* $40\\%$ of the total score is awarded for correctly solving the first two tasks.
* The total score is awarded for correctly solving all the tasks.
* **Note**: The example in the PDF is displayed in reverse order compared to how it is displayed in the tests.

# Example

`text.in`
```
pentru ca nu are

timp ion spune ca nu urmareste nici
emisiuni interesante si evident nici altfel
de

emisiuni
```

`text.out`
```
13
19
ion
nu
urmareste
emisiuni
interesante
evident
```

## Explanation

From the entire text which is made up of $19$ words, $13$ words are eliminated and the resulting words, in order, are:
* `ion`
* `nu`
* `urmareste`
* `emisiuni`
* `interesante`
* `evident`
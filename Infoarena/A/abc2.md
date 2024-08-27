## Task

The alphabet of the Makako language consists of only 3 symbols: $a$, $b$, and $c$. Any word in this language is a string formed from a finite number of symbols from the alphabet (just like in most languages used today). However, not all sequences of symbols form meaningful words. According to the Makako language dictionary, only certain sequences of symbols represent meaningful words (henceforth, by the word we will refer to one of these meaningful sequences of symbols). A particular feature of the Makako language is that any two words have exactly the same length. Recently, an ancient text has been discovered which is thought to be written in an old dialect of the Makako language. To verify this hypothesis, scientists want to determine in which positions of the text meaningful words from the language occur. The text can be viewed as a sequence of $L$ symbols from the Makako alphabet, where the positions of the symbols are numbered from $1$ to $L$. If a word from the language appears as a continuous sequence of symbols in the text and its starting position is $P$, then $P$ represents a candidate position. The scientists want to determine the number of candidate positions in the text. Suppose the Makako language dictionary contains only the following 3 words: $bcc$, $aba$, and $cba$, and the discovered ancient text is $cababacba$. The word $aba$ can be found at positions $2$ and $4$ in the text. The word $cba$ can be found at position $7$. The word $bcc$ does not appear in the text. Therefore, there are 3 candidate positions in the text.

## Input data

The first line of the input file `abc2.in` contains the ancient text that needs to be analyzed. The following lines, until the end of the file, each contain one word from the Makako language dictionary.

## Output data

In the output file `abc2.out`, you will print a single number representing the number of candidate positions found within the ancient text.

## Constraints and clarifications

The ancient text consists of at most $10\ 000\ 000$ characters.  
The Makako language dictionary will contain at most $50\ 000$ words.  
Words have a length of at most $20$ characters.  
Due to the difficulty faced by those who wrote the dictionary in working with such a large number of words, it is possible that some words may appear multiple times in the dictionary.

## Example

`abc2.in`
```
bbcabbabcba
abba
bbca
abcb
bbca
aaaa
```

`abc2.out`
```
3
```
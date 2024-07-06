It appears that extraterrestrial life hunters have finally discovered something! During the SETI@home project, a sequence was isolated that could represent a signal from other intelligent life forms. Consequently, the SETI@ONI project aims to verify if this signal truly originates from extraterrestrials or just from some kids drinking Fanta.

# Task
For convenience, the portion of the signal that needs to be analyzed is available to you as a succession of Latin alphabet letters. You are also provided with a dictionary of extraterrestrial words, encoded in the same way. Your goal is to count how many times each of these words appears in the potential extraterrestrial message. Based on this data, linguists can start working on translating the message.

# Input data
The first line of the input file `seti.in` contains the number $N$ of lines of the message. The next $N$ lines, each containing exactly $64$ letters of the Latin alphabet followed by the end-of-line marker, represent the message to be analyzed, formed by joining these pieces, consisting of $64 \times N$ letters. The following line contains the number $M$ of words in the dictionary. The next $M$ lines, each containing a word from the dictionary, represented as a sequence of at least one and at most $16$ letters. The words are not necessarily distinct.

# Output data
The output file `seti.out` will contain exactly $M$ lines. On line number $i$, the number of occurrences in the extraterrestrial message of the word number $i$ from the dictionary will be printed. The number of occurrences will never exceed $65535$. Any occurrence of a word must be counted, even if it overlaps with other occurrences. There will be a distinction between uppercase and lowercase letters.

# Constraints and clarifications
* $0 \leq N < 2\ 048$;
* $0 \leq M \leq 32\ 000$.

# Example

`seti.in`
```
2
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaBaba
babaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaBaB
3
b
bab
b
```

`seti.out`
```
3
2
3
```

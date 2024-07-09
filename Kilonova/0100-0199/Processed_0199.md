A string of characters consisting of `N` lowercase letters from the Latin alphabet is given, representing a phrase; there are no spaces between words. A vocabulary is also given, consisting of `M` words that are not necessarily different and do not appear in a predetermined order.

# Task
Separate the phrase into a minimum number of words; all these words must exist in the given vocabulary.

# Input data
Input file: `textmare.in`

- The first line contains the phrase which needs to be split into words;
- The next line contains the number of words in the vocabulary;
- The following lines each contain one word from the vocabulary;

# Output data
Output file: `textmare.out`
The file consists of the phrase split into words. There will be exactly one blank space between any two consecutive words. The file will end with an empty line. If there is no solution, the output file will only contain the digit `0`;

# Constraints and clarifications:
* Let `S` be the total number of characters in the dictionary.
* For `25` points: `1 \ \leq N, M \ \leq 1\ 000` and each word in the vocabulary has at most `16` characters.
* For another `35` points: `1 \ \leq N, M \ \leq 32\ 000` and each word in the vocabulary has at most `16` characters.
* For another `40` points: `1 \ \leq N \ \leq 100\ 000, 1 \ \leq M \ \leq 500\ 000, 1 \ \leq S \ \leq 500\ 000`.
* If there are multiple solutions, only one will be produced at the output;
* In a phrase, a single word from the vocabulary can appear multiple times.

# Example

`textmare.in`
```
acestaesteuntext
8
text
acesta
acest
a
care
este
un
simplu
```

`textmare.out`
```
acesta este un text

```
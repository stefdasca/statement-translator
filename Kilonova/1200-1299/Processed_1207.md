
The Dragon Arhirel decides to learn biology, so he wants to buy the 10th-grade textbook. Unfortunately, it is no longer available on the market, but Arhirel manages to find a copy from a friend. After starting to read, Arhirel notices that there are mistakes in his friend's copy, and in a burst of energy, he decides to correct the textbook. He has a dictionary of $M$ words from which he needs to extract variants for the incorrect word. Regarding the incorrect word, the dragon can make the following changes to turn it into a variant from the dictionary:
- he can delete a letter;
- he can insert a letter;
- he can change one letter to another letter.
However, the Dragon Arhirel is lazy, so he does not want to perform more than $K$ changes to the incorrect word to bring it to a correct form (existing in the dictionary).

# Task

Help the Dragon Arhirel find out which words from the dictionary could be variants of the incorrect word.

# Input data

The input file `cuvinte.in` contains the following on the first line: two numbers $M$ and $K$, separated by a space, representing the number of words in the dictionary and the maximum number of changes that can be made to the incorrect word. The second line contains, separated by a space, the length of the incorrect word, $L_{word}$, and the incorrect word. The next $M$ lines contain the words from the dictionary, one word per line in the following format: on line $i$, the length $L_{i-2}$ of word $i-2$, separated by a single space from word $i-2$.

# Output data

The output file `cuvinte.out` will contain $M$ lines. On line $i$ there is the value $1$ if word $i$ from the dictionary is a variant for the given incorrect word, or the value $0$ otherwise.

# Constraints and clarifications

* $0 < M < 21$
* $0 < K < 31$
* $0 <$ length of any word (including the incorrect one) < $10 \ 001$
* Words are formed only from Latin alphabet letters, and lowercase letters are different from uppercase letters (for example, `Z` is not the same as `z`).

# Example

`cuvinte.in`
```
6 2
6 radiux
5 ladin
6 Radius
6 ridica
5 radio
6 adipos
5 cadiu
```

`cuvinte.out`
```
0
1
0
1
0
1
```

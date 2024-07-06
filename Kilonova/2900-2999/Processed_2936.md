Sure, here is the translated text:

---

Viitorel, preparing intensely for international competitions, wants to learn as many languages as possible (currently, he is focusing on just one). For this, he must first know the sounds of the language and how words are formed. He opens the manual and observes that at the beginning there are presented two strings of characters: $w$ representing the sequence of vowels and $k$ representing the sequence of consonants.

Moreover, this language has strict rules regarding the form a syllable can have. The *pattern* of a syllable represents a string consisting of the characters `C` (mandatory consonant), `c` (optional consonant) and `V` (vowel). There is **exactly** one vowel in each syllable.

For example, a syllable can have the pattern `cCVc`, meaning a vowel preceded by one or two consonants and followed by a consonant or none. Considering the sequences $w$ and $k$ corresponding to the Romanian language, the word `revista` can be split into syllables according to that pattern (`re-vis-ta`), while the word `ziar` cannot, because the vowel `a` is not preceded by a consonant.

# Task

Viitorel tried to speak a sentence in the language he is learning, but he got stuck and asks you for help.

1. Determine how many valid syllable splits each word in the sentence has.
2. To make his work easier, Viitorel takes each word and rearranges its letters (in all possible ways). Calculate, for each word in the sentence, how many of these rearrangements are valid words (including the initial word).

# Input data

The file `polyglot.in` will contain:
* The first two lines contain the strings $w$ and $k$.
* The third line contains the pattern of a syllable.
* The fourth line contains the natural numbers $C$ and $N$ separated by a space, representing the task that needs to be solved, respectively the number of words in the sentence.
* The fifth line contains $N$ words separated by a space.

# Output data

The file `polyglot.out` will contain on the first line $N$ natural numbers, representing the answers to task $C$, **modulo $10^9 + 7$!**

# Constraints and clarifications

* The sounds of the language are only vowels and consonants, not semivowels.
* Each sound represents a unique letter and vice versa (there is a bijection between sounds and letters).
* The strings $w$ and $k$ are formed from lowercase English alphabet letters.
* $w \cap k = \varnothing$
* $c \subset (w \cup k)$, for any word $c$ in the sentence.
* It is guaranteed that the pattern of a syllable has exactly one vowel.
* A syllable has between $1$ and $100$ sounds inclusive.
* A word has between $1$ and $2\ 000$ letters inclusive.
* $1 \leq N \leq 50\ 000$.

# Example 1

`polyglot.in`
```
aeiou
bcdfghjklmnpqrstvwxyz
cCVc
1 3
revista este scumpa
```

`polyglot.out`
```
2 0 2
```

## Explanation

Task 1 is solved. The first word has two valid syllable splits (`re-vis-ta`, `re-vi-sta`), the second has none (the first `e` is not preceded by a consonant), the last has two (`scum-pa`, `scu-mpa`).

# Example 2

`polyglot.in`
```
aeiou
bcdfghjklmnpqrstvwxyz
cCVc
2 2
cumpar masa
```

`polyglot.out`
```
192 2
```

## Explanation

Task 2 is solved. The second word can be arranged as `masa` or `sama`.
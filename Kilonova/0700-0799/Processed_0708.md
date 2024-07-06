Here's the translated text, preserving the original structure, format, and syntax, adapted to English:

---

A word consisting only of lowercase letters is given. We call an anagram a word formed from the letters of the given word, possibly changing the order of the letters. For example, an anagram of the word tamara is the word armata. Obviously, a word can be considered an anagram of itself.

# Task

Write a program that generates all anagrams of a given word in lexicographical order.

# Input data

The input file `anagrame.in` contains on the first line the given word.

# Output data

The output file `anagrame.out` will contain in order the anagrams of the given word, one per line.

# Constraints and clarifications

* The given word has at most $10$ lowercase letters.
* The word $x = x_1 \\ x_2 \\dots x_n$ precedes the word $y = y_1 \\ y_2 \\dots y_n$ if there exists an index $k \\in \{1, 2, \\dots, n\}$ such that $x_i = y_i$, $i \\in \{1, 2, \\dots, k - 1\}$, and the letter $x_k$ precedes the letter $y_k$ in the alphabet.

# Example

`anagrame.in`
```
ana
```

`anagrame.out`
```
aan
ana
naa
```


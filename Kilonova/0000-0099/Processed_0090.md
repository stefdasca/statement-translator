Here is the translated text:

---

The Ratină language has only `N` words, numbered from `1` to `N`. Two or more words are called `k`-similar if they have the first `k` identical letters. 

The degree of similarity between `t` words is `k` if the `t` words are `k`-similar but not `(k+1)`-similar.

# Task
Write a program that for a given set of `t` words, responds to queries like: "What is the degree of similarity between words $x_1 x_2 ... x_t$" ?

# Input data
The input file `ratina.in` will contain on the first line two natural numbers `N`, `M` separated by a space, representing the number of words in the Ratină language, and the number of queries, respectively. The following `N` lines will contain the words in the Ratină language, one word per line. Specifically, on line `i+1` the word with the order number `i` is written. The words are formed of lowercase letters from the English alphabet. The next `M` lines, each representing a query, contain: the first number on the line, a natural number `t` representing the number of words in the query, then follow the `t` order numbers of the words in the query, separated by spaces.

# Output data
The output file `ratina.out` will contain `M` lines, one for each query from the input file. Each line `i` will contain the degree of similarity of the words in query `i`. 

# Constraints and clarifications
* $1 \ \leq \ N \ \leq \ 10\ 000$
* $1 \ \leq \ \text{length of a word} \ \leq \ 2\ 000$
* $1 \ \leq \ \sum \text{lengths of all words} \ \leq \ 200\ 000$
* $1 \ \leq \ M \ \leq \ 100\ 000$
* $1 \ \leq \ t \ \leq \ 10$ for each query
* For `30` points: $1 \ \leq \ N \ \leq \ 200$, $1 \ \leq \ \text{length of a word} \ \leq \ 100$, $1 \ \leq \ M \ \leq \ 10\ 000$
* For another `20` points: $1 \ \leq \ N \ \leq \ 200$, $1 \ \leq \ \text{length of a word} \ \leq \ 500$, $1 \ \leq \ M \ \leq \ 100\ 000$
* The tests are different from those in the contest.

# Example

`ratina.in`
```
6 5
asdf
asdeffff
gata
gara
pesistem
pestesistem
2 1 2
2 3 4
2 5 6
3 1 3 5
2 1 1
```

`ratina.out`
```
3
2
3
0
4
```

Explanation
---
The first query asks for the degree of similarity between the words `asdf` and `asdeffff`, which is `3` (because the two words have the first `3` identical letters, but not the first `4` letters).
The second query asks for the degree of similarity between the words `gata` and `gara`, which is `2`.
The third query asks for the degree of similarity between the words `pesistem` and `pestesistem`, which is `3`.
The fourth query asks for the degree of similarity between the words `asdf`, `gata`, and `pesistem`, which is `0`.
The last query is obvious: a word is `k`-similar with itself where `k` is exactly the length of the word.

---

If you find any grammar and/or syntax errors, please inform me so I can correct them appropriately according to the rules of the English language.
Here's the translated text:

---

Olimpia D’Info found an engraved plaque that contains several words written with unknown graphic signs, each word being made up of exactly $5$ graphic signs. By carefully studying the words, she deduced that $12$ distinct graphic signs are used in writing them and associated each sign with a lowercase letter from the English alphabet. After the association, she established a complexity for each sign, writing the letters in ascending order of the complexities she had previously determined. Olimpia considers this "complexity" as the most appropriate criterion for lexicographic ordering.

# Task

Knowing the order of the signs and the words from the plaque, determine:
1) The number of distinct words on the plaque.
2) The sequence of words ordered lexicographically according to the criterion formulated by Olimpia.

# Input data

The input file `zimeria.in` contains:
* The first line contains a natural number $p \in \{1,2\}$, representing the variant of the task to be solved;
* The second line contains a natural number $n$, representing the number of words on the plaque;
* The third line contains $12$ characters, lowercase letters of the English alphabet, which represent the coded signs, in the lexicographic order of the signs;
* Each of the following $n$ lines contains a word.

# Output data

* If the value of $p$ is $1$, then **only point 1** of the task will be solved. In this case, the output file `zimeria.out` will contain the number of distinct words on the plaque.
* If the value of $p$ is $2$, then **only point 2** of the task will be solved. In this case, the output file `zimeria.out` will contain $n$ lines, each line containing a word in lexicographic order, according to the complexity established by Olimpia.

# Constraints and clarifications

* $n < 400\ 000$;
* $30\%$ of the tests will have $1$ as the value on the first line, and the remaining $70\%$ of the tests will have $2$ on the first line.

# Example 1

`zimeria.in`
```
1
5
qwertyuiopas
reeet
wyuty
reeet
oiopp
oiopp
```

`zimeria.out`
```
3
```

## Explanation

The plaque contains $3$ distinct words.

# Example 2

`zimeria.in`
```
2
5
qwertyuiopas
oiopp
reeet
wyuty
reeet
oiopp
```

`zimeria.out`
```
wyuty
reeet
reeet
oiopp
oiopp
```

## Explanation

We sort the words and obtain `wyuty`, `reeet`, `reeet`, `oiopp`, `oiopp`.

---

I have carefully reviewed the translation and ensured that there are no grammatical or syntactical errors in the English language.
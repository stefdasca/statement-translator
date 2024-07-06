Ion is a passionate linguist. Recently, he discovered a text written in an unknown language. The text is written on multiple lines and consists of words written in lowercase Latin alphabet letters, separated by spaces and/or punctuation marks (`,:;.!?-`).

Ion was struck by the many similarities between words in the text. Being very rigorous, Ion defines the similarity of two words as follows.

Let $c_1$ and $c_2$ be two words. The word $c_1$ can be obtained from the word $c_2$ through a sequence of elementary operations. The elementary operations that can be used are:
* deletion of a character
* insertion of a character
* modification of a character

We define the similarity between $c_1$ and $c_2$ as the minimum number of operations applied to the word $c_1$ to transform it into the word $c_2$.

Let $c_0$ be the first word in the text. Starting with $c_0$ we can construct chains of $k$-similarity. 

A $k$-similarity chain is a sequence of distinct words in the text with the following properties:
- if the word $x$ appears in the chain before the word $y$, then the first appearance of $x` in the text precedes the first appearance of $y$ in the text;
- if $x$ and $y$ are consecutive words in the chain (in the order $x\\ y$), then the similarity between $x$ and $y$ is $\\leq k$;
- the chain is maximal (i.e., we cannot add another word at the end of this chain, in such a way that the previous properties are respected).

# Task
Write a program that determines the number of $k$-similarity chains that start with $c_0$.

# Input data
The input file `lant.in` contains on the first line the value $k$. The following lines contain the given text.

# Output data
The output file `lant.out` will contain a single line that will print the number of $k$-similarity chains that start with $c_0$.

# Constraints and clarifications
* The length of a line in the text does not exceed $1\ 000$ characters.
* The length of a word does not exceed $30$ characters.
* The total number of words $\\leq 150$.
* For the test data, the number of $k$-similarity chains that start with $c_0$ will be $\\leq 2\ 000\ 000\ 000$.
* The statement has been modified.

# Example

`lant.in`
```
5
ana are mere, banane,
pere si castane.
```

`lant.out`
```
6
```

Explanations
---

The $5$-similarity chains that can be formed are:
ana are mere pere
ana are pere
ana are banane castane
ana are si
ana banane castane
ana si
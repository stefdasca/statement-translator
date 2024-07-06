Lunasorab decided to start a business. Thus, he began cracking codes (for a fee, of course). He receives a list of $N$ candidate words of the same length $L$ and needs to find out how many distinct complete words compatible with at least one of them exist.

A word is called a candidate if it contains only lowercase letters from the Latin alphabet and the character `?` (which can be replaced with any lowercase letter of the Latin alphabet). We say that a word is complete if it consists only of lowercase letters of the Latin alphabet, and we say that a complete word is compatible with a candidate word if there is an assignment of the `?` characters such that the two words become identical.

However, because it involves a lot of money and he believes it might be his only chance to "make success," he tests you by giving you $NR$ extensions of the alphabet. An alphabet extension consists of the union of the lowercase letters of the Latin alphabet with a set of distinct additional characters (only the cardinality of the extensions is important). These characters from the extension can represent possible assignments of the `?` characters.

Since the answer Lunasorab is looking for can be quite large, he asks you to give the result modulo $10^9 + 7$.

# Task

Given a list of candidate words and $NR$ extensions, determine how many distinct complete words compatible with at least one of the candidate words exist for each extension.

# Input data

The input file afacere.in contains on the first line the natural numbers $N \\ L \\ NR$. The following $N$ lines contain the candidate words. The next $NR$ lines each contain a natural number $v$, representing the cardinality of an extension.

# Output data

The output file `afacere.out` will contain for each of the $NR$ extensions a line that will contain a natural number representing the number of distinct complete words compatible with at least one of the candidate words from the list, using the alphabet consisting of the Latin alphabet letters together with an additional number of characters equal to the cardinality of the extension.

# Constraints and clarifications

* $1 \leq N \leq 20$
* $1 \leq L \leq 100$
* $1 \leq NR \leq 100$
* For $10\%$ of the tests, $N \leq 5$ and $L \leq 5$
* For another $30\%$ of the tests, $N \leq 15$ and $L \leq 50$
* The cardinality of an extension will be less than or equal to $1 \\ 000$
* The candidate words in the input file will contain only lowercase Latin alphabet letters and `?`

# Example

`afacere.in`
```
3 2 2
ab
a?
cb
0
2
```

`afacere.out`
```
27
29
```

## Explanation

For the first extension, we do not have any additional characters, so the possible compatible complete words are `aa`, `ab`, `ac`, $\dots$, `az` and `cb`.

For the second example, we have two additional characters into which `?` can be transformed, so the possible compatible complete words are `aa`, `ab`, `ac`, $\dots$, `az`, `aA`, `aB` and `cb`, where `A` and `B` denote the two additional characters.
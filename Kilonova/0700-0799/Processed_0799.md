```markdown
A series of words separated pairwise by a space is considered. Each word is characterized by its order number, which represents its position in the series of words (the first word has the order number $1$). A word $i$ can repeatedly undergo the following transformations: the first character of the word (the leftmost) is removed from its position and added after the last character of the word. Thus, from a word $s$ with $k$ characters, other $k-1$ words can be obtained, which we call words obtained from the transformation of the word $s$. For example, from a word consisting of $4$ characters $c_1 c_2 c_3 c_4$, the words obtained by transforming it are: $c_2 c_3 c_4 c_1$, $c_3 c_4 c_1 c_2$, $c_4 c_1 c_2 c_3$.

In the series of words, the first pair of neighboring words $(a,b)$ is searched for, where the second word in the pair (word $b$) is identical to a word obtained from the transformation of $a$. If such a pair exists, the word $b$ is removed from the series. By removing the word $b$ from the series, it will have one less word! The above search operation is repeated until there is no pair $(a,b)$ of neighboring words left in the remaining series, such that $b$ is obtained by transforming $a$.

It is known that during the modifications, the words do not change their order numbers which they had initially.

# Task

Write a program that reads the series of words and displays:

1. the order number of the first word deleted or the value $0$ if no word is deleted
2. the order numbers of the words remaining after completing the modification operations.

# Input data

The input file `cuvinte.in` contains a single line with the series of words separated pairwise by a space.

**After the last word in the series, there is the character `!`.**

# Output data

The output file `cuvinte.out` will contain the first line the order number of the first word deleted or the value $0$ if no word is deleted.

The second line will contain the order numbers of the words remaining at the end in the series of words, separated by a space. These numbers can be written in any order.

# Constraints and clarifications

* Each word has a maximum of $10$ characters, and in the initial series, there are no more than $25$ words.
* The initial series of words consists of at least one word. A pair of neighboring words $(a,b)$ in the series of words is characterized by the fact that, after word $a$, word $b$ immediately follows.
* Partial scores are awarded: requirement 1 is $40\ \%$ of the score, and requirement 2 is $60\ \%$ of the score.

# Example

`cuvinte.in`
```
alfa faal alfa fala lafa afal calfa calfa!
```

`cuvinte.out`
```
2
1 3 4 7 8
```

## Explanation

The words obtained by transforming the word `alfa` are: `lfaa`, `faal`, `aalf`.

The first pair of neighboring words that meet the requirements are the words with order numbers $1$ and $2$. The word with order number $2$ will be deleted.

The resulting series consists of the following $7$ words: `alfa`, `alfa`, `fala`, `lafa`, `afal`, `calfa`, `calfa`. The first pair that meets the requirements in the new series is the pair of words `fala` and `lafa`, having order numbers $4$ and $5$, because the list of words obtained by transforming the word `fala` are: `alaf`, `lafa`, `afal`. The word with order number $5$ will be deleted.

The resulting series after deletion is: `alfa`, `alfa`, `fala`, `afal`, `calfa`, `calfa`. The first pair that meets the problem requirements in the new series is `fala` and `afal`. The word `afal` with order number $6$ will be deleted.

The resulting series after deletion is: `alfa`, `alfa`, `fala`, `calfa`, `calfa`. In this series, there is no more pair that meets the requirements. Thus, the remaining words are: `alfa`, `alfa`, `fala`, `calfa`, `calfa`, which have order numbers $1$, $3$, $4$, $7$, $8$.
```
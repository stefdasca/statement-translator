# Task

While on vacation, RAU-Gigel spends a lot of time playing on his phone. He has a word game, like Scrabble, where the pieces are inscribed with letters (uppercase or lowercase from the English alphabet), each letter having a known value, a natural number. The value of a word is equal to the sum of the values of the letters in the word, without considering their frequency.

~[img1.jpg|align=center|width=40em]

For example, the value of the word `Abac` is $Val($`Abac`$) = Val($`A`$) + Val($`b`$) + Val($`c`$) = 1+2+4=7$. By merging two words, the smallest (alphanumeric) word is formed from all the letters present in both words, without considering the case (uppercase/lowercase) or the number of occurrences. We denote this word by $a*b$. The cost of merging two words is obtained by summing the values of the letters present in $a*b$, but which are not in $a$, and which are not in $b$, ignoring their case.

For example, by merging the words $a =\\ $`Abac` and $b =\\ $`cade`, we get the word $a*b =\\ $`ABCDE`, and the cost of merging can be calculated as follows: $Val($`DE`$) + Val($`B`$) = 24 + 2 = 26$.

RAU-Gigel's application generates a linear sequence with $N$ words, and RAU-Gigel has to merge two adjacent words from the sequence, pay the necessary cost for merging them, and then replace the two words in the sequence with the word obtained by merging. In the end, the sequence will have a single word, and to obtain it, RAU-Gigel will pay the sum of all the costs generated along the way.

If, for example, we have $3$ words: `Abac`, `cade`, and `DAC`, one of the possible merging sequences is illustrated below:

| Word sequence | Action | Cost |
| - | ----- | ------------ |
| `Abac`, `cade`, `DAC` | First, the words `Abac` and `cade` are merged to obtain `ABCDE`. | $26$ |
| `ABCDE`, `DAC` | `ABCDE` and `DAC` are merged. The cost is calculated by summing the values of the letters `B` and `E`. | $18$ |
| `ABCDE` |  | Final cost: $44$ |

The smallest word formed by merging the $3$ words, without considering the case (uppercase/lowercase) or frequency, will be `ABCDE`, and the total cost to obtain it, according to the choices above, will be $26 + 18 = 44$. But there is another option: RAU-Gigel can first merge the words `cade` and `DAC` to obtain `ACDE`, with a cost of $16$, then merge `Abac` and `ACDE` to obtain `ABCDE`, with a cost of $26$. This time, the total cost will be: $16 + 26 = 42$.

Therefore, the minimum total cost is given by the second option and is $42$.

# Task

Given a sequence of $N$ words, find the final word resulting from the merging of two adjacent words, one step at a time, and the minimum total cost necessary to obtain it.

# Input data

The file `scrabble.in` contains the first line with the non-zero natural number $N$, representing the number of words. The next $N$ lines contain the $N$ words.

# Output data

The file `scrabble.out` will contain, on a single line, the two values: the final word and the minimum total cost necessary to obtain it, according to the task. The two values are separated by a space.

# Constraints and clarifications

* $2 \leq N \leq 10^2$, the words have no more than $100$ letters each.
* For tests worth 20 points, $N \leq 4$.
* For tests worth another 10 points, all the $N$ words have the same value.
* For tests worth another 20 points, any word includes, in its composition, the letters of the words to its left (ignoring case), plus perhaps other letters.
* Case type = uppercase or lowercase letter.

# Example

`scrabble.in`
```
3
Abac
cade
DAC
```

`scrabble.out`
```
ABCDE 42
```

## Explanation

The smallest word formed by merging the $3$ words, without considering the case (uppercase/lowercase) or frequency, is: `ABCDE`, and the minimum total cost necessary to obtain it is $42$.
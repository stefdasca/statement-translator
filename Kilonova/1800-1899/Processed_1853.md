Let's consider two sentences made up of words written in capital letters of the English alphabet, any two consecutive words being separated by one or more spaces.
Let's consider $c = c_1 \\ c_2 \\dots c_n$ and $d = d_1 \\ d_2 \\dots d_m$ two words. To calculate the distance between the words $c$ and $d$, noted as $dist(c, d)$, the shorter word is filled at the end with the character `@` (which has the ASCII code $64$) until two words of the same length are obtained. Then, the sum of the absolute differences between the ASCII codes of the characters located in the words $c$ and $d$ at corresponding positions is calculated:

$$dist(c, d) = |c_1 - d_1| + |c_2 - d_2| + \dots + |c_{lg} - d_{lg}|,$$ where $lg = \max(n, m)$.

We define the distance between two sentences as the sum of the distances between the words located in the sentences at corresponding positions. If one of the sentences has fewer words than the other, it is considered that empty words (words of length $0$) are at the end of this sentence until the required number of words is reached.

For example, let's consider the sentence $P_1$ = "ANA ARE MERE" and the sentence $P_2$ = "VASILE NU". The distance between the sentence $P_1$ and the sentence $P_2$ is:

$$dist(P_1, P_2) = dist("ANA", "VASILE") + dist("ARE", "NU") + dist("MERE","").$$
$$dist("ANA","VASILE") = |A - V| + |N - A| + |A - S| + |@ - I| + |@ - L| + |@ - E| = |65 - 86| + |78 - 65| + |65 - 83| + |64 - 73| + |64 - 76| + |64 - 69| = 21 + 13 + 18 + 12 + 9 + 5 = 78$$
$$dist("ARE","NU") = |A - N| + |R - U| + |E - @| = |65 - 78| + |82 - 85| + |69 - 64| = 13 + 3 + 5 = 21$$
$$dist("MERE","") = |M - @| + |E - @| + |R - @| + |E - @| = |77 - 64| + |69 - 64| + |82 - 64| + |69 - 64| = 13 + 5 + 18 + 5= 41$$
Thus, $$dist(P_1, P_2) = 78 + 21 + 41 = 140$$

In order to minimize the distance between the two sentences, we can perform one or more operations on the second sentence. An operation consists of moving the first letter of a word to the end of the previous word (if it exists) or the last letter of a word to the beginning of the next word. Empty words can only be at the end of a sentence, not at the beginning or in the middle of it (neither in the given sentences nor in the sentences obtained after applying the operations). The words in the sentence and the words obtained after the operations cannot exceed $20$ letters.

# Task

Determine the minimum distance that can be obtained between the two sentences by performing operations of the type described in the statement. It is also required to determine the minimum number of operations that must be performed on the second sentence to obtain the minimum distance.

# Input data

The input file `dist.in` contains the first sentence on the first line and the second sentence on the second line.

# Output data

The output file `dist.out` will contain a single line with two natural numbers separated by a space $d_{min} \\ nr_{min}$, representing in order the minimum distance between the two sentences and the minimum number of operations that must be performed on the second sentence to obtain the minimum distance.

# Constraints and clarifications

* The total length of a sentence does not exceed $500$ characters.
* The maximum length of a word does not exceed $20$ characters, either in the given sentences or in the sentence obtained after applying the operations from the statement.
* The maximum number of words in a sentence is $100$.
* $60$\% of the score is awarded for determining the minimum distance, and $100$\% for solving both requirements.

# Example

`dist.in`
```
ANA ARE   MERE
VASILE NU
```

`dist.out`
```
62 9
```

## Explanation

The second sentence, after applying the $9$ operations, is:
`V ASI LENU
Young Harry Potter discovered in one of the rooms of the Hogwarts castle a map, and after a spell, a secret text appeared. The text written only with lowercase letters of the English alphabet constitutes a key to a new spell useful in Quidditch matches. The new key is obtained as follows:

* From the secret text, form all possible words from letters located at consecutive positions.
* Among the formed words, choose the one that is the largest in lexical order.

Consider that two words $a_1 a_2 a_3 \dots a_k$ < $b_1 b_2 b_3 \dots b_l$, the words being given by the characters that make them up, are in lexical order if there exists an index $i \leq k$ or $i \leq l$ such that $a_i < b_i$ and $a_j = b_j$ for any $j < i$.

Example: if the text found by Harry is `abcd`, then the words obtained are: `a`, `b`, `c`, `d`, `ab`, `bc`, `cd`, `abc`, `bcd`, `abcd`, and the solution is `d` as it is the largest in lexical order.

# Task

Write a program that, reading the initial text, determines the largest word in lexical order among all the words formed in the manner explained above.

# Input data

The input file `harry.in` contains a single line that contains the initial text.

# Output data

The output file `harry.out` will contain on the first line the word that constitutes the solution.

# Constraints and clarifications

* $1 \leq$ length of text $\leq 255$;

# Example 1

`harry.in`
```
tatep
```

`harry.out`
```
tep
```

## Explanation

The words that can be formed are: `t`, `a`, `t`, `e`, `p`, `ta`, `at`, `te`, `ep`, `tat`, `ate`, `tep`, `tate`, `atep`, `tatep`.

# Example 2

`harry.in`
```
tgtep
```

`harry.out`
```
tgtep
```

## Explanation

The words that can be formed are: `t`, `g`, `t`, `e`, `p`, `tg`, `gt`, `te`, `ep`, `tgt`, `gte`, `tep`, `tgte`, `gtep`, `tgtep`.
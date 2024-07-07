
Given a language consisting of $N$ words and an encrypted text consisting of $M$ words. We say that a word is permuted after a sequence $x_1, x_2, ..., x_k$ if the first letter is permuted with $x_1$, the second with $x_2$, ..., and the last with $x_k$.
For example, after the sequence $1 \\ 5 \\ 6$, `"abc"` becomes `"bgi"`. The permutation is done in the order of lowercase letters in the English alphabet. If a letter exceeds the end of the alphabet, it wraps around and then the next letter is permuted with $1$. 
In the case where the last letter exceeds the end of the alphabet, then the word becomes invalid. For example, `"zza"` permuted after the sequence $1 \\ 2 \\ 3$, becomes `"ace"`. (addition is done with carry starting from the left). If `"zzz"` were permuted after the sequence $1 \\ 2 \\ 3$, it would become invalid. The most "significant" letters are from right to left.
We want to decrypt the text, using multiple valid sequences. The best decryption sequence is the one for which the number of words in the encrypted text found in the language, after the operation, is maximal.

# Task

Determine the best decryption sequence among those given. If there are multiple such sequences, the one with the smallest index will be displayed.

# Input data
The first line of the file `cripto.in` contains four natural numbers $N, M, P, Q$. The next line contains the language, consisting of the $N$ words of length $K$. The third line contains the $M$ words. Finally, there are the $Q$ sequences, each of $K$ numbers on a separate line.

# Output data

The output file `cripto.out` will contain on the first line, the index of the best sequence, and its similarity.

# Constraints and clarifications

* $N, M, Q \leq 10^5$, $M * Q \leq 10^7$. The values in the sequences are strictly less than $26$;
* For 30% of the tests $N, M, Q \leq 100$;
* $K \leq 12$. For another 20% of the tests $K \leq 3$.

# Example

`cripto.in`
```
6 3 4 2
info olte niaa este inva lcea
hlck njqa hlcj
1 2 3 5 
1 2 3 4
```

`cripto.out`
```
2 2
```

## Explanation

The words on the second line are permuted, after each sequence, from the two.
The answer is the second sequence, $1 \\ 2 \\ 3 \\ 4$, because the input becomes `info olte infn`.
Thus, $2$ of the words are found in the first language.

If we used the first sequence, the result would be $1$: `infp oltf info`.

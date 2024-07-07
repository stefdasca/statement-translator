Two characters whose names will be given in the input data (for now we call them Bossanip and Dicsi) spend their nights in discos. Everyone knows that Bossanip is a V.I.P. member in all discos around the world, and Dicsi always takes advantage of his friend's fame. Having arrived in a foreign land, Dicsi faced a very big problem. How can he get into the V.I.P. area when he is on his own? Thus, Dicsi started committing crimes such as identity theft. Dicsi wants to permute the letters in his name (to find an anagram of his own name) so that the new name differs in exactly $ K $ positions from Bossanip's name. Moreover, he wants this anagram to be lexicographically minimal. If he manages to do this, he might be able to impersonate Bossanip and enter as a V.I.P. member.

# Task

# Input data

In the text file `vip.in`, the first line contains the natural number $ T $. The following $ 3 \cdot T $ lines describe $ T $ sets of input data. Each set occupies 3 lines as follows: the first line of a set contains two numbers $ N $ (the length of Bossanip's and Dicsi's real names) and $ K $; the second line of a set contains Bossanip's name given by a string of characters $ s_1 $; the third line of a set contains Dicsi's name given by a string of characters $ s_2 $. Fortunately for Dicsi, both characters have names of the same length.

# Output data

In the text file `vip.out`, each of the $ T $ lines will contain a string of characters, with the $ j $-th line containing the anagram corresponding to the $ j $-th test (the new name for Dicsi) or $ -1 $ if there is no such anagram.

# Constraints and clarifications

* $ 1 \leq N, K \leq 10^5 $
* The sum of the values of $ N $ across all test sets $ \leq 10^6 $
* All letters are lowercase letters of the English alphabet
* If there is no solution for a test, then the value $ -1 $ will be displayed
* A string $ p_1, p_2, \dots, p_N $ is lexicographically smaller than another string $ q_1, q_2, \dots, q_N $, if there exists a position $ i $, $ 1 \leq i \leq N $, such that $ p_i < q_i $ and $ p_j = q_j $, for any $ j $, $ 1 \leq j < i $

# Example

`vip.in`
```
2
8 6
corleone
vasilica
5 2
marko
ghita
```

`vip.out`
```
caaliisv
-1
```

## Explanation

In the first set, the smallest anagram of the string **vasilica**, from a lexicographical point of view, that differs from the string **corleone** in exactly 6 positions is **caaliisv**.

In the second set, none of the anagrams of the string **ghita** can differ in exactly two positions from the string **marko**.
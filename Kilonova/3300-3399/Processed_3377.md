# Task

You want to form a word but you don't have enough of the letters you need, and you have others that are useless. Fortunately, the wizard Jaxson has $M$ offers for you: "Give me the letter $L_1$ and $X$ gold coins, and I will give you the letter $L_2$". You will do your best to build your word. Can you form it? If yes, what is the minimum number of gold coins you need to pay?  
<br>
Solve for $T$ tests.

# Input data

The first line contains $T$, followed by $T$ tests.  
For each test, the following information is read in order: the word you want to form, your stock of letters, the number of offers, and the offers (The explanation is in the example).  
Your stock of letters is an array of $26$ natural numbers. The first number indicates how many letters $a$ you have in stock, the second how many letters $b$...

# Output data

Print $T$ lines, on each line either "NU" (NO) or "DA" (YES) followed by the minimum cost that needs to be paid.

# Constraints and clarifications

* $1 \leq T \leq 5$
* It is guaranteed that the pairs of letters read are distinct.
* The length of the word read in each test is $\leq 10^6$.
* The number of initial copies of a letter is $\leq 10^6$.
* The cost for an exchange is strictly positive and $\leq 10^9$

# Example 1

`stdin`
```
5
aab
3 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
1
a b 1
aab
0 0 5 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
3
c d 1
d a 1
c b 1
abc
3 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
1
a b 1
abbcb
2 2 2 0 0 8 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
2
a b 5
c b 4
abcd
4 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 9 9 1999
4
a b 6
d c 1
c b 2
a d 1
```

`stdout`
```
DA 1
DA 5
NU
DA 4
DA 7
```

## Explanation

For the first test, we have the letters ${'a', 'a', 'a'}$ at our disposal and we want to form the word $aab$, for this we will use the only available offer and exchange one letter $a$ for one $b$ at the cost of $1$, now we have the letters ${'a','a','b'}$, with these we can form the words $aab$, $aba$, $baa$.

For the second test, we will exchange one $c$ for a $b$, then $2$ $c$ for $2$ $d$, followed by $2$ $d$ for two $a$.

For the third test, we cannot form the word only with the available offers.

For the fourth test, we can either exchange one $a$ for a $b$ or one $c$ for a $b$, we will exchange the $c$ since it has a lower cost. It's observed that we also have $8$ $f$ letters, but this does not help or hinder us in any way.
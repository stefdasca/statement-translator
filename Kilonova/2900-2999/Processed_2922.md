Sure, here is the translated statement:

---

Consider a sentence made up of lowercase letters from the English alphabet and possibly spaces. Words are formed from lowercase letters and are separated by one or more spaces.

We define the $power$ associated with a word $C_1 C_2 \dots C_k$ as a natural number $v$ equal to the product of powers of the form $P^i$, where $P$ is the position in the alphabet of the letter $C_i$, $i=1,\dots,k$. Thus, the word `dab` is associated with a $power$ equal to $v = 4^1 \cdot 1^2 \cdot 2^3 = 4 \cdot 1 \cdot 8$, that is, $v = 32$, because the letter `d` is in position $4$, `a` in position $1`, and `b` in position $2` in the alphabet.

We define the $value$ of a word $C_1 C_2 \dots C_k$ as the number $nrd$ modulo $k$, where $nrd$ is the number of divisors of $v$, $v$ being the $power$ of the word $C$. The $value$ of the word `dab` is $0$, because $nrd=6$ (the $12$ divisors of $2048$ are: $1$, $2$, $4$, $8$, $16$, $32$), $k=3$ (the word contains $3$ letters) and $6$ modulo $3 = 0$.

We define the $value$ of a sentence as the sum of the $values$ of the words in it.

By $subsentence$ we mean a new sentence formed from some words of the initial sentence.

Given a series of $N$ numbers $x_1, x_2, \dots, x_N$, we are interested in checking whether for each number $x_i$, $i=1, 2, \dots, N$, there exists at least one subsentence that has the value $x_i$ ($1$ - exists, $0$ - does not exist).

# Task

For a sentence as described and $N$ natural numbers, we require:
1. The value of the first word in the sentence
2. A series of $N$ values of $0$ or $1$ corresponding to the existence or non-existence of a subsentence in the given sentence with the values from the series of numbers $x_1$, $x_2$, \dots, $x_N$.

# Input data

The input file `subprop.in` contains on the first line the task $C$ ($1$ or $2$), on the second line the sentence, on the third line the number $N$, and on the last line the $N$ numbers $x_1$, $x_2$, \dots, $x_N$ separated by a space.

# Output data

The output file `subprop.out` will contain on the first line a number corresponding to task $1$, if $C = 1$, respectively a series of $N$ digits $0$ or $1$ separated by a space corresponding to task $2$, if $C = 2$.

# Constraints and clarifications

* $1 \leq N \leq 10 \ 000$;
* the sentence has at most $100 \ 000$ characters;
* a sentence has at most $ 10 \ 000$ words and a word has at most $1 \ 000$ letters;
* $x_1$, $x_2$, \dots, $x_N$ are natural numbers $\leq 50 \ 000$;
* $A$ modulo $k$ represents the remainder of the division of $A$ by $k$;
* Correct resolution of task $1$ will be awarded $20$ points.
* Correct resolution of task $2$ will be awarded $80$ points.

# Example 1

`subprop.in`
```
1
dab ac dacaa
3
2 3 1
```

`subprop.out`
```
0
```

## Explanation

$C = 1$. The value of the first word `dab` is $0$.

# Example 2

`subprop.in`
```
2
dab ac dacaa
2
3 5 
```

`subprop.out`
```
1 0
```

## Explanation

$C = 2$. The values of the words `dab`, `ac`, and `dacaa` are $0$, $1$, and respectively $2$. A subsentence with the value $3$ is formed from the words `ac` and `dacaa`. No subsentence exists with the value $5$.

---
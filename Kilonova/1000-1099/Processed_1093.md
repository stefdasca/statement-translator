Here is the translated competitive programming problem statement:

----

At the birth of a girl in the Ragan Ama tribe, parents must find the most beautiful name possible. Beautiful names are considered only anagrams of a word that, in their language, means "*beautiful as the morning dew, gentle as the wind's caress among leaves, blessed by the light of the sun and the moon*."  
The girl's life will be under a lucky star if her name is the smallest lexicographically, different from any of the girls in the tribe.

# Task

Since today a girl was born in the tribe, write a program that, knowing the names of the girls in the tribe, solves the following tasks:
1. display the name that the parents should give the girl so that her life is under a lucky star;
2. determine how many beautiful names, different from the names of the girls in the tribe, exist.

# Input data

The input file `raganama.in` contains the first line a natural number $C$, representing the task that must be solved ($1$ or $2$). The following lines contain the names of the girls in the tribe, one name per line, in lexicographical order; all names are anagrams of the same word.

# Output data

The input file `raganama.out` will contain a single line.

* If $C = 1$, this line will contain the name that the parents should give the girl.
* If $C = 2$, this line will contain the number of beautiful names, different from the girls' names in the tribe.

# Constraints and clarifications

* The names of the girls consist of a maximum of $100$ lowercase letters from the English alphabet.
* There are at most $100 \ 000$ girls in the tribe.
* An anagram of a word is formed from the same letters as the given word, possibly in a different order. For example, the word "*armata*" is an anagram of the word "*tamara*".
* We say that a word $a_1 \ a_2 \dots a_n$ is lexicographically smaller than a word $b_1 \ b_2 \dots b_n$ if there is $1 \leq k \leq n$ such that $a_i = b_i$, for any $1 \leq i < k$ and $a_k < b_k$.
* It is guaranteed that for the test data there is a name that can be given to the newborn girl.
* For tests worth $20$ points, the result for task $2$ will have at most $18$ digits.
* For tests worth $50$ points, the task is $1$.

# Example 1

`raganama.in`
```
1
aacn
aanc
acan
acna
anac
caan
cana
```

`raganama.out`
```
anca
```

# Example 2

`raganama.in`
```
2
aacn
aanc
acan
acna
anac
caan
cana
```

`raganama.out`
```
5
```

## Explanation

There are a total of $12$ anagrams:

```
aacn
aanc
acan
acna
anac
anca
caan
cana
cnaa
naac
naca
ncaa
```

The first name in lexicographical order that does not belong to any girl in the tribe is `anca`. Of the $12$ existing anagrams, $7$ are already the names of girls in the tribe, leaving $12 - 7 = 5$ beautiful names.

----
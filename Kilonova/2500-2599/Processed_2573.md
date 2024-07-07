
Muguraș has finally started studying computer science, and Mugurel, his father, is the proudest of his choice.

Not knowing which is the best language for beginners, he chose to learn *Mac*, the simplest programming language in the “Empire of Rubber Ducks�.

In the *Mac* language, we have only two possible types of operations:
* $x := s$ (direct assignment). After this operation, the variable identified by $x$ will hold the string given by $s$.
* $x = a + b$ (memory assignment). After this operation, the variable identified by $x$ will hold the concatenation of the strings (in this order) from the variable identified by $a$ and the variable identified by $b$ (variables $a$ and $b$ remain unchanged, only the variable $x$ is modified).

# Task

Mugurel wants to send Muguraș to the Local Informatics Olympiad for Ducks, but first, he needs to make sure he knows how to code and gives him the following problem to solve: after performing $N$ operations in the *Mac* language, how many times does $S$ appear as a subsequence in the variable $V$?

Unfortunately, he is still at the beginning of the journey, so Muguraș asks you to help him reach the Olympiad.

# Input data

The input file will contain on the first line an integer $N$, representing the number of operations. The second line contains two strings, $S$ and $V$, separated by a space, representing the string to be searched for and the variable from which the result must be determined. The next $N$ lines contain one string each, representing an operation in the *Mac* programming language.

# Output data

The output file will contain on the first line a single integer $K$, representing the required result.

# Constraints and clarifications

We denote by $|X|$ the length of a variable name and by $|T|$ the length of a string in the direct assignment.
* $1 \leq N \leq 100\ 000$
* $1 \leq |V|, |S| \leq 10$
* $1 \leq |X|, |T| \leq 10$
* All variable names and strings contain only lowercase English letters.
* A subsequence is a consecutive sequence of characters from a string.
* Variables used in memory assignments never contain empty strings.
* It is guaranteed that $1 \leq K \leq 10^{18}$.
* It is guaranteed that all operations are correct.
* Muguraș does not recommend learning *Mac*, there are much more useful programming languages.
* For tests worth $5$ points, $|X| = 1$ and $|S| = 1$.
* For other tests worth $5$ points, $|S| = 1$.
* For other tests worth $10$ points, $N \leq 15$.
* For other tests worth $20$ points, $|X| = 1$.
* For other tests worth $60$ points, there are no additional restrictions.

# Example 1

`muguras.in`
```
5
abc x
p := ab
q := cdef
x = p + q
q := tabc
x = x + q
```

`muguras.out`
```
2
```

## Explanation

After the third operation, $x$ will hold the string `abcdef`. After the fifth operation, $x$ will hold the string `abcdeftabc`, in which the string `abc` appears 2 times as a subsequence.

# Example 2

`muguras.in`
```
5
haha v
a := haha
b := haha
c := ha
v = a + b
v = v + c
```

`muguras.out`
```
4
```

## Explanation

After the fourth operation, $v$ will hold the string `hahahaha`. After the fifth operation, $v$ will hold the string `hahahahaha`, in which the string `haha` appears 4 times as a subsequence (letters in a string can appear in multiple subsequences).

# Example 3

`muguras.in`
```
7
a ax
ax := a
ax = ax + ax
ax = ax + ax
ax = ax + ax
ax = ax + ax
ax = ax + ax
ax = ax + ax
```

`muguras.out`
```
64
```

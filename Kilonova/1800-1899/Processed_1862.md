```markdown
The Solarian children often play by sending encrypted messages to each other. For encryption, they use a cipher based on a permutation $p$ of the solarian alphabet letters and a natural number $d$. The solarian alphabet contains $m$ very complicated letters, so we will represent them by numbers from $1$ to $m$. 

Given a message in the solarian language, represented by us as a sequence of $n$ numbers between $1$ and $m$, $c_1 \\ c_2 \\dots c_n$, the message is encrypted as follows: each letter $c_i$ is replaced with $p(c_i)$, then the obtained string $p(c_1) \\ p(c_2) \\dots p(c_n)$ is rotated to the right, making a circular permutation with $d$ positions resulting in the string $p(c_{n-d+1}) \\dots p(c_{n-1}) \\ p(c_n) \\ p(c_1) \\ p(c_2) \\dots p(c_{n-d})$.

For example, for the message $2 \\ 1 \\ 3 \\ 3 \\ 2 \\ 1$, the permutation $p = (3 \\ 1 \\ 2)$ (i.e., $p(1)=3$, $p(2)=1$, $p(3)=2$) and $d=2$. Applying the permutation $p$ we will obtain the string $1 \\ 3 \\ 2 \\ 2 \\ 1 \\ 3$, then rotating the string to the right by two positions we get the encryption $1 \\ 3 \\ 1 \\ 3 \\ 2 \\ 2$.

# Task

Given an uncoded message and its encoded version, determine the used cipher (the permutation $p$ and the number $d$).

# Input data

The input file `cifru.in` contains:

- The first line contains the natural numbers $n$ and $m$, separated by a space, representing the length of the message and the number of letters in the solarian alphabet.
- The second line contains the uncoded message as a sequence of $n$ numbers between $1$ and $m$ separated by a space.
- The third line contains the encoded message as a sequence of $n$ numbers between $1$ and $m$ separated by a space.

# Output data

The output file `cifru.out` will contain:

- The first line contains the natural number $d$, representing the number of positions with which the circular permutation was made to the right. If there are multiple possible values for $d$, the minimum value will be chosen.
- The next line describes the permutation $p$. More precisely, the values $p(1)$, $p(2)$, $\dots$, $p(m)$ will be written, separated by a space.

# Constraints and clarifications

* $n \leq 100\ 000$
* $m \leq 9\ 999$
* The message contains each natural number from the interval $[1, m]$ at least once.
* For tests with $m \leq 5$, $40$ points are awarded, of which $20$ for tests also with $n \leq 2\ 000$.

# Example

`cifru.in`
```
6 3
2 1 3 3 2 1
1 3 1 3 2 2
```

`cifru.out`
```
2
3 1 2
```
```
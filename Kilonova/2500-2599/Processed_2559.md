After helping to connect the cities of Nordemos and Suderim, Negrimon decided to follow his destiny and become a red programamon. To start his journey, he needs to leave Udobje Lurrak and pass through Sha’ar Azih, the magical gate at the exit of the city of Estumar. This gate is based on a system of runix set in a line, numbered from $1$ to $N$. A runix is a square with a lowercase letter inscribed, from a restricted alphabet consisting of the first $L$ letters of the English alphabet. The restricted alphabet is circular, so that after the last letter follows the first one, and before the first letter is the last letter in the alphabet. In the initial state of the system, the first runix is set to the letter $a$, the second runix is set to the next letter in the restricted alphabet, and so on.

For example, for $N = 8$ and $L = 3$, the system has the initial configuration: `abcabcab`

- for $N = 11$ and $L = 4$, the system has the initial configuration: `abcdabcdabc`
- for $N = 14$ and $L = 7$, the system has the initial configuration: `abcdefgabcdefg`

When Negrimon reaches the gate, it comes to life and a series of actions of the following type occurs:
1. The runix with number $r$ along with all runix to its left moves and separates from those to its right (if there are any), thus forming two independent groups (initially all runix form a single group).
2. All runix in the group to which the runix with number $r$ belongs execute a step change $p$. This consists of replacing the associated letter with the next $p$-th letter in the alphabet ($p > 0$) or with the previous $(-p)$-th letter in the alphabet ($p < 0$). Due to the circularity of the alphabet, no matter how large $p$ is, there will be a letter that is at a distance $p$ from the current letter.
3. Negrimon receives a question of the type: on which letter is the runix with number $r$ set?

The gate opens if Negrimon answers all the received questions correctly and thus can continue his journey in Azih Lurrak.

# Task

Help Negrimon open the gate.

# Input data

The first line of the file `gate.in` contains the values $N$, $L$, $M$, separated by a space, meaning: $N$ - number of runix in the system, $L$ - number of letters in the restricted alphabet, $M$ - number of actions performed. Each of the next $M$ lines contain the values $t$ - type of action, $r$ - the number of the runix referred to, $p$ – the step change of the runix, if the action is of type 2 ($t = 2$), all separated by a space.

# Output data

The file `gate.out` will contain the answers to the received questions, in the order in which they are asked. Each answer occupies a line and consists of a single character representing the letter on which the runix with the given number in the question is set.

# Constraints and clarifications

- $1 \leq N, M \leq 200\ 000$
- $1 \leq r \leq N$
- $-100\ 000 \leq p \leq 100\ 000, p \ne 0$
- For tests worth 20 points, $N \cdot M \leq 25\ 000\ 000$

# Example

`gate.in`
```
8 3 8
1 3
2 4 1
3 8
1 5
2 2 2
3 1
2 5 -1
3 5
```

`gate.out`
```
c
c
b
```

# Explanation

The initial state of the system: $\text{abcabcab}$

1. `1 3` — $\text{ab\underline{c}\ abcab}$
2. `2 4 1` — $\text{abc\ \underline{b}cabc}$
3. `3 8` — $\text{abc\ bcab\underline{c}}$
4. `1 5` — $\text{abc\ b\underline{c}\ abc}$
5. `2 2 2` — $\text{c\underline{a}b\ bc\ abc}$
6. `3 1` — $\text{\underline{c}ab\ bc\ abc}$
7. `2 5 -1` — $\text{cab\ a\underline{b}\ abc}$
8. `3 5` — $\text{cab\ a\underline{b}\ abc}$

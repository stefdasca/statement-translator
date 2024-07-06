After many pranks together, Alex and Cipri are no longer allowed to meet. Alex – the strategist of the team – planned a new prank and decided to transmit his friend the **battle plan**, consisting of certain words in a message $\\text{m}[0]$. To avoid being discovered, he later sent multiple messages $\\text{m}[1], \\text{m}[2], \\dots$ to Cipri, who needs to decipher them using the secret convention established at the beginning of their friendship and "act." Each message $\\text{m}[i]$ is composed of multiple words, separated by a space, numbered consecutively, starting from $1$.
To find the plan, Cipri needs to find the largest value $i \\geq 0$ such that the messages $\\text{m}[i]$ and $\\text{m}[0]$ contain at least one identical word having the same order number in both messages. From $\\text{m}[0]$, all words which are also found in the message $\\text{m}[i]$ with the same order number as in $\\text{m}[0]$ are kept.
The words kept must be ordered in descending lexicographic order of their **power**. The **power** of the word with order number $j$ in $\\text{m}[0]$ is equal to the ordered decreasing string of indices of the messages in which it appears with the same order number as in $\\text{m}[0]$. Thus, a word that appeared with order number $2$ in messages $\\text{m}[0], \\text{m}[6]$ and $\\text{m}[8]$ has the power $\\{8, 6, 0\\}$. If two words have the same power, they will remain in the order from the initial message.
Cipri only has to read each word from right to left and the entire **battle plan** is deciphered!

# Task

Knowing the messages sent by Alex, help Cipri decipher the **battle plan** according to the secret convention.

# Input data

The input file `mesaje.in` contains in order the messages $\\text{m}[0], \\text{m}[1], \\text{m}[2], \\dots,$ one per line.

# Output data

The output file `mesaje.out` will contain in the first line the number $n$ of words in the battle plan, and in the second line the $n$ words of the battle plan.

# Constraints and clarifications

* The messages are stored one per line, composed of words separated by a space.
* The length of a word is at most $20$ characters, in lowercase English alphabet.
* The length of a message is at most $30\ 002$ characters.
* All messages have the same number of words.
* The input file contains at least $1$ and at most $128$ messages.
* Any line from the input file (message) ends with a newline marker (\_newline\_). The \_newline\_ character (`\\n`) will not be considered as part of the message.
* There are no empty messages.
* $40\\%$ of the score is awarded for determining the value $n$ and the entire score for correctly solving both tasks.

# Example 1

`mesaje.in`
```
inosos yy ataeclud ni
a yy ataeclud ni
yy inosos ni yy
inosos bb ataeclud ni
acni in e enib
```

`mesaje.out`
```
3
dulceata in sosoni
```

## Explanation

Messages $\\text{m}[0]$ and $\\text{m}[4]$ do not contain identical words with the same order number.
Messages $\\text{m}[0]$ and $\\text{m}[3]$ contain three identical words with the same order number: `inosos`, `ataeclud`, `ni`.
In order of power, they are: `ataeclud` $\\{3, 1, 0\\}$, `ni` $\\{3, 1, 0\\}$, `inosos` $\\{3, 0\\}$.

# Example 2

`mesaje.in`
```
miras ep maeg
```

`mesaje.out`
```
3
sarim pe geam
```

## Explanation

Because a single message was received, the **battle plan** contains the mirrored words from the initial text, all having the same power, read from right to left.
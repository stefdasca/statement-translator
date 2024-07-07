Chip and Dale are bored with their usual games and decided it's time to combine acorn gathering with a game that stimulates their intelligence. Chip suggested, â€œI will put the acorns I collected into a sequence of $C$ hollows, and you put the acorns you collected into another sequence of $D$ hollows.â€ ~[image.png|align=right]

Dale agreed and proposed that the game continues as follows: â€œIf, when dividing the number of acorns in the first hollow of my sequence by the number of acorns in each of the hollows in your sequence, the same remainder is obtained, then I consider my hollow properly filled and I write the digit $1$ on paper, otherwise, I consider it improperly filled and write the digit $0$. Then I check, applying the same rule, whether the second hollow in my sequence is properly filled, meaning whether dividing the number of acorns in it by the number of acorns in each hollow of your sequence results in the same remainder. I continue to note the result of the check ($0$ or $1$) on the paper. We end the game when we finish checking all $D$ of my hollows using this rule.â€

# Task

Write a program that reads from the file `alune.in` the positive natural numbers $C$ and $D$ and the number of acorns in each of Chip's and Dale's hollows, respectively. The program should determine the sequence of digits noted by Dale on the paper.

# Input data

The input file `alune.in` contains on the first line the two natural numbers, $C$ and $D$, the second line contains $C$ natural numbers representing the number of acorns in each of Chip's hollows, and the third line contains $D$ natural numbers representing the number of acorns in each of Dale's hollows. All numbers on the same line of the input file are separated by a space.

# Output data

The output file `alune.out` contains a single line with the determined sequence. The digits in this sequence are not separated by spaces.

# Constraints and clarifications

* $1 \leq C, D \leq 100\ 000$
* The number of acorns in Chip's hollows, written on the second line of the input file, are natural numbers in the range $[1, 2 \ 000\ 000\ 000]$.
* The number of acorns in Dale's hollows, written on the third line of the input file, are natural numbers in the range $[0, 2 \ 000\ 000\ 000]$.

# Example

`alune.in`
```
3 2
3 4 5
8 2
```

`alune.out`
```
01
```

## Explanation

The first hollow of Dale is improperly filled, because the remainders of dividing $8$ by $3, 4$, and $5$ are different, so the result of the check is $0$. The second hollow of Dale is properly filled because the remainders of dividing $2$ by $3, 4$, and $5$ are equal, and the result of the check is $1$.
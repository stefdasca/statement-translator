~[cufar.png|align=right|width=25%]

Alex, the heroine from *Minecraft*, is very brave and hardworking. Over time, she has stored various fragile objects (such as eggs) or hard objects (such as stones) in $n$ chests.

A chest is a wooden box with $27$ compartments arranged in $3$ rows, with $9$ compartments on each row. A compartment can store a group of one or more **identical** items: a maximum of $16$ fragile items or a maximum of $64$ hard items. Multiple compartments can contain the same type of items, and some compartments can be empty.

Alex labeled both the compartments and the items with numbers constructed according to the following rule:
* An item has a natural number label between $10$ and $99$ inclusive, as follows: a prime number if it is fragile, or a composite number if it is hard;
* All identical items receive the same label;
* A compartment has a natural number label formed of two concatenated values: the number of items in the stored group followed by their common label (for example, if the compartment label is $1994$, it means that it stores a group of $19$ items, each labeled $94$);
* Empty compartments are labeled with $0$.

Alex wants to **rearrange** the items in the chests so that:
* The space is optimized, meaning as few chests as possible are occupied and, within a chest, as few compartments as possible are occupied;
* The compartments in the available chests are occupied in order, starting with the first chest, and, within a chest, starting with the first row and, within a row, from left to right. In other words, the first chest is filled first, starting with the first row, and each row from left to right, then the second chest in the same manner, and so on;
* The items are taken in the ascending order of labels and from the total identical items, maximum groups are formed first, and only the last group can be partially incomplete;
* Each of these groups is deposited, as they form, into a compartment of the current chest; if it fills up, the next chest is used.

After rearranging the items, the compartments are labeled again according to the same rule.

# Task

Given the $n$ chests containing the items in their initial order, Alex asks you to create a program that determines:
1. For each distinct item label found in the $n$ chests, the total number of items with that label;
2. The new labels of the compartments that make up the $n$ chests after rearranging the items.

# Input data

The input file `cufere.in` contains:
* The first line contains the number $c$ representing the task to be solved ($1$ or $2$).
* The second line contains the non-zero natural number $n$, as described in the problem statement.
* Each of the next $3n$ lines contains $9$ numbers representing the initial labels of the compartments in a row of a chest, in the order they are in the chests, from the first chest to the last, within each chest from the first row to the third row, and within each row from left to right. Numbers on the same line of the file are separated by a space.

# Output data

The output file `cufere.out` will contain either the answer for task $1$ (if $c = 1$) or the answer for task $2$ (if $c = 2$). \
For task $1$, for each distinct label in strictly ascending order, a pair consisting of the respective label and the number of items with that label will be displayed. Each pair of numbers will be displayed on a separate line. \
For task $2$, the labels of the compartments will be displayed according to their placement in the chests, $9$ per line of the file, from the first chest to the last, within each chest from the first row to the third row, and within each row from left to right. \
Numbers on the same line of the file are separated by a space.

# Constraints and clarifications
* $c \in \{1,2\}$;
* $1 \leq n \leq 10 \ 000$;
* The label of an item is between $10$ and $99$ inclusive.
* In the case of task $2$, the labels will be displayed for all compartments, even if they are empty or come from completely empty chests.
* For $40$ points, $c = 1$;
* For $60$ points, $c = 2$.

# Example 1

`cufere.in`
```
1
2
1488 1573 1437 4465 1099 1073 0 499 765
537 1173 4288 1273 2299 1555 1241 655 841
1141 237 5621 199 921 621 3465 1315 4155
1099 341 4765 6155 355 1099 6088 3988 255
4955 155 1329 1932 3099 114 3020 855 5555
1173 1388 673 2533 1488 1473 4033 2099 2065
```

`cufere.out`
```
14 1
15 13
20 30
21 71
29 13
32 19
33 65
37 21
41 34
55 241
65 152
73 79
88 182
99 107
```

## Explanation

In this example, task $c = 1$ is solved, and there are $n = 2$ chests. In the chests, there are:
* $1$ item labeled $14$;
* $13$ items labeled $15$;
* $30$ items labeled $20$;
* ...
* $107$ items labeled $99$.

# Example 2

`cufere.in`
```
2
2
1488 1573 1437 4465 1099 1073 0 499 765
537 1173 4288 1273 2299 1555 1241 655 841
1141 237 5621 199 921 621 3465 1315 4155
1099 341 4765 6155 355 1099 6088 3988 255
4955 155 1329 1932 3099 114 3020 855 5555
1173 1388 673 2533 1488 1473 4033 2099 2065
```

`cufere.out`
```
114 1315 3020 6421 721 1329 1932 6433 133
1637 537 1641 1641 241 6455 6455 6455 4955
6465 6465 2465 1673 1673 1673 1673 1573 6488
6488 5488 6499 4399 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
```

## Explanation

In this example, task $c = 2$ is solved, and there are $n = 2$ chests. After rearrangement, the items are placed in ascending order of labels. For the first three labels, only one group is formed, each being placed in the first three compartments of the first chest. Then, the $71$ items labeled $21$ (hard) are split into a group of $64$ (in the fourth compartment) and a group of $7$ (in the fifth compartment). The same process is followed for the other objects, so the first chest is completely occupied, the first row of the second chest is partially occupied to the left, and the last two rows are empty.
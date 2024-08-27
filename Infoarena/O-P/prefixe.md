## Prefixes

As you know, Gigel likes the digits $0$ and $1$. In this problem, he also likes the digit $2$. He analyzes a string $T$ composed only of $0$, $1$, and $2$, and is fascinated by the patterns he notices in the string. The character $T_1$ is the first character of the string, $T_2$ the second, and so on. The string has a length $N$. Gigel is interested in the prefixes $T_1, \dots, T_i$ of this string $(1 \leq i \leq N)$. He notices that such a prefix of length $i$ has, in turn, certain prefixes that are also suffixes. For example, if $T = 0101012$ and $i = 5$, in the prefix $01010$ there is the prefix $010$ which is also a suffix. He asks you to find for each prefix $T_1, \dots, T_i$ the length of the largest prefix different from $T_1, \dots, T_i$ which is also a suffix of $T_1, \dots, T_i$.

## Input data

The input file `prefixe.in` contains on the first line the number $Z$ of tests. The next $Z$ lines each contain a test. A test consists of a string composed of $0$, $1$, and $2$.

## Output data

In the output file `prefixe.out` print for each prefix $T_1, \dots, T_i$ of the given input string the length of the largest prefix different from $T_1, \dots, T_i$ which is also a suffix for $T_1, \dots, T_i$. Lengths must be separated by spaces.

## Constraints

$1 \leq N \leq 131072$

$1 \leq Z \leq 128$

## Example

`prefixe.in`
```
1
010010010010
```

`prefixe.out`
```
0 0 1 1 2 3 4 5 6 7 8 9
```

## Explanation

For $T_1, \dots, T_5$, the prefix $T_1, T_2$ is equal to the suffix $T_4, 5$, so the 5th number in the output is $2$, the length of the string $T_1, T_2$.
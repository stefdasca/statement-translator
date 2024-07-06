Sure! Here is the translated text:

```
Constănțean's fortune increased after building the hotel in Bansko. Long live the schools in Constanța! Now, however, evil people are trying to steal his wealth. To stop them, he changes his password daily at the bank account. The Dobrogeana Bank sends him over $T$ days, a pair of two natural numbers $A$ and $B$, $A < B$. For maximum protection, the entrepreneur needs to find the "tri-xor" sum of a pair of numbers included in the interval $[A, B]$.

The "tri-xor" operation is analogous to the "xor" operation, but it applies to the numbers written in base 3 in "trits" (the digits of the number in base 3) that are on the same level, and the value table is as follows:

|trit| 0 | 1 | 2 |
|:---:|:---:|:---:|:---:|
|**0**| 0 | 1 | 2 |
|**1**| 1 | 2 | 0 |
|**2**| 2 | 0 | 1 |

For example, `15(0120) “tri-xor” 30(1010) = 36(1100)` or `2(0002) “tri-xor” 2(0002) = 1(0001)`.

# Task

Help Constănțean find for each of the $T$ pairs of the form $(A, B)$, the maximum “tri-xor” sum that can be obtained using two numbers from the interval $[A, B]$. Who knows? Maybe you'll get a room with a ski slope view!

# Input data

The input file `tri-xor.in` will contain on the first line the number $T$ of tests.
On the next $T$ lines will contain $2$ numbers, $A$ and $B$, separated by a space.

# Output data

Print $T$ numbers, each on a separate line of the `tri-xor.out` file, so that on line $i$ there is the answer to the $i$-th question.

# Constraints and clarifications

* $1 \leq T \leq 100 \ 000$;
* $0 \leq A, B \leq 10^{18} $;

| # | Points | Constraints |
|:---:|:----:|:----:|
| 1 | 30 | $ T, A, B \leq 100$|
| 2 | 40 | $ T, A, B \leq 1 \ 000$ |
| 3 | 30 | Without additional constraints | 

# Example

`tri-xor.in`
```
5
15 26
1 9
2 37
45 168
0 1005
```

`tri-xor.out`
```
23
18
74
242
2006
```

## Explanation

* $15$ “tri-xor” $17 = 23$
* $9$ “tri-xor” $9 = 18$
* $37$ “tri-xor” $37 = 74$
* $74$ “tri-xor” $168 = 242$
* $1001$ “tri-xor” $1005 = 2006$

All these solutions are maximum but not necessarily unique.
```

I have translated the text as specified and made sure everything is grammatically correct in English.
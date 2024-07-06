Once upon a time, there was a magical fairy named Ursul Brumi. One day, the fairy decided to stroll through the forest when, seemingly out of nowhere, an old woman (*@lavgiorgionicusor12* on TikTok) started yelling at her:
> I thought you were hurt, fairy. Ursul Brumi, I’ve come to eat you!

Upon hearing this, Ursul Brumi realized that he had to disintegrate into multiple pieces to become invisible to the old woman. Thus, he escaped the danger, and finally, he integrated back into one piece, once again becoming a fairy of grade $10$.

# Task
Given an array $v$ of $N$ numbers. We define $xum(i \ldots j) = v_{i} \oplus v_{i+1} \oplus \ldots \oplus v_{j}$, where $1 \leq i \leq j \leq N$, and $\oplus$ denotes the bitwise *$xor^1$* operator.
Calculate $S = \sum_{1 \leq i \leq j \leq n} xum(i \ldots j)$.

# Input data 
The first line of the file `xum.in` will contain $N$, the number of elements in $v$. The next line will contain the $N$ elements of $v$.

# Output data
Print in the file `xum.out` the required result.

# Constraints and clarifications
* $1 \leq N \leq 10^5$;
* $VMAX \leq 10^3$;
* $1 \leq v_{i} \leq VMAX$;
* $20\%$ of the tests have $N \leq 10^3$;
* $^1$About the "xor" operator, you can read more in [this](https://en.wikipedia.org/wiki/Bitwise_operation#XOR) very fine article.

# Example
`xum.in`
```
3
1 2 3
```

`xum.out`
```
10
```

## Explanation
$1 + 2 + 3 + (1 \oplus 2) + (2 \oplus 3) + (1 \oplus 2 \oplus 3) = 10$
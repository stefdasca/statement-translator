```markdown
Let $N$ be a natural number composed of **non-zero** digits.

# Task

Determine the sum of all distinct numbers that can be formed using all the digits of the number $N$.

# Input data

The input file `sumall.in` contains on the first line the natural number $N$.

# Output data

The output file `sumall.out` will contain on the first line the sum of all distinct numbers that can be formed using all the digits of the number $N$.

# Constraints and clarifications

* $1 \leq N < 10^{19}$

# Example 1

`sumall.in`
```
123
```

`sumall.out`
```
1332
```

## Explanation

All distinct numbers that can be formed with the digits $1$, $2$, $3$ are: $123$, $132$, $213$, $231$, $312$, $321$.
$123 + 132 + 213 + 231 + 312 + 321 = 1 \ 332$.

# Example 2

`sumall.in`
```
788
```

`sumall.out`
```
2553
```

## Explanation

All distinct numbers that can be formed with the digits $7$, $8$, $8$ are: $788$, $878$, $887$.
$788 + 878 + 887 = 2 \ 553$
```
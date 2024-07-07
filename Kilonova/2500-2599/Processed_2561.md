
# Task

Gigel, the resident wizard in Peppers, discovered a magic natural number $n$.

Dissatisfied with the value of this number, Gigel invented a spell that can modify the magic number. This spell works as follows:

- The spell will find the minimum digit in $n$, which will be denoted by $c$.
- The spell will find the maximum digit in $n$, which will be denoted by $d$.
- The spell will subtract from $n$ the product of $c$ and $d$.

For example, if $n=291$, then $c=1$ and $d=9$, and $n$ will have the new value $291 - 1 \cdot 9 = 282$.

Gigel would like to apply $k$ successive spells on the magic number, but he is not sure if the final value of $n$ will be satisfactory. Therefore, he asks you to help him find the final value of the magic number after $k$ successive spells.

# Input data

The first line of the file `nkspells.in` contains two natural numbers $n$ ($10 \le n \le 1\,000\,000\,000$) — the initial value of the magic number, and $k$ ($0 \le k \le 1\,000\,000\,000$) — the number of spells Gigel wants to perform.

# Output data

The file `nkspells.out` should contain a natural number, the value of $n$ after Gigel performs the $k$ spells.

# Constraints and clarifications
|#|Score|Constraints                           |
|-|-----|--------------------------------------|
|1| 10  | $k=0$                                |
|2| 30  | $k=1$                                |
|3| 35  | $k \le 100\,000$                     |
|4| 25  | No further constraints               |

# Example 1

`nkspells.in`

```
291 4
```

`nkspells.out`
```
244
```

## Explanation 

In the first example, the values of $n$ will be, in order: $291 \rightarrow 282 \rightarrow 266 \rightarrow 254 \rightarrow 244$.

# Example 2

`nkspells.in`

```
75 2
```

`nkspells.out`

```
40
```

## Explanation

In the second example, the values of $n$ will be, in order: $75 \rightarrow 40 \rightarrow 40$.
```

Double-checked for potential grammar and syntax errors. The translation maintains the original structure and data while ensuring clarity and accuracy in English.
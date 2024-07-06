```markdown
A flower shop wants to achieve a Guinness book record with the largest floral arrangement. They have `t` types of flowers, out of which four types are more special: gerbera, orchid, azalea, and hydrangea. The workers have decided to place the flowers evenly spaced in several rows, with exactly `n` flowers in each row. There will not be two identical rows, but all rows will comply with certain requirements:
* They have observed that hydrangeas have a much longer lifespan if they are in the same row as an azalea and an orchid, regardless of whether the order is azalea-hydrangea-orchid or orchid-hydrangea-azalea.
* Gerberas will be placed such that there are at least `p` flowers between any two gerberas, the type of which can be anything but gerbera.

For example, if we have `t=5` types of flowers: azalea (denoted as `a`), hydrangeas (denoted as `h`), orchids (denoted as `o`), gerberas (denoted as `g`), and begonias (denoted as `b`), there will be at least `p=3` flowers between two gerberas, and the row will consist of `n=6` flowers, then the following floral arrangements are correct: `aoaaoo`, `ahohag`, `gbbbgo`, `gbbbog`, `bbbbbb`.

However, the following arrangements are not correct: `ohoaha` (the hydrangeas are not between an orchid and an azalea), `gogbao` (the two gerberas are not separated by at least three flowers), `ahohah` (the last hydrangea is not adjacent to an orchid).

For `n=6, p=3, t=5`, the number of different floral arrangements is `2906`.

# Task
Given the values of `n, p` and `t`, determine the number of distinct lines that can be obtained with the above requirements.

# Input data
The `ikebana.in` file contains on a single line `3` natural numbers `n, p` and `t` separated by a space.
`n` - represents the number of flowers on a row;
`p` - the minimum number of flowers that must separate two gerberas in a row;
`t` - the number of distinct types of flowers available to the flower shop.

# Output data
The `ikebana.out` file will contain on the single line a single number: the number of distinct arrangements modulo `666013`.

# Constraints and clarifications
* `1 \leq n \leq 1\ 000\ 000\ 000`;
* `3 \leq p \leq 20`;
* `4 \leq t \leq 20`;

# Examples

`ikebana.in`
```
6 3 5 
```

`ikebana.out`
```
2906
```

Explanations
---

The number of distinct arrangements is `2906`

`ikebana.in`
```
10 6 8 
```

`ikebana.out`
```
620160
```

Explanations
---
The number of distinct arrangements is `181775696`, and we have: `181775696 % 666013 = 620160`
```
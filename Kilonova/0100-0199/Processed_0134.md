After a long career in the plumbing industry, Dorel decided to invest his accumulated wealth in the stocks of several companies. Thus, he has a list of `N` companies in which he wants to buy stocks, over `M` consecutive days.

On the first day, the amount of money invested in company `i` is `s[1][i] = a[i]`, for any $i = \overline{1, N}$, where the values `a[i]` are given.

**The numbers `a[1], a[2], ..., a[N]` represent a permutation of the numbers `1, 2, ..., N`**.

On the `j`-th day, he will invest in company `i` an amount of money equal to `s[j][i] = s[j - 1][a[i]]`, for any day $j = \overline{2, M}$ and any company $i = \overline{1, N}$.

# Task
After completing the investment plan, Dorel wants to generate `Q` statistics regarding the invested amounts.

Given `Q` sets of values $z_i, z_f, c_l, c_r$, he wishes to know the total amount invested in the period between days $z_i$ and $z_f$ (inclusive), in companies whose order numbers are between $c_l$ and $c_r$ (inclusive).

# Input data
The first line of the input file `investitie.in` contains the numbers `N` and `M`, separated by a space.
The second line contains the values `a[1], a[2], ..., a[N]`, separated by spaces.
The third line contains the value `Q`.
Each of the next `Q` lines contains four values, $z_i, z_f, c_l, c_r$, separated by spaces.

# Output data
The output file `investitie.out` will contain, on separate lines, the invested amounts corresponding to each of the `Q` statistics from the input file.

# Constraints and clarifications
* `1 \leq N, Q \leq 100 000`
* `1 \leq M \leq 1 000 000 000`
* $1 \leq z_i \leq z_f \leq M$
* $1 \leq c_l \leq c_r \leq N$
* $0 \leq c_r - c_l \leq 100$
* For `10` points: `M = 1`
* For another `20` points: `1 \leq N, M \leq 100, 1 \leq Q \leq 1 000`
* For another `12` points: `101 \leq N, M \leq 3 000`
* For another `24` points: `1 \leq N \leq 50`
* For another `34` points: Without other restrictions

# Examples

`investitie.in`

```
8 3
3 1 7 2 6 4 5 8
5
1 1 3 7
1 2 1 4
1 3 2 8
2 3 3 6
3 3 3 3
```

`investitie.out`

```
24
29
93
24
6
```

Explanation
---

The invested amounts over the three days, in the stocks of the eight companies, will be:

```
3 1 7 2 6 4 5 8
7 3 5 1 4 2 6 8
5 7 6 3 2 1 4 8
```

The first statistic asks for the amount invested on the first day in companies with order numbers from `3` to `7`. The sum is `7 + 2 + 6 + 4 + 5 = 24`.

The second statistic asks for the amount invested in the first two days in companies with order numbers from `1` to `4`. The sum is `(3 + 1 + 7 + 2) + (7 + 3 + 5 + 1) = 29`. 
Similar calculations are done for the other statistics.
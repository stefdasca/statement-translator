
Fujiwara-san loves dates! She calls a date a string of form `y/m/d` where `d, m` and `y` are positive integers without leading zeroes that represent a calendar date (`d` is the day, `m` is the month, `y` is the year). The precise rules for a valid date is the following:
* `y ∈ {1, 2, . . .}`.
* `m ∈ {1, . . . , 12}`
* If `m ∈ {1, 3, 5, 7, 8, 10, 12}`, then `d ∈ {1, . . . , 31}`.
* If `m ∈ {4, 6, 9, 11}`, then `d ∈ {1, . . . , 30}`.
* If `m = 2` and `y` is either not a multiple of `4`, or both a multiple of `100` and not a multiple of `400`, then `d ∈ {1, . . . , 28}`.
* If `m = 2` and `y` is a multiple of `4`, and either not a multiple of `100` or a multiple of `400`, then `d ∈ {1, . . . , 29}`.

For example, `2022/2/14, 2024/2/29` and `2000/2/29` are valid dates; whereas `2022/02/14, 2022/2/29` and `2100/2/29` are not valid dates.

Fujiwara-san has recently received a sequence of symbols $s_1, ..., s_n$, where $s_i ∈ \{0, 1, ..., 9, /\}$. She now wants to ask: how many sequences of indices $1 \leq i_1 < ... < i_k \leq n$ exist such that $ s_{i_1}, ..., s_{i_k} $ are a valid date?

# Task
The first line of the input contains the integer `n`. The second line contains the symbols $s_1, ..., s_n$, not separated by spaces.

# Output data
Output the answer modulo $10^9 + 7$.

# Constraints and clarifications
* `1 \leq n \leq 100\ 000`.

## Subtask 1 (12 points)
* `n \leq 15`
## Subtask 2 (7 points)
* `n \leq 1\ 000`
* $s_i \in \{5, /\}$
## Subtask 3 (8 points)
* $s_i \in \{5, /\}$
## Subtask 4 (7 points)
* $s_i = / $ or $s_i \geq 5$
## Subtask 5 (8 points)
* $s_i \neq 0, s_i \neq 2$
## Subtask 6 (9 points)
* `n \leq 1000` 
* $s_i \neq 2$
## Subtask 7 (11 points)
* $s_i \neq 2$
## Subtask 8 (38 points)
* No further restrictions.

# Examples

`stdin`

```
8
55/55/55
```

`stdout`

```
12
```

Explanation
---

`5/5/5` appears `8` times within the input, and `55/5/5` appears `4` times.

`stdin`

```
7
44/2/29
```

`stdout`

```
9
```

Explanation
---

`4/2/2, 4/2/9, 4/2/29` all appear `2` times, and `44/2/2, 44/2/9, 44/2/29` all appear once.

`stdin`

```
8
11/11/31
```

`stdout`

```
24
```

Explanation
---

`1/1/1, 1/1/3, 1/1/31` appear `4` times each, `1/11/1, 1/11/3, 11/1/1, 11/1/3, 11/1/31` appear `2` times each, and `11/11/1, 11/11/3` appear once.

`stdin`

```
22
11/2/43432/534/123/234
```

`stdout`

```
66078
```

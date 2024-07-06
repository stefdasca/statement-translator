```markdown
Robert got bored of his white t-shirt, so he decided to dye it in his favorite color, blue. He received from his friend, Georgian, multiple pills of `N` different shades of blue, now having $p_i$ pills of the `i`-th shade of blue (for `i` from `1` to `N`). To dye the t-shirt, Robert will put the t-shirt in the washing machine along with various pills.

Bored of the usual shades of blue, he will create a new shade by taking $a_1, ..., a_N$ pills ($a_i$ pills from the initial shade `i`). Robert will take **at least one pill** from each initial shade and at most $p_i$ pills from shade `i`. Also, he can only use an integer number of pills from each type. Two shades $a_1, ..., a_N$ and $b_1, ..., b_N$ will be considered the same if and only if $\\frac{a_1}{b_1} = ... = \\frac{a_N}{b_N}$.

Now, Robert wonders how many different new shades of blue he can create. Knowing that this number can be very large, he is satisfied with the answer **modulo 1 000 000 007**.

# Input data
The first line contains an integer `N`, representing the number of distinct shades.
The second line contains `N` integers $p_1 ... p_N$, representing the number of pills available from the `i`-th initial shade.

# Output data
Print a single line containing a single integer, representing the number of different shades that can be formed **modulo 1 000 000 007**.

# Constraints and clarifications
* We will denote $V_{min} = min(p_1, ..., p_N)$ and $V_{max} = max(p_1, ..., p_N)$.
* `1 \\leq N \\leq 200 000`
* $1 \\leq V_{min} \\leq V_{max} \\leq 200 \ 000$

## Subtask 1 (2 points)
* $V_{min} = 1$

## Subtask 2 (6 points)
* $1 \\leq N, V_{max} \\leq 7$

## Subtask 3 (4 points)
* $1 \\leq N, V_{max} \\leq 8$

## Subtask 4 (16 points)
* $1 \\leq N, V_{max} \\leq 100$

## Subtask 5 (11 points)
* $1 \\leq N, V_{max} \\leq 1 \ 000$

## Subtask 6 (7 points)
* $1 \\leq N, V_{max} \\leq 5 \ 000$

## Subtask 7 (15 points)
* $1 \\leq N, V_{max} \\leq 30 \ 000$

## Subtask 8 (10 points)
* $V_{min} = V_{max}$

## Subtask 9 (8 points)
* $1 \\leq V_{min} \\leq 100$

## Subtask 10 (21 points)
* Without additional restrictions.

# Examples

`stdin`

```
3
2 3 2
```

`stdout`

```
11
```

`stdin`

```
4
7 7 7 7
```

`stdout`

```
2303
```

`stdin`

```
7
15 8 19 7 15 8 19
```

`stdout`

```
36191027
```

`stdin`

```
2
31124 150719
```

`stdout`

```
851838928
```

Explanations
---

For the first example, the `11` possible shades are:
* ⟨1, 1, 1⟩ (the same as ⟨2, 2, 2⟩)
* ⟨1, 1, 2⟩
* ⟨1, 2, 1⟩
* ⟨1, 2, 2⟩
* ⟨1, 3, 1⟩
* ⟨1, 3, 2⟩
* ⟨2, 1, 1⟩
* ⟨2, 1, 2⟩
* ⟨2, 2, 1⟩
* ⟨2, 3, 1⟩
* ⟨2, 3, 2⟩
```

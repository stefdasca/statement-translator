Here is the translated text:

---

Zgăbeață Iftode is the son of a tavern keeper from Văscăuți. As a punishment for the poor impression left during the director's inspection, the pedagogue ordered the entire class to solve a difficult math exercise.

~[iftode.png]
*The pedagogue and the student Zgăbeață Iftode. Dem Rădulescu and Vasile Muraru in “Doi Vulpoi” (1983).*

For a natural number `X`, the following three types of operations can be performed:
1. Add `1` to `X`. Thus, the new value of `X` will be `X + 1`.
2. Subtract `1` from `X`. Thus, the new value of `X` will be `X - 1`. The operation is valid only for `X > 0`.
3. Halve `X`. Thus, the new value of `X` will be $\\frac{X}{2}$. The operation is valid only for even `X`.

Whatever the initial number `X` is, it is always possible to eventually reach `X = 0` using the above operations. Let’s denote the minimum number of operations required by $c_X$. For example, $c_1 = 1$, because we can perform one type `2` operation and reach `0`, $c_7 = 5$, because we can perform the operations as follows: `7 \rightarrow 8 \rightarrow 4 \rightarrow 2 \rightarrow 1 \rightarrow 0`, and $c_6 = 4$, because we can proceed as follows: `6 \rightarrow 3 \rightarrow 2 \rightarrow 1 \rightarrow 0`.

Iftode found an efficient method to calculate $c_X$ in an old math book, as follows (it is guaranteed that this method is correct):

$$
c_X = \\left\\{  
 \\begin{array}{ll}
        0 & X = 0 \\\\
        1 + c_{\\frac{X}{2}} & X > 0 \\text{ and even} \\\\
        3 & X = 3 \\\\
        1 + c_{X+1} & X \\neq 3, \\text{odd and } \\frac{X-1}{2} \\text{ odd} \\\\
        1 + c_{X-1} & \\text{ otherwise}
    \\end{array}
\\right.
$$

The pedagogue asks the students to calculate the sum $S = \\sum_{X=L+1}^{R} c_X$ for two given numbers `L, R`. The answer should be **modulo 1 000 000 007**. Moreover, the numbers `L`, `R` are given in base `2`.

# Input data
The first line contains the number `L`. The second line contains the number `R`. The numbers are given in base `2`.

# Output data

Print on the first line the sum `S`, **modulo 1 000 000 007**.

# Constraints and clarifications
## Subtask 1 (2 points)
* $0 \\leq L \\leq R < 2^{18}$
## Subtask 2 (7 points)
* $0 \\leq L \\leq R < 2^{60}$
## Subtask 3 (5 points)
* $0 \\leq L \\leq R < 2^{300}$
* $R - L \\leq 10^5$
## Subtask 4 (7 points)
* $0 \\leq L \\leq R < 2^{300}$
## Subtask 5 (7 points)
* $0 \\leq L \\leq R < 2^{800}$
## Subtask 6 (8 points)
* $0 = L \\leq R < 2^{2 \\ 500}$
* `R + 1` is a power of `2`
## Subtask 7 (7 points)
* $0 \\leq L \\leq R < 2^{2 \\ 500}$
## Subtask 8 (9 points)
* $0 = L \\leq R < 2^{100 \\ 000}$
* `R + 1` is a power of `2`
## Subtask 9 (48 points)
* $0 \\leq L \\leq R < 2^{100 \\ 000}$

# Examples

`stdin`

```
100
111
```

`stdout`

```
13
```

`stdin`

```
10110111110101
110000101010110
```

`stdout`

```
256512
```

Explanations
---

In the first example, `L = 4` and `R = 7`. We have $c_5 = 4, c_6 = 4, c_7 = 5$, whose sum is `S = 13`.

In the second example, `L = 11765` and `R = 24918`. The required sum is $S = \\sum_{X=11766}^{24918} c_X = 256512$.

---
### Task

~[patience-is-the-key-geometry-dash.gif|align=right|width=30%]

After many sleepless nights trying to beat the level **Limbo** from **Geometry Dash**, you gave up and fell asleep in your chair. In your astral journey, you found $8$ keys, arranged in the form of a matrix with $4$ rows and $2$ columns. We denote $C_{i,j}$ as the key in row $i$ and column $j$. The matrix $C$ is indexed from $0$. Each key has an associated color. The colors of the keys are pairwise distinct.

On this key assembly, the following operations can be performed:
- `X0` - swap $C_{0,0}$ with $C_{1,1}$; $C_{0,1}$ with $C_{1,0}$; $C_{2,0}$ with $C_{3,1}$; $C_{2,1}$ with $C_{3,0}$;
- `X1` - swap $C_{0,0}$ with $C_{3,1}$; $C_{0,1}$ with $C_{3,0}$; $C_{1,0}$ with $C_{2,1}$; $C_{1,1}$ with $C_{2,0}$;
- `Ol` - $C_{0,0}$; $C_{0,1}$; $C_{1,1}$; $C_{2,1}$; $C_{3,1}$; $C_{3,0}$; $C_{2,0}$; $C_{1,0}$ are rotated left circularly;
- `Or` - $C_{0,0}$; $C_{0,1}$; $C_{1,1}$; $C_{2,1}$; $C_{3,1}$; $C_{3,0}$; $C_{2,0}$; $C_{1,0}$ are rotated right circularly;
- `ol` - $C_{0,0}$; $C_{0,1}$; $C_{1,1}$; $C_{1,0}$ and $C_{2,0}$; $C_{2,1}$; $C_{3,1}$; $C_{3,0}$ are rotated left circularly;
- `or` - $C_{0,0}$; $C_{0,1}$; $C_{1,1}$; $C_{1,0}$ and $C_{2,0}$; $C_{2,1}$; $C_{3,1}$; $C_{3,0}$ are rotated right circularly;
- `S` - swap $C_{0,0}$ with $C_{2,0}$; $C_{0,1}$ with $C_{2,1}$; $C_{1,0}$ with $C_{3,0}$; $C_{1,1}$ with $C_{3,1}$;
- `R` - the matrix $C$ will be rotated by $180$ degrees.

### Task

Only one of these keys is the correct one. For simplicity, we will consider that the correct key is always initially located at position $(0, 0)$. You are bored and apply exactly $N$ random operations. After applying the operations, display the probability in the form $P \cdot {Q}^{-1}$ for each position $(i, j)$ in the matrix that the correct key is located at $(i, j)$ after the $N$ operations, modulo ${10}^{9}+7$.

### Constraints and clarifications:
* $0 \leq N \leq {10}^9$
* For $10 \%$ of the tests: $N \leq 7$
* For $60 \%$ of the tests: $N \leq 1 \ 000 \ 000$
* It can be proven that all probabilities can be represented as an irreducible fraction in the form $P / Q$.

### Example 1:

`stdin`
```
0
```

`stdout`
```
1 0
0 0
0 0
0 0
```

#### Explanation
No moves are performed. The correct key remains in cell $(0, 0) \ (\frac{1}{1} = 1)$.

### Example 2:

`stdin`
```
1
```

`stdout`
```
0 250000002
250000002 125000001
125000001 0
0 250000002
```

#### Explanation:
There are exactly $8$ possible move sequences.

For $(0, 0)$ there is no sequence of $1$ move after which the correct key is in cell $(0, 0)$.
For $(0, 1)$ there are $2$ sequences of $1$ move after which the correct key is in cell $(0, 1)$: `Or` and `or`.
For $(1, 0)$ there are $2$ sequences of $1$ move after which the correct key is in cell $(1, 0)$: `Ol` and `ol`.
For $(1, 1)$ there is $1$ sequence of $1$ move after which the correct key is in cell $(1, 1)$: `X0`.
For $(2, 0)$ there is $1$ sequence of $1$ move after which the correct key is in cell $(2, 0)$: `S`.
For $(2, 1)$ there is no sequence of $1$ move after which the correct key is in cell $(2, 1)$.
For $(3, 0)$ there is no sequence of $1$ move after which the correct key is in cell $(3, 0)$.
For $(3, 1)$ there are $2$ sequences of $1$ move after which the correct key is in cell $(3, 1)$: `R` and `X1`.

### Example 3:

`stdin`
```
26
```

`stdout`
```
265464296 292931484
340193730 718335589
531664420 909806279
957068525 984535713
```

#### Explanation:
In the **Limbo** level of **Geometry Dash**, exactly $26$ random moves are applied every time.

### Example 4:
`stdin`
```
69420
```

`stdout`
```
595491153 534885681
436356732 994853266
255146743 813643277
715114328 654508856
```

#### Explanation:
https://dexonline.ro/definitie/dum%C4%83/516869
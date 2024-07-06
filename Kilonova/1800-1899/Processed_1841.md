```markdown
_Note: In the statement, $\\overline{b_1 \dots b_k}$ represents an integer written in binary notation, where $b_1$ is the most significant bit, and $b_k$ is the least significant bit._

While flying on her broomstick through the galaxy, the witch Roxana discovered a new planet (planet BR-PERM) where all inhabitants were involved in a new dance. In this dance, participants stand in a line and then reorder themselves. In a dance with $2^k$ inhabitants, the person at position $\\overline{b_1 \dots b_k}$ will move to position $\\overline{b_k \dots b_1}$ (indexed from $0$).

Roxana realized that each person on BR-PERM wears clothing of one of the $26$ colors. These colors will be represented by letters of the Latin alphabet.

BR-PERM inhabitants consider as special the dance sequences where the sequence of colors that inhabitants wear before and after the dance remains the same. They call such sequences _cute_. For example, when $k = 2$, we have a sequence of $4$ dancers $0$, $1$, $2$, $3$, which after the dance will be ordered as follows: $0$, $2$, $1$, $3$. So, the sequence of colors `abba` is _cute_, but `abca` is not.

# Task

The BR-PERM inhabitants ask Roxana to help them with this problem (it seems that witches always help people solve their problems). They show her a sequence of $n$ dancers and ask her to answer multiple questions: “Is the subarray of length $2^k$ that starts at dancer $i$ _cute_?”

# Interaction Protocol

The contestant must implement two functions, the first of which is:

```cpp
void init (int n, const char s[]);
```

This function will be called once at the beginning of the interaction and will provide the contestant with the sequence of colors of the dancers' clothing through the parameter $s$.

The second function that needs to be implemented is:

```cpp
int query (int i, int k);
```

This function will be called exactly $Q$ times and will return $1$ if and only if the continuous subarray of length $2^k$ in $s$ starting at the $i$-th dancer (indexed from $0$) is _cute_. Otherwise, it will return $0$.

# Constraints and clarifications

* $1 \leq N \leq 500 \ 000$
* $1 \leq Q \leq 500 \ 000$

| # | Points | Constraints          |
| - | ------- | ------------------- |
| 1 | 13      | $1 \leq N, Q \leq 1 \ 000$ |
| 2 | 37      | $1 \leq N, Q \leq 100 \ 000$      |
| 3 | 17      | $s$ contains only the characters `a` and `b`. Colors are chosen randomly and independently with a fixed probability for each test.   |
| 4 | 33      | Without additional constraints    |

# Example

`input`
```
init(8, "axxyxxyb")
```

`output`
```
query(0, 3) = true
query(1, 1) = true
query(1, 2) = false
query(3, 2) = true
```
```
Here is the translated competitive programming problem statement:

---

Let $ N $ be a natural number. We say that $ (A, B, C) $ is *a geometric triplet bounded by $ N $*, if $ A, B $ and $ C $ are three natural numbers such that
\[ 1 \leq A < B < C \leq N \]
and
\[ B = \sqrt{A \cdot C}. \]

# Task

Determine the number of geometric triplets bounded by the natural number $ N $.

# Input data

The input file `tg.in` contains on the first line a natural number $ N $.

# Output data

The output file `tg.out` contains on the first line the number of geometric triplets bounded by the natural number $ N $.

# Constraints and clarifications

* $ 4 \leq N \leq 4 \ 000 \ 000 $

# Example 1

`tg.in`
```
8
```

`tg.out`
```
2
```

## Explanation

The two triplets are $ (1,2,4) $ and $ (2,4,8) $.

---
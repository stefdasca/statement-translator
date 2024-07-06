# Task

Armando bought a rectangular pool consisting of $n \times m \times 1$ cubic regions with a side length of $1$ meter, which he wants to fill with water.

Due to high pool rates, Armando could no longer pay his water bills. Hence, he will have to fetch water for the pool from the nearby river using a bucket inherited from his father.

With one full bucket, Armando can fill a cubic region of $1 \times 1 \times 1$ meters from the pool.

When a non-filled region is adjacent in a line or column with two or more regions filled with water, this one will also get filled as if by magic. This process will continue either until the pool is filled or until no other region can be filled with water:

* $$ \begin{bmatrix}1&0&0\\\\0&1&0\\\\1&0&1\end{bmatrix} \rightarrow \begin{bmatrix}1&1&0\\\\1&1&1\\\\1&1&1\end{bmatrix} \rightarrow \begin{bmatrix}1&1&1\\\\1&1&1\\\\1&1&1\end{bmatrix} $$
* $$ \begin{bmatrix}1&1&0\\\\0&0&1\\\\0&0&0\end{bmatrix} \rightarrow \begin{bmatrix}1&1&1\\\\0&1&1\\\\0&0&0\end{bmatrix} \rightarrow \begin{bmatrix}1&1&1\\\\1&1&1\\\\0&0&0\end{bmatrix} $$

What is the minimum number of buckets of water that Armando needs to carry to fill the pool?

# Input data

The first line of the input file `piscinus.in` will contain two numbers $n$ and $m$ - the length and width of Armando's pool.

# Output data

The output file `piscinus.out` will contain the minimum number of buckets of water that Armando needs to carry to fill the pool.

# Constraints and clarifications
- $1 \le n,m \le 10^9$

|#|Points|Constraints                            |
|--|------|--------------------------------------|
|1 | 10   | $n=1$                                |
|2 | 10   | $n=m$                                |
|4 | 25   | $n,m \le 5$                          |
|5 | 55   | No additional constraints            |

# Example 1

`piscinus.in`

```
2 2
```

`piscinus.out`
```
2
```

## Explanation 

Armando will carry two buckets of water to fill the regions $(1,1)$ and $(2,2)$: $$ \begin{bmatrix}1&0\\\\0&1\end{bmatrix} \rightarrow \begin{bmatrix}1&1\\\\1&1\end{bmatrix} $$

# Example 2

`piscinus.in`

```
4 3
```

`piscinus.out`
```
4
```

## Explanation 

Armando will carry four buckets of water to fill the regions $(1,2)$, $(2,3)$, $(3,1)$ and $(4,3)$:
$$ \begin{bmatrix}0&1&0\\\\0&0&1\\\\1&0&0\\\\0&0&1\end{bmatrix} \rightarrow \begin{bmatrix}0&1&1\\\\0&1&1\\\\1&0&0\\\\0&0&1\end{bmatrix} \rightarrow  \begin{bmatrix}0&1&1\\\\1&1&1\\\\1&1&1\\\\0&0&1\end{bmatrix} \rightarrow \begin{bmatrix}1&1&1\\\\1&1&1\\\\1&1&1\\\\0&1&1\end{bmatrix} \rightarrow \begin{bmatrix}1&1&1\\\\1&1&1\\\\1&1&1\\\\1&1&1\end{bmatrix} $$
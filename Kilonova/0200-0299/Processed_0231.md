```markdown
A matrix with `m` rows and `n` columns is given, with non-zero natural number elements and a fixed non-zero natural number `k`.

# Task

For the given matrix and number `k`, answer `q` questions of the form: "How many square submatrices with side `L` have the greatest common divisor of elements equal to `k` in the given matrix?"

# Input data

The input file `xcmmdc.in` contains in the first line four non-zero natural numbers separated by a space: `m` and `n` - the number of rows and the number of columns of the matrix, `k` - the given natural number, and `q` - the number of questions. The next `m` lines contain the rows of the matrix. Each of these lines contains `n` natural numbers separated by a space - the elements of the corresponding line in the matrix. The next `q` lines describe the questions. Each of these lines contains a single natural number `L` - the side of the submatrix in the corresponding question.

# Output data

The output file `xcmmdc.out` will contain `q` lines. Each of these lines will contain a single natural number representing the answer to the corresponding question in the input file.

# Constraints and clarifications

* `1 \leq n, m \leq 1002`
* For `50%` of the tests `1 \leq n, m \leq 502`
* `1 \leq q \leq 50002`
* $1 \leq k \leq 10^9+2$
* The elements of the matrix are non-zero natural numbers less than or equal to $10^9+2$.
* `1 \leq L \leq min(m,n)` for each question

# Example

`xcmmdc.in`

```
3 3 3 4
3 6 2
9 12 3
2 6 3
2
1
3
2
```

`xcmmdc.out`

```
2
3
0
2
```

Explanation
---

For the first and last questions, there are two submatrices:

```
3 6
9 12
```

```
12 3
6 3
```

The first submatrix is obtained by the intersection of the first two rows with the first two columns, and the second by the intersection of the last two rows with the last two columns.
```
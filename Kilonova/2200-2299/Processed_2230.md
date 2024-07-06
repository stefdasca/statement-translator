### Task

We have $m$ segments, all of the same length. These segments can be used to construct closed polygons of length $3$, $4$, $5$, etc., which we will call eyes.

~[lant.png]

These eyes will be connected to each other using $0$ or more segments. Such a chain always starts and ends with an eye. The examples below show a chain formed with $3$ eyes from $16$ segments.

~[lant2.png]

Two chains are considered equivalent if they contain the same number $m$ of segments, the same number $k$ of eyes, and the corresponding eyes have the same size and are connected by the same number of segments. If two chains are not equivalent, we will call them different.
The chains in examples $1$ and $2$ are equivalent, while the chains in examples $3$ and $4$ differ from the other three chains.

Determine the number of different chains formed from $m$ segments and having $k$ eyes.

### Input data

The file `lant.in` contains on a single line the two natural numbers $m$ and $k$ separated by a space.

### Output data

The file `lant.out` will contain a single natural number, representing the number of distinct chains modulo $666 \ 013$.

### Constraints and clarifications

* $3 \leq m \leq 600 \ 000$
* $k \leq \frac{m}{3}$
* For $30\%$ of the tests $m \leq 200$.
* For another $30\%$ of the tests $m \leq 1 \ 500$.

### Example 1

`lant.in`
```
10 3
```

`lant.out`
```
3
```

#### Explanation

We have three distinct chains with $3$ eyes from $10$ segments:

~[lant3.png]

### Example 2

`lant.in`
```
21 4
```

`lant.out`
```
2520
```
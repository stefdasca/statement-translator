## Task

Tică the Trickster is a big fan of bitwise operations. One evening, to ward off monotony, he took an array $v$ of $N$ natural numbers, strictly less than $2^B$, and constructed a matrix $w$ with $N$ rows and $N$ columns based on the following rule:

if $(i + j) \% 4 = 0$

$$w[i][j] = v[i] \wedge v[j]$$

if $(i + j) \% 4 = 2$

$$w[i][j] = v[i] \& v[j]$$

if $(i + j) \% 2 = 1$

$$w[i][j] = v[i] \rightarrow v[j]$$

The symbols $\wedge$ and $\&$ represent bitwise XOR and bitwise AND operations, respectively. The operation $x \rightarrow y$ means the following:

- Consider the binary representations of $x$ and $y$ over $B$ bits
- Perform bitwise logical implication
- Convert the result back to base 10

Logical implication is defined by the rule:

- 0 $\rightarrow$ 0 = 1
- 0 $\rightarrow$ 1 = 1
- 1 $\rightarrow$ 0 = 0
- 1 $\rightarrow$ 1 = 1

For example, if $B = 2$ then $1 \rightarrow 1 = 3$. The next day, Tică shows the matrix $w$ he described to his friend Ionel and challenges him to guess the initial array of numbers. Tică is known for liking to trick his friends from time to time. Thus, there is a possibility that for the matrix Tică hands over to Ionel, there is no array that can generate it following the described process. Knowing the numbers $N$ and $B$, as well as the matrix $w$, write a program to help Ionel determine a possible solution for the array $v$ or specify if such a solution does not exist.

## Input data

The input file `operatie.in` contains on the first line the numbers $N$ and $B$ as described above. The next $N$ lines contain $N$ natural numbers each, representing the description of the matrix $w$.

## Output data

The output file `operatie.out` will contain, on a single line, $N$ numbers separated by a space, representing a possible solution for the array $v$, in case it exists. If such a solution does not exist, the file will contain only the value $-1$.

## Constraints and clarifications

$$2 \leq N \leq 1000$$

$$2 \leq B \leq 30$$

The elements of the array $v$ are indexed from 0. Both the rows and columns of the matrix $w$ are indexed from 0.

For tests worth 20 points

$$N \leq 5$$ 
$$B \leq 4$$

For other tests worth another 20 points 

$$N \leq 1000$$ 
$$B \leq 10$$

## Example

`operatie.in`

```
3 4
0 15 8
15 11 12
8 15 0
```

`operatie.out`

```
11 11 8
```

## Explanation:

In the first example, the binary representations over $B$ bits of the numbers in $v$ are:

- $v[0] = 1011$
- $v[1] = 1011$
- $v[2] = 1000$

We observe that the values in $w$ correspond. For example:

- $w[0][2] = (1011) \& (1000) = 1000 = 8$
- $w[1][2] = (1011) \rightarrow (1000) = 1100 = 12$
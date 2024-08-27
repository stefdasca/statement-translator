### Deletegcd

A sequence is called "smecher" if the greatest common divisor of all its elements is different from $1$. A sequence is called "almost-smecher" if by deleting a single element from it, the sequence becomes "smecher". You are given a sequence of natural numbers $A$ of length $n$ and $q$ queries. For each query, you are given $2$ indices $l$ and $r$ and you need to determine if the subarray from $l$ to $r$ of the array $A$ is an "almost-smecher" sequence. In particular, a sequence that is "smecher" is also considered "almost-smecher".

## Input data

The file `deletegcd.in` contains $q+2$ lines. The first line contains $n$ and $q$. The next line contains $n$ numbers representing the elements of the array $A$. The next $q$ lines contain $2$ numbers each, representing the parameters $l$ and $r$ for the $q$ queries.

## Output data

In the file `deletegcd.out` you will print a string containing the characters $0$ and $1$ without spaces. At position $i$ in the string, print $1$ if the sequence given in query $i$ is "almost-smecher", otherwise print $0$.

## Constraints

$1 \leq N \leq 10^6$

$1 \leq Q \leq 10^6$

$1 \leq l < r \leq N$

$1 \leq A[i] \leq 10^6$

All sequences in the queries are of length at least $3$.

Attention! The tests are grouped:
- For $15$ points, $1 \leq N, Q, A[i] \leq 10^2$ (test group $1-3$)
- For another $20$ points, $1 \leq N, Q, A[i] \leq 10^3$ (test group $4-7$)
- For another $40$ points, $1 \leq N, Q, A[i] \leq 2 \cdot 10^5$ (test group $8-15$)
- For the remaining $25$ points, the initial constraints apply (test group $16-20$)

ATTENTION! Parsing the `deletegcd.in` file is recommended. You can use the code provided by us on the website (for both C++ users with syntax similar to fstream, and pure C lovers). Also, it is recommended to output the result as a string of characters (not one character at a time).

## Example

`deletegcd.in`
```
5 3
1 2 3 4 5
1 3
2 4
3 5
```

`deletegcd.out`
```
010
```

`10 3`
```
95 97 62 15 47 85 26 80 44 18
1 10
4 6
6 9
```

`011`

`10 36`
```
111174 6 555870 2 30 555870 21 277935 185290 26470
1 3
1 4
1 5
1 6
1 7
1 8
1 9
1 10
2 4
2 5
2 6
2 7
2 8
2 9
2 10
3 5
3 6
3 7
3 8
3 9
3 10
4 6
4 7
4 8
4 9
4 10
5 7
5 8
5 9
5 10
6 8
6 9
6 10
7 9
7 10
8 10
```

`111111001111100111100111001111111111`

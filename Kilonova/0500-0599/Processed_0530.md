```markdown
On his birthday, Florin received a **periodic** and **infinite** string of characters. Its period has a length $n$ and contains only lowercase letters of the English alphabet.

Since he is curious, he wants to customize the received string in various ways. To do this, he provides $q$ operations on the given string, operations of two types, as follows:

- `1 x y`: The letter at position $x$ becomes equal to $y$, where $y$ is a lowercase letter of the English alphabet.
- `2 a b c`: Florin wants to know how many characters equal to $c$ exist between positions $[a, b]$ in the string.

Since he does not want to disrupt the periodicity of the string too much, Florin guarantees that for all update operations, the modified positions have at most $k$ bits equal to $1$ in their binary representation.

# Task

Write a program that, given the string of characters and the updates, responds to queries.

# Input data

The input file `perioade.in` contains on the first line $n$ and $k$, representing the length of the period of the character string and the maximum number of $1$ bits that a modified position has in a type $1$ operation, respectively.

The second line contains the initial period of the character string.

The third line contains $q$, representing the number of operations performed by Florin.

The following $q$ lines contain the operations, which follow the description in the statement.

# Output data

The output file `perioade.out` will contain the answers to the type $2$ operations, one answer per line, in the order given in the input data.

# Constraints and clarifications
* $1 \leq n, q \leq 250\ 000$;
* $1 \leq k \leq 4$;
* For all queries, $1 \le x, a, b \le 10^{18}$, $a \le b$. The modified positions have at most $k$ bits equal to $1$;
* For $14$ points, $1 \le n, q \le 2\ 000$ and $1 \le pos \le 4\ 000$;
* For $25$ points, $k \le 2$, $n, q \le 10^5$;
* For $14$ points, $1 \le pos \le 2 * 10^{5}$;
* For $47$ points, there are no additional constraints.

# Example

`perioade.in`
```
3 4
bun
11
1 9 a
1 7 a
2 3 11 n
1 4 x
2 7 13 b
1 6 o
1 12 b
1 8 r
2 1 15 u
1 7 b
2 3 12 b
```

`perioade.out`
```
2
2
4
3
```

## Explanation

- Before the operations, the string is `bunbunbunbunbunbun...`
- After the first two updates, the string becomes `bunbunauabunbunbun...`
- For the first type $2$ operation, the letter $n$ is at positions $3$ and $6$.
- After the next update, the string becomes `bunxunauabunbunbun...`
- For the second type $2$ operation, the letter $b$ is at positions $10$ and $13$.
- After the next three updates, the string becomes `bunxuoarabubbunbun...`
- For the third type $2$ operation, the letter $u$ is at positions $2$, $5$, $11$ and $14$.
- After the next update, the string becomes `bunxuobrabubbunbun...`
- For the last type $2$ operation, the letter $b$ is at positions $7$, $10$ and $12$.
```
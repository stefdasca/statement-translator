# Polybius

The Polybius cipher is a cipher used by the Ancient Greeks that is based on a table of $5$ rows and $5$ columns for encrypting or decrypting a string of characters. For encryption, we take each character in the string and display the row and column in the table where the character is located. For decryption, we display the character that is in the table at the given row and column.

For example, using the table:

| \# | 1 | 2 | 3 | 4 | 5 |
| -- | - | - | - | - | - |
| 1  | A | B | C | D | E |
| 2  | F | G | H | I | K |
| 3  | L | M | N | O | P |
| 4  | Q | R | S | T | U |
| 5  | V | W | X | Y | Z |

With the string `INF`, we display $243321$ because letter `I` is at position $(2, 4)$, letter `N` is at position $(3, 3)$, and letter `F` is at position $(2, 1)$.

# Task

Given a number $p$, a string $t$ of $25$ characters corresponding to the table, and a string $s$. Determine:
1. For $p = 1$, encrypt the string $s$, consisting only of uppercase letters, using the table $t$.
2. For $p = 2$, decrypt the string $s$, consisting only of digits, using the table $t$.

# Input data

The input file `polybius.in` contains on the first line the number $p$, the second line contains the string $t$ consisting of $25$ characters representing all table elements from left to right and from top to bottom. The third line contains the string of letters $s$ to be encrypted if $p=1$, and the string of digits to be decrypted if $p=2$.

# Output data

- For $p = 1$, the output file `polybius.out` will contain on the first line the result of the encryption. The digits are displayed without spaces between them.
- For $p = 2$, the output file `polybius.out` will contain on the first line the result of the decryption.

# Constraints and clarifications

- $1 \leq p \leq 2$;
- the length of the string $t$ is $25$ characters;
- $1 \leq \text{length of the string of letters s} \leq 500\ 000$;
- It is guaranteed that all characters in $s$ are included in the string $t$ and the characters in $t$ are distinct two by two.
- One letter of the alphabet will always be missing from the table because it is a $5 \times 5$ table and the alphabet has $26$ characters.

# Example 1

`polybius.in`

```
1
ABCDEFGHIKLMNOPQRSTUVWXYZ
ANAAREMERE
```

`polybius.out`

```
11331111421532154215
```

# Example 2

`polybius.in`

```
2
ABCDEFGHIKLMNOPQRSTUVWXYZ
11331111421532154215
```

`polybius.out`

```
ANAAREMERE
```

## Explanation

The table in the examples corresponding to the string is:

| \# | 1 | 2 | 3 | 4 | 5 |
| -- | - | - | - | - | - |
| 1  | A | B | C | D | E |
| 2  | F | G | H | I | K |
| 3  | L | M | N | O | P |
| 4  | Q | R | S | T | U |
| 5  | V | W | X | Y | Z |

**Dexter** has defined his own algorithm for archiving his favorite string $T$, a string composed only of lowercase English alphabet letters. The archived string, denoted $S$, may consist of digits, lowercase English alphabet letters, square brackets `[` and `]`, round brackets `(` and `)`, as well as the character `*`.

**Fixi**, curious by nature, discovers the algorithm and tries to decompress the string $S$ by performing repeated transformations. A transformation can be one of the following $3$ types, where $C$ is a sequence in $S$ consisting only of letters.

1. A sequence in $S$ of the form `n(C)`, where n is the natural number immediately preceding the round bracket, transforms into a sequence $D$ obtained by concatenating the string $C$, $n$ times.
   Example: for the sequence `10(ab)`, we have $n=10$ and the resulting sequence $D=$ `abababababababababab`.
2. A sequence in $S$ of the form `[*C]` transforms into an even-length palindromic sequence obtained by concatenating the sequence $C$ with its reverse.
   Example: the sequence `[*abc]` results in the even-length palindromic sequence abccba.
3. A sequence in $S$ of the form `[C*]` transforms into an odd-length palindromic sequence obtained by concatenating the sequence $C$ with its reverse minus the first character.
   Example: the sequence `[abc*]` results in the odd-length palindromic sequence abcba.

A string is considered decompressed if it consists only of lowercase English alphabet letters.

# Task

Given the archived string $S$, determine the number of transformations of the $3$ types above performed by **Fixi** in the decompression algorithm, as well as the final decompressed form $T$ of the string $S$.

# Input data

The input file `arh.in` contains the archived string $S$.

# Output data

The output file `arh.out` must contain **exactly** two lines. The first line should contain the required number of transformations, and the second line should contain the required character string $T$.

# Constraints and clarifications

* The length of the archived string $S$ is between $1$ and $10\ 000$, inclusive;
* The length of the decompressed string $T$ is between $1$ and $100\ 000$, inclusive;
* $2 \leq n \leq 1\ 000$;
* A sequence of a string is a succession of characters in consecutive positions in the string;
* In the string $S$:
   * A digit may appear only immediately before an opening round bracket or another digit;
   * Each opening round bracket has at least one digit immediately before it;
   * All brackets, both square and round, close correctly;
   * The character `*` may appear only immediately after an opening square bracket or immediately before a closing square bracket.
* A sequence of a string is palindromic if the first element of the sequence equals the last, the second equals the second last, etc.;
* The reverse of a sequence is obtained by writing its characters in reverse order;
* $20\%$ of the test's score is awarded for correctly writing the number of requested transformations, and $80\%$ of the test's score for correctly writing the requested string;
* For $30$ points, the archived string $S$ can be decompressed using only transformations of type $1$;
* For another $30$ points, the archived string $S$ can be decompressed using only transformations of types $2$ and $3$.

# Example 1

`arh.in`
```
2(a)[*a2(b)]xy[2(c)b*]d
```

`arh.out`
```
5
aaabbbbaxyccbccd
```

## Explanation

```
2(a) => aa
2(b) => bb
[*a2(b)] => [*abb] => abbbba
2(c) => cc
[2(c)b*] => [ccb*] => ccbcc
```

# Example 2

`arh.in`
```
2(ab[cd*])a3(xyz)
```

`arh.out`
```
3
abcdcabcdcaxyzxyzxyz
```

## Explanation

```
3(xyz) => xyzxyzxyz
[cd*] => cdc
2(ab[cd*]) => 2(abcdc) => abcdcabcdc
```

# Example 3

`arh.in`
```
abcd
```

`arh.out`
```
0
abcd
```

## Explanation

No transformation is needed, and the decompressed string is identical to the archived one.
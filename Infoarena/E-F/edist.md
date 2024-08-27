## Task

Given any string of characters, we define the following 3 operations on it: 
- insertion: add any character at any position,
- deletion: remove the character at any position from the string,
- replacement: replace the character at any position in the string with any other character.

Two strings $S_{1}$ and $S_{2}$ containing only lowercase letters of the English alphabet and having $N$ and $M$ characters respectively are given. The edit distance between the two strings is the minimum number of the aforementioned operations that need to be applied on the first string to transform it into the second string. The same type of operation can be applied multiple times. Find the edit distance between the two strings, knowing that it is less than or equal to a given integer $K$.

## Input data

The first line of the input file `edist.in` contains three integers: $N$, $M$, and $K$. The second line of the file contains $N$ lowercase letters of the English alphabet representing the string $S_{1}$. The third line of the file contains $M$ lowercase letters of the English alphabet representing the string $S_{2}$.

## Output data

The output file `edist.out` will contain a single integer representing the edit distance between the two strings.

## Constraints

$1 \leq N, M \leq 20\,000$

$1 \leq K \leq 500$

For 70% of the tests:

$N, M \leq 2\,000$.

## Example

`edist.in`

```
5 6 5
harpa
armura
```

`edist.out`

```
4
```

`edist.in`

```
5 5 5
carte
antet
```

`edist.out`

```
5 4
```

## Explanation

One possible way to transform the string `harpa` into `armura` using $4$ operations is:
1. delete the letter $h$ from the first string,
2. replace the letter $p$ with the letter $m$,
3. add the letter $u$ before the last letter in the first string,
4. add the letter $r$ before the last letter in the first string.
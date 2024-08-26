## Domains

Seeing the potential of character strings, the BFR gods realized the treasure they have stumbled upon. But since we are at FMI No Stress and the winter holidays are approaching, they decided to be kind to you today. Today, they have gifted you a character string of length $n$ which contains lowercase letters and the character "." (dot) and they want you to find out the number of domain-type subsequences of this character string. A domain-type subsequence is a subsequence of the form $.letter1letter2$, where $letter1$ and $letter2$ are different. Even if a domain appears multiple times as a subsequence, we will count it for each occurrence. Practically, you need to count the number of triplets $(i, j, k)$ such that $i < j < k$ , $s[i] = '.'$ , and $s[j]$ and $s[k]$ are different letters.

## Input data

The input file `domenii.in` contains on the first line the number $n$, the length of the character string. The next line contains the character string $s$ of length $n$.

## Output data

The output file `domenii.out` will contain on the first line the number of domain-type subsequences of the character string.

## Constraints

$1 \leq n \leq 10^6$

For 20\% of the tests,

$1 \leq n \leq 200$

For another 20\% of the tests,

$1 \leq n \leq 2000$

The string can contain only the character "." (dot) or lowercase letters of the English alphabet.

## Example

`domenii.in`
```
7
.p.zior
```

`domenii.out`
```
16
```

## Explanation

The valid domains are $.pz$, $.pi$, $.po$, $.pr$, $.zi$, $.zo$, $.zr$, $.zi$, $.zo$, $.zr$, $.io$, $.ir$, $.io$, $.ir$, $.or$, $.or$. As mentioned, a domain is counted each time it appears, even if in this example we have two occurrences of $.ir$, we will count both of them.

~[name.png]
For writing messages, soldiers in a military unit use $9$ lowercase letters: `a`, `e`, `i`, `o`, `u`, `m`, `n`, `r`, `s` and the space character. These letters are encoded using the digits $1, 2, \dots, 9$ (in the above order), and the digit $0$ is used for the space character. Thus, the text `ana are mere` can be encoded as the natural number $171018206282$.

To increase the security level of transmitted messages, soldiers perform an over-coding, replacing each digit $k$ used in the encoding with the power $2^k$. Thus, the previous text is over-coded as: $2128212256416442564$.

# Task

Write a program that, given an over-code, determines the initial text. If there are multiple such texts, determine them all.

# Input data

The input file `codif.in` contains on the first line, $n$ the number of digits used in the over-coded text, and on the second line contains the over-code.

# Output data

The output file `codif.out` will contain on the first line the number $m$ of texts that correspond to the given over-code, and on the following $m$ lines, the texts, each on a separate line, in _longest-lexicographic_ order.

# Constraints and clarifications

* $0 < n < 83$
* For two texts $u = u_1 u_2 \dots u_a$ and $v = v_1 v_2 \dots v_b$, $u$ is before $v$ in _longest-lexicographic_ order if $a < b$ or if $a = b$ and there exists an index $1 \leq i \leq a$ with the property that $u_1 = v_1, \dots, u_{i-1} = v_{i-1}$, $u_i < v_i$. The order of the characters is given by their ASCII codes. For example, in _longest-lexicographic_ order, the text `aerss` is before the text `aeumr`, and after the text `sun`.
* Each line in the output file will end with a newline character.
* For all tests, the number of texts that correspond to the same over-code is less than or equal to $70$.

# Example

`codif.in`
```
19
2128212256416442564
```

`codif.out`
```
4
ana are mere
ana areoeere
a aia are mere
a aia areoeere
```


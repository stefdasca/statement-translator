Let $S$ be a string of length $N$ indexed from 1. On such a string, a `swap` operation is defined: an index $i$ ($1 \leq i < N$) is chosen, and the characters $S[i]$ and $S[i+1]$ are swapped.

The lucky number corresponding to a string $S$ is equal to the minimum number of `swap` operations that need to be performed successively to obtain at least one `bingo` subarray in the string $S$. If the `bingo` subarray appears in the initial string, the lucky number is equal to $0$.

# Task

Given a natural number $T$ and $T$ strings. Determine for each given string $S_i$ ($1 \leq i \leq T$) its lucky number.

# Input data

The input file `bingo.in` contains on the first line a non-zero natural number $T$. The following $T$ lines each contain a string consisting only of lowercase letters of the English alphabet.

# Output data

The output file `bingo.out` contains the lucky numbers determined for each of the $T$ given strings. These should be printed each on a separate line, in the order the strings are given in the input file.

# Constraints and clarifications

* $1 \leq T \leq 10 \ 000$;
* $\sum_{i=1}^{T}|S_i| \leq 100 \ 000$, where $|S|$ denotes the number of characters in the string $S$;
* A subarray of length $L$ of a string $S$ represents a sequence of $L$ characters that are in consecutive positions in the string $S$.
* It is guaranteed that each string read contains at least once each character from the set $\{b,i,n,g,o\}$;
* For $17$ points, $|S_i|=5$ ($1 \leq i \leq T$);
* For $21$ points, in each string $S_i$ ($1 \leq i \leq T$), each character from the set $\{b,i,n,g,o\}$ appears exactly once;
* For $11$ points, $1 \leq T \leq 10$ and in each string $S_i$ ($1 \leq i \leq T$), each character from the set $\{b,i,n,g,o\}$ appears at most 10 times;
* For $51$ points, there are no additional restrictions.

# Example

`bingo.in`

```
8
nbbigo
ibhpnogg
bihhhhhhhhngo
nbxgyoi
uobsioboisinosaogvnibn
hgibaisianiaosanbviaobi
ybingo
btgpntoipipqiamytoghoi
```

`bingo.out`
```
3
6
16
8
7
14
0
9
```

## Explanation

The lucky number of the first read string is $3$, and a possible sequence of operations is: $nbbigo \rightarrow bnbigo \rightarrow bbnigo \rightarrow bbingo$.
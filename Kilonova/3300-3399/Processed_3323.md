
# Task

Given a number $N$ and a target string, $S$, with $N$ characters containing lowercase letters of the Latin alphabet.

You have $K$ strings available, each containing lowercase letters of the Latin alphabet. Knowing that you can use any prefix of these strings, as many times as needed, what is the minimum cost to obtain the initial string by concatenating (without overlap) the selected prefixes? The cost will increase by $1$ for each use of a prefix.

# Input data

The first line contains a number, $N$.  
The second line contains the string $S$.  
The third line contains a number, $K$.  
Each of the next $K$ lines will contain one of the $K$ strings.

# Output data

The first line will contain a single integer, the minimum cost to form the initial string. If the initial string cannot be formed, print $-1$.

# Constraints and clarifications

* $1 \leq N \leq 1 \ 000 \ 000$;
* $1 \leq K \leq 1 \ 000 \ 000$;
* The sum of the lengths of the $K$ strings $\leq 1 \ 000 \ 000$;
* All strings contain only lowercase letters of the Latin alphabet.

# Example 1

`stdin`
```
5
abcab
4
acde
bca
cab
aa
```

`stdout`
```
3
```

## Explanation

The string `abcab` can be formed using the prefixes `a`, `b`, `cab`.

# Example 2

`stdin`
```
5
abcaz
4
acde
bca
cab
aa
```

`stdout`
```
-1
```

## Explanation

The character `z` is not present in the $4$ strings that we can use.

# Example 3

`stdin`
```
5
aaaaa
2
a
aa
```

`stdout`
```
3
```

## Explanation

The string `aaaaa` can be formed using the prefixes `a`, `aa`, `aa`.

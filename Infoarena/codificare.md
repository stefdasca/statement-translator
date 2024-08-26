## Encoding

In the last mission he participated in, $Birkhoff$ had to break the criminals' radio telecommunication system - a trivial task for him, of course. Now that the mission has ended successfully, $Birkhoff$ knows the encryption code used by the enemies and is studying it to write his mission report. The encryption code is a string $C$ of length $N$ formed from lowercase English alphabet characters. $Birkhoff$ wonders in how many ways the string $C$ can be obtained starting from a subsequence $S$ of length $1$, using the following operations successively: prefix the string $S$ with a character; suffix the string $S$ with a character. While you were reading the problem, $Birkhoff$ has already started writing his report. If you want to be like him someday, you will have to answer his question for any subsequence $S$.

## Input data

The input file `codificare.in` contains on the first line the natural number $N$ and on the second line the string of characters $C$.

## Output data

The output file `codificare.out` must contain on the first line the natural number $K$ representing the number of distinct subsequences of length $1$ of the string $C$. On each of the following $K$ lines will be found, separated by a space, a subsequence $S$ and the number of ways to reach the string $C$ from it modulo $666013$. The $K$ lines will be sorted lexicographically.

## Constraints and clarifications

$1 \leq N \leq 100000$

For $25\%$ of the tests it is guaranteed that $N \leq 20$.

For $50\%$ of the tests it is guaranteed that $N \leq 1000$.

## Example

`codificare.in`  
```
3
aba
```

`codificare.out`  
```
2
a 2
b 2
```

## Explanation

The distinct subsequences $S$ are $a$ and $b$. For each, there are two ways to obtain the string $C$: 
$a \rightarrow ab \rightarrow aba$  
$a \rightarrow ba \rightarrow aba$  
$b \rightarrow ba \rightarrow aba$  
$b \rightarrow ab \rightarrow aba$
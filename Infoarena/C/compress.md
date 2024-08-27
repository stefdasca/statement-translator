Compress

Ionel has a challenge for you again: he received a task that he doesn't know how to solve and he asks for your help. Given a string $S$ of length $N$, you need to encode it according to the following rule: each maximal sequence formed of the same character will be replaced by the character followed by the length of the sequence (for example, the string $aaaa$ becomes $a4$). A sequence is maximal if it cannot be extended further.

## Input data

The input file `compress.in` will contain on the first line the string $S$. 

## Output data

The output file `compress.out` will have a single line containing the encoding of the given string.

## Constraints and clarifications

$1 \leq N \leq 100000$

The string $S$ will consist only of lowercase English letters.

## Example

`compress.in` 
```
aaaaaaaaaabcbbb
```

`compress.out` 
```
a10b1c1b3
```
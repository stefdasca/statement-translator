## Task

Our budding programmer, Por Costel, has just returned from the programming camp at Petrozaporksk. There, he learned many things: how to boil a cob of corn, how to use the keyboard to scratch his belly, etc. He also vaguely remembers a programming problem: A semipalindrome is defined as a word $c$ in which there exists a subword such that it is a prefix of it and (the reversed word) is a suffix of it. For example, '$ababba$' is a semipalindrome because there exists a subword 'ab' which is a prefix of the word and 'ba' is a suffix of the word. Considering only semipalindromes that contain the letters 'a' and 'b', the problem requires finding the $k$-th lexicographical semipalindrome of length $n$. Por Costel does not remember if the statement was exactly like this at Petrozaporksk, but he still finds the problem interesting and asks for your help with it.

## Input data

The input file `semipal.in` will contain on the first line the number $t$, the number of tests, and on the following lines, two numbers each, $n$ and $k$.

## Output data

The output file `semipal.out` will contain $t$ lines, each line containing the answer to the $k$-th test.

## Constraints

$1 \leq t \leq 100$

$1 \leq n \leq 50$

$1 \leq k \leq$ the number of semipalindromes of length $n$

## Example

`semipal.in`

```
2
5 1
5 14
```

`semipal.out`

```
aaaaa
bbabb
```
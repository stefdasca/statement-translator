# Subarrays2

Valerică has a string with $N$ characters. Being a minimalist person, each character in the string can be either the letter $a$ or the letter $b$. Valerică is now wondering in how many ways he can distribute all the characters of the initial string such that two identical subarrays result. Thus, denoting by $X$ and $Y$ two subarrays that would result from a possible distribution and analyzing one by one all the characters from the initial string, in the order in which they appear in the string, Valerică will decide for each whether to introduce it at the end of subarray $X$ or at the end of subarray $Y$. For example, for the initial string $abab$, Valerică can introduce the first and second character into subarray $X$ and the third and fourth character into subarray $Y$, thus obtaining two identical subarrays.

## Task

Write a program to help Valerică count all distinct possibilities of forming two identical subarrays from the initial string of characters.

## Input data

The first line of the file `subsiruri2.in` contains the natural number $N$ representing the number of characters in the initial string. The next line contains the string composed of $N$ characters from the set $\{a,b\}$.

## Output data

The output file `subsiruri2.out` will contain a single line which will be the written number of total possibilities to form two identical subarrays from the initial string.

## Constraints and clarifications

$1 \leq N \leq 40$  
$N$ is even for $20 \%$ of the tests  
$N \leq 16$

## Example

`subsiruri2.in`  
```
4
abab
```

`subsiruri2.out`  
```
2
```

## Explanation

The first possibility is to form subarray $X$ from the first two characters and subarray $Y$ from the last two characters. The second possibility is to form subarray $X$ from the last two characters and subarray $Y$ from the first two characters. 

`subsiruri2.in`  
```
6
abaaaa
```

`subsiruri2.out`  
```
0
```

## Explanation

There are no possibilities to form two identical subarrays.
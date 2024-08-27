## Task

Any word can be split into a larger or smaller number of subarrays, each subarray being a palindrome (in the worst case, each subarray has a length of $1$). Given a word, determine the minimum number of palindromes into which it can be split.

## Input data

The input file `pali.in` contains one line with a string of letters, representing the given word.

## Output data

In the output file `pali.out` print the minimum number of palindromes into which the word from the input file can be split.

## Constraints and clarifications

The number of letters in the word will not exceed $5000$.

The word consists only of lowercase letters of the English alphabet.

## Examples

`pali.in`  
aaaabbaa

`pali.out`  
$2$

`pali.in`  
abccbazzz

`pali.out`  
$2$

## Explanation

aaaabbaa = aa + aabbaa

abccbazzz = abccba + zzz
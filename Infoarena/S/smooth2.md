# Smooth2

A string is called smooth if:
- It consists only of lowercase letters from the English alphabet.
- For each of its prefixes, it is true that the difference between the maximum and minimum frequency of any letter is at most $1$. In this condition, only letters that appear at least once in the entire string are considered, regardless of the examined prefix.

For example, the strings $abca$, $aaaaaaa$, and $baab$ are smooth, whereas the strings $aab$ and $abracadabra$ are not smooth.

Given a string of lowercase English letters, what is the minimum number of characters that must be replaced to transform the string into a smooth string?

## Input data

The input file `smooth2.in` contains a string of lowercase English letters.

## Output data

The output file `smooth2.out` contains the minimum number of letters that must be replaced for the given string to become smooth.

## Constraints and clarifications

$1 \leq$ number of letters $\leq 100\ 000$

For tests worth $10$ points  
$1 \leq$ number of letters $\leq 8$

For other tests worth $10$ points  
$1 \leq$ number of letters $\leq 1000$ and the answer is at most $2$.

We call a prefix of a string any continuous subarray that starts from the first position of the string.

You will receive evaluation results only on the example input files. These will not affect the problem score, having an associated score of $0$.

## Example

`smooth2.in`  
`smooth2.out`

## Explanation

$aaba$ $1$  
Change the first letter, the string becomes $baba$

$aabaa$ $1$  
Change the third letter, the string becomes $aaaaa$

$abccbbcc$ $2$  
Change the sixth and seventh letters, the string becomes $abccbabc$

$jjbjqbqqjbqqjqj$ $4$  
Four changes are sufficient.
## Task

A palindrome is a string of characters that is equal to its reverse. For example, $aerisirea$ is a palindrome. Given a string of characters, you are asked to determine the minimum number of inversions needed to transform it into a palindrome. An inversion represents the swapping of two adjacent characters.

To transform $aeriseair$ into a palindrome, 4 inversions are needed:
swap $ai$ : $aeriseiar$
swap $ei$ : $aerisiear$
swap $ar$ : $aerisiera$
swap $er$ : $aerisirea$

## Input data (file: $palind.in$)
The input file will contain multiple tests. The first line will contain the number $T$ of tests. Each of the following $T$ tests will contain a string of characters (lowercase letters of the Latin alphabet). Each line ends with an enter.

## Output data (file: $palind.out$)
The output file will contain $T$ lines. Line $i$ will contain the minimum number to obtain a palindrome from the string of characters found on line $i+1$ in the input file or $-1$ if it is not possible to obtain a palindrome.

## Constraints and clarifications

The number of characters in a string will not exceed $10^5$ 

$ T \leq 10^5$ 

## Example

$palind.in$
```
4
aeriseair
mamad
asd
aabb
```

$palind.out$
```
4
3
-1
2
```
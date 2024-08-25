# Cpal

Knowing that you have at your disposal $F[x]$ digits of $x$ for all $1 \leq x \leq 9$, decide if a palindrome can be formed using all the given digits. A palindrome is a natural number that is equal to its mirror image. For example, "121" is a palindrome, but "2430241" is not a palindrome. Note! A natural number has at least one digit.

## Input data

The input file `cpal.in` will contain exactly $10$ lines, each of them constituting a test. One line is formed of $9$ numbers, the $i$-th number signifying the number of digits of type $i$ generously provided by the administrators.

## Output data

The output file `cpal.out` will also contain $10$ lines, each containing the answer for the corresponding test. Print $1$ for a positive answer and $0$ otherwise.

## Constraints and clarifications

$0 \leq F[x] \leq 10^{9}$

## Example

`cpal.in`  `cpal.out`  
$0\ 1\ 0\ 0\ 0\ 0\ 0\ 0\ 0$  $1$ 

## Explanation

The only number we can construct is $2$, which is indeed a palindrome. Note that the example does not reflect the input file. It will have exactly $10$ lines, according to the task.
## Task

Because he does not like long statements, Bulanel offers you the following problem: Given a natural number $N$, calculate how many strings composed of $N$ characters from the English alphabet exist such that the strings do not contain palindromic subarrays of length greater than or equal to $3$. The result will be displayed modulo $10^9 + 7$. For example, the string `cabad` will not be counted because it contains the subarray `aba`, which is a palindrome of length greater than or equal to $3$. On the other hand, the string `abccef` is valid because it does not contain palindromic subarrays of length greater than or equal to $3$. 

## Input data

The input file `aiafarapalindroame.in` contains on the first line a natural number $N$. 

## Output data

The output file `aiafarapalindroame.out` contains a single number representing the number of strings that respect the property required by Bulanel (modulo $10^9 + 7$). 

## Constraints and clarifications

$1 \leq N \leq 1\,000\,000\,000$ 

For tests worth $10$ points $N \leq 5$

For tests worth $70$ points $N \leq 1\,000\,000$

The English alphabet contains $26$ letters (the letters from $a$ to $z$)

The problem will be evaluated on tests worth $90$ points

$10$ points are automatically granted (test $10$ is the first example) 

## Example

`aiafarapalindroame.in` `aiafarapalindroame.out` 

## Explanation

`2 676` There are $26^2 = 676$ possible strings and all respect the property required by Bulanel. `100 873567312` You will have to take our word for it.
## Triti2

Triti are numbers composed of the digits 0, 1, and 2 with the property that the absolute difference between any two neighboring digits (on consecutive positions) is exactly $1$.

## Task

Very curious by nature, Țirbi wants to find out which is the $N$-th triti with exactly $K$ digits. Since he is passionate about Silverlight and not algorithms, he asks you to help him.

## Input data

The input file `triti2.in` contains on the first line the natural numbers $K$ and $N$ separated by a single space.

## Output data

The output file `triti2.out` contains the $N$-th triti with exactly $K$ digits if it exists, or "-1" (without quotes) if there are not at least $N$ distinct tritis with exactly $K$ digits.

## Constraints and clarifications

$1 \leq K \leq 1\,000$  
$1 \leq N \leq 10\,1000$  
Since tritis are numbers, they cannot have the first digit $0$.  
The numbering of tritis starts from $1$.  
The $N$-th triti is the smallest triti that has exactly $N-1$ tritis smaller than it. Tritis are compared the same way as numbers.  
For $25\%$ of the tests $N \leq 10^6$  
For another $45\%$ of the tests $N \leq 10^{18}$  

## Example

`triti2.in`  
$7\ 13$  

`triti2.out`  
$2121010$  

## Explanation

$1010101$  
$1010121$  
$1012101$  
$1012121$  
$1210101$  
$1210121$  
$1212101$  
$1212121$  
$2101010$  
$2101012$  
$2101210$  
$2101212$  
$2121010$  
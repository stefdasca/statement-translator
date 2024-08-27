## Task

Given a sequence of integers, compute the following: the length of the longest strictly decreasing subsequence and the number of strictly decreasing subsequences of maximum length. When counting the number of solutions, two subsequences are considered identical (and counted only once) if they are formed from the same sequence of numbers (i.e., they "look the same" when comparing the values of the elements of the $2$ subsequences).

## Input data

The first line of the file `decrease.in` contains the number $N$ of elements of the sequence. The next $N$ lines contain one element of the sequence each.

## Output data

The first (and only) line of the file `decrease.out` should contain $2$ integers, separated by a space: the length of the longest strictly decreasing subsequence and the number of strictly decreasing subsequences of maximum length.

## Constraints

$1 \leq N \leq 5000$  
$1 \leq$ each value in the sequence $\leq 32767$  
It is guaranteed that the number of subsequences fits into an unsigned $32$-bit integer.

## Example

`decrease.in`  
$5$  
$780$  
$710$  
$760$  
$690$  
$630$

`decrease.out`  
$4\ 2$
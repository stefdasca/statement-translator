# RangeMode

Given a sequence of $N$ integers. Answer $M$ questions of the type: What is the most frequent element in the interval $[st, dr]$?

## Input data

The input file `rangemode.in` contains on its first line the numbers $N$ and $M$ signifying the length of the sequence and the number of questions, respectively. On the next line we find the sequence of integers. The following $M$ lines contain each a pair $st$ $dr$ representing the endpoints of the interval for which we want to find the answer.

## Output data

The output file `rangemode.out` will contain $M$ lines, with the $i^{th}$ line containing the answer to the $i^{th}$ question.

## Constraints and clarifications

$1 \leq N, M \leq 100\ 000$ 

The numbers in the sequence are in the range $[1, 100\ 000]$

If there are multiple elements with maximum frequency for a certain interval, the element with the smallest value among them will be displayed.

## Example

`rangemode.in`  

7 3  
1 2 2 3 1 3 3  
1 3  
4 5  
1 7  

`rangemode.out`  

2  
1  
3
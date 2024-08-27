## Task

Marian Buzdugan has decided to complete his "Faculty of Computer Science and What Was the Other Thing?" and for that, he needs to increase his scores in $N$ exams. Fortunately, the boosts are paid in heavy lei. Petre Căpraru, being from Vâlcea, obtained sponsorships overnight for a budget of $B$ lei (note, these are heavy lei). Each boost for an exam has a characteristic price $P[i]$ (not necessarily unique). Petre suggested to Marian not to pay more than $C$ lei for each exam because there are additional sessions for re-re-re-exams. Marian agreed but aimed to use as much of the $B$ lei provided by Petre as possible. Help Marian find the appropriate $C$ to spend as much as possible of the $B$ heavy lei provided by Petre.

## Input Data

The input file `buget.in` contains on the first line 2 numbers separated by a space, $N$ and $B$, with the meanings described above. On the next line, there will be $N$ elements separated by spaces, representing the price $P[i]$ of the $N$ boosts.

## Output Data

The first line of the file `buget.out` will contain the sought number.

## Constraints and clarifications

$1 \leq N < 10^5$  
$1 \leq B < 10^{15}$  
$0 \leq P[i] < 10^9$ for any $1 \leq i \leq N$  
$B < \text{Sum}(P[i])$  
All exams must be paid.

## Example

`buget.in`  
`5 30`  
`1 7 5 9 10`  

`buget.out`  
`8`  

## Explanation

For the limit $C = 1$ the array of prices will be [1,1,1,1,1] and the sum is $5$.  
For the limit $C = 8$ the array of prices will be [1,7,5,8,8] and the sum is $29$.  
Thus, for the limit $C = 8$ the sum will be maximal but still $\leq B$
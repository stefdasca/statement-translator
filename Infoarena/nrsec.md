Nrsec

Electra is preparing for the Informatics Olympiad. Recently, she came across the following problem. You are given an array of $N$ integers and a natural number $K$. The task is to find the smallest integer $S$ such that the number of subarrays whose sum is less than or equal to $S$ is at least $K$. Solve the problem so you can give Electra a hint on how to do it. If you help her, Electra will reward you as best she can.

## Input data

The input file `nrsec.in` will contain on the first line the numbers $N$ and $K$. The next line contains the array of $N$ integers separated by spaces.

## Output data

In the output file `nrsec.out` you will print the number $S$ that satisfies the above task.

## Constraints

$1 \leq N \leq 10^5$  
$1 \leq K \leq N \times (N + 1) / 2$  
The absolute value of the numbers in the array will not exceed $10^9$  
The sum of a subarray is the sum of the elements contained in that subarray.

## Example

`nrsec.in`
4 5
4 -2 3 -1

`nrsec.out`
2

## Explanation

The sums of all subarrays are: $4, 2, 5, 4, -2, 1, 0, 3, 2, -1$. It can be observed that $6$ of these sums are less than or equal to $2$. Therefore, $2$ is the answer that represents the smallest integer such that there are at least $5$ subarrays whose sum is less than or equal to $2$.